# Track 3 — cost & latency

Per-model efficiency over the FahMai matrix (cost = tokens × Track-1 OpenRouter rates).

**Caveats:** (1) **Typhoon is free** ($0); its endpoint omits `usage` on most calls so its OUTPUT-token count is under-reported — irrelevant to cost. (2) **Sonnet was run via Anthropic Message Batches** (50% billing, applied) — batch `elapsed_ms` is round-trip, so Sonnet has **no per-item latency** (would need a sequential re-run). Configs with median elapsed > 60 s are auto-flagged `batch`. (3) gpt-5.4 price is an **estimate** — confirm.

## Per-model rollup

| model | items | errors | in-tok | out-tok | cost (4 cfg) | $/item | latency med / p90 |
|---|--:|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | 2504 | 13 | 29,143,647 | 1,206,552 | $3.156 | $0.001 | 6.4s / 23.9s |
| deepseekv4pro | 2504 | 14 | 25,859,187 | 1,133,676 | $12.235 | $0.005 | 9.0s / 21.8s |
| gemini30flash | 2504 | 5 | 15,683,893 | 493,235 | $9.322 | $0.004 | 4.1s / 8.5s |
| gemma4 | 2504 | 1 | 19,893,818 | 275,327 | $2.489 | $0.001 | 5.5s / 23.1s |
| glm51 | 2504 | 26 | 25,736,693 | 890,065 | $27.963 ⚠est | $0.011 | 11.7s / 24.6s |
| gpt54med | 2504 | 0 | 21,579,585 | 854,509 | $62.494 ⚠est | $0.025 | 5.8s / 11.7s |
| gpt55low | 2504 | 143 | 27,939,020 | 788,622 | $163.354 | $0.065 | 6.8s / 24.0s |
| gpt55med | 2504 | 201 | 28,579,034 | 907,066 | $170.107 ⚠est | $0.068 | 6.7s / 24.4s |
| minimax | 2504 | 29 | 28,633,206 | 1,230,909 | $9.466 | $0.004 | 10.6s / 27.7s |
| opentyphoon | 2504 | 7 | 6,113,771 | 57,655 | free | free | 0.8s / 3.7s |
| sonnet | 2504 | 1 | 13,757,421 | 781,321 | $26.496 | $0.011 | batch (n/a) |
| typhoon8b | 2504 | 24 | 13,542,555 | 377,961 | free | free | 1.3s / 4.1s |

## Per-config detail

| model | config | items | err | in-tok | out-tok | cost | median lat |
|---|---|--:|--:|--:|--:|--:|--:|
| deepseekv4flash | t1_grep | 626 | 6 | 11,521,656 | 386,331 | $1.229 | 9.6s |
| deepseekv4flash | t2_search | 626 | 1 | 6,372,575 | 257,451 | $0.689 | 6.4s |
| deepseekv4flash | t3_both | 626 | 0 | 7,483,835 | 258,817 | $0.800 | 3.8s |
| deepseekv4flash | t4_repl | 626 | 6 | 3,765,581 | 303,953 | $0.437 | 8.6s |
| deepseekv4pro | t1_grep | 626 | 8 | 10,106,216 | 374,823 | $4.722 | 12.4s |
| deepseekv4pro | t2_search | 626 | 0 | 5,364,148 | 245,525 | $2.547 | 9.5s |
| deepseekv4pro | t3_both | 626 | 4 | 7,190,972 | 252,863 | $3.348 | 7.1s |
| deepseekv4pro | t4_repl | 626 | 2 | 3,197,851 | 260,465 | $1.618 | 7.8s |
| gemini30flash | t1_grep | 626 | 3 | 4,395,963 | 119,165 | $2.555 | 4.6s |
| gemini30flash | t2_search | 626 | 2 | 3,888,620 | 156,773 | $2.415 | 4.2s |
| gemini30flash | t3_both | 626 | 0 | 5,022,245 | 135,959 | $2.919 | 3.5s |
| gemini30flash | t4_repl | 626 | 0 | 2,377,065 | 81,338 | $1.433 | 4.1s |
| gemma4 | t1_grep | 626 | 0 | 5,583,322 | 59,858 | $0.692 | 5.5s |
| gemma4 | t2_search | 626 | 0 | 5,277,265 | 63,129 | $0.657 | 4.3s |
| gemma4 | t3_both | 626 | 1 | 6,617,167 | 63,798 | $0.818 | 5.2s |
| gemma4 | t4_repl | 626 | 0 | 2,416,064 | 88,542 | $0.323 | 7.0s |
| glm51 | t1_grep | 626 | 9 | 10,652,597 | 271,632 | $11.276 | 11.4s |
| glm51 | t2_search | 626 | 0 | 4,893,061 | 200,959 | $5.414 | 10.6s |
| glm51 | t3_both | 626 | 2 | 6,267,260 | 207,512 | $6.781 | 11.8s |
| glm51 | t4_repl | 626 | 15 | 3,923,775 | 209,962 | $4.492 | 13.1s |
| gpt54med | t1_grep | 626 | 0 | 7,640,244 | 215,926 | $21.260 | 5.6s |
| gpt54med | t2_search | 626 | 0 | 4,974,432 | 209,498 | $14.531 | 5.6s |
| gpt54med | t3_both | 626 | 0 | 6,018,580 | 208,366 | $17.130 | 6.1s |
| gpt54med | t4_repl | 626 | 0 | 2,946,329 | 220,719 | $9.573 | 6.1s |
| gpt55low | t1_grep | 626 | 0 | 6,329,279 | 92,700 | $34.427 | 4.4s |
| gpt55low | t2_search | 626 | 133 | 10,252,569 | 361,115 | $62.096 | 10.9s |
| gpt55low | t3_both | 626 | 10 | 9,113,419 | 229,387 | $52.449 | 9.5s |
| gpt55low | t4_repl | 626 | 0 | 2,243,753 | 105,420 | $14.381 | 4.9s |
| gpt55med | t1_grep | 626 | 0 | 7,713,584 | 128,608 | $42.426 | 5.0s |
| gpt55med | t2_search | 626 | 182 | 9,182,203 | 411,722 | $58.263 | 10.4s |
| gpt55med | t3_both | 626 | 19 | 9,264,928 | 231,746 | $53.277 | 8.5s |
| gpt55med | t4_repl | 626 | 0 | 2,418,319 | 134,990 | $16.141 | 5.2s |
| minimax | t1_grep | 626 | 8 | 7,468,073 | 350,923 | $2.505 | 8.8s |
| minimax | t2_search | 626 | 4 | 6,740,953 | 275,931 | $2.212 | 11.3s |
| minimax | t3_both | 626 | 6 | 10,462,000 | 276,555 | $3.251 | 9.8s |
| minimax | t4_repl | 626 | 11 | 3,962,180 | 327,500 | $1.498 | 12.6s |
| opentyphoon | t1_grep | 626 | 1 | 1,738,519 | 11,830 | free | 0.7s |
| opentyphoon | t2_search | 626 | 2 | 1,482,372 | 14,114 | free | 0.8s |
| opentyphoon | t3_both | 626 | 3 | 2,487,109 | 15,140 | free | 0.8s |
| opentyphoon | t4_repl | 626 | 1 | 405,771 | 16,571 | free | 0.8s |
| sonnet | t1_grep | 626 | 0 | 5,997,700 | 199,450 | $10.492 | batch |
| sonnet | t2_search | 626 | 0 | 2,906,499 | 186,662 | $5.760 | batch |
| sonnet | t3_both | 626 | 0 | 3,785,333 | 185,367 | $7.068 | batch |
| sonnet | t4_repl | 626 | 1 | 1,067,889 | 209,842 | $3.176 | batch |
| typhoon8b | t1_grep | 626 | 1 | 2,860,915 | 87,299 | free | 1.3s |
| typhoon8b | t2_search | 626 | 8 | 3,724,636 | 95,806 | free | 1.0s |
| typhoon8b | t3_both | 626 | 9 | 4,753,965 | 90,518 | free | 1.3s |
| typhoon8b | t4_repl | 626 | 6 | 2,203,039 | 104,338 | free | 1.6s |

_⚠est = price is an estimate (confirm). batch = Anthropic Message Batches: 50% billing, elapsed is round-trip not per-item latency._