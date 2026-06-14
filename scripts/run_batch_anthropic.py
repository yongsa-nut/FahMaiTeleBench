"""Round-batched agentic runner for Anthropic models (Sonnet/Opus) — ONE tool config.

You can't batch a full agentic item (the tool loop is interactive — we execute
grep/search/repl locally between turns). But requests WITHIN a round are independent,
so we go breadth-first: submit ALL active items' current turn as one Message Batch,
poll, execute every returned tool call locally, then submit the next round for the
items still going. ~50% Batch discount + prompt caching, and full parallelism.

CLI mirrors run_opentyphoon_baseline.py (so run_wave4_sweep.py --batch can drive it),
and it writes the identical run-dir layout (raw/<id>.md, traces/<id>.json, manifest.json).

  python scripts/run_batch_anthropic.py --model sonnet --tool both --stamp t3_both_full \
      --questions questions/questions_v02_all.csv --answer-key questions/questions_v02.json --resume
"""
from __future__ import annotations

import argparse, csv, io, json, os, sys, time
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

# Import tool PRIMITIVES directly. These guard their stdout-wrap under `if __name__=="__main__"`,
# so importing them is side-effect-free — importing run_opentyphoon_baseline would re-wrap
# sys.stdout unconditionally and orphan/close our buffer.
from fahmai_csv_tool import SEARCH_EMPLOYEES_TOOL, search_employees  # noqa: E402
from fahmai_repl_tool import PYTHON_REPL_TOOL, python_repl, create_repl_globals  # noqa: E402
from fahmai_grep_tool import GREP_CSV_TOOL, READ_CSV_ROWS_TOOL, grep_csv, read_csv_rows  # noqa: E402
import anthropic  # noqa: E402

MAX_TOOL_ROUNDS = 7  # was 5 (too tight for 4-hop E5 chains — left no slack for a wrong turn)
DEFAULT_QUESTIONS = ROOT / "kaggle_competition" / "data" / "questions.csv"
ANSWER_KEY = ROOT / "questions" / "questions.json"
PROMPT_FILES = {"L1": HERE / "fahmai_system_prompt_L1.md", "L2": HERE / "fahmai_system_prompt.md",
                "L2fs": HERE / "fahmai_system_prompt_L2_fs.md"}
# anthropic models (native Messages API). Opus 4.7 would omit temperature.
MODELS = {"sonnet": {"model_id": "claude-sonnet-4-6", "key_env": "ANTHROPIC_API_KEY",
                     "params": {"max_tokens": 8192, "temperature": 0}}}


def _load_env() -> None:
    here = Path(__file__).resolve()
    for d in [here.parent] + list(here.parents)[:6]:
        p = d / ".env"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ[k.strip()] = v.strip()  # .env is canonical → override stale OS env


_load_env()


def anthropic_tools(tool_name: str):
    raw = {"search": [SEARCH_EMPLOYEES_TOOL], "repl": [PYTHON_REPL_TOOL],
           "grep": [GREP_CSV_TOOL, READ_CSV_ROWS_TOOL], "grep-only": [GREP_CSV_TOOL],
           "both": [SEARCH_EMPLOYEES_TOOL, GREP_CSV_TOOL, READ_CSV_ROWS_TOOL]}
    if tool_name not in raw:
        raise ValueError(f"Unknown tool: {tool_name}")
    return raw[tool_name]


def _dispatch(name, args, repl_globals):
    try:
        if name == "search_employees":
            return search_employees(**args)
        if name == "grep_csv":
            return grep_csv(**args)
        if name == "read_csv_rows":
            return read_csv_rows(**args)
        if name == "python_repl":
            return python_repl(args.get("code", ""), repl_globals)
        return {"error": f"unknown tool '{name}'"}
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


TOOL_RESULT_CAP = 16000  # chars; a runaway grep result must not bloat the next round's request


def _cap(s: str, n: int = TOOL_RESULT_CAP) -> str:
    return s if len(s) <= n else s[:n] + f"\n…[truncated {len(s) - n} chars]"


def _retry(fn, *a, **k):
    """Retry a batch-API call on transient failures (overloaded/5xx/timeout)."""
    delay, last = 3.0, None
    for i in range(4):
        try:
            return fn(*a, **k)
        except Exception as exc:
            last = exc
            if i == 3:
                raise
            time.sleep(delay)
            delay *= 2
    raise last  # unreachable


def new_trace(it, model_id, tool):
    return {"id": it["id"], "bucket": it.get("bucket"), "language": it.get("language"),
            "question": it["question"], "model": model_id, "tool": tool,
            "rounds": [], "final_text": None, "tool_calls_total": 0,
            "input_tokens_total": 0, "output_tokens_total": 0, "error": None, "elapsed_ms": None}


def finalize(st, raw_dir, trace_dir):
    tr = st["trace"]
    tr["elapsed_ms"] = int((time.time() - st["t0"]) * 1000)
    final = tr.get("final_text") or (f"[agent error: {tr['error']}]" if tr.get("error") else "")
    (raw_dir / f"{tr['id']}.md").write_text(final, encoding="utf-8")
    (trace_dir / f"{tr['id']}.json").write_text(json.dumps(tr, ensure_ascii=False, indent=2), encoding="utf-8")


def _process_result(r, round_idx, with_tools, states, raw_dir, trace_dir) -> bool:
    """Process one batch result for its item. Returns True if the item is now finalized."""
    st = states[r.custom_id]; tr = st["trace"]
    res = r.result
    if res.type != "succeeded":
        tr["error"] = f"batch_{res.type}"
        finalize(st, raw_dir, trace_dir); return True
    msg = res.message
    u = getattr(msg, "usage", None)
    if u is not None:
        tr["input_tokens_total"] += (getattr(u, "input_tokens", 0) or 0)
        tr["output_tokens_total"] += (getattr(u, "output_tokens", 0) or 0)
    tool_uses = [bk for bk in msg.content if bk.type == "tool_use"]
    text = "".join(bk.text for bk in msg.content if bk.type == "text")
    round_rec = {"round": round_idx, "finish_reason": msg.stop_reason,
                 "tool_calls": [{"id": bk.id, "name": bk.name, "args": json.dumps(bk.input, ensure_ascii=False),
                                 "is_error": False} for bk in tool_uses],
                 "content": text}
    asst = []
    for bk in msg.content:
        if bk.type == "text":
            asst.append({"type": "text", "text": bk.text})
        elif bk.type == "tool_use":
            asst.append({"type": "tool_use", "id": bk.id, "name": bk.name, "input": bk.input})
    st["messages"].append({"role": "assistant", "content": asst})

    if not tool_uses or not with_tools:
        tr["final_text"] = text
        if not tool_uses and tr.get("error") == "max_tool_rounds_exhausted":
            tr["error"] = None  # it actually answered
        tr["rounds"].append(round_rec)
        finalize(st, raw_dir, trace_dir); return True

    results = []
    for bk in tool_uses:
        out = _dispatch(bk.name, bk.input or {}, st["repl_globals"])
        if isinstance(out, dict) and out.get("error"):
            for c in round_rec["tool_calls"]:
                if c["id"] == bk.id:
                    c["is_error"] = True
        tr["tool_calls_total"] += 1
        results.append({"type": "tool_result", "tool_use_id": bk.id,
                        "content": _cap(json.dumps(out, ensure_ascii=False))})
    st["messages"].append({"role": "user", "content": results})
    tr["rounds"].append(round_rec)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="sonnet", choices=list(MODELS))
    ap.add_argument("--tool", choices=["search", "repl", "grep", "grep-only", "both"], required=True)
    ap.add_argument("--prompt", choices=list(PROMPT_FILES), default="L2")
    ap.add_argument("--questions", default=str(DEFAULT_QUESTIONS))
    ap.add_argument("--answer-key", default=str(ANSWER_KEY))
    ap.add_argument("--stamp", default=None)
    ap.add_argument("--resume", action="store_true")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--ids", type=str, default=None)
    ap.add_argument("--poll", type=float, default=20.0, help="seconds between batch status polls")
    ap.add_argument("--chunk", type=int, default=250, help="max requests per batch (bounds payload/memory)")
    args = ap.parse_args()

    spec = MODELS[args.model]
    key = os.environ.get(spec["key_env"], "")
    if not key:
        raise SystemExit(f"{spec['key_env']} not set in .env")
    client = anthropic.Anthropic(api_key=key)
    model_id, params = spec["model_id"], dict(spec["params"])

    system_prompt = PROMPT_FILES[args.prompt].read_text(encoding="utf-8")
    system = [{"type": "text", "text": system_prompt, "cache_control": {"type": "ephemeral"}}]
    tools = anthropic_tools(args.tool)

    # items + bucket metadata
    items = []
    with open(args.questions, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            items.append({"id": row["id"], "language": row.get("language", ""), "question": row["question"]})
    ak = json.loads(Path(args.answer_key).read_text(encoding="utf-8"))
    bucket = {q["id"]: q.get("bucket") for q in (ak.get("items") or ak.get("questions") or [])}
    for it in items:
        it["bucket"] = bucket.get(it["id"])
    if args.ids:
        wanted = set(args.ids.split(","))
        items = [x for x in items if x["id"] in wanted]
    if args.limit:
        items = items[: args.limit]

    stamp = args.stamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = ROOT / "runs" / f"{args.model}_{args.tool}_{args.prompt}_{stamp}"
    raw_dir, trace_dir = run_dir / "raw", run_dir / "traces"
    raw_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    (run_dir / "manifest.json").write_text(json.dumps({
        "model": model_id, "model_key": args.model, "base_url": None, "tool": args.tool,
        "tool_name": {"search": "search_employees", "repl": "python_repl", "grep": "grep_csv+read_csv_rows",
                      "grep-only": "grep_csv", "both": "search_employees+grep_csv+read_csv_rows"}[args.tool],
        "kb": os.environ.get("FAHMAI_KB", "knowledge_base/employees.csv"),
        "answer_key": args.answer_key, "prompt_variant": args.prompt,
        "prompt_file": PROMPT_FILES[args.prompt].name, "prompt_chars": len(system_prompt),
        "questions_file": args.questions, "item_count": len(items),
        "started_at": datetime.now().isoformat(), "max_tool_rounds": MAX_TOOL_ROUNDS,
        "mode": "batch",
    }, indent=2), encoding="utf-8")

    # init per-item state (resume: skip items already traced)
    states = {}
    for it in items:
        if args.resume and (trace_dir / f"{it['id']}.json").exists():
            continue
        states[it["id"]] = {"messages": [{"role": "user", "content": it["question"]}],
                            "repl_globals": create_repl_globals() if args.tool == "repl" else None,
                            "trace": new_trace(it, model_id, args.tool), "t0": time.time()}
    active = set(states)
    print(f"Run dir: {run_dir}\nModel: {model_id} · tool {args.tool} · {len(states)} items (batched, ≤{MAX_TOOL_ROUNDS} rounds)")

    t_start = time.time()
    for round_idx in range(MAX_TOOL_ROUNDS + 1):
        if not active:
            break
        with_tools = round_idx < MAX_TOOL_ROUNDS  # final round: drop tools to force a text answer
        if not with_tools:
            for cid in active:
                states[cid]["messages"].append({"role": "user",
                    "content": "Please give your final answer now based on what you've found."})
                states[cid]["trace"]["error"] = "max_tool_rounds_exhausted"

        finished = set()
        active_list = sorted(active)
        for ci in range(0, len(active_list), args.chunk):
            chunk = active_list[ci:ci + args.chunk]
            reqs = []
            for cid in chunk:
                p = {"model": model_id, "system": system, "messages": states[cid]["messages"], **params}
                if with_tools:
                    p["tools"] = tools
                reqs.append({"custom_id": cid, "params": p})
            try:
                batch = _retry(client.messages.batches.create, requests=reqs)
                while True:
                    b = _retry(client.messages.batches.retrieve, batch.id)
                    if b.processing_status == "ended":
                        break
                    time.sleep(args.poll)
                results = _retry(lambda: list(client.messages.batches.results(batch.id)))
            except Exception as exc:  # contain a bad chunk — mark its items errored, keep the sweep alive
                for cid in chunk:
                    states[cid]["trace"]["error"] = f"batch_api_error: {type(exc).__name__}: {exc}"
                    finalize(states[cid], raw_dir, trace_dir)
                    finished.add(cid)
                print(f"  round {round_idx} chunk@{ci}: API error → {len(chunk)} items errored ({type(exc).__name__})")
                continue
            for r in results:
                if _process_result(r, round_idx, with_tools, states, raw_dir, trace_dir):
                    finished.add(r.custom_id)
        active -= finished
        print(f"  round {round_idx}: finished {len(finished)} · {len(active)} active · {time.time()-t_start:.0f}s")

    for cid in active:  # safety: anything unfinished
        states[cid]["trace"]["error"] = states[cid]["trace"].get("error") or "unfinished"
        finalize(states[cid], raw_dir, trace_dir)

    errs = sum(1 for it in items if (trace_dir / f"{it['id']}.json").exists()
               and json.loads((trace_dir / f"{it['id']}.json").read_text(encoding="utf-8")).get("error"))
    print(f"Done in {time.time()-t_start:.0f}s · errors {errs}\nGrade: python scripts/grade.py {run_dir} --questions {args.answer_key}")


if __name__ == "__main__":
    main()
