# Track 3 — leaderboard with item-level bootstrap 95% CIs

B = 2000 resamples, seed 0. Each cell = single greedy pass; CI is the item-sampling interval (resample items with replacement, recompute accuracy, 2.5/97.5 percentiles). Agent-errors count as failures.

| tier | model | T1 grep | T2 search | T3 both | T4 repl |
|---|---|---|---|---|---|
| Closed source | gpt-5.4 (med) | 97.1 [95.7–98.2] | 97.4 [96.0–98.6] | 98.2 [97.1–99.2] | 98.9 [97.9–99.7] |
| Closed source | gpt-5.5 (med) | 96.3 [94.9–97.8] | 74.1 [70.8–77.6] | 95.8 [94.1–97.3] | 97.1 [95.7–98.4] |
| Closed source | gpt-5.5 (low) | 96.2 [94.7–97.6] | 67.1 [63.4–70.8] | 93.8 [91.9–95.7] | 97.0 [95.7–98.2] |
| Closed source | Claude Sonnet 4.6 | 94.2 [92.5–96.0] | 94.6 [92.8–96.3] | 95.5 [93.8–97.1] | 91.7 [89.5–93.9] |
| Closed source | Gemini-3-Flash | 89.5 [86.9–91.9] | 87.5 [85.0–90.1] | 90.9 [88.7–93.0] | 78.1 [74.9–81.3] |
| Open weight | GLM-5.1 | 98.2 [97.1–99.2] | 95.7 [94.1–97.3] | 97.8 [96.5–98.9] | 95.5 [93.8–97.1] |
| Open weight | DeepSeek-V4-Pro | 96.5 [94.9–97.8] | 96.2 [94.6–97.6] | 96.8 [95.4–98.1] | 97.1 [95.7–98.2] |
| Open weight | DeepSeek-V4-Flash | 95.2 [93.6–96.8] | 95.8 [94.2–97.3] | 96.8 [95.4–98.1] | 95.5 [93.8–97.1] |
| Open weight | Gemma-4-31B | 86.6 [83.9–89.1] | 90.1 [87.7–92.3] | 92.0 [89.9–94.1] | 85.0 [82.3–87.9] |
| Open weight | MiniMax-M2.7 | 88.0 [85.3–90.6] | 90.4 [88.0–92.7] | 92.2 [90.1–94.2] | 88.5 [85.9–90.9] |
| Thai open weight | Typhoon-2.5 (30B) | 56.5 [52.4–60.5] | 67.3 [63.6–70.8] | 72.5 [69.0–76.0] | 59.9 [56.2–63.4] |
| Thai open weight | Typhoon-S-8B | 36.9 [33.2–40.7] | 31.3 [28.0–35.0] | 35.9 [32.1–39.9] | 24.9 [21.9–28.3] |
