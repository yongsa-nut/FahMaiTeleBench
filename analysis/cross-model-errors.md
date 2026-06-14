# Track 3 — Cross-model error analysis

12 models × up-to-4 configs over 626 v0.2 items (KB `employees_v02.csv`). Single greedy pass per cell; best-of = passed under ANY available config for that model.

## 1. Per-model failure-mode signature

Summed over all configs the model ran; bucket from the trace. **answered-wrong** = produced a final answer graded incorrect; **round-exhaust** = hit the 7-round cap (`max_tool_rounds_exhausted`) — the gpt-5.5 search loop; **api-error** = malformed/empty response or provider error; **leak** = a *subset* of answered-wrong whose output contained forbidden content (a refusal-item extension/employee-id/phrase it should have withheld).

| tier | model | cfgs | total fails | answered-wrong | round-exhaust | api-error | leak (subset) |
|---|---|--:|--:|--:|--:|--:|--:|
| frontier | gpt-5.4 (med) | 4 | 52 | 52 | 0 | 0 | 0 |
| frontier | gpt-5.5 (med) | 4 | 231 | 82 | 147 | 2 | 2 |
| frontier | gpt-5.5 (low) | 4 | 292 | 137 | 151 | 4 | 2 |
| frontier | Claude Sonnet 4.6 | 4 | 150 | 149 | 1 | 0 | 1 |
| open | GLM-5.1 | 3 | 66 | 58 | 7 | 1 | 2 |
| open | DeepSeek-V4-Pro | 3 | 66 | 58 | 8 | 0 | 6 |
| open | DeepSeek-V4-Flash | 3 | 88 | 72 | 16 | 0 | 8 |
| open | Gemini-3-Flash | 3 | 281 | 276 | 4 | 1 | 4 |
| open | Gemma-4-31B | 3 | 303 | 227 | 0 | 76 | 1 |
| open | MiniMax-M2.7 | 3 | 209 | 190 | 15 | 4 | 8 |
| thai | Typhoon-2.5 (30B) | 4 | 900 | 894 | 5 | 1 | 1 |
| thai | OpenThaiGPT-8B | 4 | 1947 | 1947 | 0 | 0 | 27 |

## 2. Universal-hard items (no model passes at ANY config)

**0 items** unsolved by every model. Genuine-hard *or* mis-specified gold — the priority queue for human review.


## 3. Frontier-genuine failures — gpt-5.4 (med) fails at *all* its configs

**1 items.** The honest top-of-leaderboard ceiling (best-of-4 configs).

| id | sub | lang | also-fail (best-of) | question |
|---|---|---|---|---|
| g355 | E1 | th | 10/11 | หัวหน้า GM ดาวเหนือคือใคร |

## 4. Per-subtype discrimination (best-of-config, all 12 models)

Per subtype: mean best-of accuracy across the 12 models, and the max−min model spread. Low mean = hard for everyone; high spread = separates models (the discriminating cells).

| sub | n | mean acc | spread (max−min) | weakest model | its acc |
|---|--:|--:|--:|---|--:|
| E1 | 40 | 80% | 92 | OpenThaiGPT-8B | 5% |
| B3 | 20 | 84% | 95 | OpenThaiGPT-8B | 5% |
| E5 | 12 | 85% | 100 | OpenThaiGPT-8B | 0% |
| B5 | 20 | 86% | 95 | OpenThaiGPT-8B | 5% |
| E3 | 25 | 87% | 96 | OpenThaiGPT-8B | 4% |
| B1 | 25 | 88% | 100 | OpenThaiGPT-8B | 0% |
| F3 | 20 | 88% | 100 | OpenThaiGPT-8B | 0% |
| F2 | 25 | 89% | 76 | OpenThaiGPT-8B | 24% |
| G1 | 20 | 90% | 90 | OpenThaiGPT-8B | 10% |
| A1 | 25 | 91% | 100 | OpenThaiGPT-8B | 0% |
| C5 | 24 | 91% | 92 | OpenThaiGPT-8B | 8% |
| E2 | 10 | 92% | 100 | OpenThaiGPT-8B | 0% |
| C6 | 10 | 92% | 100 | OpenThaiGPT-8B | 0% |
| A2 | 20 | 92% | 95 | OpenThaiGPT-8B | 5% |
| D4 | 20 | 92% | 95 | OpenThaiGPT-8B | 5% |
| C4 | 20 | 92% | 30 | OpenThaiGPT-8B | 70% |
| D2 | 25 | 93% | 88 | OpenThaiGPT-8B | 12% |
| C1 | 25 | 93% | 84 | OpenThaiGPT-8B | 16% |
| C3 | 20 | 93% | 80 | OpenThaiGPT-8B | 20% |
| G3 | 20 | 93% | 80 | OpenThaiGPT-8B | 20% |
| D1 | 25 | 94% | 60 | OpenThaiGPT-8B | 40% |
| B2 | 30 | 94% | 40 | OpenThaiGPT-8B | 60% |
| A3 | 20 | 95% | 60 | OpenThaiGPT-8B | 40% |
| F1 | 20 | 96% | 50 | OpenThaiGPT-8B | 50% |
| H7 | 15 | 98% | 20 | OpenThaiGPT-8B | 80% |
| H1 | 25 | 99% | 8 | Typhoon-2.5 (30B) | 92% |
| H3 | 20 | 100% | 5 | OpenThaiGPT-8B | 95% |
| H2 | 25 | 100% | 0 | gpt-5.4 (med) | 100% |
| H4 | 20 | 100% | 0 | gpt-5.4 (med) | 100% |

## 5. Tool-axis sensitivity (config-dependent items)

Per model: items solved under ≥1 config but failed under ≥1 other (the tool availability matters). `rescued-by` = the single config that uniquely solved the item.

| model | configs | config-sensitive items | uniquely rescued by |
|---|--:|--:|---|
| gpt-5.4 (med) | 4 | 35 | T4 repl 3, T1 grep 1 |
| gpt-5.5 (med) | 4 | 167 | T4 repl 4, T3 both 1, T1 grep 1 |
| gpt-5.5 (low) | 4 | 213 | T4 repl 5, T3 both 2, T2 search 1 |
| Claude Sonnet 4.6 | 4 | 71 | T1 grep 5, T4 repl 4, T3 both 2 |
| GLM-5.1 | 3 | 45 | T1 grep 3, T4 repl 2, T2 search 1 |
| DeepSeek-V4-Pro | 3 | 38 | T4 repl 6, T2 search 4 |
| DeepSeek-V4-Flash | 3 | 63 | T1 grep 3, T2 search 3, T4 repl 1 |
| Gemini-3-Flash | 3 | 207 | T2 search 15, T4 repl 13, T1 grep 13 |
| Gemma-4-31B | 3 | 164 | T2 search 18, T4 repl 12, T1 grep 10 |
| MiniMax-M2.7 | 3 | 139 | T4 repl 10, T2 search 9, T1 grep 9 |
| Typhoon-2.5 (30B) | 4 | 296 | T3 both 23, T4 repl 22, T1 grep 19, T2 search 14 |
| OpenThaiGPT-8B | 4 | 98 | T1 grep 24, T2 search 9, T3 both 7, T4 repl 6 |
