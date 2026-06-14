# Track 3 Wave 4 — baseline · `typhoon-v2.5-30b-a3b-instruct` (stamp `full`, KB `employees_v02.csv`)

Model: typhoon-v2.5-30b-a3b-instruct (`opentyphoon`) · 626 items × 4 configs.

## Overall pass-rate by config

| config | pass/total | rate | errors |
|---|---|---|---|
| T1 grep | 354/626 |   57% | 0 |
| T2 search | 421/626 |   67% | 1 |
| T3 both | 454/626 |   73% | 0 |
| T4 repl | 375/626 |   60% | 0 |

## Subtype × config matrix

| sub | n | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|--:|
| A1 | 25 |   40% |   84% |   88% |   36% |
| A2 | 20 |    0% |  100% |  100% |   75% |
| A3 | 20 |   75% |  100% |   95% |   75% |
| B1 | 25 |   56% |   12% |   16% |   32% |
| B2 | 30 |   70% |   53% |   57% |   63% |
| B3 | 20 |    0% |   15% |   25% |    0% |
| B5 | 20 |   70% |   60% |   70% |   50% |
| C1 | 25 |   76% |   64% |   76% |   36% |
| C3 | 20 |   75% |   65% |   65% |   50% |
| C4 | 20 |   35% |   65% |   75% |  100% |
| C5 | 24 |   42% |   50% |   54% |   75% |
| C6 | 10 |    0% |   50% |   40% |   80% |
| D1 | 25 |   80% |   72% |   68% |   92% |
| D2 | 25 |   40% |   92% |   84% |   48% |
| D4 | 20 |   70% |   75% |   90% |   85% |
| E1 | 40 |    8% |   40% |   55% |   25% |
| E2 | 10 |   60% |   90% |  100% |   90% |
| E3 | 25 |   80% |   64% |   72% |   56% |
| E5 | 12 |    0% |   25% |   50% |    0% |
| F1 | 20 |   75% |   90% |   85% |   80% |
| F2 | 25 |    4% |   44% |   40% |    0% |
| F3 | 20 |   50% |   60% |   60% |   55% |
| G1 | 20 |   60% |   70% |   80% |   55% |
| G3 | 20 |   80% |   80% |  100% |   50% |
| H1 | 25 |   92% |   76% |   92% |   88% |
| H2 | 25 |  100% |  100% |  100% |  100% |
| H3 | 20 |  100% |  100% |  100% |  100% |
| H4 | 20 |  100% |  100% |  100% |  100% |
| H7 | 15 |   93% |   80% |   93% |   93% |

## Group rollup

| grp | T1 grep | T2 search | T3 both | T4 repl |
|---|--:|--:|--:|--:|
| A |   38% |   94% |   94% |   60% |
| B |   52% |   36% |   42% |   39% |
| C |   52% |   60% |   65% |   66% |
| D |   63% |   80% |   80% |   74% |
| E |   33% |   51% |   64% |   38% |
| F |   40% |   63% |   60% |   42% |
| G |   70% |   75% |   90% |   52% |
| H |   97% |   91% |   97% |   96% |

## retry@T1 (grep-only; cohort B2/B3/B5/F1)

| sub | n | retried | retry% | pass·if-retried | pass·if-not |
|---|--:|--:|--:|--:|--:|
| B2 | 30 | 0 | 0% |   –  (0) |   70% (30) |
| B3 | 20 | 0 | 0% |   –  (0) |    0% (20) |
| B5 | 20 | 0 | 0% |   –  (0) |   70% (20) |
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
| B5 | search | 20 | 0 | 0 |
| C1 | grep | 25 | 0 | 0 |
| C3 | grep | 16 | 3 | 1 |
| C4 | search | 20 | 0 | 0 |
| C5 | grep | 14 | 10 | 0 |
| C6 | either | 10 | 0 | 0 |
| D1 | grep | 21 | 0 | 4 |
| D2 | search | 24 | 0 | 1 |
| D4 | search | 20 | 0 | 0 |
| E1 | search | 40 | 0 | 0 |
| E2 | search | 10 | 0 | 0 |
| E3 | search | 25 | 0 | 0 |
| E5 | search | 12 | 0 | 0 |
| F1 | search | 10 | 2 | 8 |
| F2 | either | 24 | 0 | 1 |
| F3 | search | 20 | 0 | 0 |
| G1 | either | 15 | 0 | 5 |
| G3 | either | 20 | 0 | 0 |
| H1 | either | 0 | 0 | 25 |
| H2 | either | 24 | 0 | 1 |
| H3 | either | 0 | 0 | 20 |
| H4 | either | 0 | 0 | 20 |
| H7 | search | 7 | 0 | 8 |

Tool-choice accuracy (definite-optimal subtypes): **273/461 =   59%** — ⚠️ the aggregate is dominated by the search-default; use the split:
- when **search** is optimal:   89% (260/292)
- when **grep** is optimal:      8% (13/169)  ← real routing signal (does the model leave its search-default?)

## REPL over-use (T4)

Of 375 items correct under T4 repl, **316 (84%)** were also correct under T2 search alone (repl unnecessary).
