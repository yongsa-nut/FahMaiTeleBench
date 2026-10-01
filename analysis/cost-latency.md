# Track 3 — cost & latency

Per-model efficiency over the FahMai matrix (cost = tokens × Track-1 OpenRouter rates).

**Caveats:** (1) **Typhoon is free** ($0); its endpoint omits `usage` on most calls so its OUTPUT-token count is under-reported — irrelevant to cost. (2) **Sonnet was run via Anthropic Message Batches** (50% billing, applied) — batch `elapsed_ms` is round-trip, so Sonnet has **no per-item latency** (would need a sequential re-run). Configs with median elapsed > 60 s are auto-flagged `batch`. (3) gpt-5.4 price is an **estimate** — confirm.

## Per-model rollup

| model | items | errors | in-tok | out-tok | cost (4 cfg) | $/item | latency med / p90 |
|---|--:|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | 2504 | 13 | 29,113,506 | 1,188,395 | $3.149 | $0.001 | 6.5s / 23.8s |
| deepseekv4pro | 2504 | 14 | 25,802,005 | 1,123,050 | $12.201 | $0.005 | 8.9s / 21.7s |
| gemini30flash | 2504 | 5 | 15,645,557 | 493,085 | $9.302 | $0.004 | 4.1s / 8.4s |
| gemma4 | 2504 | 2 | 19,788,965 | 276,714 | $2.477 | $0.001 | 5.5s / 22.2s |
| glm51 | 2504 | 26 | 25,711,106 | 882,671 | $27.916 ⚠est | $0.011 | 11.7s / 24.5s |
| gpt54med | 2504 | 0 | 21,214,372 | 852,881 | $61.565 ⚠est | $0.025 | 5.9s / 11.7s |
| gpt55low | 2504 | 143 | 27,906,073 | 788,541 | $163.187 | $0.065 | 6.8s / 24.0s |
| gpt55med | 2504 | 205 | 28,652,929 | 911,068 | $170.597 ⚠est | $0.068 | 6.8s / 25.1s |
| minimax | 2504 | 31 | 28,925,229 | 1,234,404 | $9.551 | $0.004 | 10.6s / 27.3s |
| opentyphoon | 2504 | 7 | 6,556,444 | 63,804 | free | free | 0.8s / 3.6s |
| sonnet | 2504 | 1 | 13,835,470 | 779,372 | $26.598 | $0.011 | batch (n/a) |
| typhoon8b | 2504 | 24 | 13,487,503 | 372,040 | free | free | 1.3s / 4.2s |

## Per-config detail

| model | config | items | err | in-tok | out-tok | cost | median lat |
|---|---|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | t1_grep | 626 | 6 | 11,506,413 | 379,401 | $1.227 | 9.5s |
| deepseekv4flash | t2_search | 626 | 1 | 6,378,449 | 254,455 | $0.689 | 6.5s |
| deepseekv4flash | t3_both | 626 | 0 | 7,509,770 | 255,074 | $0.802 | 3.8s |
| deepseekv4flash | t4_repl | 626 | 6 | 3,718,874 | 299,465 | $0.432 | 8.8s |
| deepseekv4pro | t1_grep | 626 | 8 | 10,139,749 | 374,766 | $4.737 | 11.9s |
| deepseekv4pro | t2_search | 626 | 0 | 5,364,634 | 242,178 | $2.544 | 9.5s |
| deepseekv4pro | t3_both | 626 | 4 | 7,105,614 | 248,273 | $3.307 | 7.1s |
| deepseekv4pro | t4_repl | 626 | 2 | 3,192,008 | 257,833 | $1.613 | 7.8s |
| gemini30flash | t1_grep | 626 | 3 | 4,386,536 | 118,994 | $2.550 | 4.6s |
| gemini30flash | t2_search | 626 | 2 | 3,893,390 | 156,641 | $2.417 | 4.2s |
| gemini30flash | t3_both | 626 | 0 | 4,969,745 | 135,727 | $2.892 | 3.5s |
| gemini30flash | t4_repl | 626 | 0 | 2,395,886 | 81,723 | $1.443 | 4.1s |
| gemma4 | t1_grep | 626 | 0 | 5,598,776 | 59,646 | $0.694 | 5.5s |
| gemma4 | t2_search | 626 | 0 | 5,276,323 | 62,992 | $0.656 | 4.3s |
| gemma4 | t3_both | 626 | 2 | 6,505,152 | 65,562 | $0.805 | 5.2s |
| gemma4 | t4_repl | 626 | 0 | 2,408,714 | 88,514 | $0.322 | 7.0s |
| glm51 | t1_grep | 626 | 9 | 10,643,525 | 270,920 | $11.265 | 11.5s |
| glm51 | t2_search | 626 | 0 | 4,890,672 | 196,205 | $5.397 | 10.6s |
| glm51 | t3_both | 626 | 2 | 6,266,936 | 205,208 | $6.774 | 11.8s |
| glm51 | t4_repl | 626 | 15 | 3,909,973 | 210,338 | $4.480 | 13.3s |
| gpt54med | t1_grep | 626 | 0 | 7,268,782 | 216,053 | $20.332 | 5.6s |
| gpt54med | t2_search | 626 | 0 | 4,979,534 | 208,500 | $14.534 | 5.6s |
| gpt54med | t3_both | 626 | 0 | 6,021,594 | 208,212 | $17.136 | 6.1s |
| gpt54med | t4_repl | 626 | 0 | 2,944,462 | 220,116 | $9.562 | 6.1s |
| gpt55low | t1_grep | 626 | 0 | 6,340,906 | 91,854 | $34.460 | 4.4s |
| gpt55low | t2_search | 626 | 134 | 10,255,719 | 361,828 | $62.133 | 11.0s |
| gpt55low | t3_both | 626 | 9 | 9,065,671 | 229,587 | $52.216 | 9.6s |
| gpt55low | t4_repl | 626 | 0 | 2,243,777 | 105,272 | $14.377 | 4.9s |
| gpt55med | t1_grep | 626 | 0 | 7,767,872 | 128,019 | $42.680 | 5.0s |
| gpt55med | t2_search | 626 | 186 | 9,239,169 | 415,422 | $58.659 | 10.5s |
| gpt55med | t3_both | 626 | 19 | 9,227,823 | 233,079 | $53.131 | 8.6s |
| gpt55med | t4_repl | 626 | 0 | 2,418,065 | 134,548 | $16.127 | 5.2s |
| minimax | t1_grep | 626 | 9 | 7,686,639 | 354,013 | $2.569 | 8.9s |
| minimax | t2_search | 626 | 4 | 6,759,718 | 276,717 | $2.218 | 11.4s |
| minimax | t3_both | 626 | 6 | 10,512,469 | 277,555 | $3.266 | 9.9s |
| minimax | t4_repl | 626 | 12 | 3,966,403 | 326,119 | $1.498 | 12.6s |
| opentyphoon | t1_grep | 626 | 1 | 1,784,302 | 12,302 | free | 0.7s |
| opentyphoon | t2_search | 626 | 2 | 1,633,006 | 15,696 | free | 0.8s |
| opentyphoon | t3_both | 626 | 3 | 2,697,083 | 16,598 | free | 0.8s |
| opentyphoon | t4_repl | 626 | 1 | 442,053 | 19,208 | free | 0.8s |
| sonnet | t1_grep | 626 | 0 | 6,114,070 | 199,857 | $10.670 | batch |
| sonnet | t2_search | 626 | 0 | 2,911,031 | 185,887 | $5.761 | batch |
| sonnet | t3_both | 626 | 0 | 3,748,142 | 184,053 | $7.003 | batch |
| sonnet | t4_repl | 626 | 1 | 1,062,227 | 209,575 | $3.165 | batch |
| typhoon8b | t1_grep | 626 | 1 | 2,858,845 | 87,244 | free | 1.3s |
| typhoon8b | t2_search | 626 | 7 | 3,725,741 | 91,693 | free | 1.0s |
| typhoon8b | t3_both | 626 | 11 | 4,729,786 | 90,599 | free | 1.3s |
| typhoon8b | t4_repl | 626 | 5 | 2,173,131 | 102,504 | free | 1.6s |

_⚠est = price is an estimate (confirm). batch = Anthropic Message Batches: 50% billing, elapsed is round-trip not per-item latency._