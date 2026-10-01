# Track 3 Wave 4 — baseline · `gpt-5.4` (stamp `v10full`, KB `employees_v02.csv`)

Model: gpt-5.4 (`gpt54med`) · 626 items × 4 configs.

## Overall pass-rate by config

| config | pass/total | rate | errors |
|---|---|---|---|
| T1 grep | 610/626 |   97% | 0 |
| T2 search | 610/626 |   97% | 0 |
| T3 both | 615/626 |   98% | 0 |
| T4 repl | 619/626 |   99% | 0 |

## Subtype × config matrix

| sub | n | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|--:|
| A1 | 25 |  100% |   96% |  100% |  100% |
| A2 | 20 |  100% |  100% |  100% |  100% |
| A3 | 20 |  100% |  100% |  100% |  100% |
| B1 | 25 |   96% |   96% |   96% |   96% |
| B2 | 30 |  100% |  100% |  100% |   97% |
| B3 | 20 |   95% |  100% |  100% |  100% |
| B4 | 20 |   95% |   95% |   95% |  100% |
| C1 | 25 |  100% |   96% |  100% |  100% |
| C2 | 20 |  100% |  100% |  100% |  100% |
| C3 | 20 |   95% |  100% |  100% |  100% |
| C4 | 24 |  100% |   96% |  100% |  100% |
| C5 | 10 |   90% |  100% |  100% |  100% |
| D1 | 25 |   96% |   96% |  100% |  100% |
| D2 | 25 |   96% |  100% |  100% |  100% |
| D3 | 20 |  100% |  100% |  100% |  100% |
| E1 | 40 |   88% |   88% |   88% |   90% |
| E2 | 10 |  100% |  100% |  100% |  100% |
| E3 | 25 |   96% |   84% |   84% |  100% |
| E4 | 12 |   83% |  100% |  100% |  100% |
| F1 | 20 |  100% |  100% |  100% |  100% |
| F2 | 25 |  100% |  100% |  100% |  100% |
| F3 | 20 |  100% |  100% |  100% |  100% |
| G1 | 20 |  100% |   95% |  100% |   95% |
| G2 | 20 |  100% |  100% |  100% |  100% |
| H1 | 25 |   96% |  100% |  100% |  100% |
| H2 | 25 |  100% |  100% |  100% |  100% |
| H3 | 20 |  100% |  100% |  100% |  100% |
| H4 | 20 |  100% |  100% |  100% |  100% |
| H5 | 15 |  100% |  100% |  100% |  100% |

## Group rollup

| grp | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|
| A |  100% |   98% |  100% |  100% |
| B |   97% |   98% |   98% |   98% |
| C |   98% |   98% |  100% |  100% |
| D |   97% |   99% |  100% |  100% |
| E |   91% |   90% |   90% |   95% |
| F |  100% |  100% |  100% |  100% |
| G |  100% |   98% |  100% |   98% |
| H |   99% |  100% |  100% |  100% |

## retry@T1 (grep-only; cohort B2/B3/B5/F1)

| sub | n | retried | retry% | pass·if-retried | pass·if-not |
|---|--:|--:|--:|--:|--:|
| B2 | 30 | 14 | 47% |  100% (14) |  100% (16) |
| B3 | 20 | 20 | 100% |   95% (20) |   –  (0) |
| B4 | 20 | 9 | 45% |  100% (9) |   91% (11) |
| F1 | 20 | 6 | 30% |  100% (6) |  100% (14) |

Cohort retry-rate: **49/90 = 54%**

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
| C1 | grep | 25 | 0 | 0 |
| C2 | grep | 20 | 0 | 0 |
| C3 | search | 20 | 0 | 0 |
| C4 | grep | 24 | 0 | 0 |
| C5 | either | 8 | 2 | 0 |
| D1 | grep | 25 | 0 | 0 |
| D2 | search | 25 | 0 | 0 |
| D3 | search | 20 | 0 | 0 |
| E1 | search | 39 | 1 | 0 |
| E2 | search | 10 | 0 | 0 |
| E3 | search | 24 | 1 | 0 |
| E4 | search | 12 | 0 | 0 |
| F1 | search | 13 | 1 | 6 |
| F2 | either | 25 | 0 | 0 |
| F3 | search | 19 | 1 | 0 |
| G1 | either | 20 | 0 | 0 |
| G2 | either | 20 | 0 | 0 |
| H1 | either | 0 | 0 | 25 |
| H2 | either | 25 | 0 | 0 |
| H3 | either | 0 | 0 | 20 |
| H4 | either | 0 | 0 | 20 |
| H5 | search | 15 | 0 | 0 |

Tool-choice accuracy (definite-optimal subtypes): **282/461 =   61%** — ⚠️ the aggregate is dominated by the search-default; use the split:
- when **search** is optimal:   97% (282/292)
- when **grep** is optimal:      0% (0/169)  ← real routing signal (does the model leave its search-default?)

## REPL over-use (T4)

Of 619 items correct under T4 repl, **605 (98%)** were also correct under T2 search alone (repl unnecessary).
