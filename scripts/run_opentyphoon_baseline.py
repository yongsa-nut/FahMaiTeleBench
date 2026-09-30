"""OpenTyphoon (typhoon-v2.5-30b-a3b-instruct) baseline runner.

Direct to opentyphoon.ai (not the ThaiLLM gateway). Uses the `openai` client library.
Same tool shapes as run_typhoon_baseline.py: search, repl, grep.

Usage:
  python scripts/run_opentyphoon_baseline.py --tool=search
  python scripts/run_opentyphoon_baseline.py --tool=repl --limit=10
  python scripts/run_opentyphoon_baseline.py --tool=grep
"""
from __future__ import annotations

import argparse, csv, io, json, os, sys, time
from datetime import datetime
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

from fahmai_csv_tool import SEARCH_EMPLOYEES_TOOL, search_employees  # noqa
from fahmai_repl_tool import PYTHON_REPL_TOOL, python_repl, create_repl_globals  # noqa
from fahmai_grep_tool import GREP_CSV_TOOL, READ_CSV_ROWS_TOOL, grep_csv, read_csv_rows  # noqa

DEFAULT_QUESTIONS = ROOT / "questions" / "questions_v02_all.csv"
ANSWER_KEY = ROOT / "questions" / "questions_v02.json"

PROMPT_FILES = {
    "L1": HERE / "fahmai_system_prompt_L1.md",
    "L2": HERE / "fahmai_system_prompt.md",
    "L2fs": HERE / "fahmai_system_prompt_L2_fs.md",
}

MAX_TOOL_ROUNDS = 7  # was 5 (too tight for 4-hop E5 chains — left no slack for a wrong turn)

# Model registry — adding a model is one entry. Two providers (same tool dispatch, trace, output):
#   "chat"      → /v1/chat/completions (OpenTyphoon + OpenAI-compatible gateways).
#   "responses" → /v1/responses (gpt-5.x: tools+reasoning are ONLY supported here, not chat).
# gpt-5.x: reasoning tokens count against max_output_tokens, so the budget is large to avoid empty
# output mid-tool-loop; no temperature. params are passed verbatim to the provider's create().

# Browser-like UA to clear the ThaiLLM gateway's Cloudflare WAF (see openthaigpt spec below).
_GATEWAY_HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"),
}

MODELS = {
    "opentyphoon": {"provider": "chat", "model_id": "typhoon-v2.5-30b-a3b-instruct",
                    "base_url": "https://api.opentyphoon.ai/v1", "key_env": "TYPHOON_API_KEY",
                    "params": {"max_tokens": 8192, "temperature": 0.2}},
    "gpt54med":    {"provider": "responses", "model_id": "gpt-5.4", "base_url": None,
                    "key_env": "OPENAI_API_KEY2", "key_fallback": "OPENAI_API_KEY",
                    "params": {"max_output_tokens": 16000, "reasoning": {"effort": "medium"}}},
    # "anthropic" provider → native Messages API + tool-use (system-prompt cached).
    "sonnet":      {"provider": "anthropic", "model_id": "claude-sonnet-4-6", "base_url": None,
                    "key_env": "ANTHROPIC_API_KEY",
                    "params": {"max_tokens": 8192, "temperature": 0}},

    # --- cost-probe expansion (2026-05-25): single-config (t2_search) sample → estimate the matrix.
    # OpenRouter reasoning models (deepseek/glm/minimax) are thinking-native: omit temperature, give a
    # large max_tokens so reasoning can finish before the visible answer. Gemma is non-thinking (:free=$0).
    "gpt55med":    {"provider": "responses", "model_id": "gpt-5.5", "base_url": None,
                    "key_env": "OPENAI_API_KEY2", "key_fallback": "OPENAI_API_KEY",
                    "params": {"max_output_tokens": 16000, "reasoning": {"effort": "medium"}}},
    "gpt55low":    {"provider": "responses", "model_id": "gpt-5.5", "base_url": None,
                    "key_env": "OPENAI_API_KEY2", "key_fallback": "OPENAI_API_KEY",
                    "params": {"max_output_tokens": 16000, "reasoning": {"effort": "low"}}},
    # via OpenRouter (NOT Google direct): Gemini-3 + tools needs a thought_signature round-trip on the
    # Google OpenAI-compat endpoint (400s otherwise); OpenRouter handles that quirk server-side.
    "gemini30flash": {"provider": "chat", "model_id": "google/gemini-3-flash-preview",
                    "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY",
                    "params": {"max_tokens": 24000}},
    # ThaiLLM gateway sits behind Cloudflare: it WAF-blocks the default httpx/SDK User-Agent (403
    # "error code: 1010" BEFORE the key is checked). A browser-like UA via default_headers clears it;
    # the THAILLM_API_KEY is valid (fix mirrors track1/.../run_editing.py, re-verified 2026-05-25).
    # Typhoon-S 8B on the ThaiLLM gateway — a Thai 8B that DOES emit tool calls (unlike OpenThaiGPT-8B).
    "typhoon8b":   {"provider": "chat", "model_id": "typhoon-s-thaillm-8b-instruct",
                    "base_url": "https://thaillm.or.th/api/v1", "key_env": "THAILLM_API_KEY",
                    "extra_headers": _GATEWAY_HEADERS,
                    # 16k context: 4096 output tokens 400s ("max_tokens too large") on large tool
                    # dumps; 2048 is ample for a directory answer and leaves room under the cap.
                    "params": {"max_tokens": 2048, "temperature": 0.2}},
    # DeepSeek first-party (api.deepseek.com): far cheaper than OpenRouter, which has no
    # economical provider for V4-Pro. First-party model id has no "deepseek/" prefix.
    "deepseekv4pro": {"provider": "chat", "model_id": "deepseek-v4-pro",
                    "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY",
                    "params": {"max_tokens": 24000}},
    "deepseekv4flash": {"provider": "chat", "model_id": "deepseek-v4-flash",  # first-party; the reported T2 cell used deepseek/deepseek-v4-flash via OpenRouter
                    "base_url": "https://api.deepseek.com", "key_env": "DEEPSEEK_API_KEY",
                    "params": {"max_tokens": 24000}},
    # DeepSeek's first-party API now serves newer versions under the V4 names; these routes reach the
    # April 2026 V4 weights (the reported checkpoints) on fp8 hosts through OpenRouter.
    "deepseekv4pro_fp8": {"provider": "chat", "model_id": "deepseek/deepseek-v4-pro",
                    "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY",
                    "params": {"max_tokens": 24000, "extra_body": {"provider": {
                        "only": ["deepinfra", "parasail", "novita", "siliconflow", "gmicloud"],
                        "quantizations": ["fp8"], "allow_fallbacks": True}}}},
    "deepseekv4flash_fp8": {"provider": "chat", "model_id": "deepseek/deepseek-v4-flash",
                    "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY",
                    "params": {"max_tokens": 24000, "extra_body": {"provider": {
                        "only": ["deepinfra", "parasail", "novita", "siliconflow", "gmicloud"],
                        "quantizations": ["fp8"], "allow_fallbacks": True}}}},
    "glm51":       {"provider": "chat", "model_id": "glm-5.1",  # direct Z.ai (own key) — not OpenRouter
                    "base_url": "https://api.z.ai/api/paas/v4", "key_env": "ZAI_API_KEY",
                    "params": {"max_tokens": 24000}},
    "gemma4":      {"provider": "chat", "model_id": "google/gemma-4-31b-it",  # paid ($0.12/$0.37); :free 429-rate-limits
                    "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY",
                    "params": {"max_tokens": 2048, "temperature": 0}},
    "minimax":     {"provider": "chat", "model_id": "minimax/minimax-m2.7",
                    "base_url": "https://openrouter.ai/api/v1", "key_env": "OPENROUTER_API_KEY",
                    "params": {"max_tokens": 24000}},
}

# bound in main() once --model is parsed
MODEL_ID = ""
PROVIDER = "chat"
CALL_PARAMS: dict = {}
SYSTEM_PROMPT = ""


# ---------------- env ----------------
def _load_env() -> None:
    here = Path(__file__).resolve()
    for d in [here.parent] + list(here.parents)[:6]:
        p = d / ".env"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            os.environ[k.strip()] = v.strip()  # .env is canonical → OVERRIDE stale OS env (e.g. refreshed ANTHROPIC_API_KEY)


_load_env()

from openai import OpenAI  # noqa

client = None  # built in main() from the chosen --model spec


# ---------------- tool adapters (OpenAI-shape) ----------------
def to_openai_tool(t: dict) -> dict:
    return {
        "type": "function",
        "function": {
            "name": t["name"],
            "description": t["description"],
            "parameters": t["input_schema"],
        },
    }


def build_tools(tool_name: str):
    if tool_name == "search":
        return [to_openai_tool(SEARCH_EMPLOYEES_TOOL)], _run_search
    if tool_name == "repl":
        return [to_openai_tool(PYTHON_REPL_TOOL)], None
    if tool_name == "grep":
        return [to_openai_tool(GREP_CSV_TOOL), to_openai_tool(READ_CSV_ROWS_TOOL)], _run_grep
    if tool_name == "grep-only":
        return [to_openai_tool(GREP_CSV_TOOL)], _run_grep
    if tool_name == "both":  # T3 — search + grep_csv + read_csv_rows together
        return [to_openai_tool(SEARCH_EMPLOYEES_TOOL), to_openai_tool(GREP_CSV_TOOL),
                to_openai_tool(READ_CSV_ROWS_TOOL)], _run_both
    raise ValueError(f"Unknown tool: {tool_name}")


def _run_search(tc, _state=None):
    args = json.loads(tc.function.arguments or "{}")
    try:
        return search_employees(**args)
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def _run_repl(tc, state):
    args = json.loads(tc.function.arguments or "{}")
    return python_repl(args.get("code", ""), state["repl_globals"])


def _run_grep(tc, _state=None):
    name = tc.function.name
    args = json.loads(tc.function.arguments or "{}")
    try:
        if name == "grep_csv":
            return grep_csv(**args)
        if name == "read_csv_rows":
            return read_csv_rows(**args)
        return {"error": f"unknown tool '{name}'"}
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def _run_both(tc, _state=None):  # T3 dispatcher: route by tool name
    if tc.function.name == "search_employees":
        return _run_search(tc)
    return _run_grep(tc)


def _chat(messages, tools, tool_choice):
    """chat.completions.create with per-model params (MODEL_ID/CALL_PARAMS) + retry/backoff."""
    delay, last = 2.0, None
    for attempt in range(4):
        try:
            return client.chat.completions.create(
                model=MODEL_ID, messages=messages, tools=tools,
                tool_choice=tool_choice, **CALL_PARAMS)
        except Exception as exc:  # transient: rate-limit / 5xx / timeout
            last = exc
            if attempt == 3:
                raise
            time.sleep(delay)
            delay *= 2
    raise last  # unreachable


def _acc_usage(trace, resp):  # accumulate token usage across rounds (chat + responses shapes)
    u = getattr(resp, "usage", None)
    if u is not None:
        trace["input_tokens_total"] += getattr(u, "prompt_tokens", None) or getattr(u, "input_tokens", 0) or 0
        trace["output_tokens_total"] += getattr(u, "completion_tokens", None) or getattr(u, "output_tokens", 0) or 0


# ---------------- per-item loop ----------------
def run_item(item: dict, tool_name: str, run_dir: Path, resume: bool = False) -> dict:
    if PROVIDER == "responses":
        return run_item_responses(item, tool_name, run_dir, resume)
    if PROVIDER == "anthropic":
        return run_item_anthropic(item, tool_name, run_dir, resume)
    iid = item["id"]
    question = item["question"]
    raw_dir = run_dir / "raw"
    trace_dir = run_dir / "traces"
    trace_path = trace_dir / f"{iid}.json"
    if resume and trace_path.exists():  # restart-safe: skip already-run items
        return json.loads(trace_path.read_text(encoding="utf-8"))
    raw_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    tool_schemas, _ = build_tools(tool_name)
    state = {}
    if tool_name == "repl":
        state["repl_globals"] = create_repl_globals()
        run_tc = _run_repl
    elif tool_name in ("grep", "grep-only"):
        run_tc = _run_grep
    elif tool_name == "both":
        run_tc = _run_both
    else:
        run_tc = _run_search

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question},
    ]
    trace = {
        "id": iid, "bucket": item.get("bucket"), "language": item.get("language"),
        "question": question, "model": MODEL_ID, "tool": tool_name,
        "rounds": [], "final_text": None, "tool_calls_total": 0,
        "input_tokens_total": 0, "output_tokens_total": 0,
        "error": None, "elapsed_ms": None,
    }
    t0 = time.time()

    try:
        for round_idx in range(MAX_TOOL_ROUNDS + 1):
            resp = _chat(messages, tool_schemas, "auto")
            _acc_usage(trace, resp)
            choice = resp.choices[0]
            msg = choice.message
            tool_calls = msg.tool_calls or []
            round_rec = {
                "round": round_idx,
                "finish_reason": choice.finish_reason,
                "served_model": getattr(resp, "model", None),
                "served_provider": (getattr(resp, "model_extra", None) or {}).get("provider"),
                "tool_calls": [{"id": tc.id, "name": tc.function.name,
                                "args": tc.function.arguments,
                                "is_error": False} for tc in tool_calls],
                "content": msg.content,
            }

            # Append assistant turn. DeepSeek V4 thinking-mode requires reasoning_content to be
            # echoed back on the assistant turn that produced tool calls (400 otherwise); other
            # providers don't emit it, so getattr returns None and it is harmlessly skipped.
            asst = {"role": "assistant", "content": msg.content or ""}
            _rc = getattr(msg, "reasoning_content", None)
            if _rc:
                asst["reasoning_content"] = _rc
            if tool_calls:
                asst["tool_calls"] = [
                    {"id": tc.id, "type": "function",
                     "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                    for tc in tool_calls
                ]
            messages.append(asst)

            if not tool_calls:
                trace["final_text"] = msg.content or ""
                trace["rounds"].append(round_rec)
                break

            for tc in tool_calls:
                result = run_tc(tc, state)
                if result.get("error"):
                    for c in round_rec["tool_calls"]:
                        if c["id"] == tc.id:
                            c["is_error"] = True
                trace["tool_calls_total"] += 1
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result, ensure_ascii=False),
                })
            trace["rounds"].append(round_rec)

            if round_idx == MAX_TOOL_ROUNDS:
                trace["error"] = "max_tool_rounds_exhausted"
                messages.append({
                    "role": "user",
                    "content": "Please give your final answer now based on what you've found.",
                })
                try:
                    resp2 = _chat(messages, tool_schemas, "none")
                    _acc_usage(trace, resp2)
                    trace["final_text"] = resp2.choices[0].message.content or ""
                except Exception:
                    trace["final_text"] = ""
                break
    except Exception as exc:
        trace["error"] = f"{type(exc).__name__}: {exc}"

    trace["elapsed_ms"] = int((time.time() - t0) * 1000)
    final_text = trace.get("final_text") or (f"[agent error: {trace['error']}]" if trace.get("error") else "")
    (raw_dir / f"{iid}.md").write_text(final_text, encoding="utf-8")
    (trace_dir / f"{iid}.json").write_text(
        json.dumps(trace, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return trace


# ---------------- responses provider (gpt-5.x: tools+reasoning only on /v1/responses) ----------
def _resp(**kwargs):
    """client.responses.create with retry/backoff."""
    delay, last = 2.0, None
    for attempt in range(4):
        try:
            return client.responses.create(**kwargs)
        except Exception as exc:  # transient
            last = exc
            if attempt == 3:
                raise
            time.sleep(delay)
            delay *= 2
    raise last  # unreachable


def _dispatch_responses(name, args, repl_globals):
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


def run_item_responses(item: dict, tool_name: str, run_dir: Path, resume: bool = False) -> dict:
    """Responses-API tool loop (chained via previous_response_id so reasoning persists
    server-side). Same trace schema + raw/<id>.md output as the chat path."""
    iid = item["id"]
    question = item["question"]
    raw_dir = run_dir / "raw"
    trace_dir = run_dir / "traces"
    trace_path = trace_dir / f"{iid}.json"
    if resume and trace_path.exists():
        return json.loads(trace_path.read_text(encoding="utf-8"))
    raw_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    chat_tools, _ = build_tools(tool_name)  # flatten chat-shape -> responses function-tool shape
    resp_tools = [{"type": "function", "name": t["function"]["name"],
                   "description": t["function"]["description"],
                   "parameters": t["function"]["parameters"]} for t in chat_tools]
    repl_globals = create_repl_globals() if tool_name == "repl" else None

    trace = {
        "id": iid, "bucket": item.get("bucket"), "language": item.get("language"),
        "question": question, "model": MODEL_ID, "tool": tool_name,
        "rounds": [], "final_text": None, "tool_calls_total": 0,
        "input_tokens_total": 0, "output_tokens_total": 0,
        "error": None, "elapsed_ms": None,
    }
    t0 = time.time()
    prev_id = None
    next_input = [{"role": "user", "content": question}]
    try:
        for round_idx in range(MAX_TOOL_ROUNDS + 1):
            kw = dict(model=MODEL_ID, instructions=SYSTEM_PROMPT, tools=resp_tools,
                      tool_choice="auto", input=next_input, **CALL_PARAMS)
            if prev_id:
                kw["previous_response_id"] = prev_id
            r = _resp(**kw)
            _acc_usage(trace, r)
            prev_id = r.id
            fcalls = [o for o in r.output if getattr(o, "type", None) == "function_call"]
            text = getattr(r, "output_text", "") or ""
            round_rec = {
                "round": round_idx, "finish_reason": getattr(r, "status", None),
                "tool_calls": [{"id": fc.call_id, "name": fc.name, "args": fc.arguments,
                                "is_error": False} for fc in fcalls],
                "content": text,
            }
            if not fcalls:
                trace["final_text"] = text
                trace["rounds"].append(round_rec)
                break
            next_input = []  # previous_response_id carries history; send only the new outputs
            for fc in fcalls:
                try:
                    args = json.loads(fc.arguments or "{}")
                except Exception:
                    args = {}
                result = _dispatch_responses(fc.name, args, repl_globals)
                if result.get("error"):
                    for c in round_rec["tool_calls"]:
                        if c["id"] == fc.call_id:
                            c["is_error"] = True
                trace["tool_calls_total"] += 1
                next_input.append({"type": "function_call_output", "call_id": fc.call_id,
                                   "output": json.dumps(result, ensure_ascii=False)})
            trace["rounds"].append(round_rec)

            if round_idx == MAX_TOOL_ROUNDS:
                trace["error"] = "max_tool_rounds_exhausted"
                next_input.append({"role": "user",
                                   "content": "Please give your final answer now based on what you've found."})
                try:
                    r2 = _resp(model=MODEL_ID, instructions=SYSTEM_PROMPT, tools=resp_tools,
                               tool_choice="none", input=next_input, previous_response_id=prev_id, **CALL_PARAMS)
                    _acc_usage(trace, r2)
                    trace["final_text"] = getattr(r2, "output_text", "") or ""
                except Exception:
                    trace["final_text"] = ""
                break
    except Exception as exc:
        trace["error"] = f"{type(exc).__name__}: {exc}"

    trace["elapsed_ms"] = int((time.time() - t0) * 1000)
    final_text = trace.get("final_text") or (f"[agent error: {trace['error']}]" if trace.get("error") else "")
    (raw_dir / f"{iid}.md").write_text(final_text, encoding="utf-8")
    (trace_dir / f"{iid}.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2), encoding="utf-8")
    return trace


# ---------------- anthropic provider (Sonnet/Opus: native Messages API + tool-use) ----------
def anthropic_tools(tool_name: str):
    """Raw tool dicts are already {name, description, input_schema} = Anthropic's shape."""
    raw = {"search": [SEARCH_EMPLOYEES_TOOL], "repl": [PYTHON_REPL_TOOL],
           "grep": [GREP_CSV_TOOL, READ_CSV_ROWS_TOOL], "grep-only": [GREP_CSV_TOOL],
           "both": [SEARCH_EMPLOYEES_TOOL, GREP_CSV_TOOL, READ_CSV_ROWS_TOOL]}
    if tool_name not in raw:
        raise ValueError(f"Unknown tool: {tool_name}")
    return raw[tool_name]


def _msg(**kwargs):
    """client.messages.create with retry/backoff."""
    delay, last = 2.0, None
    for attempt in range(4):
        try:
            return client.messages.create(**kwargs)
        except Exception as exc:  # transient: rate-limit / 5xx / overloaded
            last = exc
            if attempt == 3:
                raise
            time.sleep(delay)
            delay *= 2
    raise last  # unreachable


def run_item_anthropic(item: dict, tool_name: str, run_dir: Path, resume: bool = False) -> dict:
    """Anthropic Messages-API tool loop. System prompt is cached (ephemeral) to cut cost
    across the sweep. Same trace schema + raw/<id>.md output as the other providers."""
    iid = item["id"]
    question = item["question"]
    raw_dir = run_dir / "raw"
    trace_dir = run_dir / "traces"
    trace_path = trace_dir / f"{iid}.json"
    if resume and trace_path.exists():
        return json.loads(trace_path.read_text(encoding="utf-8"))
    raw_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    tools = anthropic_tools(tool_name)
    repl_globals = create_repl_globals() if tool_name == "repl" else None
    system = [{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}]
    messages = [{"role": "user", "content": question}]
    trace = {
        "id": iid, "bucket": item.get("bucket"), "language": item.get("language"),
        "question": question, "model": MODEL_ID, "tool": tool_name,
        "rounds": [], "final_text": None, "tool_calls_total": 0,
        "input_tokens_total": 0, "output_tokens_total": 0,
        "error": None, "elapsed_ms": None,
    }
    t0 = time.time()
    try:
        for round_idx in range(MAX_TOOL_ROUNDS + 1):
            r = _msg(model=MODEL_ID, system=system, messages=messages, tools=tools, **CALL_PARAMS)
            _acc_usage(trace, r)
            tool_uses = [b for b in r.content if getattr(b, "type", None) == "tool_use"]
            text = "".join(b.text for b in r.content if getattr(b, "type", None) == "text")
            round_rec = {
                "round": round_idx, "finish_reason": r.stop_reason,
                "tool_calls": [{"id": b.id, "name": b.name,
                                "args": json.dumps(b.input, ensure_ascii=False), "is_error": False}
                               for b in tool_uses],
                "content": text,
            }
            messages.append({"role": "assistant", "content": r.content})  # pass blocks back verbatim
            if not tool_uses:
                trace["final_text"] = text
                trace["rounds"].append(round_rec)
                break
            results = []
            for b in tool_uses:
                result = _dispatch_responses(b.name, b.input or {}, repl_globals)
                if result.get("error"):
                    for c in round_rec["tool_calls"]:
                        if c["id"] == b.id:
                            c["is_error"] = True
                trace["tool_calls_total"] += 1
                results.append({"type": "tool_result", "tool_use_id": b.id,
                                "content": json.dumps(result, ensure_ascii=False)})
            messages.append({"role": "user", "content": results})
            trace["rounds"].append(round_rec)

            if round_idx == MAX_TOOL_ROUNDS:
                trace["error"] = "max_tool_rounds_exhausted"
                messages.append({"role": "user",
                                 "content": "Please give your final answer now based on what you've found."})
                try:
                    r2 = _msg(model=MODEL_ID, system=system, messages=messages, **CALL_PARAMS)  # no tools → forces text
                    _acc_usage(trace, r2)
                    trace["final_text"] = "".join(b.text for b in r2.content if getattr(b, "type", None) == "text")
                except Exception:
                    trace["final_text"] = ""
                break
    except Exception as exc:
        trace["error"] = f"{type(exc).__name__}: {exc}"

    trace["elapsed_ms"] = int((time.time() - t0) * 1000)
    final_text = trace.get("final_text") or (f"[agent error: {trace['error']}]" if trace.get("error") else "")
    (raw_dir / f"{iid}.md").write_text(final_text, encoding="utf-8")
    (trace_dir / f"{iid}.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2), encoding="utf-8")
    return trace


def main():
    global SYSTEM_PROMPT, MODEL_ID, CALL_PARAMS, client, PROVIDER
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", choices=list(MODELS), default="opentyphoon",
                    help="Model spec key (default opentyphoon).")
    ap.add_argument("--tool", choices=["search", "repl", "grep", "grep-only", "both"], required=True)
    ap.add_argument("--prompt", choices=list(PROMPT_FILES.keys()), default="L2",
                    help="System prompt variant: L1 (medium), L2 (current strong), L2fs (L2 + refusal few-shot).")
    ap.add_argument("--questions", type=str, default=str(DEFAULT_QUESTIONS))
    ap.add_argument("--answer-key", type=str, default=str(ANSWER_KEY),
                    help="JSON with items/questions for bucket metadata (v0.2: questions_v02.json).")
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--ids", type=str, default=None)
    ap.add_argument("--stamp", type=str, default=None)
    ap.add_argument("--resume", action="store_true", help="Skip items whose trace already exists.")
    ap.add_argument("--concurrency", type=int, default=1,
                    help="Parallel in-flight items (thread pool). Each item writes its own trace/raw "
                         "files + measures its own per-request latency, so latency stays clean. Use for "
                         "slow OpenRouter reasoning models (e.g. DeepSeek-pro ~10h serial → ~1.5h @8).")
    args = ap.parse_args()

    spec = MODELS[args.model]
    key = os.environ.get(spec["key_env"]) or os.environ.get(spec.get("key_fallback", ""), "")
    if not key:
        raise SystemExit(f"{spec['key_env']} (or fallback) not set in .env")
    if spec["provider"] == "anthropic":
        import anthropic
        client = anthropic.Anthropic(api_key=key)
    else:
        kw = {"api_key": key}
        if spec.get("base_url"):
            kw["base_url"] = spec["base_url"]
        if spec.get("extra_headers"):           # browser UA for the Cloudflare-fronted ThaiLLM gateway
            kw["default_headers"] = spec["extra_headers"]
        client = OpenAI(**kw)
    MODEL_ID, CALL_PARAMS, PROVIDER = spec["model_id"], spec["params"], spec["provider"]

    SYSTEM_PROMPT = PROMPT_FILES[args.prompt].read_text(encoding="utf-8")

    items: list[dict] = []
    with open(args.questions, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            items.append({"id": row["id"], "language": row.get("language", ""), "question": row["question"]})

    ak = json.loads(Path(args.answer_key).read_text(encoding="utf-8"))
    ak_items = ak.get("items") or ak.get("questions") or []  # v0.1 uses "items", v0.2 uses "questions"
    bucket_by_id = {q["id"]: q.get("bucket") for q in ak_items}
    for it in items:
        it["bucket"] = bucket_by_id.get(it["id"])

    if args.ids:
        wanted = set(args.ids.split(","))
        items = [x for x in items if x["id"] in wanted]
    if args.limit:
        items = items[: args.limit]

    stamp = args.stamp or datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = ROOT / "runs" / f"{args.model}_{args.tool}_{args.prompt}_{stamp}"
    run_dir.mkdir(parents=True, exist_ok=True)

    manifest = {
        "model": MODEL_ID,
        "model_key": args.model,
        "base_url": spec.get("base_url"),
        "tool": args.tool,
        "tool_name": {"search": "search_employees", "repl": "python_repl",
                      "grep": "grep_csv+read_csv_rows",
                      "grep-only": "grep_csv",
                      "both": "search_employees+grep_csv+read_csv_rows"}[args.tool],
        "kb": os.environ.get("FAHMAI_KB", "knowledge_base/employees.csv"),
        "answer_key": args.answer_key,
        "prompt_variant": args.prompt,
        "prompt_file": str(PROMPT_FILES[args.prompt].name),
        "prompt_chars": len(SYSTEM_PROMPT),
        "questions_file": args.questions,
        "item_count": len(items),
        "started_at": datetime.now().isoformat(),
        "max_tool_rounds": MAX_TOOL_ROUNDS,
    }
    (run_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

    print(f"Run dir: {run_dir}")
    print(f"Model:   {MODEL_ID}")
    print(f"Tool:    {args.tool}")
    print(f"Prompt:  {args.prompt} ({len(SYSTEM_PROMPT)} chars)")
    print(f"Items:   {len(items)}")

    t0 = time.time()
    tc_total = err_total = 0
    conc = max(1, args.concurrency)

    def _report(i, trace):
        nonlocal tc_total, err_total
        tc_total += trace["tool_calls_total"]
        if trace.get("error"): err_total += 1
        if i % 10 == 0 or i == len(items):
            elapsed = time.time() - t0
            rate = i / elapsed if elapsed else 0
            eta = (len(items) - i) / rate if rate else 0
            print(f"  [{i}/{len(items)}] {trace['id']} tc={tc_total} err={err_total} · "
                  f"{elapsed:.0f}s · ETA {eta:.0f}s")

    if conc == 1:
        for i, it in enumerate(items, 1):
            _report(i, run_item(it, args.tool, run_dir, resume=args.resume))
    else:
        # Items are independent (own trace/raw files, own state, thread-safe SDK client) → fan out.
        from concurrent.futures import ThreadPoolExecutor, as_completed
        print(f"Concurrency: {conc}")
        done = 0
        with ThreadPoolExecutor(max_workers=conc) as ex:
            futs = {ex.submit(run_item, it, args.tool, run_dir, args.resume): it for it in items}
            for fut in as_completed(futs):
                done += 1
                _report(done, fut.result())

    print(f"\nDone in {time.time()-t0:.0f}s. tool_calls={tc_total} errors={err_total}")
    print(f"Grade: python scripts/grade.py {run_dir}")


if __name__ == "__main__":
    main()
