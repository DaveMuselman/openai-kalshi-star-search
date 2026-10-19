# Independent anomaly discovery

The research begins with **source-vetted underlying market movements and Kalshi order-book reactions**, not pre-existing paper trading winners.

Outcome-blind feature families include spot movement at 5s and 10s, acceleration, YES/NO bid reaction, quote stalling or repricing, near-strike distance, spread, depth imbalance, liquidity and entry timing. Candidate conditions are frozen using TRAIN-only source observations **before outcome-based filtering**.

The historical October 19 search combined 12 original feature ideas with YES/NO sides, price caps, exit targets and time/depth checks; **190 configurations generated modeled trades**. Simulation is book-depth- and fee-aware, with explicit latency/slippage stress, no-fill handling and official settlement proxies for positions that cannot exit.

Do not change thresholds based on later results and still call those later results untouched validation. Archive all failed trials. Report per-coin trade counts, net, adverse individual losses, chronological CHECK and HOLDOUT performance, and later observation dates.

The stalled-YES-bid / accelerating-spot example was **exploratory only**. Re-auditing the original compressed ZEC sources changed the eligible sample and ranking. The corrected TRAIN-frozen top 12 produced **no strategy with positive results on both later validation periods**.

See [protocol](PROTOCOL.md), [historical re-audit](OCTOBER_19_2026_REAUDIT.md) and [limitations](LIMITATIONS.md).
