# STAR SEARCH research protocol

**Version:** Public specification 0.1 (October 19, 2026). Historical research rules are frozen by run; changes require a new version.

## Boundaries
Independent hypothesis discovery from vetted Kalshi L2 and corresponding underlying market recordings. No broker orders, no funded/paper bot changes. Existing paper strategies are not hypothesis inputs.

## Data to collect
For each coin/window, preserve the original gzip JSONL tapes, arrival timestamp, packet type, WebSocket sequence/continuity markers, target/strike metadata (and time first known), native benchmark ticks, all snapshot and orderbook delta packets, trading window boundaries, and separately verified official settlement.

## Read and audit original source
- Inventory all expected archives and hash the **compressed** bytes (SHA-256). Missing, duplicate or corrupt archives must be explicit.
- Stream-decompress **every file to its CRC/trailer** and validate every JSONL record. Never silently skip malformed lines.
- Check received times for backsteps, periods of lost reception, reconnects and recorder failure markers. A discontinuity can invalidate a book for the *next* 15-minute market when that ticker's snapshot was already received in a previous archive.
- Apply snapshot then signed delta updates in the original causal sequence. Reject negative liquidity, missing initial snapshot, unrecovered invalidation, unavailable strike/spot, impossible prices, crossed synthetic quotes and stale book or spot.
- If a gap/restart occurs **after a future market's snapshot**, require a replacement valid snapshot for that market; simply starting a new file does not restore integrity.
- Perform independent replay rather than only checking previously derived QA flags.

## Reconstruction
15-minute contracts are represented on a **200 ms time grid** of 4,500 rows. A 200 ms grid does not imply 200 ms source updates (some benchmarks update about once a second).

At each grid timestamp use **only previously received** information. Historical October 19 implementation required spot age ≤ 1,500 ms and last book update age ≤ 1,800 ms, known floor strike, both nonempty book sides, and valid YES/NO bids. Compute synthetic YES ask as `1 - NO best bid`, and NO ask as `1 - YES best bid`; preserve signed depth by price level. Never infer quantities from an ask that has no opposing bid inventory.

The historical study also used **≥ 80% valid grid coverage** and first usable quote by approximately **T+42s**, together with continuity flags, as its core market eligibility filter. Publish all reasons when a market fails; separate source completeness from trade executability.

## Freeze and separate data
Declare train/check/holdout chronological boundaries, quality filters, trial universe, discovery features, execution model and selection criteria **before** looking at the corresponding outcomes. Save all attempted configurations, including those that fail. A holdout used for selection is no longer untouched validation.

## Simulation
For a hypothetical entry/exit, use actual reconstructed bid/ask/depth, whole-share quantity, per-side fees, constrained walk across book levels, modeled delays, partial/no fill, and unsettled exposure. Bid quotes alone do not guarantee a marketable fill. Always show 2s, 4s and 8s latency/slippage sensitivity where feasible. Official settlement verifies the outcome, not whether a trading order could have filled.

## Results
Show by coin, rule and period: accepted/excluded windows; buy/resolved/unresolved counts; wins/losses; dollar net and worst single position; tail loss; execution stress; any source inconsistencies. No live readiness from solely simulated P&L.

## Reproducibility controls
Isolate runs in dated folders; do not edit frozen inputs, baselines or prior scores. Save SHA-256 manifests of originals and derived data; store source-to-grid mapping; publish evidence of independent quote parity and every exclusion. See [independent re-audit](OCTOBER_19_2026_REAUDIT.md).
