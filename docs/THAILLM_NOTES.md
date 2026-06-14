# ThaiLLM API — reverse-engineered reference

Discovered during Gate G exploration (2026-04-19). No public developer docs found — figured out by probing `api.thaillm.or.th` directly.

## Endpoint

```
https://api.thaillm.or.th/<family>/v1/chat/completions
```

OpenAI-compatible chat/completions schema. Same gateway (Kong in front of vLLM backend) for all 4 model families.

## Authentication

Header:

```
apikey: <THAILLM_API_KEY>
```

Lowercase, no hyphen. **Not** `Authorization: Bearer ...`, **not** `x-api-key`. Bearer/x-api-key return 401 "No API key found in request"; only `apikey` is read by the Kong plugin. The workspace `.env` key is 32 chars.

## Model families and model IDs

| Family URL | Model ID | Underlying model | Notes |
|---|---|---|---|
| `/typhoon/` | `/model` | typhoon-s-thaillm-8b-instruct | SCB 10X — **native tool-calling works** |
| `/openthaigpt/` | `/model` | openthaigpt-thaillm-8b-instruct-v0.7.2 | AIEAT — emits `<think>` reasoning, no tool_calls |
| `/pathumma/` | `/model` | pathumma-thaillm-8b-think | NECTEC — reasoning model (`-think` suffix), no tool_calls |
| `/kbtg/` | `/model` | THaLLE-0.2-ThaiLLM-8B-fa | KBTG — no tool_calls |

Always pass `"model": "/model"` in the request body (the gateway routes by URL path, not model ID).

Context window: **16,384 tokens** across all four. The full 1,995-row FahMai CSV does NOT fit — tool-use/retrieval is mandatory.

## Tool schema format

**OpenAI-compatible**, NOT Anthropic flat shape.

```json
{
  "type": "function",
  "function": {
    "name": "search_employees",
    "description": "...",
    "parameters": { ...JSON schema... }
  }
}
```

Our `fahmai_csv_tool.SEARCH_EMPLOYEES_TOOL` uses Anthropic's flat `{name, description, input_schema}` shape. Convert before sending:

```python
oai_tool = {
    "type": "function",
    "function": {
        "name": t["name"],
        "description": t["description"],
        "parameters": t["input_schema"],
    },
}
```

## Tool-use response shape

OpenAI-compat. When `finish_reason == "tool_calls"`:

```json
{
  "message": {
    "role": "assistant",
    "content": null,
    "tool_calls": [{"id": "...", "type": "function",
                    "function": {"name": "...", "arguments": "{\"k\":\"v\"}"}}]
  }
}
```

Feed results back as `{"role": "tool", "tool_call_id": "...", "content": "<json>"}`.

## End-to-end smoke test (Typhoon)

`Q: ขอเบอร์ต่อของ CFO หน่อย` → Typhoon emits a tool_call for `search_employees(unit="CFO", position_contains="CFO", position_serves_unit="CFO", limit=1)` → we execute locally → Typhoon replies. Confirms the pipeline works.

Observed weaknesses:
- **Over-constrains filters** (ANDs 3 redundant parameters so 0 rows match).
- **Canonical-phrase selection is lossy** — used `ขอปฏิเสธคำขอ` (injection canonical) when zero results came back, instead of `ไม่พบข้อมูล` (not-found canonical).

Both are prompt/harness issues solvable by better tool-description instructions and few-shot examples in the starter notebook.

## For the 3 non-tool-calling families (OpenThaiGPT / Pathumma / KBTG)

They generate `<think>` reasoning but **do not format tool calls**. Any baseline for these must use the **two-pass pattern**:

1. Prompt model: "Output a JSON object for `search_employees` filters."
2. Parse JSON → execute `search_employees(**filters)` locally.
3. Prompt model again: "Here are the rows. Answer the user's question."

This pattern belongs in the starter notebook as the fallback path.

## Cost

The gateway is described on `thaillm.or.th` as "currently free to the public." No known rate limit documented — don't stress-test without pacing. For a 349-item baseline run with a 1.5s per-call average, expect ~10 minutes end-to-end for Typhoon.

## Minimal working example

```python
import json, urllib.request, os
KEY = os.environ["THAILLM_API_KEY"]
body = {
    "model": "/model",
    "messages": [{"role": "user", "content": "สวัสดี"}],
    "max_tokens": 100,
}
req = urllib.request.Request(
    "https://api.thaillm.or.th/typhoon/v1/chat/completions",
    data=json.dumps(body).encode("utf-8"),
    headers={"apikey": KEY, "Content-Type": "application/json"},
)
print(json.loads(urllib.request.urlopen(req).read()))
```
