# STAR SEARCH — Independent Crypto Market Anomaly Discovery

**Research software and an auditable methodology for finding, challenging, and rejecting hypotheses in Kalshi 15-minute cryptocurrency markets.**

> **Status: research only. No validated live-trading strategy.** Modeled executions are not exchange-confirmed fills, historical profits are not realized profits, and this project does not place orders. This is an independent community research project, **not an official OpenAI or Kalshi project** and not endorsed by either organization.

## What STAR SEARCH does

STAR SEARCH begins with original recorded market data—not existing paper-trading winners. It follows an evidence-first loop:

1. **Collect** original compressed, timestamped WebSocket recordings for underlying CF Benchmarks prices, Kalshi YES/NO L2 order books, target/strike metadata and market lifecycle records.
2. **Independently audit the recordings**: read every gzip stream, parse every record, check provenance, timing, discontinuities, sequence/gap markers, strike changes and book integrity.
3. **Reconstruct causally** from snapshots and deltas into time-aligned 200 ms book grids, with native underlying tick cadence and strict age limits; never interpolate from the future.
4. **Freeze admissibility before inspecting outcomes**. Record all excluded markets and failure reasons. Never count missing data as a win or quietly change the sample.
5. **Discover anomalies** using training-only spot movement, book repricing, spread, liquidity, strike distance, and lead/lag structure. Define hypotheses *before* consulting held-out P&L.
6. **Simulate executable trades**, not imaginary midpoint prints: bid/ask direction, displayed-depth constraints, order sizing, transaction fees, latency, slippage, partial/no fill and unresolved settlement.
7. **Freeze finalists and challenge them chronologically** on later windows, other dates and execution stress. Retain losing candidates and failure cases.
8. **Report per coin, per rule and per day**, including exclusions, worst individual outcomes, unknowns and provenance. Never promote merely on an attractive pooled win rate.

STAR SEARCH is **not** a Kalshi executor, an account connector, a paper-winner leaderboard, or a bot-arming tool. Existing YES55/paper strategies may be *controls only*, never sources for candidate generation.

## October 19, 2026: why the independent audit matters

The October 19 audit covered seven coins (**ETH, HYPE, BNB, XRP, NEAR, ZEC, DOGE**) and:
- Fully read **756/756 original gzip files**, totaling about **1.67 GB compressed** and **68,573,025 decoded JSON objects**; no gzip corruption or invalid JSON was found.
- Independently reconstructed **749 market windows** from original sources and compared historical valid quote/spot/depth observations with the existing 200 ms grids.
- Found that **362** previously accepted markets included **one falsely accepted ZEC market**. A gap in the *preceding* archive invalidated the carried-forward order book; the market originally marked clean could not be reconstructed continuously.
- Kept **361** markets meeting both the prior conservative screen and the independent raw/grid validation. More intervals reconstructed as usable by the new reader were **not** retroactively inserted into the old sample.
- Repeated discovery on **348 quality-admissible windows** (training + later check + early-morning holdout), with an additional **13 later clean windows** available as a further challenge.
- Evaluated **190** strategy configurations producing modeled fills; **91** met training-only minima. After re-audit, **none of the frozen top 12 finalists** was profitable across both later validation splits.

**Conclusion: zero candidates approved for live deployment.** Earlier apparent successes are preserved as research history, not advertisements for a profitable system. [Full case study](docs/OCTOBER_19_2026_REAUDIT.md).

## Read in order

| Document | Purpose |
|---|---|
| [Research protocol](docs/PROTOCOL.md) | Definitions, quality gates, chronology, executable simulation and versioning |
| [Data contract](docs/DATA_AND_PROVENANCE.md) | Exact source types, chronology, schemas, archive handling and exclusions |
| [October 19 independent re-audit](docs/OCTOBER_19_2026_REAUDIT.md) | Verified counts, discovered warmup fault, corrected selection and limitations |
| [Discovery methodology](docs/DISCOVERY.md) | Outcome-blind features, training/cross-date evaluation, negative results |
| [Reproducing the work](docs/REPRODUCIBILITY.md) | Setup, evidence requirements, available code and current gaps |
| [Limitations and safety](docs/LIMITATIONS.md) | Simulated fills, selection bias, losses, no automated orders |
| [Questions and contributions](CONTRIBUTING.md) | How to file a reproducibility question or propose a new hypothesis |

## Code and data availability

The repository is intended to publish a **portable, inspectable implementation**. Public source-integrity utilities live in `tools/`; research specifications and historical case evidence live in `docs/`. Some historical scripts were written for a private macOS research workstation and need path removal, dependency isolation and independent review before release. **Do not assume every step of the October 19 run is reproducible from this repository alone yet.** Track the remaining work in [reproducibility](docs/REPRODUCIBILITY.md) and repository issues.

**Raw market tapes, API credentials, funded orders, account identifiers, personal paths and third-party datasets are intentionally not committed.** To reproduce historical numerical results exactly, researchers need the original time-aligned recordings and frozen inputs, subject to their rights to access and redistribute them. The documentation provides a manifest/checksum approach so a reader can verify local data without publishing it.

## Expected behavior from contributors

All proposed strategies must come with raw-source quality provenance, frozen definitions, chronology, losing trades, fee/depth/latency assumptions and an untouched later test. Claims of guaranteed income, exchange-verified P&L derived solely from a simulation, or a “winning strategy” without invalid data accounting will not be accepted.

## License and association

Original repository software and documentation are offered under the [MIT License](LICENSE), excluding any third-party datasets, exchange content, logos, credentials, or independently licensed components. “OpenAI” in the repository name denotes the user's naming choice; it does **not** confer OpenAI affiliation, endorsement, ownership or official status.
