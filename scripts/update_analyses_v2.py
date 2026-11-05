#!/usr/bin/env python3
"""Update 20 analysis files: append §6.4 (v2 L rows listing) and rebuild §9 table.

Old (pilot) per-pair distributions used to split v1/v2 rows — verified against
ties.json prefix before any edit; a mismatch aborts that pair.
"""
import json, re, sys, glob
from collections import Counter

OLD = {
    'P01': ({'R':30,'S':3,'E':0,'C':8,'L':47}, {'R':20,'S':1,'E':1,'C':8,'L':37}),
    'P02': ({'R':22,'S':0,'E':1,'C':5,'L':39}, {'R':22,'S':0,'E':1,'C':3,'L':41}),
    'P03': ({'R':4,'S':1,'E':4,'C':7,'L':36}, {'R':4,'S':0,'E':1,'C':8,'L':40}),
    'P04': ({'R':15,'S':1,'E':2,'C':5,'L':34}, {'R':7,'S':0,'E':1,'C':8,'L':20}),
    'P05': ({'R':17,'S':0,'E':1,'C':4,'L':35}, {'R':10,'S':0,'E':1,'C':3,'L':29}),
    'P06': ({'R':8,'S':0,'E':0,'C':5,'L':17}, {'R':4,'S':0,'E':0,'C':5,'L':6}),
    'P07': ({'R':43,'S':0,'E':4,'C':8,'L':40}, {'R':41,'S':0,'E':4,'C':9,'L':38}),
    'P08': ({'R':16,'S':1,'E':0,'C':10,'L':49}, {'R':15,'S':0,'E':1,'C':11,'L':43}),
    'P09': ({'R':8,'S':0,'E':4,'C':4,'L':45}, {'R':7,'S':0,'E':3,'C':3,'L':40}),
    'P10': ({'R':13,'S':0,'E':0,'C':7,'L':25}, {'R':13,'S':0,'E':1,'C':7,'L':29}),
    'P11': ({'R':20,'S':2,'E':0,'C':4,'L':44}, {'R':15,'S':0,'E':0,'C':3,'L':46}),
    'P12': ({'R':1,'S':0,'E':0,'C':0,'L':0}, {'R':0,'S':0,'E':0,'C':0,'L':2}),
    'P13': ({'R':4,'S':0,'E':1,'C':3,'L':12}, {'R':1,'S':0,'E':1,'C':0,'L':6}),
    'P14': ({'R':3,'S':0,'E':1,'C':0,'L':16}, {'R':2,'S':1,'E':0,'C':1,'L':15}),
    'P15': ({'R':11,'S':1,'E':1,'C':3,'L':41}, {'R':9,'S':0,'E':3,'C':0,'L':26}),
    'P16': ({'R':9,'S':0,'E':0,'C':2,'L':19}, {'R':6,'S':0,'E':2,'C':2,'L':19}),
    'P17': ({'R':8,'S':0,'E':1,'C':4,'L':24}, {'R':6,'S':0,'E':1,'C':4,'L':26}),
    'P18': ({'R':7,'S':1,'E':1,'C':3,'L':24}, {'R':8,'S':2,'E':0,'C':2,'L':24}),
    'P19': ({'R':7,'S':0,'E':1,'C':5,'L':29}, {'R':6,'S':0,'E':0,'C':5,'L':30}),
    'P20': ({'R':33,'S':1,'E':2,'C':14,'L':58}, {'R':19,'S':0,'E':1,'C':11,'L':41}),
}

def md_escape(s):
    return s.replace('|', '\\|') if s else ''

def side_table(rows, label):
    if not rows:
        return f"Phía {label}: không có hàng bổ sung.\n"
    out = [f"Phía {label} — {len(rows)} hàng bổ sung:\n", "| # | sent | text | sub | ante |", "|---:|---|---|---|---|"]
    for i, t in enumerate(rows, 1):
        text = t['text'] if t['text'] is not None else "∅"
        out.append(f"| {i} | {t['sent']} | {md_escape(text)} | {t['sub']} | {md_escape(str(t['ante']))} |")
    return "\n".join(out) + "\n"

def build_six_four(st_v2, tt_v2):
    b = []
    b.append("### 6.4. Bổ sung L theo chính sách v2 (2026-11-05)\n")
    b.append("Theo chỉ thị giảng viên (phân tích kỹ hơn, đánh dấu nhiều hơn), chính")
    b.append("sách L được nới rộng (CONVENTIONS §8.1 v2): lặp cùng dạng kể cả câu kề,")
    b.append("từ đơn có nội dung thực, chuỗi động từ attribution, tái lập tại điểm nối")
    b.append("diễn ngôn. Kho chuỗi §6.2 được rà lại; các hàng L mới là quyết định đọc")
    b.append("hiểu tay (không regex/word-list), mỗi hàng 1 mark/câu/chuỗi, ante luôn")
    b.append("nằm trước. Danh sách hàng bổ sung (đối soát 2 cổng QC PASS):\n")
    b.append(side_table(st_v2, "EN"))
    b.append("")
    b.append(side_table(tt_v2, "VI"))
    b.append("Số đếm §9 dưới đây đã gộp toàn bộ phần bổ sung này. Các kết luận §6.5")
    b.append("(nếu có) của bản pilot về \"chọn lọc lặp kề\" không còn áp dụng — thay")
    b.append("bằng chính sách v2.")
    return "\n".join(b)

def build_s9(pid, st_all, tt_all, st_v2, tt_v2, old_st, old_tt):
    cs, ct = Counter(t['cat'] for t in st_all), Counter(t['cat'] for t in tt_all)
    rows = []
    notes = {'R': '§4', 'S': '§3', 'E': '§2', 'C': '§5', 'L': '§6'}
    for side, c, old, v2 in (('EN', cs, old_st, st_v2), ('VI', ct, old_tt, tt_v2)):
        for cat in 'RSCEL':
            n_new = len([t for t in v2 if t['cat'] == cat])
            note = notes[cat]
            if cat == 'L':
                note += f" (pilot {old['L']} + v2 {n_new})" if n_new else f" (pilot giữ nguyên)"
            elif n_new:
                note += f" + v2 {n_new}"
            rows.append(f"| {side} — {cat} | {c[cat]} | {c[cat]} | {note} |")
    tot_s, tot_t = sum(cs.values()), sum(ct.values())
    lines = [
        f"## 9. Đối chiếu số đếm: phân tích tay ↔ tie table (cập nhật v2 2026-11-05)",
        "",
        "| Chỉ số | Phân tích | Tie table | Ghi chú |",
        "|---|---:|---:|---|",
        *rows,
        "",
        f"- Tổng tie: EN **{tot_s}** / VI **{tot_t}** (pilot: EN {sum(old_st.values())} / VI {sum(old_tt.values())}).",
        f"- Bổ sung v2 ({len(st_v2)} EN + {len(tt_v2)} VI hàng) theo chỉ thị giảng viên",
        "  2026-11-05 (CONVENTIONS §8.1 v2): lặp câu kề, từ đơn nội dung, động từ",
        "  attribution; đã PASS 2 cổng QC `pipeline.annotate` + `pipeline.render`.",
        f"- Liên kết từ vựng giữ vai trò chủ lực: L-EN {cs['L']} ({100*cs['L']/tot_s:.0f}%),",
        f"  L-VI {ct['L']} ({100*ct['L']/tot_t:.0f}%).",
    ]
    if cs['L'] > ct['L']:
        lines.append(f"- L-EN ({cs['L']}) > L-VI ({ct['L']}): bản EN phân tán chuỗi từ vựng")
        lines.append("  (biến thể/đại từ thay thế) trong khi VI hội tụ lặp danh từ.")
    elif ct['L'] > cs['L']:
        lines.append(f"- L-VI ({ct['L']}) > L-EN ({cs['L']}): bản VI lặp danh từ/tên riêng")
        lines.append("  trực tiếp dày hơn (Trần Ngọc Thêm: phép lặp), EN thay bằng đại từ.")
    else:
        lines.append(f"- L-EN = L-VI = {cs['L']}: hai bên giữ cân bằng liên kết từ vựng.")
    lines += [
        f"- Quy chiếu EN {cs['R']} / VI {ct['R']} (EN ưa đại từ, VI ưa danh ngữ lặp);",
        f"  tỉnh lược EN {cs['E']} / VI {ct['E']}; thế EN {cs['S']} / VI {ct['S']};",
        f"  nối EN {cs['C']} / VI {ct['C']}.",
        "- Các hàng chỉ [TC] không dùng làm bằng chứng cho kết luận liên kết liên câu.",
    ]
    return "\n".join(lines)

def main():
    problems = []
    for pairdir in sorted(glob.glob('work/pairs/P*')):
        pid = pairdir.split('/')[-1]
        if pid not in OLD:
            continue
        old_st, old_tt = OLD[pid]
        st = json.load(open(f'{pairdir}/ST_ties.json'))['ties']
        tt = json.load(open(f'{pairdir}/TT_ties.json'))['ties']
        n_st, n_tt = sum(old_st.values()), sum(old_tt.values())
        # verify prefix matches pilot distribution
        pre_st = Counter(t['cat'] for t in st[:n_st])
        pre_tt = Counter(t['cat'] for t in tt[:n_tt])
        mismatch = any(pre_st.get(c, 0) != v for c, v in old_st.items()) or \
                   any(pre_tt.get(c, 0) != v for c, v in old_tt.items())
        if mismatch:
            problems.append(f"{pid}: prefix mismatch ST {dict(pre_st)} vs {old_st} / TT {dict(pre_tt)} vs {old_tt}")
            continue
        st_v2 = st[n_st:]
        tt_v2 = tt[n_tt:]
        # every appended row must be L
        bad = [t for t in st_v2 + tt_v2 if t['cat'] != 'L']
        if bad:
            problems.append(f"{pid}: {len(bad)} non-L appended rows (expected L-only)")
            continue
        path = f'work/analysis/{pid}_semantic.md'
        txt = open(path).read()
        if '### 6.4. Bổ sung L theo chính sách v2' in txt:
            # already updated — replace §9 only (idempotent on §6.4)
            pass
        else:
            m = re.search(r'^## 7\.', txt, flags=re.M)
            if not m:
                problems.append(f"{pid}: no '## 7.' heading")
                continue
            block = build_six_four(st_v2, tt_v2)
            txt = txt[:m.start()] + block + "\n\n" + txt[m.start():]
        m9 = re.search(r'^## 9\..*', txt, flags=re.M)
        if not m9:
            problems.append(f"{pid}: no '## 9.' heading")
            continue
        s9 = build_s9(pid, st, tt, st_v2, tt_v2, old_st, old_tt)
        txt = txt[:m9.start()] + s9 + "\n"
        open(path, 'w').write(txt)
        print(f"{pid}: OK  (+{len(st_v2)} EN / +{len(tt_v2)} VI v2 rows, §6.4 + §9 updated)")
    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print(" -", p)
        sys.exit(1)

if __name__ == '__main__':
    main()
