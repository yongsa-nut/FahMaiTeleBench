# Track 3 Wave 4 — baseline · `claude-sonnet-4-6` (stamp `v10full`, KB `employees_v02.csv`)

Model: claude-sonnet-4-6 (`sonnet`) · 626 items × 4 configs.

## Overall pass-rate by config

| config | pass/total | rate | errors |
|---|---|---|---|
| T1 grep | 588/626 |   94% | 0 |
| T2 search | 585/626 |   93% | 0 |
| T3 both | 595/626 |   95% | 0 |
| T4 repl | 576/626 |   92% | 0 |

## Subtype × config matrix

| sub | n | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|--:|
| A1 | 25 |   96% |   96% |   96% |   96% |
| A2 | 20 |  100% |  100% |  100% |  100% |
| A3 | 20 |  100% |  100% |  100% |  100% |
| B1 | 25 |  100% |   92% |   92% |   80% |
| B2 | 30 |  100% |  100% |  100% |   97% |
| B3 | 20 |   90% |   50% |   70% |   65% |
| B4 | 20 |   95% |   90% |   95% |   95% |
| C1 | 25 |  100% |   96% |   96% |  100% |
| C2 | 20 |   85% |  100% |  100% |   95% |
| C3 | 20 |   95% |   85% |   80% |  100% |
| C4 | 24 |  100% |  100% |  100% |  100% |
| C5 | 10 |   60% |   90% |  100% |  100% |
| D1 | 25 |   96% |  100% |  100% |   96% |
| D2 | 25 |   96% |   96% |  100% |   88% |
| D3 | 20 |  100% |  100% |  100% |  100% |
| E1 | 40 |   70% |   78% |   78% |   78% |
| E2 | 10 |  100% |  100% |  100% |  100% |
| E3 | 25 |   88% |   92% |   88% |   88% |
| E4 | 12 |  100% |  100% |  100% |   67% |
| F1 | 20 |   90% |  100% |  100% |   90% |
| F2 | 25 |  100% |  100% |  100% |   88% |
| F3 | 20 |   85% |   65% |   80% |   85% |
| G1 | 20 |   85% |   90% |  100% |   85% |
| G2 | 20 |  100% |  100% |  100% |   95% |
| H1 | 25 |  100% |  100% |  100% |  100% |
| H2 | 25 |   96% |  100% |  100% |  100% |
| H3 | 20 |  100% |  100% |  100% |  100% |
| H4 | 20 |  100% |  100% |  100% |  100% |
| H5 | 15 |  100% |  100% |  100% |   87% |

## Group rollup

| grp | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|
| A |   98% |   98% |   98% |   98% |
| B |   97% |   85% |   91% |   85% |
| C |   92% |   95% |   95% |   99% |
| D |   97% |   99% |  100% |   94% |
| E |   83% |   87% |   86% |   82% |
| F |   92% |   89% |   94% |   88% |
| G |   92% |   95% |  100% |   90% |
| H |   99% |  100% |  100% |   98% |

## retry@T1 (grep-only; cohort B2/B3/B5/F1)

| sub | n | retried | retry% | pass·if-retried | pass·if-not |
|---|--:|--:|--:|--:|--:|
| B2 | 30 | 7 | 23% |  100% (7) |  100% (23) |
| B3 | 20 | 19 | 95% |   95% (19) |    0% (1) |
| B4 | 20 | 10 | 50% |   90% (10) |  100% (10) |
| F1 | 20 | 3 | 15% |  100% (3) |   88% (17) |

Cohort retry-rate: **39/90 = 43%**

## tool-choice@T3 (first tool when both offered)

| sub | optimal | search | grep | none |
|---|---|--:|--:|--:|
| A1 | search | 25 | 0 | 0 |
| A2 | search | 20 | 0 | 0 |
| A3 | search | 20 | 0 | 0 |
| B1 | grep | 25 | 0 | 0 |
| B2 | grep | 30 | 0 | 0 |
| B3 | grep | 20 | 0 | 0 |
| B4 | search | 20 | 0 | 0 |
| C1 | grep | 23 | 2 | 0 |
| C2 | grep | 20 | 0 | 0 |
| C3 | search | 20 | 0 | 0 |
| C4 | grep | 24 | 0 | 0 |
| C5 | either | 8 | 2 | 0 |
| D1 | grep | 25 | 0 | 0 |
| D2 | search | 25 | 0 | 0 |
| D3 | search | 20 | 0 | 0 |
| E1 | search | 40 | 0 | 0 |
| E2 | search | 10 | 0 | 0 |
| E3 | search | 25 | 0 | 0 |
| E4 | search | 12 | 0 | 0 |
| F1 | search | 12 | 1 | 7 |
| F2 | either | 25 | 0 | 0 |
| F3 | search | 20 | 0 | 0 |
| G1 | either | 20 | 0 | 0 |
| G2 | either | 20 | 0 | 0 |
| H1 | either | 0 | 0 | 25 |
| H2 | either | 25 | 0 | 0 |
| H3 | either | 0 | 0 | 20 |
| H4 | either | 0 | 0 | 20 |
| H5 | search | 15 | 0 | 0 |

Tool-choice accuracy (definite-optimal subtypes): **286/461 =   62%** — ⚠️ the aggregate is dominated by the search-default; use the split:
- when **search** is optimal:   97% (284/292)
- when **grep** is optimal:      1% (2/169)  ← real routing signal (does the model leave its search-default?)

## REPL over-use (T4)

Of 576 items correct under T4 repl, **556 (97%)** were also correct under T2 search alone (repl unnecessary).
