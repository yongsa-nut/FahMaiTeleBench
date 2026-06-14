"""Grep+Read tool shape for FahMai directory — no code execution.

Mimics Claude Code's Grep/Read primitives over the employees.csv:
  - grep_csv(pattern): case-insensitive substring across all rows → matching rows
  - read_csv_rows(start, end): windowed slice of the CSV by row index

Contrast with:
  - fahmai_csv_tool.py — structured filter (`unit=`, `department=`, ...)
  - fahmai_repl_tool.py — arbitrary pandas code execution

This tool gives the model text-level access without letting it write code.
"""
from __future__ import annotations

import csv
import io
import os
import sys
from pathlib import Path
from typing import Any

_DEFAULT_KB = Path(__file__).resolve().parent.parent / "knowledge_base" / "employees.csv"
CSV_PATH = Path(os.environ.get("FAHMAI_KB", _DEFAULT_KB))  # set FAHMAI_KB=...employees_v02.csv for v0.2

with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    _FIELDS = reader.fieldnames or []
    _ROWS: list[dict] = list(reader)

MAX_GREP = 50
MAX_READ = 100


def grep_csv(pattern: str, max_matches: int = MAX_GREP) -> dict:
    """Case-insensitive substring search across all cells. Returns row index + row dict.

    max_matches caps output to avoid flooding the model; caller can narrow the pattern.
    """
    p = (pattern or "").lower()
    if not p:
        return {"error": "empty pattern", "matches": [], "total": 0}
    hits: list[dict] = []
    total = 0
    for i, row in enumerate(_ROWS):
        if any(p in (v or "").lower() for v in row.values()):
            total += 1
            if len(hits) < max_matches:
                hits.append({"row": i, **row})
    return {
        "total": total,
        "returned": len(hits),
        "truncated": total > len(hits),
        "matches": hits,
    }


def read_csv_rows(start: int, end: int) -> dict:
    """Return rows[start:end] (0-indexed, end-exclusive), capped at MAX_READ."""
    if start < 0 or end < 0 or end <= start:
        return {"error": "invalid range", "rows": []}
    if end - start > MAX_READ:
        end = start + MAX_READ
    return {
        "fields": _FIELDS,
        "total_rows": len(_ROWS),
        "start": start,
        "end": end,
        "rows": [{"row": i, **_ROWS[i]} for i in range(start, min(end, len(_ROWS)))],
    }


GREP_CSV_TOOL: dict[str, Any] = {
    "name": "grep_csv",
    "description": (
        f"Case-insensitive substring search across ALL cells of the FahMai employee CSV "
        f"({len(_ROWS)} rows × {len(_FIELDS)} columns). Returns matching rows (up to {MAX_GREP}) "
        f"with their 0-indexed row number. Columns: {', '.join(_FIELDS)}. "
        "Example row (shape only, not a real employee): "
        "Employee ID=08234567 (8 digits, starts with 00/08), Department=TEC (3-letter code), "
        "Section=TEC-MOB, Unit=TEC-MOB-3 (C-level units are CFO/CTO/...; VPs are SFVP/DNVP/...; EAs are CEO-EA/FIN-EA/...), "
        "Position in Thai=วิศวกรซอฟต์แวร์, Position in English=SOFTWARE ENGINEER (uppercase), "
        "First Name Thai=สมชาย, Last Name Thai=ใจดี, First Name English=SOMCHAI, Last Name English=JAIDEE (uppercase), "
        "Nickname Thai=บีม, Nickname English=BEAM (may be blank), "
        "Email Address=SOMCHAI.JA@FAHMAI.CO.TH, Phone Extension=72345 (5 digits, may be blank), "
        "Mobile No.=081-234-5678 (may be blank), Office Location=FahMai Tower 8F, "
        "Branch=BKK-R9 (HQ; other codes CNX, KKN, HKT, HDY, ...), Start Year=2021, "
        "Position Level=IC (one of C-level/VP/Director/Manager/Lead/IC). "
        "Use this to find a person by any field (name, nickname, unit code, extension, email, etc.). "
        "Narrow the pattern if `truncated=true`."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "pattern": {"type": "string", "description": "Substring to search for. Case-insensitive."},
            "max_matches": {"type": "integer", "description": f"Max rows to return (default {MAX_GREP}).", "default": MAX_GREP},
        },
        "required": ["pattern"],
    },
}

READ_CSV_ROWS_TOOL: dict[str, Any] = {
    "name": "read_csv_rows",
    "description": (
        f"Read a contiguous slice of the FahMai CSV (0-indexed, end-exclusive). "
        f"Returns up to {MAX_READ} rows per call. Use after `grep_csv` when you need to "
        "inspect nearby rows (e.g. to see a whole section/department). "
        f"Columns: {', '.join(_FIELDS)}."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "start": {"type": "integer", "description": "Starting row index (0-based)."},
            "end": {"type": "integer", "description": "Ending row index (exclusive). Capped so end-start ≤ 100."},
        },
        "required": ["start", "end"],
    },
}

GREP_READ_TOOLS = [GREP_CSV_TOOL, READ_CSV_ROWS_TOOL]


if __name__ == "__main__":
    import json
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(f"Loaded {len(_ROWS)} rows × {len(_FIELDS)} cols")
    print("\n--- grep_csv('CFO') ---")
    print(json.dumps(grep_csv("CFO"), ensure_ascii=False, indent=2)[:1000])
    print("\n--- read_csv_rows(0, 3) ---")
    print(json.dumps(read_csv_rows(0, 3), ensure_ascii=False, indent=2)[:1000])
