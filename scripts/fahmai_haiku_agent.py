"""Haiku 4.5 agent for FahMai directory questions.

Port of `the source telephone-directory project/ikq_haiku_agent.py` with:
  - System prompt: fahmai_system_prompt.md (FahMai universe + canonical refusals)
  - Tool: fahmai_csv_tool.SEARCH_EMPLOYEES_TOOL
  - Workspace .env discovery walked up to the workspace root
  - Model picked via FAHMAI_AGENT_MODEL env var (default: Haiku)
"""
from __future__ import annotations

import json, os, sys, time
from pathlib import Path
from typing import Any

import anthropic

from fahmai_csv_tool import SEARCH_EMPLOYEES_TOOL, search_employees
from fahmai_grep_tool import GREP_CSV_TOOL, READ_CSV_ROWS_TOOL, grep_csv, read_csv_rows

MODEL = os.environ.get("FAHMAI_AGENT_MODEL", "claude-haiku-4-5-20251001")
MAX_TOKENS = 4096
MAX_TOOL_ROUNDS = int(os.environ.get("FAHMAI_MAX_TOOL_ROUNDS", "3"))
TOOL_MODE = os.environ.get("FAHMAI_TOOL", "search")  # search | grep | grep-only

_HERE = Path(__file__).resolve().parent
_SYSTEM_PROMPT_PATH = _HERE / "fahmai_system_prompt.md"


def _find_env_file() -> Path | None:
    for d in [_HERE] + list(_HERE.parents)[:6]:
        p = d / ".env"
        if p.exists(): return p
    return None


def _load_env() -> None:
    p = _find_env_file()
    if p is None: return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line: continue
        k, _, v = line.partition("=")
        os.environ[k.strip()] = v.strip()


_load_env()
if not os.environ.get("ANTHROPIC_API_KEY"):
    raise SystemExit("ANTHROPIC_API_KEY not set. Add it to workspace .env or export in shell.")

SYSTEM_PROMPT = _SYSTEM_PROMPT_PATH.read_text(encoding="utf-8")
_client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def _tools_for_mode(mode: str) -> list[dict]:
    """Return Anthropic-shape tool definitions for the selected mode."""
    if mode == "search":
        return [SEARCH_EMPLOYEES_TOOL]
    if mode == "grep":
        return [GREP_CSV_TOOL, READ_CSV_ROWS_TOOL]
    if mode == "grep-only":
        return [GREP_CSV_TOOL]
    raise ValueError(f"Unknown FAHMAI_TOOL: {mode}")


def _run_tool_call(name: str, input_: dict):
    if name == "search_employees":
        return search_employees(**input_)
    if name == "grep_csv":
        return grep_csv(**input_)
    if name == "read_csv_rows":
        return read_csv_rows(**input_)
    return {"error": f"unknown tool '{name}'"}


_TOOLS_CACHED = [
    {**t, "cache_control": {"type": "ephemeral"}}
    for t in _tools_for_mode(TOOL_MODE)
]


def _extract_text(blocks) -> str:
    return "\n".join(b.text for b in blocks if getattr(b, "type", None) == "text").strip()


def _to_content_dicts(blocks) -> list[dict]:
    out = []
    for b in blocks:
        t = getattr(b, "type", None)
        if t == "text":
            out.append({"type": "text", "text": b.text})
        elif t == "tool_use":
            out.append({"type": "tool_use", "id": b.id, "name": b.name, "input": b.input})
    return out


def run_item(item: dict, run_dir: Path, verbose: bool = False) -> dict:
    iid = item["id"]
    question = item["question"]
    raw_dir = run_dir / "raw"
    trace_dir = run_dir / "traces"
    raw_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    messages: list[dict] = [{"role": "user", "content": question}]
    trace: dict[str, Any] = {
        "id": iid, "bucket": item.get("bucket"), "question": question, "model": MODEL,
        "rounds": [], "final_text": None, "stop_reason": None,
        "tool_calls_total": 0, "input_tokens_total": 0, "output_tokens_total": 0,
        "error": None, "elapsed_ms": None,
    }
    t0 = time.time()

    try:
        for round_idx in range(MAX_TOOL_ROUNDS + 1):
            resp = _client.messages.create(
                model=MODEL,
                system=[{"type": "text", "text": SYSTEM_PROMPT,
                         "cache_control": {"type": "ephemeral"}}],
                tools=_TOOLS_CACHED,
                max_tokens=MAX_TOKENS, messages=messages,
            )
            stop_reason = resp.stop_reason
            content_dicts = _to_content_dicts(resp.content)
            in_tok = getattr(resp.usage, "input_tokens", 0) or 0
            out_tok = getattr(resp.usage, "output_tokens", 0) or 0
            cache_read = getattr(resp.usage, "cache_read_input_tokens", 0) or 0
            cache_create = getattr(resp.usage, "cache_creation_input_tokens", 0) or 0
            trace["input_tokens_total"] += in_tok
            trace["output_tokens_total"] += out_tok
            trace.setdefault("cache_read_total", 0)
            trace.setdefault("cache_create_total", 0)
            trace["cache_read_total"] += cache_read
            trace["cache_create_total"] += cache_create
            round_rec = {"round": round_idx, "stop_reason": stop_reason, "tool_calls": [],
                         "usage": {"input_tokens": in_tok, "output_tokens": out_tok,
                                   "cache_read": cache_read, "cache_create": cache_create}}
            messages.append({"role": "assistant", "content": content_dicts})

            if stop_reason == "tool_use":
                tool_results_msg = []
                for b in resp.content:
                    if getattr(b, "type", None) != "tool_use": continue
                    tool_input = b.input or {}
                    try:
                        result = _run_tool_call(b.name, tool_input); is_error = False
                    except Exception as exc:
                        result = {"error": f"{type(exc).__name__}: {exc}"}; is_error = True
                    if isinstance(result, dict) and result.get("error"):
                        is_error = True
                    round_rec["tool_calls"].append({
                        "tool": b.name, "input": tool_input,
                        "total_matches": result.get("total_matches") or result.get("total") if isinstance(result, dict) and not is_error else None,
                        "is_error": is_error,
                    })
                    trace["tool_calls_total"] += 1
                    tool_results_msg.append({
                        "type": "tool_result", "tool_use_id": b.id,
                        "content": json.dumps(result, ensure_ascii=False), "is_error": is_error,
                    })
                messages.append({"role": "user", "content": tool_results_msg})
                trace["rounds"].append(round_rec)
                if round_idx == MAX_TOOL_ROUNDS:
                    trace["error"] = "max_tool_rounds_exhausted"; break
                continue

            trace["rounds"].append(round_rec)
            trace["stop_reason"] = stop_reason
            trace["final_text"] = _extract_text(resp.content)
            break

    except anthropic.APIError as exc:
        trace["error"] = f"APIError: {exc}"

    trace["elapsed_ms"] = int((time.time() - t0) * 1000)
    final_text = trace.get("final_text") or (f"[agent error: {trace['error']}]" if trace.get("error") else "")
    (raw_dir / f"{iid}.md").write_text(final_text, encoding="utf-8")
    (trace_dir / f"{iid}.json").write_text(json.dumps(trace, ensure_ascii=False, indent=2), encoding="utf-8")

    if verbose:
        tc, it_, ot = trace["tool_calls_total"], trace["input_tokens_total"], trace["output_tokens_total"]
        print(f"  {iid} [{item.get('bucket','?'):22}] — {tc} tool calls, in={it_} out={ot}, {trace['elapsed_ms']}ms")

    return trace


if __name__ == "__main__":
    import tempfile
    sys.stdout.reconfigure(encoding="utf-8")
    tmp = Path(tempfile.mkdtemp(prefix="fahmai_agent_probe_"))
    item = {"id": "probe_cfo", "bucket": "evp_identity_by_code", "question": "ใครเป็น CFO"}
    t = run_item(item, tmp, verbose=True)
    print(json.dumps({k: v for k, v in t.items() if k != "rounds"}, ensure_ascii=False, indent=2))
    print(f"Raw: {(tmp / 'raw' / 'probe_cfo.md').read_text(encoding='utf-8')}")
