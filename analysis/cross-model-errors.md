# Track 3 — Cross-model error analysis

12 models × up-to-4 configs over 626 v0.2 items (KB `employees_v02.csv`). Single greedy pass per cell; best-of = passed under ANY available config for that model.

## 1. Per-model failure-mode signature

Summed over all configs the model ran; bucket from the trace. **answered-wrong** = produced a final answer graded incorrect; **round-exhaust** = hit the 7-round cap (`max_tool_rounds_exhausted`) — the gpt-5.5 search loop; **api-error** = malformed/empty response or provider error; **leak** = a *subset* of answered-wrong whose output contained forbidden content (a refusal-item extension/employee-id/phrase it should have withheld).

| tier | model | cfgs | total fails | answered-wrong | round-exhaust | api-error | leak (subset) |
|---|---|--:|--:|--:|--:|--:|--:|
| frontier | gpt-5.4 (med) | 4 | 50 | 50 | 0 | 0 | 0 |
| frontier | gpt-5.5 (med) | 4 | 231 | 77 | 154 | 0 | 2 |
| frontier | gpt-5.5 (low) | 4 | 290 | 134 | 156 | 0 | 2 |
| frontier | Claude Sonnet 4.6 | 4 | 160 | 156 | 4 | 0 | 1 |
| open | GLM-5.1 | 4 | 74 | 67 | 6 | 1 | 3 |
| open | DeepSeek-V4-Pro | 4 | 81 | 74 | 5 | 2 | 10 |
| open | DeepSeek-V4-Flash | 4 | 92 | 83 | 8 | 1 | 8 |
| open | Gemini-3-Flash | 4 | 327 | 323 | 4 | 0 | 5 |
| open | Gemma-4-31B | 4 | 254 | 252 | 1 | 1 | 1 |
| open | MiniMax-M2.7 | 4 | 249 | 226 | 18 | 5 | 9 |
| thai | Typhoon-2.5 (30B) | 4 | 863 | 857 | 6 | 0 | 1 |
| thai | Typhoon-S-8B | 4 | 1709 | 1683 | 13 | 13 | 1 |

## 2. Universal-hard items (no model passes at ANY config)

**0 items** unsolved by every model. Genuine-hard *or* mis-specified gold — the priority queue for human review.


## 3. Frontier-genuine failures — gpt-5.4 (med) fails at *all* its configs

**1 items.** The honest top-of-leaderboard ceiling (best-of-4 configs).

| id | sub | lang | also-fail (best-of) | question |
|---|---|---|---|---|
| g355 | E1 | th | 9/11 | หัวหน้า GM ดาวเหนือคือใคร |

## 4. Per-subtype discrimination (best-of-config, all 12 models)

Per subtype: mean best-of accuracy across the 12 models, and the max−min model spread. Low mean = hard for everyone; high spread = separates models (the discriminating cells).

| sub | n | mean acc | spread (max−min) | weakest model | its acc |
|---|--:|--:|--:|---|--:|
| E1 | 40 | 83% | 72 | Typhoon-S-8B | 25% |
| B3 | 20 | 87% | 85 | Typhoon-S-8B | 15% |
| F3 | 20 | 87% | 45 | Typhoon-S-8B | 55% |
| F2 | 25 | 88% | 96 | Typhoon-S-8B | 4% |
| E4 | 12 | 89% | 67 | Typhoon-S-8B | 33% |
| B1 | 25 | 90% | 80 | Typhoon-S-8B | 20% |
| H3 | 20 | 92% | 95 | Typhoon-S-8B | 5% |
| H4 | 20 | 93% | 80 | Typhoon-S-8B | 20% |
| B2 | 30 | 94% | 43 | Typhoon-S-8B | 57% |
| H1 | 25 | 94% | 64 | Typhoon-S-8B | 36% |
| E3 | 25 | 95% | 12 | Gemini-3-Flash | 88% |
| D1 | 25 | 96% | 32 | Typhoon-S-8B | 68% |
| H5 | 15 | 96% | 47 | Typhoon-S-8B | 53% |
| B4 | 20 | 97% | 20 | Typhoon-S-8B | 80% |
| D3 | 20 | 98% | 30 | Typhoon-S-8B | 70% |
| D2 | 25 | 98% | 28 | Typhoon-S-8B | 72% |
| F1 | 20 | 98% | 25 | Typhoon-S-8B | 75% |
| C3 | 20 | 98% | 25 | Typhoon-S-8B | 75% |
| C2 | 20 | 98% | 20 | Typhoon-S-8B | 80% |
| A1 | 25 | 98% | 12 | Typhoon-S-8B | 88% |
| G2 | 20 | 99% | 15 | Typhoon-S-8B | 85% |
| G1 | 20 | 99% | 10 | Gemma-4-31B | 90% |
| A2 | 20 | 99% | 10 | Typhoon-S-8B | 90% |
| E2 | 10 | 99% | 10 | Typhoon-S-8B | 90% |
| C5 | 10 | 99% | 10 | Typhoon-S-8B | 90% |
| C4 | 24 | 99% | 8 | Typhoon-S-8B | 92% |
| C1 | 25 | 100% | 4 | Typhoon-S-8B | 96% |
| A3 | 20 | 100% | 0 | gpt-5.4 (med) | 100% |
| H2 | 25 | 100% | 0 | gpt-5.4 (med) | 100% |

## 5. Tool-axis sensitivity (config-dependent items)

Per model: items solved under ≥1 config but failed under ≥1 other (the tool availability matters). `rescued-by` = the single config that uniquely solved the item.

| model | configs | config-sensitive items | uniquely rescued by |
|---|--:|--:|---|
| gpt-5.4 (med) | 4 | 36 | T1 grep 1 |
| gpt-5.5 (med) | 4 | 180 | T4 repl 6, T3 both 1, T1 grep 1 |
| gpt-5.5 (low) | 4 | 228 | T4 repl 5, T2 search 2, T3 both 2 |
| Claude Sonnet 4.6 | 4 | 75 | T4 repl 5, T1 grep 5, T3 both 3, T2 search 1 |
| GLM-5.1 | 4 | 52 | T4 repl 2, T1 grep 1 |
| DeepSeek-V4-Pro | 4 | 52 | T2 search 4, T4 repl 1 |
| DeepSeek-V4-Flash | 4 | 64 | T3 both 1, T4 repl 1, T1 grep 1 |
| Gemini-3-Flash | 4 | 203 | T3 both 5, T4 repl 4, T1 grep 2, T2 search 1 |
| Gemma-4-31B | 4 | 96 | T1 grep 6, T4 repl 5, T3 both 4, T2 search 1 |
| MiniMax-M2.7 | 4 | 152 | T4 repl 7, T2 search 6, T1 grep 4, T3 both 3 |
| Typhoon-2.5 (30B) | 4 | 287 | T3 both 22, T4 repl 18, T1 grep 17, T2 search 13 |
| Typhoon-S-8B | 4 | 339 | T1 grep 78, T4 repl 35, T3 both 32, T2 search 24 |
