# Raw recordings, data contract and provenance

## Required inputs
Each captured 15-minute market needs original `.jsonl.gz` WebSocket archives for its **preceding warmup interval** and the market interval. JSONL records may include:

- `kind: "RECEIVED"`, `received_ms`, `payload.type: "orderbook_snapshot"` and `payload.msg.market_ticker`, with `yes_dollars_fp` and `no_dollars_fp` price/depth pairs.
- `payload.type: "orderbook_delta"`, `price_dollars`, signed `delta_fp`, `side`, `sid`, `seq` and market ticker.
- `payload.type: "cfbenchmarks_value_5hz"` or `"cfbenchmarks_value"` with `msg.index_id` (e.g. `ETHUSD_RTI`), native value and receive timestamp. Some one-second records retain a nested `data` string rather than a top-level numerical value: distinguish these formats explicitly, do not invent missing readings.
- `kind: "TARGET_METADATA"`, ticker, `floor_strike`, `received_ms` and window metadata.
- `SEQUENCE_GAP`, `DISCONNECT_OR_FAILURE`, `STREAM_ERROR`, `CONNECTED`, `SOCKET_CONNECT_ATTEMPT`, rotation and subscription lifecycle markers.

Preserve **raw receive order**. Exchange-supplied timestamps may be later than the local time of receipt or represent a different clock; never use those timestamps to introduce a tick before it was received.

## An independently useful checksum manifest

Provide one entry per archive: market/coin, window start, relative archive path, compressed byte size, SHA-256 of the exact compressed contents, JSON record count, gzip CRC success, first/last receive timestamp, gap markers and known issues. The signed depth of historical books depends on replaying all packets after the last valid snapshot.

## Reproducing the October 19 dataset

The historical full re-audit covered **756 archives** / **749 market windows**, including a preceding warmup archive for the first tested window, seven coins, and market start times from October 18, 07:15 ET through October 19, 09:45 ET. The frozen prior screen marked 362 markets clean; independent source/grid verification rejected one additional ZEC market.

The original recordings are **not included**. Their source-access and redistribution permissions must be established independently. Public aggregate counts and methodological descriptions do not provide a byte-for-byte substitute for these tapes. The repository's original-source audit tool is intended for user-owned or lawfully available recordings.

## Data safety

Never upload an entire personal Downloads directory, credentials, private account data, funded-order histories, API tokens or raw third-party data without a documented rights review. Exclude credentials from logs and reports, too. The `.gitignore` defaults to excluding compressed archives and data dumps.
