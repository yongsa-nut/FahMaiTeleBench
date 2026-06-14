"""Track-3 cost ($) & latency (ms) report from run-dir traces.

The FahMai task is easy structured-data retrieval, so EFFICIENCY (cost + latency) is a real
leaderboard axis. This reads each model's sweep manifest (runs/wave4_<model>_full.json -> {configs:
{label: run_dir}}), aggregates traces/*.json per (model, config), and reports tokens, cost, and latency.

Pricing (USD per 1M tokens, prompt/completion) is reused from Track-1 run_cost.py (OpenRouter
2026-05-24). Keyed by the runner's model-spec key (manifest "model"). Two caveats handled:
  * Typhoon's OpenAI-compat endpoint omits usage -> 0 tokens. It is FREE ($0) anyway; tokens shown "n/a".
  * Anthropic Message Batches bill at 50% and their per-item elapsed_ms is ROUND-TRIP, not latency.
    Configs whose median elapsed_ms > 60 s are auto-flagged "batch": latency = n/a, cost x0.5.

Usage:
  python cost_latency_report.py                       # auto-discover runs/wave4_*_full.json
  python cost_latency_report.py <manifest.json> ...   # explicit
"""
from __future__ import annotations
import json, statistics, sys
from pathlib import Path
_REPO_ROOT = Path(__file__).resolve().parents[1]

HERE = Path(__file__).resolve().parent
BENCH = HERE.parents[2] / "the source exam" / _REPO_ROOT
RUNS = BENCH / "runs"

# price keyed by runner model-spec key -> (prompt $/Mtok, completion $/Mtok); None = free.
PRICE = {
    "opentyphoon": None, "typhoon25": None,
    "sonnet": (3.000, 15.000),
    "gpt54med": (2.500, 10.000),          # ⚠ ESTIMATE — confirm gpt-5.4 medium pricing
    "gpt55med": (5.000, 30.000), "gpt55low": (5.000, 30.000), "gpt55high": (5.000, 30.000),
    "gemini35flash": (1.500, 9.000), "gemini-3.5-flash": (1.500, 9.000),
    "gemini30flash": (0.500, 3.000),      # OpenRouter authoritative google/gemini-3-flash-preview (2026-05-25)
    "deepseekv4pro": (0.435, 0.870), "deepseekv4flash": (0.100, 0.200),
    "glm51": (0.980, 3.080), "gemma4": (0.120, 0.370), "gemma-4-31b": (0.120, 0.370),
    "minimax": (0.279, 1.200),            # OpenRouter authoritative (2026-05-25)
    "openthaigpt": None,                  # ThaiLLM national gateway — free
}
ESTIMATED = {"gpt54med", "gpt55med", "glm51"}   # prices we are unsure about -> flag in output (glm51 now via Z.ai direct)
BATCH_LATENCY_MS = 60_000                 # median above this => batched round-trip, not per-item

CFG_ORDER = ["t1_grep", "t2_search", "t3_both", "t4_repl"]

# only count traces for ids in the CURRENT dataset (ignore orphan traces from dropped items, e.g. F5)
_QJSON = BENCH / "questions" / "questions_v02.json"
VALID_IDS = {x["id"] for x in json.loads(_QJSON.read_text(encoding="utf-8"))["questions"]}


def load_run(run_dir: Path):
    """-> (n, errors, sum_in, sum_out, [elapsed_ms...]) over traces/*.json (dataset ids only)."""
    n = err = tin = tout = 0
    lat = []
    td = Path(run_dir) / "traces"
    if not td.exists():
        return None
    for f in td.glob("*.json"):
        if f.stem not in VALID_IDS:
            continue
        try:
            t = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        n += 1
        if t.get("error"):
            err += 1
        tin += t.get("input_tokens_total") or 0
        tout += t.get("output_tokens_total") or 0
        if t.get("elapsed_ms"):
            lat.append(t["elapsed_ms"])
    return n, err, tin, tout, lat


def fmt_usd(x): return f"${x:,.3f}"


def main():
    manifests = [Path(a) for a in sys.argv[1:]] or sorted(RUNS.glob("wave4_*_full.json"))
    manifests = [m for m in manifests if "smoke" not in m.name]
    rows = []  # (model, config, n, err, tin, tout, lat[])
    for mf in manifests:
        d = json.loads(mf.read_text(encoding="utf-8"))
        model = d.get("model") or mf.stem.replace("wave4_", "").replace("_full", "")
        for label, rd in d.get("configs", {}).items():
            r = load_run(_REPO_ROOT / rd)
            if r: rows.append((model, label, *r))

    out = ["# Track 3 — cost & latency\n",
           "Per-model efficiency over the FahMai matrix (cost = tokens × Track-1 OpenRouter rates).\n",
           "**Caveats:** (1) **Typhoon is free** ($0); its endpoint omits `usage` on most calls so its "
           "OUTPUT-token count is under-reported — irrelevant to cost. (2) **Sonnet was run via Anthropic "
           "Message Batches** (50% billing, applied) — batch `elapsed_ms` is round-trip, so Sonnet has **no "
           "per-item latency** (would need a sequential re-run). Configs with median elapsed > 60 s are "
           "auto-flagged `batch`. (3) gpt-5.4 price is an **estimate** — confirm.\n"]

    # ---- per-model rollup ----
    models = {}
    for model, label, n, err, tin, tout, lat in rows:
        m = models.setdefault(model, {"n": 0, "err": 0, "tin": 0, "tout": 0, "cost": 0.0,
                                       "lat_seq": [], "any_batch": False, "free": False})
        m["n"] += n; m["err"] += err; m["tin"] += tin; m["tout"] += tout
        price = PRICE.get(model)
        is_batch = bool(lat) and statistics.median(lat) > BATCH_LATENCY_MS
        if is_batch: m["any_batch"] = True
        if price is None:
            m["free"] = True
        else:
            c = (tin * price[0] + tout * price[1]) / 1e6
            m["cost"] += c * (0.5 if is_batch else 1.0)
        if lat and not is_batch:
            m["lat_seq"].extend(lat)

    out.append("## Per-model rollup\n")
    out.append("| model | items | errors | in-tok | out-tok | cost (4 cfg) | $/item | latency med / p90 |")
    out.append("|---|--:|--:|--:|--:|--:|--:|--:|")
    for model in sorted(models):
        m = models[model]
        if m["free"] or PRICE.get(model) is None:
            cost = "free"; per = "free"
        else:
            cost = fmt_usd(m["cost"]) + (" ⚠est" if model in ESTIMATED else "")
            per = fmt_usd(m["cost"] / m["n"]) if m["n"] else "—"
        tin = f"{m['tin']:,}" if m["tin"] else "n/a"
        tout = f"{m['tout']:,}" if m["tout"] else "n/a"
        if m["lat_seq"]:
            med = statistics.median(m["lat_seq"]) / 1000
            p90 = statistics.quantiles(m["lat_seq"], n=10)[8] / 1000 if len(m["lat_seq"]) >= 10 else med
            lats = f"{med:.1f}s / {p90:.1f}s"
        else:
            lats = "batch (n/a)" if m["any_batch"] else "—"
        out.append(f"| {model} | {m['n']} | {m['err']} | {tin} | {tout} | {cost} | {per} | {lats} |")

    # ---- per-(model,config) detail ----
    out.append("\n## Per-config detail\n")
    out.append("| model | config | items | err | in-tok | out-tok | cost | median lat |")
    out.append("|---|---|--:|--:|--:|--:|--:|--:|")
    for model, label, n, err, tin, tout, lat in sorted(rows, key=lambda x: (x[0], CFG_ORDER.index(x[1]) if x[1] in CFG_ORDER else 9)):
        price = PRICE.get(model)
        is_batch = bool(lat) and statistics.median(lat) > BATCH_LATENCY_MS
        if price is None:
            cost = "free"
        else:
            c = (tin * price[0] + tout * price[1]) / 1e6 * (0.5 if is_batch else 1.0)
            cost = fmt_usd(c)
        med = (f"{statistics.median(lat)/1000:.1f}s" if lat and not is_batch
               else ("batch" if is_batch else "—"))
        tn = f"{tin:,}" if tin else "n/a"
        on = f"{tout:,}" if tout else "n/a"
        out.append(f"| {model} | {label} | {n} | {err} | {tn} | {on} | {cost} | {med} |")

    out.append("\n_⚠est = price is an estimate (confirm). batch = Anthropic Message Batches: "
               "50% billing, elapsed is round-trip not per-item latency._")
    md = "\n".join(out)
    (HERE / "cost-latency.md").write_text(md, encoding="utf-8")
    json.dump({"models": {k: {kk: (vv if not isinstance(vv, list) else len(vv)) for kk, vv in v.items()}
                          for k, v in models.items()}},
              open(HERE / "cost-latency.json", "w", encoding="utf-8"), indent=2)
    print(md)
    print("\nwrote cost-latency.md + cost-latency.json")


if __name__ == "__main__":
    main()
