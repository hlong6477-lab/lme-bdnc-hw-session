#!/usr/bin/env python3
"""Dump a compact sentence map (ID + full text) for every pair.

Agents read these one-line-per-sentence maps instead of the big *_seg.json
files: cheaper context, no offset noise, exact sentence IDs for tie tables.
"""
from __future__ import annotations

import json
from pathlib import Path

WORK = Path(__file__).resolve().parent.parent / "work"

for pdir in sorted(WORK.glob("pairs/P*")):
    if not pdir.is_dir():
        continue
    for pref, label in (("ST", "EN"), ("TT", "VI")):
        seg = json.loads((pdir / f"{pref}_seg.json").read_text(encoding="utf-8"))
        lines = []
        for s in seg["sentences"]:
            # mark subhead/standalone short lines as-is; text is byte-exact
            lines.append(f'{s["id"]}\t{s["text"]}')
        out = pdir / f"{pref}_sentmap.txt"
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"{pdir.name}/{out.name}: {len(lines)} sentences")
