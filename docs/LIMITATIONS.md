# Limitations and risk

**Research only. No approved funded trading strategy. No financial advice.**

- Hypothetical bid/ask/depth fills are **not real broker fills**. Liquidity can vanish; fees, latency, partial fills and market access can differ substantially from the model.
- Positions can lose most or all of the amount risked. Attractive mean net profit can hide large single-trade downside.
- Gzip validity does not establish book continuity. A gap during the *preceding* archive can corrupt the next market despite clean JSON.
- Native benchmark update cadence may be ~1s on some coins even where book output is sampled on a 200ms grid.
- Multiple-testing and retrospective selection bias can invalidate a seemingly profitable rule. Reusing validation as a selection criterion requires new untouched future data.
- Settlement records and exchange-confirmed order fills are distinct. Correctly predicting a settlement does not establish executable entry and exit.
- Raw archives, original full historical simulator and redistribution authorization are not available in this public repository yet; independent numerical reproduction remains incomplete.
- This is not a funded order-execution service. No API keys, personal trading information, account operations or order-placement code are required.
- This is **an independent project, not an official OpenAI or Kalshi offering**; its name does not imply endorsement.

Find corrections through GitHub Issues. Historical failures should be documented with versioned errata, not silently rewritten.
