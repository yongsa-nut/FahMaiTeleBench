"""Wave 4 sweep — 4 tool configs over all 626 v0.2 items, against employees_v02.csv.

The v2 taxonomy makes *tool availability* the experimental variable (Group I dissolved).
This driver runs the four configs with one shared base stamp, each restart-safe (--resume):

  T1 grep-only  (--tool grep-only)   retry-after-empty behaviour, tool ceiling
  T2 search     (--tool search)      structured-query formulation
  T3 both       (--tool both)        tool-choice (search vs grep when both offered)
  T4 repl       (--tool repl)        frontier pandas capability / REPL over-use

It (1) dumps questions/questions_v02_all.csv (id,language,question for all 626) from
questions_v02.json, (2) sets FAHMAI_KB to the v0.2 KB so the planted F5 GOV rows resolve,
(3) runs each config via run_opentyphoon_baseline.py, (4) grades each against
questions_v02.json, and (5) writes runs/wave4_<stamp>.json mapping config->run_dir
(consumed by analysis/wave4_report.py).

Usage:
  python scripts/run_wave4_sweep.py                      # full sweep (626 x 4)
  python scripts/run_wave4_sweep.py --limit 10           # smoke
  python scripts/run_wave4_sweep.py --configs t1_grep t3_both
  python scripts/run_wave4_sweep.py --no-grade           # run only, grade later
"""
from __future__ import annotations

import argparse, csv, io, json, os, subprocess, sys
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
QJSON = ROOT / "questions" / "questions_v02.json"
QCSV = ROOT / "questions" / "questions_v02_all.csv"
KB = ROOT / "knowledge_base" / "employees_v02.csv"
PROMPT = "L2"  # match the April baseline

# config label -> --tool value
CONFIGS = {"t1_grep": "grep-only", "t2_search": "search", "t3_both": "both", "t4_repl": "repl"}


def dump_csv() -> int:
    data = json.loads(QJSON.read_text(encoding="utf-8"))
    items = data.get("questions") or data.get("items") or []
    with open(QCSV, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["id", "language", "question"])
        for it in items:
            w.writerow([it["id"], it.get("language", ""), it["question"]])
    return len(items)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="opentyphoon", help="model spec key passed to the runner (--model).")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--ids", type=str, default=None)
    ap.add_argument("--configs", nargs="+", default=list(CONFIGS), choices=list(CONFIGS))
    ap.add_argument("--stamp", type=str, default=datetime.now().strftime("%Y%m%d_%H%M%S"))
    ap.add_argument("--no-grade", action="store_true")
    ap.add_argument("--concurrency", type=int, default=1,
                    help="parallel in-flight items per config (passed to the runner; clean per-item latency).")
    ap.add_argument("--batch", action="store_true",
                    help="use the round-batched Anthropic runner (run_batch_anthropic.py) instead of the sequential one")
    args = ap.parse_args()

    if not KB.exists():
        raise SystemExit(f"KB not found: {KB}")
    n = dump_csv()
    print(f"Dumped {n} items -> {QCSV.name}  (KB={KB.name})")

    env = dict(os.environ, FAHMAI_KB=str(KB), PYTHONUTF8="1")
    runner = HERE / ("run_batch_anthropic.py" if args.batch else "run_opentyphoon_baseline.py")
    grader = HERE / "grade.py"

    run_dirs: dict[str, str] = {}
    for label in args.configs:
        tool = CONFIGS[label]
        stamp = f"{label}_{args.stamp}"
        run_dir = ROOT / "runs" / f"{args.model}_{tool}_{PROMPT}_{stamp}"
        cmd = [sys.executable, str(runner), "--model", args.model, "--tool", tool, "--prompt", PROMPT,
               "--questions", str(QCSV), "--answer-key", str(QJSON),
               "--stamp", stamp, "--resume"]
        if args.limit:
            cmd += ["--limit", str(args.limit)]
        if args.ids:
            cmd += ["--ids", args.ids]
        if args.concurrency and args.concurrency > 1 and not args.batch:
            cmd += ["--concurrency", str(args.concurrency)]
        print(f"\n=== {label}  (--tool {tool}) ===")
        subprocess.run(cmd, env=env, check=True)
        run_dirs[label] = str(run_dir)

    if not args.no_grade:
        for label, rd in run_dirs.items():
            print(f"\n=== grade {label} ===")
            subprocess.run([sys.executable, str(grader), rd, "--questions", str(QJSON)],
                           env=env, check=True)

    manifest = ROOT / "runs" / f"wave4_{args.model}_{args.stamp}.json"
    manifest.write_text(json.dumps(
        {"model": args.model, "stamp": args.stamp, "kb": str(KB), "answer_key": str(QJSON),
         "item_count": (args.limit or n), "configs": run_dirs}, indent=2), encoding="utf-8")
    print(f"\nWrote sweep manifest: {manifest}")
    for label, rd in run_dirs.items():
        print(f"  {label}: {rd}")
    print(f"\nReport: python analysis/wave4_report.py {manifest}")


if __name__ == "__main__":
    main()
