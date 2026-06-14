# FahMai Directory Benchmark

A bilingual (Thai / English) **grounded tool-use** benchmark for evaluating LLM agents on a
**synthetic 1,995-row enterprise employee directory**. Each item pairs a natural-language query
with a set of allowed tools and a deterministic gold behaviour — either *answer* (token-graded)
or *refuse* with one of a small set of canonical phrases. Because the directory is fully
synthetic, the benchmark is contamination-free by construction.

The directory schema and question style are *inspired by a real enterprise directory deployment*;
all names, codes, contacts, and rows are generated (see `scripts/generate_employees.py`, fixed
seed). No real personal data is included.

> **Anonymized for double-blind review.** Author and institution identifiers have been removed.

## What makes it distinctive

- **Tool availability is the experimental variable.** Every item is run under four tool
  configurations, so the benchmark measures *how* a model uses tools, not just whether it knows
  the answer:

  | Config | Tools offered | Probes |
  |--------|---------------|--------|
  | **T1** | `grep_csv` + `read_csv_rows` | text-search ceiling; retry-after-empty behaviour |
  | **T2** | `search_employees` (structured filter) | query formulation over a wide schema |
  | **T3** | both of the above | tool routing when both are available |
  | **T4** | `python_repl` (pandas over the directory) | code-based aggregation / over-use |

- **Airtight, deterministic grading — no LLM judge.** Answers are graded by token containment,
  forbidden-token / leak checks, exact counts, and minimum-coverage listing (`scripts/grade.py`).
  Gold answers are unique by construction.
- **Refusal as a first-class behaviour.** ~120 items must be refused (field not in the table,
  person not found, subjective question, out-of-company entity, blank field), each with its own
  canonical phrase, plus a universal "never leak a phone extension / employee ID" guard.

## Dataset

- **626 items**, ~60% Thai / ~40% English, across **8 behaviour groups** (A–H) and ~29 subtypes:
  direct identity (A), noisy / shorthand names (B), counts & superlatives (C), homonyms & code
  collisions (D), multi-hop & hierarchy (E), brand/role routing (F), code-switching (G), and
  refusals (H). See **`docs/dataset-breakdown.md`** (and Appendix A of the paper) for the
  authoritative per-subtype counts and worked examples.
- Knowledge base: **`knowledge_base/employees_v02.csv`** (the evaluation KB) — 19 columns,
  ~95–98% surname uniqueness by design. `employees.csv` is the frozen v0.1 directory used by some
  item-construction scripts.
- Questions + gold: **`questions/questions_v02.json`**.

## Repository layout

```
knowledge_base/   employees_v02.csv (eval KB) + employees.csv (frozen v0.1)
questions/        questions_v02.json (items + gold) + questions_v02_all.csv (prompts)
name_pools/       Thai name/nickname pools used by the generator
provenance/       name_sources.md — sourcing for the name pools
scripts/          grader, the 3 tool primitives, model runners, generators, validators, system prompts
build/            per-group item-authoring scripts (*_build.py) + their emitted *_items.json
analysis/         leaderboard CIs, cross-model error analysis, tool-config matrix, cost/latency
                  + the precomputed .md/.json outputs of those scripts (the paper tables)
runs/             per-model evaluation outputs: sweep manifests + raw per-item responses
docs/             DESIGN, ORG_CHART, QUESTION_STYLE, dataset-breakdown
```

## Quickstart

```bash
pip install -r requirements.txt

# Use the benchmark with your own agent: import a tool and the grader.
python scripts/fahmai_csv_tool.py          # demo: structured search over the KB
python scripts/grade.py <run_dir> --questions questions/questions_v02.json
```

A run directory is any folder with a `raw/` subdir holding one `<item_id>.md` file per item
(the model's final answer). The grader writes `results.jsonl` + `report.md`.

## Reproducing the evaluation

The sweep runs all four tool configs for one model, restart-safe, and grades each:

```bash
# Set FAHMAI_KB so the structured/grep/repl tools read the v0.2 KB:
export FAHMAI_KB=knowledge_base/employees_v02.csv          # PowerShell: $env:FAHMAI_KB=...

python scripts/run_wave4_sweep.py --model opentyphoon       # 626 items × 4 configs
python scripts/run_wave4_sweep.py --model gpt54med --configs t1_grep t2_search
```

Then regenerate the paper tables:

```bash
python analysis/bootstrap_ci.py          # leaderboard with item-level 95% bootstrap CIs
python analysis/wave4_report.py          # model × tool-config × subtype matrix
python analysis/cross_model_errors.py    # per-model failure-mode signature + hard items
```

**Note on `runs/`.** The committed run directories include the sweep manifests and the per-item
model responses (`raw/`), which is everything `bootstrap_ci.py` and the accuracy matrix need.
The verbose tool-call **traces** are not committed (size). Scripts that read traces —
`cross_model_errors.py` (round-exhaustion classification), `wave4_report.py` (retry@T1 / tool@T3),
`cost_latency_report.py`, and `build_review_bundle.py` — therefore require a full local sweep to recompute; their
already-computed outputs are provided in `analysis/` (the `*-` and `wave4-*` `.md`/`.json` files).

## Models & environment

Adding a model is one entry in the `MODELS` registry in `scripts/run_opentyphoon_baseline.py`
(OpenAI-compatible `chat`, OpenAI `responses`, or native Anthropic). Provider credentials are read
from a `.env` file at the repo root (never committed). No keys are needed to *use* the dataset or
grader — only to re-run inference. Recognized variables:

| Variable | Provider |
|----------|----------|
| `TYPHOON_API_KEY` | OpenTyphoon |
| `OPENAI_API_KEY` | OpenAI (Responses API) |
| `ANTHROPIC_API_KEY` | Anthropic (Claude) |
| `OPENROUTER_API_KEY` | OpenRouter (Gemini, DeepSeek-Flash, Gemma, MiniMax) |
| `DEEPSEEK_API_KEY` | DeepSeek (first-party) |
| `ZAI_API_KEY` | Z.ai (GLM) |
| `THAILLM_API_KEY` | ThaiLLM gateway (OpenThaiGPT) |

## License

Code: **MIT**. Dataset (`knowledge_base/`, `questions/`, `name_pools/`): **CC BY 4.0**.
The employee directory is entirely synthetic. See `LICENSE`.
