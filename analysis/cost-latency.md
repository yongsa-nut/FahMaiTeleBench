# Track 3 — cost & latency

Per-model efficiency over the FahMai matrix (cost = tokens × Track-1 OpenRouter rates).

**Caveats:** (1) **Typhoon is free** ($0); its endpoint omits `usage` on most calls so its OUTPUT-token count is under-reported — irrelevant to cost. (2) **Sonnet was run via Anthropic Message Batches** (50% billing, applied) — batch `elapsed_ms` is round-trip, so Sonnet has **no per-item latency** (would need a sequential re-run). Configs with median elapsed > 60 s are auto-flagged `batch`. (3) gpt-5.4 price is an **estimate** — confirm.

## Per-model rollup

| model | items | errors | in-tok | out-tok | cost (4 cfg) | $/item | latency med / p90 |
|---|--:|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | 1878 | 20 | 23,076,585 | 944,565 | $2.497 | $0.001 | 8.6s / 28.0s |
| deepseekv4pro | 1878 | 12 | 19,451,132 | 895,300 | $9.240 | $0.005 | 10.2s / 24.0s |
| gemini30flash | 1878 | 3 | 10,420,124 | 286,601 | $6.070 | $0.003 | 4.4s / 9.3s |
| gemma4 | 1878 | 76 | 12,483,260 | 207,192 | $1.575 | $0.001 | 6.1s / 25.7s |
| glm51 | 1878 | 27 | 19,470,773 | 664,131 | $21.127 ⚠est | $0.011 | 11.3s / 24.0s |
| gpt54med | 2504 | 0 | 23,938,784 | 862,393 | $68.471 ⚠est | $0.027 | 5.7s / 11.5s |
| gpt55low | 2504 | 144 | 28,693,923 | 789,318 | $167.149 | $0.067 | 6.9s / 24.6s |
| gpt55med | 2504 | 203 | 29,623,107 | 910,441 | $175.429 ⚠est | $0.070 | 6.9s / 25.9s |
| minimax | 1878 | 24 | 18,084,545 | 960,035 | $6.198 | $0.003 | 11.8s / 29.4s |
| openthaigpt | 2504 | 0 | 6,212,817 | 1,633,130 | free | free | 3.5s / 17.0s |
| opentyphoon | 2504 | 7 | 4,611,793 | 38,593 | free | free | 0.7s / 3.5s |
| sonnet | 2504 | 2 | 16,848,095 | 783,346 | $31.147 | $0.012 | batch (n/a) |

## Per-config detail

| model | config | items | err | in-tok | out-tok | cost | median lat |
|---|---|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | t1_grep | 626 | 10 | 12,606,628 | 362,334 | $1.333 | 10.6s |
| deepseekv4flash | t2_search | 626 | 0 | 6,622,622 | 258,186 | $0.714 | 6.8s |
| deepseekv4flash | t4_repl | 626 | 10 | 3,847,335 | 324,045 | $0.450 | 9.5s |
| deepseekv4pro | t1_grep | 626 | 10 | 10,958,561 | 371,694 | $5.090 | 13.0s |
| deepseekv4pro | t2_search | 626 | 0 | 5,242,926 | 252,456 | $2.500 | 9.8s |
| deepseekv4pro | t4_repl | 626 | 2 | 3,249,645 | 271,150 | $1.649 | 7.8s |
| gemini30flash | t1_grep | 626 | 2 | 4,180,082 | 71,600 | $2.305 | 4.8s |
| gemini30flash | t2_search | 626 | 0 | 3,847,046 | 133,726 | $2.325 | 4.3s |
| gemini30flash | t4_repl | 626 | 1 | 2,392,996 | 81,275 | $1.440 | 4.1s |
| gemma4 | t1_grep | 626 | 71 | 4,718,675 | 55,237 | $0.587 | 7.7s |
| gemma4 | t2_search | 626 | 5 | 5,356,849 | 63,119 | $0.666 | 4.4s |
| gemma4 | t4_repl | 626 | 0 | 2,407,736 | 88,836 | $0.322 | 7.2s |
| glm51 | t1_grep | 626 | 10 | 10,696,156 | 264,382 | $11.297 | 11.1s |
| glm51 | t2_search | 626 | 0 | 4,887,368 | 193,634 | $5.386 | 10.0s |
| glm51 | t4_repl | 626 | 17 | 3,887,249 | 206,115 | $4.444 | 12.8s |
| gpt54med | t1_grep | 626 | 0 | 8,796,805 | 220,182 | $24.194 | 5.5s |
| gpt54med | t2_search | 626 | 0 | 5,014,164 | 210,245 | $14.638 | 5.4s |
| gpt54med | t3_both | 626 | 0 | 7,198,514 | 211,884 | $20.115 | 6.0s |
| gpt54med | t4_repl | 626 | 0 | 2,929,301 | 220,082 | $9.524 | 6.1s |
| gpt55low | t1_grep | 626 | 1 | 6,620,758 | 93,135 | $35.898 | 4.5s |
| gpt55low | t2_search | 626 | 130 | 10,417,662 | 355,647 | $62.758 | 10.9s |
| gpt55low | t3_both | 626 | 12 | 9,411,818 | 235,040 | $54.110 | 10.4s |
| gpt55low | t4_repl | 626 | 1 | 2,243,685 | 105,496 | $14.383 | 5.0s |
| gpt55med | t1_grep | 626 | 0 | 8,065,730 | 128,363 | $44.180 | 5.0s |
| gpt55med | t2_search | 626 | 180 | 9,618,668 | 410,391 | $60.405 | 10.7s |
| gpt55med | t3_both | 626 | 22 | 9,523,207 | 237,405 | $54.738 | 8.6s |
| gpt55med | t4_repl | 626 | 1 | 2,415,502 | 134,282 | $16.106 | 5.3s |
| minimax | t1_grep | 626 | 8 | 7,386,732 | 350,669 | $2.482 | 9.3s |
| minimax | t2_search | 626 | 4 | 6,663,353 | 277,376 | $2.192 | 12.4s |
| minimax | t4_repl | 626 | 12 | 4,034,460 | 331,990 | $1.524 | 13.3s |
| openthaigpt | t1_grep | 626 | 0 | 1,288,758 | 378,364 | free | 2.9s |
| openthaigpt | t2_search | 626 | 0 | 1,733,593 | 484,798 | free | 4.5s |
| openthaigpt | t3_both | 626 | 0 | 2,190,207 | 399,425 | free | 3.9s |
| openthaigpt | t4_repl | 626 | 0 | 1,000,259 | 370,543 | free | 3.2s |
| opentyphoon | t1_grep | 626 | 1 | 1,153,397 | 8,212 | free | 0.6s |
| opentyphoon | t2_search | 626 | 2 | 1,058,909 | 9,461 | free | 0.7s |
| opentyphoon | t3_both | 626 | 4 | 2,188,590 | 10,572 | free | 0.8s |
| opentyphoon | t4_repl | 626 | 0 | 210,897 | 10,348 | free | 0.8s |
| sonnet | t1_grep | 626 | 1 | 6,705,797 | 197,311 | $11.539 | batch |
| sonnet | t2_search | 626 | 0 | 4,381,544 | 188,790 | $7.988 | batch |
| sonnet | t3_both | 626 | 0 | 4,712,839 | 186,503 | $8.468 | batch |
| sonnet | t4_repl | 626 | 1 | 1,047,915 | 210,742 | $3.152 | batch |

_⚠est = price is an estimate (confirm). batch = Anthropic Message Batches: 50% billing, elapsed is round-trip not per-item latency._