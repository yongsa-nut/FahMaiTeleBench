# Track 3 — cost & latency

Per-model efficiency over the FahMai matrix (cost = tokens × Track-1 OpenRouter rates).

**Caveats:** (1) **Typhoon is free** ($0); its endpoint omits `usage` on most calls so its OUTPUT-token count is under-reported — irrelevant to cost. (2) **Sonnet was run via Anthropic Message Batches** (50% billing, applied) — batch `elapsed_ms` is round-trip, so Sonnet has **no per-item latency** (would need a sequential re-run). Configs with median elapsed > 60 s are auto-flagged `batch`. (3) gpt-5.4 price is an **estimate** — confirm.

## Per-model rollup

| model | items | errors | in-tok | out-tok | cost (4 cfg) | $/item | latency med / p90 |
|---|--:|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | 2504 | 17 | 29,167,411 | 1,182,809 | $3.153 | $0.001 | 6.6s / 24.7s |
| deepseekv4pro | 2504 | 14 | 26,222,151 | 1,154,826 | $12.411 | $0.005 | 9.3s / 22.2s |
| gemini30flash | 2504 | 3 | 15,358,902 | 446,129 | $9.018 | $0.004 | 4.1s / 8.7s |
| gemma4 | 2504 | 2 | 19,794,315 | 275,760 | $2.477 | $0.001 | 5.8s / 23.0s |
| glm51 | 2504 | 28 | 25,791,530 | 866,819 | $27.946 ⚠est | $0.011 | 11.3s / 23.6s |
| gpt54med | 2504 | 0 | 23,938,784 | 862,393 | $68.471 ⚠est | $0.027 | 5.7s / 11.5s |
| gpt55low | 2504 | 140 | 28,702,244 | 789,350 | $167.192 | $0.067 | 6.9s / 24.6s |
| gpt55med | 2504 | 201 | 29,626,857 | 910,457 | $175.448 ⚠est | $0.070 | 6.9s / 25.9s |
| minimax | 2504 | 29 | 28,563,423 | 1,232,930 | $9.449 | $0.004 | 11.4s / 28.8s |
| opentyphoon | 2504 | 6 | 4,673,289 | 38,794 | free | free | 0.7s / 3.5s |
| sonnet | 2504 | 2 | 16,848,095 | 783,346 | $31.147 | $0.012 | batch (n/a) |
| typhoon8b | 2504 | 23 | 13,650,862 | 386,848 | free | free | 1.3s / 4.2s |

## Per-config detail

| model | config | items | err | in-tok | out-tok | cost | median lat |
|---|---|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | t1_grep | 626 | 9 | 11,617,148 | 355,199 | $1.233 | 10.6s |
| deepseekv4flash | t2_search | 626 | 0 | 6,622,622 | 258,186 | $0.714 | 6.8s |
| deepseekv4flash | t3_both | 626 | 1 | 7,098,786 | 255,330 | $0.761 | 3.6s |
| deepseekv4flash | t4_repl | 626 | 7 | 3,828,855 | 314,094 | $0.446 | 9.5s |
| deepseekv4pro | t1_grep | 626 | 9 | 10,778,956 | 370,519 | $5.011 | 13.0s |
| deepseekv4pro | t2_search | 626 | 0 | 5,242,926 | 252,456 | $2.500 | 9.8s |
| deepseekv4pro | t3_both | 626 | 3 | 6,950,624 | 260,701 | $3.250 | 7.0s |
| deepseekv4pro | t4_repl | 626 | 2 | 3,249,645 | 271,150 | $1.649 | 7.8s |
| gemini30flash | t1_grep | 626 | 1 | 4,182,270 | 71,720 | $2.306 | 4.8s |
| gemini30flash | t2_search | 626 | 0 | 3,847,046 | 133,726 | $2.325 | 4.3s |
| gemini30flash | t3_both | 626 | 1 | 4,936,590 | 159,408 | $2.947 | 3.5s |
| gemini30flash | t4_repl | 626 | 1 | 2,392,996 | 81,275 | $1.440 | 4.1s |
| gemma4 | t1_grep | 626 | 0 | 5,473,133 | 59,753 | $0.679 | 6.2s |
| gemma4 | t2_search | 626 | 0 | 5,391,517 | 63,504 | $0.670 | 4.4s |
| gemma4 | t3_both | 626 | 2 | 6,521,929 | 63,667 | $0.806 | 5.3s |
| gemma4 | t4_repl | 626 | 0 | 2,407,736 | 88,836 | $0.322 | 7.2s |
| glm51 | t1_grep | 626 | 10 | 10,696,156 | 264,381 | $11.297 | 11.1s |
| glm51 | t2_search | 626 | 0 | 4,887,368 | 193,634 | $5.386 | 10.0s |
| glm51 | t3_both | 626 | 1 | 6,320,757 | 202,689 | $6.819 | 11.2s |
| glm51 | t4_repl | 626 | 17 | 3,887,249 | 206,115 | $4.444 | 12.8s |
| gpt54med | t1_grep | 626 | 0 | 8,796,805 | 220,182 | $24.194 | 5.5s |
| gpt54med | t2_search | 626 | 0 | 5,014,164 | 210,245 | $14.638 | 5.4s |
| gpt54med | t3_both | 626 | 0 | 7,198,514 | 211,884 | $20.115 | 6.0s |
| gpt54med | t4_repl | 626 | 0 | 2,929,301 | 220,082 | $9.524 | 6.1s |
| gpt55low | t1_grep | 626 | 0 | 6,622,383 | 93,143 | $35.906 | 4.5s |
| gpt55low | t2_search | 626 | 129 | 10,420,008 | 355,655 | $62.770 | 10.9s |
| gpt55low | t3_both | 626 | 11 | 9,414,764 | 235,048 | $54.125 | 10.3s |
| gpt55low | t4_repl | 626 | 0 | 2,245,089 | 105,504 | $14.391 | 5.0s |
| gpt55med | t1_grep | 626 | 0 | 8,065,730 | 128,363 | $44.180 | 5.0s |
| gpt55med | t2_search | 626 | 179 | 9,621,014 | 410,399 | $60.417 | 10.5s |
| gpt55med | t3_both | 626 | 22 | 9,523,207 | 237,405 | $54.738 | 8.6s |
| gpt55med | t4_repl | 626 | 0 | 2,416,906 | 134,290 | $16.113 | 5.3s |
| minimax | t1_grep | 626 | 8 | 7,207,607 | 349,350 | $2.430 | 9.3s |
| minimax | t2_search | 626 | 4 | 6,655,612 | 273,628 | $2.185 | 12.4s |
| minimax | t3_both | 626 | 7 | 10,691,434 | 281,539 | $3.321 | 10.3s |
| minimax | t4_repl | 626 | 10 | 4,008,770 | 328,413 | $1.513 | 13.3s |
| opentyphoon | t1_grep | 626 | 1 | 1,153,397 | 8,212 | free | 0.6s |
| opentyphoon | t2_search | 626 | 1 | 1,120,405 | 9,662 | free | 0.7s |
| opentyphoon | t3_both | 626 | 4 | 2,188,590 | 10,572 | free | 0.8s |
| opentyphoon | t4_repl | 626 | 0 | 210,897 | 10,348 | free | 0.8s |
| sonnet | t1_grep | 626 | 1 | 6,705,797 | 197,311 | $11.539 | batch |
| sonnet | t2_search | 626 | 0 | 4,381,544 | 188,790 | $7.988 | batch |
| sonnet | t3_both | 626 | 0 | 4,712,839 | 186,503 | $8.468 | batch |
| sonnet | t4_repl | 626 | 1 | 1,047,915 | 210,742 | $3.152 | batch |
| typhoon8b | t1_grep | 626 | 4 | 2,879,798 | 89,940 | free | 1.3s |
| typhoon8b | t2_search | 626 | 4 | 3,731,055 | 99,042 | free | 1.0s |
| typhoon8b | t3_both | 626 | 8 | 4,816,681 | 92,147 | free | 1.3s |
| typhoon8b | t4_repl | 626 | 7 | 2,223,328 | 105,719 | free | 1.6s |

_⚠est = price is an estimate (confirm). batch = Anthropic Message Batches: 50% billing, elapsed is round-trip not per-item latency._