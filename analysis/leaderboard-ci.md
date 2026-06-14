# Track 3 — leaderboard with item-level bootstrap 95% CIs

B = 2000 resamples, seed 0. Each cell = single greedy pass; CI is the item-sampling interval (resample items with replacement, recompute accuracy, 2.5/97.5 percentiles). Agent-errors count as failures.

| tier | model | T1 grep | T2 search | T3 both | T4 repl |
|---|---|---|---|---|---|
| frontier | gpt-5.4 (med) | 97.1 [95.7–98.2] | 97.4 [96.0–98.6] | 98.2 [97.1–99.2] | 98.9 [97.9–99.7] |
| frontier | gpt-5.5 (med) | 96.3 [94.9–97.8] | 74.0 [70.6–77.5] | 95.8 [94.1–97.3] | 97.0 [95.5–98.2] |
| frontier | gpt-5.5 (low) | 96.0 [94.4–97.4] | 66.9 [63.3–70.6] | 93.6 [91.7–95.5] | 96.8 [95.4–98.1] |
| frontier | Claude Sonnet 4.6 | 94.2 [92.5–96.0] | 94.6 [92.8–96.3] | 95.5 [93.8–97.1] | 91.7 [89.5–93.9] |
| open | GLM-5.1 | 98.2 [97.1–99.2] | 95.7 [94.1–97.3] | — | 95.5 [93.9–97.1] |
| open | DeepSeek-V4-Pro | 96.2 [94.7–97.6] | 96.2 [94.6–97.6] | — | 97.1 [95.7–98.4] |
| open | DeepSeek-V4-Flash | 95.0 [93.3–96.6] | 95.8 [94.2–97.4] | — | 95.0 [93.3–96.6] |
| open | Gemini-3-Flash | 89.5 [87.1–91.9] | 87.5 [84.8–90.3] | — | 78.1 [75.1–81.3] |
| open | Gemma-4-31B | 76.8 [73.5–80.2] | 89.8 [87.4–92.2] | — | 85.0 [82.1–87.9] |
| open | MiniMax-M2.7 | 87.9 [85.1–90.4] | 90.4 [88.0–92.7] | — | 88.3 [85.9–90.9] |
| thai | Typhoon-2.5 (30B) | 56.5 [52.6–60.4] | 67.3 [63.6–70.9] | 72.5 [69.0–75.9] | 59.9 [56.1–63.7] |
| thai | OpenThaiGPT-8B | 22.8 [19.6–26.0] | 21.9 [18.7–25.1] | 22.8 [19.6–26.2] | 21.4 [18.2–24.8] |
