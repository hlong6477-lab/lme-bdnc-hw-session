#!/usr/bin/env python3
"""Compute Appendix 2 aggregate statistics from all pair tie JSONs.

Outputs out/appendix2/appendix2_stats.json with:
- per-pair: sentence counts, tie counts by cat, densities, sub-type mixes,
  ref-direction mixes (A/C/E), level mixes (LC/TC)
- corpus totals EN/VI
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / "work"
OUT = ROOT / "out" / "appendix2"
OUT.mkdir(parents=True, exist_ok=True)


def side_stats(seg: dict, ties: list[dict]) -> dict:
    n_sent = len(seg["sentences"])
    by_cat = Counter(t["cat"] for t in ties)
    by_sub = Counter(f'{t["cat"]}/{t["sub"]}' for t in ties)
    by_ref = Counter(t.get("ref") for t in ties if t["cat"] == "R")
    by_level = Counter(t["level"] for t in ties)
    by_conf = Counter(t["conf"] for t in ties)
    return {
        "sentences": n_sent,
        "ties": len(ties),
        "density": round(len(ties) / n_sent, 2) if n_sent else 0,
        "by_cat": dict(sorted(by_cat.items())),
        "by_sub": dict(sorted(by_sub.items())),
        "ref_dirs": {k or "none": v for k, v in sorted(by_ref.items(), key=lambda x: (x[0] is None, x[0]))},
        "levels": dict(sorted(by_level.items())),
        "conf": dict(sorted(by_conf.items())),
    }


pairs = {}
for d in sorted(WORK.glob("pairs/P*")):
    if not d.is_dir():
        continue
    pid = d.name
    en_seg = json.loads((d / "ST_seg.json").read_text(encoding="utf-8"))
    vi_seg = json.loads((d / "TT_seg.json").read_text(encoding="utf-8"))
    en_ties = json.loads((d / "ST_ties.json").read_text(encoding="utf-8"))["ties"]
    vi_ties = json.loads((d / "TT_ties.json").read_text(encoding="utf-8"))["ties"]
    pairs[pid] = {"EN": side_stats(en_seg, en_ties), "VI": side_stats(vi_seg, vi_ties)}

# corpus roll-up
def roll(side: str) -> dict:
    agg = Counter()
    sents = ties = 0
    sub = Counter()
    ref = Counter()
    lev = Counter()
    for p in pairs.values():
        s = p[side]
        sents += s["sentences"]
        ties += s["ties"]
        agg.update(s["by_cat"])
        sub.update(s["by_sub"])
        ref.update(s["ref_dirs"])
        lev.update(s["levels"])
    return {"sentences": sents, "ties": ties,
            "density": round(ties / sents, 2),
            "by_cat": dict(sorted(agg.items())),
            "by_sub": dict(sorted(sub.items())),
            "ref_dirs": dict(ref), "levels": dict(lev)}

corpus = {"EN": roll("EN"), "VI": roll("VI")}
stats = {"corpus": corpus, "pairs": pairs}
(OUT / "appendix2_stats.json").write_text(
    json.dumps(stats, ensure_ascii=False, indent=1), encoding="utf-8")

# quick console summary
for side in ("EN", "VI"):
    c = corpus[side]
    print(f"{side}: {c['sentences']} câu, {c['ties']} tie, mật độ {c['density']}/câu")
    print("   by_cat:", c["by_cat"])
    print("   ref_dirs:", c["ref_dirs"], "| levels:", c["levels"])
print("\nPer-pair EN/VI tie totals:")
for pid, p in pairs.items():
    print(f"  {pid}: EN {p['EN']['ties']:4d} ({p['EN']['sentences']} câu) | "
          f"VI {p['VI']['ties']:4d} ({p['VI']['sentences']} câu)")
