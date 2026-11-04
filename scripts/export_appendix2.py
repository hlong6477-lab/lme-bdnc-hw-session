#!/usr/bin/env python3
"""Export Appendix2.md to a styled DOCX (then soffice makes the PDF).

Handles the subset of markdown used in the report: H1/H2/H3, ---, pipe
tables, bullet lists, bold/italic/`code` inline runs.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

SRC = Path(__file__).resolve().parent.parent / "out" / "appendix2" / "Appendix2.md"
DST = SRC.with_suffix(".docx")

INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*|`.+?`)")


def add_runs(par, text: str, base_bold=False):
    for chunk in INLINE.split(text):
        if not chunk:
            continue
        bold, italic, code = base_bold, False, False
        if chunk.startswith("**") and chunk.endswith("**") and len(chunk) > 4:
            chunk, bold = chunk[2:-2], True
        elif chunk.startswith("*") and chunk.endswith("*") and len(chunk) > 2:
            chunk, italic = chunk[1:-1], True
        elif chunk.startswith("`") and chunk.endswith("`") and len(chunk) > 2:
            chunk, code = chunk[1:-1], True
        r = par.add_run(chunk)
        r.bold = bold
        r.italic = italic
        if code:
            r.font.name = "DejaVu Sans Mono"
            r.font.size = Pt(9)


def set_cell_bg(cell, hexcolor: str):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:fill"), hexcolor)
    cell._tc.get_or_add_tcPr().append(shd)


def main() -> int:
    doc = Document()
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(10.5)
    for sec in doc.sections:
        sec.top_margin = sec.bottom_margin = Cm(2)
        sec.left_margin = sec.right_margin = Cm(2.2)

    lines = SRC.read_text(encoding="utf-8").splitlines()
    i, first_h1 = 0, True
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.strip() == "---":
            i += 1
            continue
        if ln.startswith("# ") and first_h1:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            add_runs(p, ln[2:], base_bold=True)
            for r in p.runs:
                r.font.size = Pt(16)
            first_h1 = False
        elif ln.startswith("### "):
            h = doc.add_heading(re.sub(r"\*\*", "", ln[4:]), level=3)
            for r in h.runs:
                r.font.size = Pt(12)
        elif ln.startswith("## "):
            h = doc.add_heading(re.sub(r"\*\*", "", ln[3:]), level=2)
            for r in h.runs:
                r.font.size = Pt(13.5)
        elif ln.lstrip().startswith("|"):
            # collect the whole table
            tbl_lines = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                tbl_lines.append(lines[i].strip())
                i += 1
            rows = [[c.strip() for c in r.strip("|").split("|")]
                    for r in tbl_lines
                    if not re.match(r"^\|[\s:\-|]+\|$", r)]
            if not rows:
                continue
            ncol = max(len(r) for r in rows)
            t = doc.add_table(rows=len(rows), cols=ncol)
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            numeric = all(re.fullmatch(r"[\d,.\-–—%()]*", c)
                          for r in rows[1:] for c in r)
            for ri, row in enumerate(rows):
                for ci in range(ncol):
                    cell = t.cell(ri, ci)
                    cell.paragraphs[0].text = ""
                    par = cell.paragraphs[0]
                    txt = row[ci] if ci < len(row) else ""
                    add_runs(par, txt, base_bold=(ri == 0))
                    for r in par.runs:
                        r.font.size = Pt(9.5)
                    if ri == 0:
                        set_cell_bg(cell, "E8E8E8")
                        par.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    elif numeric and ci > 0:
                        par.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            doc.add_paragraph().paragraph_format.space_after = Pt(2)
            continue
        elif ln.lstrip().startswith("- "):
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, ln.lstrip()[2:])
        elif re.match(r"^\d+\.\s", ln.strip()):
            p = doc.add_paragraph(style="List Number")
            add_runs(p, re.sub(r"^\d+\.\s+", "", ln.strip()))
        else:
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(4)
            add_runs(p, ln.strip())
        i += 1

    doc.save(DST)
    print(f"Wrote {DST} ({DST.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
