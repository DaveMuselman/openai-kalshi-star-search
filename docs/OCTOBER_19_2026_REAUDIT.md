# October 19, 2026: Independent raw-source re-audit

This documents a **historical local research run**, not an assertion that the private original recordings are available for download.

## Why it mattered

The earlier discovery relied on historical QA flags and derived grids rather than independently reading all original compressed recordings. The corrected run audited every original compressed archive and replayed the books as a continuous source stream, including each market's preceding warmup period.

| Evidence | Verified count |
|---|---:|
| Expected / fully read gzip archives | 756 / 756 |
| Original compressed bytes | 1,673,409,354 |
| Decoded JSON objects | 68,573,025 |
| Corrupt gzip / malformed JSON | 0 / 0 |
| Markets independently reconstructed | 749 |
| Markets accepted before re-audit | 362 |
| Prior-accepted markets surviving independent checks | **361** |

For all **361 surviving markets**, old valid bid, ask, depth and underlying-price-relative observations agreed with the independent reconstruction within comparison tolerances. The new reconstruction also found some usable intervals omitted by the old conservative process; these were **not backfilled** into its frozen test set.

## Discovered defect: a broken ZEC warmup

The market `KXZEC15M-26OCT190200-00` opened **October 19 at 1:45 a.m. Eastern**. The preceding 1:30 a.m. archive contained a **5,045 millisecond reception gap** at about 1:38:19–1:38:24 Eastern, *after* the upcoming market's book snapshot. There was no replacement snapshot for that ticker early enough to prove uninterrupted book state.

The old derived grid had **3,957 apparently valid rows**. A strict independent continuous replay found **zero valid rows**. This invalidated one previously accepted ZEC market and at least one previously modeled S1 trade. Across all coins, 14 adjacent markets showed this type of warmup concern; 13 were already excluded.

Source-level checks additionally flagged 56 instances without usable strike evidence, seven current-archive severe clock regressions and seven current-archive receive gaps greater than five seconds. These counts describe different failure dimensions and are not a sum of mutually exclusive archive failures.

## Corrected research

The independently source-admitted set contained **361 markets**. Of these, **348** were in the historical training/check/holdout splits; 13 later markets were available for an additional challenge.

| Fold | Markets |
|---|---:|
| TRAIN | 257 |
| CHECK | 52 |
| HOLDOUT | 39 |
| Later clean windows | 13 |

The corrected discovery search found modeled fills for **190 configurations**; **91** passed training-only criteria. The previously interesting `YES_50_PLUS15_S1_SPOT_ACCEL_CONTRACT_STALL` dropped to **training rank 14**, outside the top 12 selected on TRAIN.

For historical clarity, that S1 candidate still produced **68 modeled TRAIN buys / 61 wins / +$133.8677**, **11 CHECK buys / 9 wins / +$14.4115**, and **7 HOLDOUT buys / 6 wins / +$10.6061**. These are model outputs, **not actual realized returns**, and selecting S1 retrospectively from validation results is not independent validation.

**None of the newly TRAIN-frozen top 12 finalists was profitable in both CHECK and HOLDOUT. No strategy passed promotion to funded deployment.**

## What is needed to independently reproduce every number?

Lawfully available original compressed streams, original archive checksums, official settlement evidence, frozen derived grids, the historical parser and executable fee/depth/latency model, feature search specifications and the isolated chronological score files. This public repository does **not** yet contain the full historical replay implementation or source archives. See [reproducibility](REPRODUCIBILITY.md). No live accounts or order systems were modified during the audit.
