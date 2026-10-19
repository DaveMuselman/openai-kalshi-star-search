#!/usr/bin/env python3
"""Read-only compressed JSONL source inventory and integrity check.

Example:
 python3 tools/audit_gzip_jsonl.py --input-dir ./recordings --output-manifest audit-manifest.json

Does NOT establish order-book replay or trading quality. No exchange access.
"""
import argparse
from collections import Counter
from pathlib import Path
import gzip
import hashlib
import json
import sys


def audit(path, root, gap_ms=5000, backstep_ms=250):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1048576), b""):
            digest.update(chunk)

    counts = Counter()
    first = last = max_seen = None
    incidents = []
    failure = None
    try:
        with gzip.open(path, "rt", encoding="utf-8") as rows:
            for line_no, line in enumerate(rows, 1):
                counts["physical_lines"] += 1
                if not line.strip():
                    counts["blank_lines"] += 1
                    continue
                try:
                    event = json.loads(line)
                except (ValueError, TypeError):
                    counts["invalid_json"] += 1
                    if len(incidents) < 40:
                        incidents.append({"line": line_no, "type": "bad_json"})
                    continue
                if not isinstance(event, dict):
                    counts["nonobject_json"] += 1
                    continue
                counts["event_" + str(event.get("kind", "UNKNOWN"))] += 1
                stamp = event.get("received_ms")
                if stamp is None:
                    continue
                try:
                    stamp = int(stamp)
                except (ValueError, TypeError):
                    counts["bad_timestamp"] += 1
                    continue
                if first is None:
                    first = stamp
                last = stamp
                if max_seen is not None:
                    if stamp < max_seen:
                        counts["clock_backsteps"] += 1
                        if max_seen - stamp > backstep_ms:
                            counts["severe_backsteps"] += 1
                            if len(incidents) < 40:
                                incidents.append({"line": line_no, "type": "backstep", "ms": max_seen - stamp})
                    if stamp - max_seen > gap_ms:
                        counts["receive_gaps"] += 1
                        if len(incidents) < 40:
                            incidents.append({"line": line_no, "type": "gap", "ms": stamp - max_seen})
                max_seen = max(max_seen if max_seen is not None else stamp, stamp)
    except (OSError, EOFError, UnicodeError) as error:
        failure = type(error).__name__ + ": " + str(error)
    return {
        "path": path.relative_to(root).as_posix(),
        "compressed_bytes": path.stat().st_size,
        "sha256_compressed": digest.hexdigest(),
        "decompression_ok": failure is None,
        "error": failure,
        "first_received_ms": first,
        "last_received_ms": last,
        "counts": dict(counts),
        "incident_examples": incidents,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-manifest", type=Path, required=True)
    parser.add_argument("--gap-ms", type=int, default=5000)
    parser.add_argument("--backstep-ms", type=int, default=250)
    args = parser.parse_args()
    if args.gap_ms < 0 or args.backstep_ms < 0:
        parser.error("time thresholds must be non-negative")
    root = args.input_dir.resolve()
    if not root.is_dir():
        parser.error("the input directory does not exist")
    recordings = sorted(root.rglob("*.jsonl.gz"))
    if not recordings:
        parser.error("no original JSONL gzip recordings found")
    results = []
    for index, path in enumerate(recordings, 1):
        result = audit(path, root, args.gap_ms, args.backstep_ms)
        results.append(result)
        print(f"{index}/{len(recordings)} {result['path']}: " +
              ("OK" if result["decompression_ok"] else "ERROR"), file=sys.stderr)
    manifest = {
        "schema": "star-search-compressed-source-inventory-v1",
        "recordings_count": len(recordings),
        "fully_decompressed": sum(row["decompression_ok"] for row in results),
        "invalid_json": sum(row["counts"].get("invalid_json", 0) for row in results),
        "records": results,
        "warning": "File integrity only. Market-quality book replay is required separately.",
    }
    args.output_manifest.parent.mkdir(parents=True, exist_ok=True)
    args.output_manifest.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Manifest written:", args.output_manifest)
    return 0 if all(x["decompression_ok"] and x["counts"].get("invalid_json", 0) == 0 for x in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
