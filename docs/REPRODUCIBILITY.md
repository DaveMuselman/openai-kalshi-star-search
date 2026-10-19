# Reproducibility and release checklist

## Available in this public repository

- Research protocol and the historical October 19 case study.
- Source format and independent provenance requirements.
- A standalone gzip/JSONL integrity inventory utility (in `tools/`).
- Negative results and historical QA failure explanation.

**Not yet included:** the approved-for-release full causal order-book replayer, exact frozen anomaly search and modeled-fee execution scripts, original compressed tapes, archived officially confirmed settlements, and portable byte-identical test fixtures. The historic profit/loss numbers therefore **cannot yet be fully reproduced from this repo alone.** This limitation is deliberate and must not be obscured.

## Quick source audit

Python 3.10+; no API token and no trading account required.

```bash
python3 tools/audit_gzip_jsonl.py --input-dir ./recordings --output-manifest ./audit-manifest.json
```

This reads each `.jsonl.gz` recursively, verifies decompression, validates JSON, hashes the original compressed bytes and records basic timing warnings. **Passing file-integrity checks is not a market-level QA pass.** The independent reconstruction must also validate snapshots/deltas across warmup and current windows.

## Required to reproduce historical results

Original 756 archives, provenance and hash mapping, frozen quality decisions for 749 markets, 200 ms reconstructed quote/depth grids, verified official settlement records, feature definitions, execution-fee assumptions, chronological folds, all 190 evaluated configurations (including failures), and the later latency/slippage stress. Source data rights must be reviewed before publishing.

## Planned independent work

1. Extract and sanitize the historical independent order-book replayer, retaining source-to-200ms causal parity and cross-window invalidation.
2. Add deterministic synthetic fixtures for negative depth, dropped deltas, clock reversal, warmup gap and absent strike.
3. Package the anomaly hypothesis enumerator and historical execution simulator with separate official settlement ingestion.
4. Add tests and CI; compare case-level hash and parity results to the frozen historical study.
5. Release manifests or redistributable fixtures when provenance and rights permit.

Never upload private account data, production credentials or full third-party recordings merely to make the repository appear complete.
