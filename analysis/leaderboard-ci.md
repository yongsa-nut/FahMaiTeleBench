# Track 3 — leaderboard with item-level bootstrap 95% CIs

B = 2000 resamples, seed 0. Each cell = single greedy pass; CI is the item-sampling interval (resample items with replacement, recompute accuracy, 2.5/97.5 percentiles). Agent-errors count as failures.

| tier | model | T1 grep | T2 search | T3 both | T4 repl |
|---|---|---|---|---|---|
| Closed source | gpt-5.4 (med) | 96.8 [95.4–98.1] | 97.3 [96.0–98.4] | 98.1 [97.0–99.0] | 98.2 [97.1–99.2] |
| Closed source | gpt-5.5 (med) | 95.2 [93.5–96.8] | 73.5 [70.1–77.0] | 95.4 [93.8–97.0] | 96.3 [94.7–97.6] |
| Closed source | gpt-5.5 (low) | 95.0 [93.5–96.8] | 65.8 [61.8–69.5] | 92.5 [90.3–94.6] | 96.8 [95.4–98.1] |
| Closed source | Claude Sonnet 4.6 | 93.3 [91.2–95.2] | 93.6 [91.7–95.4] | 95.2 [93.5–96.8] | 91.4 [89.1–93.6] |
| Closed source | Gemini-3-Flash | 87.2 [84.5–89.9] | 86.7 [84.0–89.5] | 90.9 [88.7–93.0] | 78.0 [74.8–81.2] |
| Open weight | GLM-5.1 | 97.0 [95.4–98.2] | 96.2 [94.6–97.6] | 97.1 [95.7–98.4] | 95.4 [93.8–97.0] |
| Open weight | DeepSeek-V4-Pro | 96.8 [95.4–98.1] | 96.2 [94.6–97.6] | 95.4 [93.6–97.0] | 97.6 [96.3–98.7] |
| Open weight | DeepSeek-V4-Flash | 96.0 [94.4–97.4] | 95.7 [94.1–97.3] | 97.3 [96.0–98.6] | 95.4 [93.6–97.0] |
| Open weight | Gemma-4-31B | 86.6 [83.7–89.3] | 89.1 [86.7–91.5] | 91.4 [89.1–93.5] | 84.8 [82.1–87.7] |
| Open weight | MiniMax-M2.7 | 87.7 [85.0–90.3] | 90.6 [88.2–92.8] | 92.0 [89.9–94.1] | 87.5 [85.0–90.1] |
| Thai open weight | Typhoon-2.5 (30B) | 55.0 [50.8–58.9] | 66.9 [63.3–70.6] | 71.2 [67.7–74.6] | 57.8 [53.8–61.3] |
| Thai open weight | Typhoon-S-8B | 36.3 [32.6–40.1] | 30.2 [26.8–33.7] | 33.5 [29.9–37.5] | 24.3 [21.1–27.8] |
