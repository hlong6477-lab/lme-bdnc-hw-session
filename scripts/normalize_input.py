#!/usr/bin/env python3
"""Normalize the raw 2-column EN|VI markdown into the skill's canonical shape.

Why (audit note):
  The raw file is heterogeneous — titles appear (a) as in-table linked rows,
  (b) as standalone link lines before the table (some prefixed SL:/TL:, some
  ending with a hard-break backslash), (c) as H1 link headings, (d) as
  in-table bold rows, or (e) as plain in-table rows (P20, with no URL row and
  no standalone line). With the generic ``pipeline.ingest``, linked title rows
  are swallowed as URL rows and the first body row (the lede) is then popped
  as the "title" — i.e. body data is lost. SKILL.md §3 says to repair the
  markdown layout before analysis, so this script ONLY re-lays-out the file:

    ## Pair NN
    | <en_url> | <vi_url> |
    | :--- | :--- |
    | **EN title** | **VI title** |
    | body row ... | body row ... |   (verbatim, original order)

  No body text is altered; every body row is copied byte-for-byte.
  Title resolution order (recorded in the report for audit):
    1. in-table linked row (first data row, both cells links)
    2. in-table row similar to a standalone/H1/SL: title line (text match)
    3. in-table bold row (both cells, or one cell bold + short, when
       standalone lines exist)
    4. standalone / H1 link lines
    5. last resort: plain short first row when the pair has NO url row and
       NO standalone line (P20)
  URLs: url row -> in-table title links -> standalone/H1/SL:/TL: links.

Usage:
  python3 scripts/normalize_input.py
  # then: python -m pipeline.ingest --input input/appendix1.normalized.md --work work
"""
from __future__ import annotations

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "input" / "Appendix1-20-pairs.md"
OUT = ROOT / "input" / "appendix1.normalized.md"
REPORT = ROOT / "input" / "normalize_report.json"

LINK_FULL_RE = re.compile(r"^\[([^\]]*)\]\((https?://[^)\s]+)\)\s*$")
LINK_SEARCH_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)")
# trailing site tag in page titles copied from link text, e.g. "... | SBS Tiếng Việt"
SITE_TAG_RE = re.compile(r"\s*\|\s*(?:SBS[^|]*|Reuters|AP News|VOA[^|]*)$")


def split_row(line: str) -> list[str]:
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", body)]


def is_sep(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells)


def is_header(cells: list[str]) -> bool:
    if len(cells) < 2:
        return False
    a, b = cells[0].strip().lower(), cells[1].strip().lower()
    return a in {"tiếng anh", "english", "en", "eng"} and \
        b in {"tiếng việt", "vietnamese", "vi", "vie"}


def is_url_row(cells: list[str]) -> bool:
    return len(cells) >= 2 and cells[0].startswith("http") and \
        cells[1].startswith("http")


def link_parts(cell: str):
    m = LINK_FULL_RE.match(cell.strip())
    return (m.group(1).strip(), m.group(2).strip()) if m else None


def strip_emphasis(t: str) -> str:
    t = t.strip()
    if t.startswith("**") and t.endswith("**") and len(t) >= 4:
        t = t[2:-2]
    return t.strip()


def norm_sim(t: str) -> str:
    t = t.lower().strip()
    t = re.sub(r"[*_\[\]\"“”'‘’]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


def similar(a: str, b: str) -> bool:
    """Same headline test: identical, full containment of the shorter string,
    or sequence ratio >= 0.75. A long common prefix alone (P10: 'How the
    falling Aussie dollar could ...') must NOT count."""
    a, b = norm_sim(a), norm_sim(b)
    if not a or not b:
        return False
    if a == b:
        return True
    if len(a) < 20 and len(b) < 20:
        return False
    if len(a) >= 20 and len(a) <= len(b) and a in b:
        return True
    if len(b) >= 20 and len(b) <= len(a) and b in a:
        return True
    return SequenceMatcher(None, a, b).ratio() >= 0.75


def main() -> int:
    lines = RAW.read_text(encoding="utf-8").splitlines()

    chunks: list[dict] = []
    cur = {"standalone": [], "rows": []}

    def close():
        nonlocal cur
        if cur["standalone"] or cur["rows"]:
            chunks.append(cur)
        cur = {"standalone": [], "rows": []}

    for raw in lines:
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            text = s.lstrip("#").strip()
            if not text:
                continue  # empty heading — ignore
            if "](http" in text:
                # H1/H2 heading that is a link line: treat as standalone title
                if cur["rows"]:
                    close()
                cur["standalone"].append(text.rstrip("\\").strip())
            else:
                close()
            continue
        if s.startswith("|"):
            cells = split_row(s)
            if is_sep(cells):
                continue
            if is_header(cells):
                if cur["rows"]:
                    close()  # a header row after body rows starts a new pair
                continue
            if is_url_row(cells):
                if cur["rows"]:
                    close()
                cur["rows"].append({"kind": "url", "line": s, "cells": cells})
                continue
            cur["rows"].append({"kind": "row", "line": s, "cells": cells})
            continue
        # standalone non-table line (may end with a hard-break backslash,
        # may be prefixed SL:/TL:)
        t = s.rstrip("\\").strip()
        if cur["rows"]:
            close()
        cur["standalone"].append(t)
    close()

    report = {"n_chunks": len(chunks), "pairs": [], "warnings": []}
    out_lines: list[str] = []

    for i, ch in enumerate(chunks, 1):
        pid = f"P{i:02d}"
        info = {"id": pid, "n_rows_raw": len(ch["rows"]),
                "standalone_raw": ch["standalone"]}

        # --- standalone link lines -> texts / urls --------------------
        sl = ch["standalone"]
        sa_en = sa_vi = sa_enurl = sa_viurl = ""
        extracted = []
        for x in sl:
            m = LINK_SEARCH_RE.search(x)
            if m:
                text = SITE_TAG_RE.sub("", m.group(1).strip()).strip()
                extracted.append((text, m.group(2).strip()))
            else:
                extracted.append((x, ""))
        if len(extracted) >= 1:
            sa_en, sa_enurl = strip_emphasis(extracted[0][0]), extracted[0][1]
        if len(extracted) >= 2:
            sa_vi, sa_viurl = strip_emphasis(extracted[1][0]), extracted[1][1]
        if len(sl) > 2:
            report["warnings"].append(
                f"{pid}: {len(sl)} standalone lines (expected <=2): "
                + " || ".join(x[:50] for x in sl))

        # --- table rows ------------------------------------------------
        rows = ch["rows"]
        idx = 0
        en_url = vi_url = ""
        if rows and rows[0]["kind"] == "url":
            en_url, vi_url = rows[0]["cells"][0], rows[0]["cells"][1]
            idx = 1
        has_url_row = idx == 1
        has_sa = bool(sl)

        title_en = title_vi = ""
        title_rule = ""
        if idx < len(rows):
            c = rows[idx]["cells"]
            if len(c) >= 2:
                t0, t1 = strip_emphasis(c[0]), strip_emphasis(c[1])
                lp0, lp1 = link_parts(c[0]), link_parts(c[1])
                short_both = len(t0) < 220 and len(t1) < 220
                bold_both = c[0].startswith("**") and c[1].startswith("**")
                bold_either = c[0].startswith("**") or c[1].startswith("**")
                if lp0 and lp1:
                    title_en, title_vi = strip_emphasis(lp0[0]), \
                        strip_emphasis(lp1[0])
                    en_url = en_url or lp0[1]
                    vi_url = vi_url or lp1[1]
                    title_rule = "in-table linked row"
                    idx += 1
                elif has_sa and sa_en and similar(c[0], sa_en):
                    # EN side matches the citation headline -> the in-table row
                    # IS the title row (clean text, no site tag). VI-only match
                    # is NOT enough: VI desks reuse headline text in subhead
                    # positions (P08, P10) — those rows stay in the body.
                    title_en, title_vi = t0, t1
                    title_rule = "in-table row ~ standalone EN line"
                    idx += 1
                elif bold_both or (has_sa and bold_either and short_both):
                    title_en, title_vi = t0, t1
                    title_rule = "in-table bold row"
                    idx += 1
                elif (not has_sa and not has_url_row and short_both):
                    title_en, title_vi = t0, t1
                    title_rule = "last resort: plain short first row"
                    idx += 1

        if not title_en and sa_en:
            title_en = sa_en
            title_rule += " + standalone EN"
        if not title_vi and sa_vi:
            title_vi = sa_vi
            title_rule += " + standalone VI"
        en_url = en_url or sa_enurl
        vi_url = vi_url or sa_viurl

        body_rows = rows[idx:]

        if not title_en or not title_vi:
            report["warnings"].append(
                f"{pid}: missing title (en={bool(title_en)}, "
                f"vi={bool(title_vi)})")
        if not en_url or not vi_url:
            report["warnings"].append(
                f"{pid}: missing url (en={bool(en_url)}, vi={bool(vi_url)}) "
                f"— recorded as a source-data note")
        for r in body_rows:
            if len(r["cells"]) != 2:
                report["warnings"].append(
                    f"{pid}: body row with {len(r['cells'])} cells: "
                    f"{r['line'][:70]}")

        info.update({"title_en": title_en, "title_vi": title_vi,
                     "en_url": en_url, "vi_url": vi_url,
                     "title_rule": title_rule,
                     "n_body_rows": len(body_rows)})
        report["pairs"].append(info)

        esc = lambda t: t.replace("|", "\\|")
        out_lines.append(f"## Pair {i:02d}")
        out_lines.append("")
        if en_url or vi_url:
            out_lines.append(f"| {en_url} | {vi_url} |")
        out_lines.append("| :--- | :--- |")
        out_lines.append(f"| **{esc(title_en)}** | **{esc(title_vi)}** |")
        for r in body_rows:
            out_lines.append(r["line"])
        out_lines.append("")

    OUT.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")

    print(f"chunks: {len(chunks)} -> {OUT}")
    for p in report["pairs"]:
        print(f'{p["id"]}: rows={p["n_body_rows"]:3d} | rule: '
              f'{p["title_rule"][:38]:38} | EN: {p["title_en"][:45]}')
    print("\nWARNINGS:")
    for w in report["warnings"]:
        print("  -", w)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
