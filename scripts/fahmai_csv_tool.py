"""Structured-query tool over FahMai employees.csv.

Port of `the source telephone-directory project/the source CSV tool` with:
  - CSV path repointed to FahMai Level-2 knowledge_base
  - Tool description rewritten for FahMai code vocabulary (C-level + VP, not EVPN/MRVP)
  - Logic unchanged — deterministic pure-Python filter.
"""
from __future__ import annotations

import csv
import os
import re
from pathlib import Path
from typing import Any

_DEFAULT_KB = Path(__file__).resolve().parent.parent / "knowledge_base" / "employees.csv"
CSV_PATH = Path(os.environ.get("FAHMAI_KB", _DEFAULT_KB))  # set FAHMAI_KB=...employees_v02.csv for v0.2


def _load_rows(path) -> list[dict]:
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


_ROWS: list[dict] = _load_rows(CSV_PATH)


def _project(row: dict) -> dict:
    return {
        "employee_id": row.get("Employee ID", "").strip(),
        "name_th": f"{row.get('First Name Thai','').strip()} {row.get('Last Name Thai','').strip()}".strip(),
        "name_en": f"{row.get('First Name English','').strip()} {row.get('Last Name English','').strip()}".strip(),
        "nickname_th": row.get("Nickname Thai", "").strip(),
        "nickname_en": row.get("Nickname English", "").strip(),
        "unit": row.get("Unit", "").strip(),
        "department": row.get("Department", "").strip(),
        "section": row.get("Section", "").strip(),
        "position_en": row.get("Position in English", "").strip(),
        "position_th": row.get("Position in Thai", "").strip(),
        "extension": row.get("Phone Extension", "").strip(),
        "mobile": row.get("Mobile No.", "").strip(),
        "email": row.get("Email Address", "").strip(),
        "office_location": row.get("Office Location", "").strip(),
        "branch": row.get("Branch", "").strip(),
        "start_year": row.get("Start Year", "").strip(),
        "position_level": row.get("Position Level", "").strip(),
    }


def _name_match(row: dict, needle: str) -> bool:
    needle = needle.strip().lower()
    if not needle:
        return False
    fields = [row.get("First Name Thai", ""), row.get("Last Name Thai", ""),
              row.get("First Name English", ""), row.get("Last Name English", "")]
    haystack = " ".join(f.lower() for f in fields)
    tokens = [t for t in needle.replace(",", " ").split() if t]
    return all(t in haystack for t in tokens) if tokens else False


def _nickname_match(row: dict, needle: str) -> bool:
    needle = needle.strip().lower()
    if not needle:
        return False
    return needle in row.get("Nickname Thai", "").lower() or needle in row.get("Nickname English", "").lower()


def _position_contains(row: dict, needle: str) -> bool:
    needle = needle.strip().lower()
    if not needle:
        return False
    return needle in row.get("Position in English", "").lower() or needle in row.get("Position in Thai", "").lower()


def _position_serves_unit(row: dict, unit_token: str) -> bool:
    unit_token = unit_token.strip()
    if not unit_token:
        return False
    pt = row.get("Position in Thai", "")
    pe = row.get("Position in English", "")
    tokens_th = set(re.split(r"[^A-Za-z0-9]+", pt))
    tokens_en = set(re.split(r"[^A-Za-z0-9]+", pe))
    return unit_token in tokens_th or unit_token in tokens_en


def _org_contains(row: dict, needle: str) -> bool:
    needle = needle.strip().upper()
    if not needle:
        return False
    return needle in row.get("Department", "").upper() or \
           needle in row.get("Unit", "").upper() or \
           needle in row.get("Section", "").upper()


def search_employees(
    unit: str | None = None,
    position_contains: str | None = None,
    position_serves_unit: str | None = None,
    name: str | None = None,
    nickname: str | None = None,
    extension: str | None = None,
    mobile: str | None = None,
    department: str | None = None,
    section: str | None = None,
    org_contains: str | None = None,
    branch: str | None = None,
    position_level: str | None = None,
    employee_id: str | None = None,
    email: str | None = None,
    limit: int = 50,
) -> dict[str, Any]:
    """Filter FahMai employee rows. All filters combine with AND. Returns total_matches + results."""
    # Treat blank/whitespace string params as "not provided" — some models (e.g. gpt-5.x) fill
    # EVERY field with "" rather than omitting unused ones; "" is not None, so an empty filter
    # like position_contains="" would otherwise match nothing and zero out the whole result.
    _b = lambda v: None if (isinstance(v, str) and not v.strip()) else v
    unit, position_contains, position_serves_unit, name, nickname, extension, mobile, \
        department, section, org_contains, branch, position_level, employee_id, email = (
            _b(unit), _b(position_contains), _b(position_serves_unit), _b(name), _b(nickname),
            _b(extension), _b(mobile), _b(department), _b(section), _b(org_contains),
            _b(branch), _b(position_level), _b(employee_id), _b(email))
    limit = max(1, min(int(limit or 50), 500))
    matches: list[dict] = []
    for row in _ROWS:
        if unit is not None and row.get("Unit", "").strip().upper() != unit.strip().upper(): continue
        if department is not None and row.get("Department", "").strip().upper() != department.strip().upper(): continue
        if section is not None and row.get("Section", "").strip().upper() != section.strip().upper(): continue
        if org_contains is not None and not _org_contains(row, org_contains): continue
        if branch is not None and row.get("Branch", "").strip().upper() != branch.strip().upper(): continue
        if position_level is not None and row.get("Position Level", "").strip().lower() != position_level.strip().lower(): continue
        if employee_id is not None and row.get("Employee ID", "").strip() != employee_id.strip(): continue
        if extension is not None and row.get("Phone Extension", "").strip() != extension.strip(): continue
        if mobile is not None and mobile.strip() not in row.get("Mobile No.", ""): continue
        if email is not None and email.strip().lower() not in row.get("Email Address", "").lower(): continue
        if position_contains is not None and not _position_contains(row, position_contains): continue
        if position_serves_unit is not None and not _position_serves_unit(row, position_serves_unit): continue
        if name is not None and not _name_match(row, name): continue
        if nickname is not None and not _nickname_match(row, nickname): continue
        matches.append(row)

    total = len(matches)
    returned = matches[:limit]
    return {
        "total_matches": total,
        "returned": len(returned),
        "truncated": total > len(returned),
        "results": [_project(r) for r in returned],
    }


SEARCH_EMPLOYEES_TOOL: dict[str, Any] = {
    "name": "search_employees",
    "description": (
        "Search the FahMai (ฟ้าใหม่) employee directory. Filters combine with AND; pass only the fields you need. "
        "Returns total_matches, returned rows, and a truncated flag. "
        "Use `unit` for exact role codes like CFO, CTO, SFVP, TECPM, FIN-EA, LOGVP-SEC. "
        "Use `position_contains` + `position_serves_unit` to find a specific role's secretary "
        "(e.g. position_contains='เลขา', position_serves_unit='CFO'). "
        "Use `department` for broad divisions (FIN, TEC, MKT, SF, DN, KS, WK, JC, RET, SUP, B2B, LOG, HR, LEG, OPS, CEO). "
        "Use `org_contains` when the user uses informal shorthand ('DN', 'SaiFah', 'retail network'). "
        "Never guess from memory — always query."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "unit": {"type": "string", "description": "Exact Unit code. NARROW — each person's specific role/team cell. For C-level: CEO, CFO, CTO, COO, CMO, CPO, CHRO. For VP tier: SFVP, DNVP, TECVP, MKTVP, OPSVP, HRVP, LEGVP, LOGVP, SUPVP, RETVP, B2BVP, KSVP, WKVP, JCVP, TECPM, MKTDG, SUPCX, LOGFL, OPSQA, RETBKK, RETUPC, B2BACC. EAs: CEO-EA, FIN-EA, TEC-EA, OPS-EA, MKT-EA, CPO-EA, HR-EA. VP secretaries: <code>-SEC (e.g. LEGVP-SEC, MKTVP-SEC). Directors: SFDR, FINFP, MKTBR, FIN-ACCDR, FIN-FINDR. GMs: SF-GM, DN-GM, KS-GM, WK-GM, JC-GM. IC-level units look like TEC-MOB-92, RET-CBI-22, etc. Case-insensitive exact match."},
            "position_contains": {"type": "string", "description": "Case-insensitive substring in Position English or Thai, e.g. 'เลขา', 'MANAGER', 'GENERAL MANAGER'."},
            "position_serves_unit": {"type": "string", "description": "Unit token that must appear in the person's position text (e.g. 'CFO' matches 'เลขานุการของ CFO')."},
            "name": {"type": "string", "description": "Person's first and/or last name only (Thai or English). Substring-matched against First/Last Name Thai/English. Strip conversational framing like 'พี่', 'คุณ', 'น้อง', 'ขอเบอร์', 'please', 'who is'. All whitespace-separated tokens must appear. Example: for 'ขอเบอร์พี่วิรัตน์ สมศรี หน่อย', pass name='วิรัตน์ สมศรี'."},
            "nickname": {"type": "string", "description": "Nickname token only. Substring-match against Nickname Thai/English. Pass just the nickname ('ปิ๊ง', 'Mook'). Variants like 'พี่มุกกี้' or 'นัตตี้' should first be stripped to the base ('มุก', 'นัต') before passing."},
            "extension": {"type": "string", "description": "Exact 5-digit extension for reverse lookup (e.g. '73048')."},
            "mobile": {"type": "string", "description": "Substring of mobile number for reverse lookup (e.g. '064-970-0992' or '0649700992')."},
            "department": {"type": "string", "description": "Exact Department code. BROAD — covers the whole division (up to 380 people). Valid codes: CEO, FIN, TEC, OPS, MKT, SF, HR, LEG, LOG, SUP, RET, B2B, DN, KS, WK, JC. Thai 'แผนก' / English 'dept / division / members of X' map here, NOT to `unit`."},
            "section": {"type": "string", "description": "Exact Section code — intermediate grouping inside a dept (e.g. FIN-AP, TEC-MOB, LEG-COM, MKT-BR, SF-OPS). Sections hold 2–30 people."},
            "org_contains": {"type": "string", "description": "Case-insensitive substring across Department/Unit/Section. Use for informal shorthand (e.g. 'DN', 'SF', 'RET', 'MKT'). Do NOT use for precise unit codes — use `unit=` instead."},
            "branch": {"type": "string", "description": "Exact Branch code. Mapping: BKK-R9=HQ (Rama IX), BKK-SIAM=สาขาสยาม, BKK-LP=สาขาลาดพร้าว, BKK-BNA=สาขาบางนา, BKK-PKT=สาขาปากเกร็ด, CNX=เชียงใหม่/Chiang Mai, KKN=ขอนแก่น/Khon Kaen, NMA=โคราช/Nakhon Ratchasima, CBI=ชลบุรี/Chonburi, HKT=ภูเก็ต/Phuket, HDY=หาดใหญ่/Hat Yai, REMOTE=remote. Use when the user references a location by name."},
            "position_level": {"type": "string", "description": "One of: C-level, VP, Director, Manager, Lead, IC. Use for tier listings ('list all VPs')."},
            "employee_id": {"type": "string", "description": "Exact Employee ID (format: 0000#### or 08######)."},
            "email": {"type": "string", "description": "Case-insensitive substring of Email Address. Full email or username ('WIRAT.SO@FAHMAI.CO.TH' or 'WIRAT.SO')."},
            "limit": {"type": "integer", "description": "Max rows to return (default 50, up to 500). Check truncated flag.", "default": 50},
        },
        "required": [],
    },
}


if __name__ == "__main__":
    import json, sys, io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    print(f"Loaded {len(_ROWS)} rows from {CSV_PATH}")
    print("--- unit=CFO ---")
    print(json.dumps(search_employees(unit="CFO"), ensure_ascii=False, indent=2))
    print("--- position_serves_unit=CFO + position_contains=เลขา ---")
    print(json.dumps(search_employees(position_contains="เลขา", position_serves_unit="CFO"), ensure_ascii=False, indent=2))
    print("--- nickname=ไอซ์ department=TEC ---")
    print(json.dumps(search_employees(nickname="ไอซ์", department="TEC"), ensure_ascii=False, indent=2))
