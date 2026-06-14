"""Pandas REPL tool for FahMai directory questions.

Contrast to `fahmai_csv_tool.py` (custom-filter `search_employees`):
  - This tool exposes a single `python_repl(code)` that executes against a
    persistent DataFrame `df` holding the employee CSV.
  - Pre-loaded globals: `df` (1995 rows × 19 cols), `pd`.
  - Last expression's repr is returned Jupyter-style; stdout is captured.
  - Output truncated to ~4 KB to avoid flooding the model's context.

Design intent: mirror what a subagent with Bash/Python access has at hand.
Comparing the two baselines shows how much of "tool-calling baseline score"
is driven by tool engineering vs raw model capability.
"""
from __future__ import annotations

import ast
import io
import os
import sys
from pathlib import Path
from typing import Any

import pandas as pd

_DEFAULT_KB = Path(__file__).resolve().parent.parent / "knowledge_base" / "employees.csv"
CSV_PATH = Path(os.environ.get("FAHMAI_KB", _DEFAULT_KB))  # set FAHMAI_KB=...employees_v02.csv for v0.2

# Load once at import.
_DF = pd.read_csv(CSV_PATH, encoding="utf-8-sig", dtype=str).fillna("")


def create_repl_globals() -> dict:
    """Fresh globals dict per conversation — prevents cross-item state leak."""
    return {"df": _DF.copy(), "pd": pd}


def python_repl(code: str, globals_dict: dict) -> dict:
    """Execute `code` against the persistent globals_dict.

    Returns {stdout, result, error}:
      - stdout:  everything printed during execution
      - result:  repr() of the last expression (Jupyter-style), or None
      - error:   exception type + message, or None
    All strings truncated to ~4KB.
    """
    buf = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buf
    result_value: Any = None
    error: str | None = None
    try:
        tree = ast.parse(code, mode="exec")
        if tree.body and isinstance(tree.body[-1], ast.Expr):
            # Split: exec everything except last statement, then eval last expr.
            exec_src = ast.Module(body=tree.body[:-1], type_ignores=[])
            expr = ast.Expression(body=tree.body[-1].value)
            exec(compile(exec_src, "<repl>", "exec"), globals_dict)
            result_value = eval(compile(expr, "<repl>", "eval"), globals_dict)
        else:
            exec(compile(tree, "<repl>", "exec"), globals_dict)
    except Exception as exc:
        error = f"{type(exc).__name__}: {exc}"
    finally:
        sys.stdout = old_stdout

    stdout = buf.getvalue()
    if error:
        return {"stdout": _trunc(stdout), "result": None, "error": error}

    result_repr: str | None = None
    if result_value is not None:
        try:
            result_repr = repr(result_value)
        except Exception as exc:  # noqa: BLE001
            result_repr = f"<unrepresentable: {type(exc).__name__}>"

    return {"stdout": _trunc(stdout), "result": _trunc(result_repr), "error": None}


def _trunc(s: str | None, n: int = 4000) -> str | None:
    if s is None:
        return None
    return s if len(s) <= n else s[:n] + f"\n... [truncated {len(s)-n} chars]"


PYTHON_REPL_TOOL: dict[str, Any] = {
    "name": "python_repl",
    "description": (
        "Execute Python code against a persistent pandas DataFrame `df` holding "
        "the FahMai employee directory (1995 rows × 19 columns). "
        "Columns: `Employee ID`, `Department`, `Section`, `Unit`, `Position in Thai`, "
        "`Position in English`, `First Name Thai`, `Last Name Thai`, `First Name English`, "
        "`Last Name English`, `Nickname Thai`, `Nickname English`, `Email Address`, "
        "`Phone Extension`, `Mobile No.`, `Office Location`, `Branch`, `Start Year`, "
        "`Position Level`. All cells are strings. `pd` and `df` are pre-imported. "
        "The last expression's repr is returned Jupyter-style (include it to see data). "
        "Use standard pandas filters, e.g. "
        "`df[df['Unit']=='CFO'][['First Name Thai','Last Name Thai','Phone Extension']].to_dict('records')`. "
        "Outputs truncated to ~4KB; paginate or narrow the query if needed."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "code": {
                "type": "string",
                "description": "Python code to execute. Multi-line allowed. Last expression is returned.",
            },
        },
        "required": ["code"],
    },
}


if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    g = create_repl_globals()
    print(f"Loaded {len(_DF)} rows")
    print("\n--- df[df['Unit']=='CFO'][['First Name Thai','Last Name Thai','Phone Extension']] ---")
    r = python_repl("df[df['Unit']=='CFO'][['First Name Thai','Last Name Thai','Phone Extension']]", g)
    print(r)
    print("\n--- multi-statement ---")
    r = python_repl(
        "cfo = df[df['Unit']=='CFO'].iloc[0]\n"
        "f\"{cfo['First Name Thai']} {cfo['Last Name Thai']} / ext {cfo['Phone Extension']}\"",
        g,
    )
    print(r)
    print("\n--- error case ---")
    r = python_repl("df[df['BadCol']=='x']", g)
    print(r)
