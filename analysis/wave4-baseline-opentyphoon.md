# Track 3 Wave 4 — baseline · `typhoon-v2.5-30b-a3b-instruct` (stamp `v10full`, KB `employees_v02.csv`)

Model: typhoon-v2.5-30b-a3b-instruct (`opentyphoon`) · 626 items × 4 configs.

## Overall pass-rate by config

| config | pass/total | rate | errors |
|---|---|---|---|
| T1 grep | 362/626 |   58% | 0 |
| T2 search | 435/626 |   69% | 0 |
| T3 both | 465/626 |   74% | 0 |
| T4 repl | 379/626 |   61% | 0 |

## Subtype × config matrix

| sub | n | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|--:|
| A1 | 25 |   40% |   84% |   88% |   36% |
| A2 | 20 |    0% |  100% |  100% |   75% |
| A3 | 20 |   75% |  100% |   95% |   75% |
| B1 | 25 |   60% |   12% |   12% |   32% |
| B2 | 30 |   67% |   53% |   57% |   67% |
| B3 | 20 |    0% |   15% |   25% |    0% |
| B4 | 20 |   45% |   65% |   75% |   40% |
| C1 | 25 |   80% |   68% |   92% |   48% |
| C2 | 20 |   75% |   65% |   65% |   50% |
| C3 | 20 |   30% |   60% |   55% |  100% |
| C4 | 24 |   96% |   96% |   96% |   96% |
| C5 | 10 |   10% |   70% |   50% |   70% |
| D1 | 25 |   80% |   72% |   68% |   92% |
| D2 | 25 |   40% |   92% |   84% |   48% |
| D3 | 20 |   70% |   75% |   90% |   85% |
| E1 | 40 |    8% |   40% |   55% |   25% |
| E2 | 10 |   60% |   90% |  100% |   90% |
| E3 | 25 |   88% |   60% |   72% |   56% |
| E4 | 12 |    0% |   33% |   33% |    0% |
| F1 | 20 |   75% |   90% |   85% |   80% |
| F2 | 25 |    4% |   44% |   40% |    0% |
| F3 | 20 |   35% |   60% |   60% |   50% |
| G1 | 20 |   60% |   70% |   90% |   50% |
| G2 | 20 |   80% |   80% |  100% |   50% |
| H1 | 25 |   92% |   76% |   92% |   88% |
| H2 | 25 |  100% |  100% |  100% |  100% |
| H3 | 20 |  100% |  100% |  100% |  100% |
| H4 | 20 |  100% |  100% |  100% |  100% |
| H5 | 15 |   93% |   80% |   93% |   93% |

## Group rollup

| grp | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|
| A |   38% |   94% |   94% |   60% |
| B |   46% |   37% |   42% |   38% |
| C |   66% |   73% |   76% |   73% |
| D |   63% |   80% |   80% |   74% |
| E |   36% |   51% |   62% |   38% |
| F |   35% |   63% |   60% |   40% |
| G |   70% |   75% |   95% |   50% |
| H |   97% |   91% |   97% |   96% |

## retry@T1 (grep-only; cohort B2/B3/B5/F1)

| sub | n | retried | retry% | pass·if-retried | pass·if-not |
|---|--:|--:|--:|--:|--:|
| B2 | 30 | 0 | 0% |   –  (0) |   67% (30) |
| B3 | 20 | 0 | 0% |   –  (0) |    0% (20) |
| B4 | 20 | 0 | 0% |   –  (0) |   45% (20) |
| F1 | 20 | 0 | 0% |   –  (0) |   75% (20) |

Cohort retry-rate: **0/90 = 0%**

## tool-choice@T3 (first tool when both offered)

| sub | optimal | search | grep | none |
|---|---|--:|--:|--:|
| A1 | search | 25 | 0 | 0 |
| A2 | search | 20 | 0 | 0 |
| A3 | search | 7 | 13 | 0 |
| B1 | grep | 24 | 0 | 1 |
| B2 | grep | 24 | 0 | 6 |
| B3 | grep | 20 | 0 | 0 |
| B4 | search | 20 | 0 | 0 |
| C1 | grep | 25 | 0 | 0 |
| C2 | grep | 16 | 3 | 1 |
| C3 | search | 20 | 0 | 0 |
| C4 | grep | 14 | 10 | 0 |
| C5 | either | 10 | 0 | 0 |
| D1 | grep | 21 | 0 | 4 |
| D2 | search | 24 | 0 | 1 |
| D3 | search | 20 | 0 | 0 |
| E1 | search | 40 | 0 | 0 |
| E2 | search | 10 | 0 | 0 |
| E3 | search | 25 | 0 | 0 |
| E4 | search | 12 | 0 | 0 |
| F1 | search | 10 | 2 | 8 |
| F2 | either | 24 | 0 | 1 |
| F3 | search | 20 | 0 | 0 |
| G1 | either | 18 | 0 | 2 |
| G2 | either | 20 | 0 | 0 |
| H1 | either | 0 | 0 | 25 |
| H2 | either | 24 | 0 | 1 |
| H3 | either | 0 | 0 | 20 |
| H4 | either | 0 | 0 | 20 |
| H5 | search | 7 | 0 | 8 |

Tool-choice accuracy (definite-optimal subtypes): **273/461 =   59%** — ⚠️ the aggregate is dominated by the search-default; use the split:
- when **search** is optimal:   89% (260/292)
- when **grep** is optimal:      8% (13/169)  ← real routing signal (does the model leave its search-default?)

## REPL over-use (T4)

Of 379 items correct under T4 repl, **326 (86%)** were also correct under T2 search alone (repl unnecessary).
