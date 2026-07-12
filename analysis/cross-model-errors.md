# Track 3 — Cross-model error analysis

12 models × up-to-4 configs over 626 v0.2 items (KB `employees_v02.csv`). Single greedy pass per cell; best-of = passed under ANY available config for that model.

## 1. Per-model failure-mode signature

Summed over all configs the model ran; bucket from the trace. **answered-wrong** = produced a final answer graded incorrect; **round-exhaust** = hit the 7-round cap (`max_tool_rounds_exhausted`) — the gpt-5.5 search loop; **api-error** = malformed/empty response or provider error; **leak** = a *subset* of answered-wrong whose output contained forbidden content (a refusal-item extension/employee-id/phrase it should have withheld).

| tier | model | cfgs | total fails | answered-wrong | round-exhaust | api-error | leak (subset) |
|---|---|--:|--:|--:|--:|--:|--:|
| frontier | gpt-5.4 (med) | 4 | 52 | 52 | 0 | 0 | 0 |
| frontier | gpt-5.5 (med) | 4 | 229 | 82 | 147 | 0 | 2 |
| frontier | gpt-5.5 (low) | 4 | 288 | 137 | 151 | 0 | 2 |
| frontier | Claude Sonnet 4.6 | 4 | 150 | 149 | 1 | 0 | 1 |
| open | GLM-5.1 | 4 | 80 | 72 | 7 | 1 | 3 |
| open | DeepSeek-V4-Pro | 4 | 84 | 78 | 6 | 0 | 10 |
| open | DeepSeek-V4-Flash | 4 | 104 | 91 | 13 | 0 | 8 |
| open | Gemini-3-Flash | 4 | 338 | 333 | 5 | 0 | 5 |
| open | Gemma-4-31B | 4 | 290 | 289 | 1 | 0 | 1 |
| open | MiniMax-M2.7 | 4 | 256 | 234 | 16 | 6 | 9 |
| thai | Typhoon-2.5 (30B) | 4 | 900 | 895 | 5 | 0 | 1 |
| thai | Typhoon-S-8B | 4 | 1696 | 1674 | 15 | 7 | 1 |

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
| E1 | 40 | 83% | 65 | Typhoon-S-8B | 32% |
| B3 | 20 | 87% | 85 | Typhoon-S-8B | 15% |
| F2 | 25 | 88% | 96 | Typhoon-S-8B | 4% |
| E5 | 12 | 90% | 67 | Typhoon-S-8B | 33% |
| B1 | 25 | 90% | 76 | Typhoon-S-8B | 24% |
| H3 | 20 | 92% | 95 | Typhoon-S-8B | 5% |
| F3 | 20 | 93% | 45 | Typhoon-S-8B | 55% |
| H4 | 20 | 93% | 80 | Typhoon-S-8B | 20% |
| B5 | 20 | 93% | 20 | Typhoon-2.5 (30B) | 80% |
| B2 | 30 | 94% | 47 | Typhoon-S-8B | 53% |
| H1 | 25 | 94% | 64 | Typhoon-S-8B | 36% |
| C4 | 20 | 94% | 20 | Typhoon-S-8B | 80% |
| E3 | 25 | 94% | 12 | Gemma-4-31B | 88% |
| D1 | 25 | 96% | 32 | Typhoon-S-8B | 68% |
| H7 | 15 | 96% | 47 | Typhoon-S-8B | 53% |
| D4 | 20 | 97% | 35 | Typhoon-S-8B | 65% |
| C6 | 10 | 98% | 30 | Typhoon-S-8B | 70% |
| C5 | 24 | 98% | 12 | Typhoon-S-8B | 88% |
| D2 | 25 | 98% | 28 | Typhoon-S-8B | 72% |
| F1 | 20 | 98% | 25 | Typhoon-S-8B | 75% |
| C3 | 20 | 98% | 20 | Typhoon-S-8B | 80% |
| G1 | 20 | 98% | 10 | Gemma-4-31B | 90% |
| A1 | 25 | 98% | 12 | Typhoon-S-8B | 88% |
| G3 | 20 | 99% | 15 | Typhoon-S-8B | 85% |
| A2 | 20 | 99% | 10 | Typhoon-S-8B | 90% |
| E2 | 10 | 99% | 10 | Typhoon-S-8B | 90% |
| C1 | 25 | 99% | 4 | Typhoon-2.5 (30B) | 96% |
| A3 | 20 | 100% | 0 | gpt-5.4 (med) | 100% |
| H2 | 25 | 100% | 0 | gpt-5.4 (med) | 100% |

## 5. Tool-axis sensitivity (config-dependent items)

Per model: items solved under ≥1 config but failed under ≥1 other (the tool availability matters). `rescued-by` = the single config that uniquely solved the item.

| model | configs | config-sensitive items | uniquely rescued by |
|---|--:|--:|---|
| gpt-5.4 (med) | 4 | 35 | T4 repl 3, T1 grep 1 |
| gpt-5.5 (med) | 4 | 166 | T4 repl 4, T3 both 1, T1 grep 1 |
| gpt-5.5 (low) | 4 | 213 | T4 repl 5, T3 both 2, T2 search 1 |
| Claude Sonnet 4.6 | 4 | 71 | T1 grep 5, T4 repl 4, T3 both 2 |
| GLM-5.1 | 4 | 47 | T1 grep 1, T4 repl 1 |
| DeepSeek-V4-Pro | 4 | 48 | T2 search 3, T3 both 2, T4 repl 1 |
| DeepSeek-V4-Flash | 4 | 65 | T3 both 2, T4 repl 1, T2 search 1, T1 grep 1 |
| Gemini-3-Flash | 4 | 224 | T2 search 4, T4 repl 4, T3 both 3, T1 grep 3 |
| Gemma-4-31B | 4 | 125 | T1 grep 6, T4 repl 5, T3 both 4, T2 search 2 |
| MiniMax-M2.7 | 4 | 152 | T4 repl 8, T2 search 7, T3 both 4, T1 grep 3 |
| Typhoon-2.5 (30B) | 4 | 296 | T3 both 23, T4 repl 22, T1 grep 19, T2 search 14 |
| Typhoon-S-8B | 4 | 340 | T1 grep 73, T3 both 35, T4 repl 32, T2 search 20 |
