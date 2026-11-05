#!/usr/bin/env python3
"""Regenerate Appendix2.md with v2 (widened L-policy) statistics."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
S = json.load(open(ROOT / 'out/appendix2/appendix2_stats.json'))
EN, VI = S['corpus']['EN'], S['corpus']['VI']
PAIRS = S['pairs']

GENRE = {
    'P01': 'tin tính năng (SBS)', 'P02': 'tin tính năng, nhiều trích dẫn',
    'P03': 'VI tự sinh 14 câu chuyển tiếp', 'P04': 'service journalism, VI cắt',
    'P05': 'listicle thông báo', 'P06': 'VI cắt 15/38 câu',
    'P07': 'feature giải thích, 73/73 giữ 1–1', 'P08': 'listicle thống kê giá nhà',
    'P09': 'chính sách – dữ liệu', 'P10': 'tài chính cá nhân, VI chèn 14 câu',
    'P11': 'explainer nghi thức', 'P12': 'cặp micro (2 câu thật mỗi phía)',
    'P13': 'tin ngắn, VI cắt khối 2018', 'P14': 'tin chính trị dày tên riêng',
    'P15': 'VI cắt/viết lại (VOA)', 'P16': 'tin du lịch Nga',
    'P17': 'VI lặp tên attribution', 'P18': 'tin quyên góp từ thiện',
    'P19': 'tin pháp lý, thuật ngữ dày nhất', 'P20': 'cặp cắt mạnh nhất (23 câu EN bị bỏ)',
}

def pct(n, d): return f"{100*n/d:.1f}".replace('.', ',')
def k(n): return f"{n:,}".replace(',', '.')

te, tv = EN['ties'], VI['ties']
lc_en = EN['levels'].get('LC', 0); tc_en = EN['levels'].get('TC', 0)
lc_vi = VI['levels'].get('LC', 0); tc_vi = VI['levels'].get('TC', 0)

rows_a1 = []
for cat, name in (('R', 'quy chiếu'), ('S', 'thế'), ('E', 'tỉnh lược'), ('C', 'nối'), ('L', 'từ vựng')):
    e, v = EN['by_cat'][cat], VI['by_cat'][cat]
    rows_a1.append(f"| {cat} — {name} | {k(e)} | {pct(e, te)} | {k(v)} | {pct(v, tv)} | {'+' if e>=v else ''}{e-v} |")

rows_a2 = []
for pid in sorted(PAIRS):
    p = PAIRS[pid]
    en, vi = p['EN'], p['VI']
    rows_a2.append(
        f"| {pid} | {en['sentences']} | {vi['sentences']} | {en['ties']} | {vi['ties']} | "
        f"{str(en['density']).replace('.', ',')} | {str(vi['density']).replace('.', ',')} | {GENRE[pid]} |")

def subtable(cat):
    subs = sorted({k.split('/', 1)[1] for k in EN['by_sub'] if k.startswith(cat + '/')})
    rows = []
    for sub in subs:
        e = EN['by_sub'].get(f'{cat}/{sub}', 0)
        v = VI['by_sub'].get(f'{cat}/{sub}', 0)
        et, vt = EN['by_cat'][cat], VI['by_cat'][cat]
        rows.append(f"| {sub} | {e} | {pct(e, et) if e else '—'} | {v} | {pct(v, vt) if v else '—'} |")
    return "\n".join(rows)

L = lambda side, sub: side['by_sub'].get(f'L/{sub}', 0)
rep_e, rep_v = L(EN, 'repetition'), L(VI, 'repetition')
syn_e, syn_v = L(EN, 'synonym'), L(VI, 'synonym')

vi_heavier = [pid for pid in PAIRS if PAIRS[pid]['VI']['ties'] > PAIRS[pid]['EN']['ties']]
en_heavier = [pid for pid in PAIRS if PAIRS[pid]['EN']['ties'] > PAIRS[pid]['VI']['ties']]
equal = [pid for pid in PAIRS if PAIRS[pid]['EN']['ties'] == PAIRS[pid]['VI']['ties']]

md = f"""# Phụ lục 2 — Thống kê liên kết văn bản & tổng hợp phân tích đối chiếu EN–VI

**Bộ dữ liệu:** 20 cặp bài báo song ngữ Anh–Việt (Appendix 1) · {EN['sentences']} câu EN / {VI['sentences']} câu VI ·
{k(te)} đơn vị liên kết (tie) phía EN và {k(tv)} tie phía VI, gán nhãn thủ công từng cặp.

**Khung lý thuyết:** phía EN — Halliday & Hasan (1976), *Cohesion in English*
(quy chiếu R, thế S, tỉnh lược E, nối C, liên kết từ vựng L); phía VI — Trần
Ngọc Thêm (1985; 2006), *Hệ thống liên kết văn bản tiếng Việt* (dẫn theo Nguyễn
Thanh Tùng 2020), quy về cùng thang 5 danh mục. Trọng tâm nghiên cứu là
**liên kết vượt câu (cohesion beyond the sentence level)**: các hạng mục R/C/L
chỉ ghi ở cấp liên câu [LC]; S/E có thêm lớp bổ sung trong câu [TC] và
**không** dùng làm bằng chứng cho kết luận về liên kết liên câu.

**Chính sách phiên (v2, 2026-11-05):** theo chỉ thị giảng viên, chính sách
liên kết từ vựng được nới rộng so với bản pilot — ghi nhận lặp cùng dạng ở cả
câu kề, từ đơn có nội dung thực, và chuỗi động từ attribution
(CONVENTIONS §8.1 v2). Mọi hàng vẫn là quyết định đọc hiểu tay (manual-first).

**Kiểm soát chất lượng:** mỗi cặp qua cổng QC cơ khí hai lượt (vị trí đánh dấu,
occurrence, hướng tiền trạm, tái tạo văn bản gốc) và đối chiếu giữa số đếm tay
với tie table; 20/20 cặp PASS.

---

## A. Thống kê tổng hợp

### A.1. Toàn bộ 20 cặp

| Danh mục | EN (số) | EN (%) | VI (số) | VI (%) | Chênh EN−VI |
|---|---:|---:|---:|---:|---:|
{chr(10).join(rows_a1)}
| **Tổng** | **{k(te)}** | 100 | **{k(tv)}** | 100 | **+{te-tv}** |
| Số câu | {EN['sentences']} | | {VI['sentences']} | | +{EN['sentences']-VI['sentences']} |
| Mật độ (tie/câu) | {str(EN['density']).replace('.', ',')} | | {str(VI['density']).replace('.', ',')} | | |

### A.2. Mật độ từng cặp

| Cặp | Câu EN | Câu VI | Tie EN | Tie VI | Mật độ EN | Mật độ VI | Ghi chú thể loại |
|---|---:|---:|---:|---:|---:|---:|---|
{chr(10).join(rows_a2)}

Mật độ dao động {min(PAIRS[p]['EN']['density'] for p in PAIRS):.2f}–{max(PAIRS[p]['VI']['density'] for p in PAIRS):.2f} tie/câu theo **thể loại và mức biên tập**. Sau chính sách v2, các cặp
tên riêng/danh từ lặp dày (P13, P14, P16, P17, P19) có mật độ cao nhất; thấp
nhất vẫn là cặp micro (P12) và listicle khép kín từng mục (P05). (Bảng dùng số
câu cơ khí của bộ segment để nhất quán 20/20 cặp; một số analysis tính mật độ
theo "câu thật" sau khi loại artifact — khác biệt có ghi chú riêng.)

### A.3. Thành phần phụ từng danh mục

**Quy chiếu (R) — {EN['by_cat']['R']} EN / {VI['by_cat']['R']} VI:**

| Tiểu loại | EN | (% R EN) | VI | (% R VI) |
|---|---:|---:|---:|---:|
{subtable('R')}

**Liên kết từ vựng (L) — {k(EN['by_cat']['L'])} EN / {k(VI['by_cat']['L'])} VI:**

| Tiểu loại | EN | (% L EN) | VI | (% L VI) |
|---|---:|---:|---:|---:|
{subtable('L')}

**Nối (C) — {EN['by_cat']['C']} EN / {VI['by_cat']['C']} VI:** additive {EN['by_sub']['C/additive']}/{VI['by_sub']['C/additive']} · adversative {EN['by_sub']['C/adversative']}/{VI['by_sub']['C/adversative']} · causal {EN['by_sub']['C/causal']}/{VI['by_sub']['C/causal']}
· temporal {EN['by_sub']['C/temporal']}/{VI['by_sub']['C/temporal']} · continuative {EN['by_sub'].get('C/continuative', 0)}/{VI['by_sub'].get('C/continuative', 0)}.

**Thế (S) — {EN['by_cat']['S']} EN / {VI['by_cat']['S']} VI:** EN nominal {EN['by_sub'].get('S/nominal', 0)}, verbal {EN['by_sub'].get('S/verbal', 0)}; VI nominal {VI['by_sub'].get('S/nominal', 0)}, verbal {VI['by_sub'].get('S/verbal', 0)},
clausal {VI['by_sub'].get('S/clausal', 0)}.

**Tỉnh lược (E) — {EN['by_cat']['E']} EN / {VI['by_cat']['E']} VI:** EN nominal {EN['by_sub']['E/nominal']}, verbal {EN['by_sub']['E/verbal']}, clausal {EN['by_sub']['E/clausal']}; VI
nominal {VI['by_sub']['E/nominal']}, verbal {VI['by_sub']['E/verbal']}, clausal {VI['by_sub']['E/clausal']}.

### A.4. Hướng quy chiếu và cấp liên kết

| Chỉ số | EN | VI |
|---|---:|---:|
| Hồi quy A | {EN['ref_dirs']['A']} ({pct(EN['ref_dirs']['A'], EN['by_cat']['R'])}% R) | {VI['ref_dirs']['A']} ({pct(VI['ref_dirs']['A'], VI['by_cat']['R'])}% R) |
| Tiến chỉ C | {EN['ref_dirs'].get('C', 0)} ({pct(EN['ref_dirs'].get('C', 0), EN['by_cat']['R'])}%) | {VI['ref_dirs'].get('C', 0)} |
| Ngoại văn bản E | {EN['ref_dirs']['E']} ({pct(EN['ref_dirs']['E'], EN['by_cat']['R'])}% R) | {VI['ref_dirs']['E']} ({pct(VI['ref_dirs']['E'], VI['by_cat']['R'])}% R) |
| Cấp [LC] (liên câu) | {k(lc_en)} ({pct(lc_en, te)}%) | {k(lc_vi)} ({pct(lc_vi, tv)}%) |
| Cấp [TC] (trong câu — chỉ S/E) | {tc_en} ({pct(tc_en, te)}%) | {tc_vi} ({pct(tc_vi, tv)}%) |

---

## B. Sáu phát hiện tổng hợp

### B.1. Liên kết từ vựng là thiết bị chủ lực tuyệt đối — và chính sách đánh dấu quyết định "ai lặp nhiều hơn"

L chiếm {pct(EN['by_cat']['L'], te)}% (EN) và {pct(VI['by_cat']['L'], tv)}% (VI) tổng số tie; trong nội bộ L, phép lặp
chiếm {pct(rep_e, EN['by_cat']['L'])}% (EN) và **{pct(rep_v, VI['by_cat']['L'])}% (VI)**. Đây là bằng chứng định lượng cho luận điểm
của Trần Ngọc Thêm rằng *phép lặp* là thiết bị liên kết nền tảng của tiếng
Việt: VI duy trì chuỗi bằng cách tái lập danh từ/tên riêng gần nguyên dạng,
trong khi EN dễ **phân rã** sang biến thể đồng nghĩa hơn hẳn (synonym EN {syn_e} ↔
VI {syn_v}). Chính sách v2 — ghi nhận đủ lặp câu kề và từ đơn — khiến khoảng
cách L EN−VI ({k(EN['by_cat']['L'])} ↔ {k(VI['by_cat']['L'])}) phản ánh trung thực hơn mức độ "đậm từ vựng"
thực của hai bản: phần chênh nằm chủ yếu ở các khối EN bị biên tập cắt.

### B.2. "Danh ngữ hóa quy chiếu" là dịch chuyển hệ thống EN → VI

Chênh R ({EN['by_cat']['R']} ↔ {VI['by_cat']['R']}) không nằm ở số lượng đại từ thuần: EN personal {EN['by_sub']['R/personal']} ({pct(EN['by_sub']['R/personal'], EN['by_cat']['R'])}%
R) nhưng VI personal chỉ {VI['by_sub']['R/personal']} ({pct(VI['by_sub']['R/personal'], VI['by_cat']['R'])}%), trong khi VI demonstrative {VI['by_sub']['R/demonstrative']} ({pct(VI['by_sub']['R/demonstrative'], VI['by_cat']['R'])})
cao hơn cả tuyệt đối lẫn tỉ lệ dù tổng R ít hơn. Kết hợp đọc từng cặp, mô típ
lặp lại nhất quán: **EN dùng đại từ/mạo từ thì VI dùng danh ngữ chỉ từ +
danh từ, hoặc lặp tên kèm danh xưng**:

- "It / This / The + N" (EN) → "Cuộc nghiên cứu này / Thỏa thuận này / Hệ
  thống này" (P20); "vụ kiện này, thời gian đó, việc này" (P19, VI 0 đại từ
  nhân xưng liên câu); "the analysis ↔ phân tích này", "the problem ↔ vấn đề
  này" (P02).
- Đại từ attribution EN "he said/she said" → VI "Ông X nói / Bà Y / Cô Z" —
  **honorific phân tầng theo nhân vật** (P02: cô/bà/ông; P11: ông/bà đi kèm
  mọi lần lặp tên; P17: "he said" → "Ông Yium"). EN chỉ mã hóa she/he; VI mã
  hóa cả giới tính lẫn thứ bậc xã giao.
- Chiều ngược cũng có nhưng hiếm: VI dùng chỉ từ "này" nơi EN chỉ lặp mạo từ
  (P02, P05) — tức cùng một vị trí, EN ghi L (lặp danh từ) còn VI ghi R
  (danh ngữ chỉ từ): hai ngôn ngữ phân công tính xác định theo hai đường.

### B.3. Quy chiếu trong tin tức gần như toàn bộ hồi quy; ref=E mang dấu vết thể loại

Hướng A chiếm {pct(EN['ref_dirs']['A'], EN['by_cat']['R'])}% (EN) và {pct(VI['ref_dirs']['A'], VI['by_cat']['R'])}% (VI). ref=E ({EN['ref_dirs']['E']} EN / {VI['ref_dirs']['E']} VI) hầu hết là đại
từ ngôi 1/2 hướng độc giả — đặc trưng **service journalism**: P04 (we/you/here
5 hàng), P05 (we/you ↔ Bạn/bạn), P10 (you/bạn 3↔3, kể cả deck/headline gọi
độc giả). ref=C chỉ {EN['ref_dirs'].get('C', 0)} trường hợp (P08), đều do cấu trúc nguồn (dek đứng trước
thân bài) chứ không phải tiến chỉ tu từ. Không có cặp nào ref=C phía VI.

### B.4. Thế và tỉnh lược hiếm, gần như toàn bộ trong câu — không dùng làm bằng chứng liên câu

S ({EN['by_cat']['S']}/{VI['by_cat']['S']}) và E ({EN['by_cat']['E']}/{VI['by_cat']['E']}) cộng lại chỉ {pct(EN['by_cat']['S']+EN['by_cat']['E'], te)}% (EN) và {pct(VI['by_cat']['S']+VI['by_cat']['E'], tv)}% (VI) tổng tie; {tc_en}/{tc_vi}
hàng [TC] đều thuộc S/E. Điểm đáng chú ý về mặt đối chiếu:

- **VI không ưa zero liên câu trong bộ liệu này**: các khe zero của VI tập
  trung ở chủ ngữ vế tọa hợp trong câu; nhiều cặp VI lấp đầy toàn bộ khe
  tỉnh lược của EN (P01: E-EN = 0 vì VI lấp đầy). Ngược lại, VI có kiểu
  "đã phê chuẩn ∅" (P20, tân ngữ zero) mà EN hiện thực hóa "ratified it".
- Phép thế EN thường được VI **hiện thực hóa**: "don't" (E-EN) ↔ "làm vậy"
  (S-VI) tại cùng vị trí P14 — bộ đối ứng chéo E↔S đẹp nhất của bộ; "do so"
  (P11, conf thấp) không có pro-form VI tương ứng.
- Chức năng "thế" của VI thường do **danh ngữ chỉ từ gánh** ("từ này", "điều
  này" — P07, nơi S = 0 hai phía nhưng demonstrative dày), phù hợp nhận định
  của Trần Ngọc Thêm rằng tiếng Việt ít dùng pro-form thuần.

### B.5. Nối gần đối xứng về số lượng và vị trí; chênh lệch nằm ở hai chiều hiện thực hóa

C {EN['by_cat']['C']} ↔ {VI['by_cat']['C']}, additive và adversative gần như cân bằng tuyệt đối ({EN['by_sub']['C/additive']}/{VI['by_sub']['C/additive']} và
{EN['by_sub']['C/adversative']}/{VI['by_sub']['C/adversative']}). Chênh causal ({EN['by_sub']['C/causal']} ↔ {VI['by_sub']['C/causal']}) phản ánh EN thích liên từ nhân–quả tường minh
nơi VI diễn đạt bằng trật tự và ngữ nghĩa. Hai chiều dịch chuyển đều thấy:
**EN ngầm → VI hiện thực** (P04: 3 liên từ VI tự sinh "Nói cách khác/Tuy nhiên/
Ngoài ra" tại đúng 3 chỗ EN dùng thiết bị khác) và **EN tường minh → VI ngầm**
(P18: "So" bị lược; P10: "in turn" và "So" bị lược). Trường hợp
đổi hạng mục: "other steps" (R, EN) ↔ "cũng" (C, VI) ở P14 — minh họa nguyên
tắc *function, not form* giữa hai khung.

### B.6. Chênh lệch tổng EN−VI ({k(te)}−{k(tv)} = +{te-tv}) chủ yếu do biên tập (cắt/gộp/tự sinh), không do hệ thống ngôn ngữ

EN đậm hơn VI ở {len(en_heavier)}/20 cặp, nhưng phân tích từng cặp cho thấy phần
lớn chênh lệch nằm ở **khối bị cắt**: P20 (23 câu EN bị bỏ, chứa {L(EN, 'repetition') and 'phần lớn'} hàng L
của EN), P06 (15/38 câu), P04, P05, P13, P15. VI đậm hơn EN ở {len(vi_heavier)} cặp ({', '.join(vi_heavier)}) —
sau chính sách v2 ghi nhận đủ lặp kề và từ đơn, các cặp VI lặp tên riêng/
attribution dày (P17: 89 vs 80) hoặc VI tự sinh chuyển tiếp (P10) nổi bật
lên — nhất quán với luận điểm "phép lặp là thiết bị nền tảng của tiếng Việt".
VI **tự sinh** câu chuyển tiếp và lede ở P03 (14 câu), P10 (14 câu), P20
(lede 3 câu) — các câu này tạo tie VI độc lập, tiền trạm trong chính văn
bản VI. Mọi so sánh cấp câu giữa hai phía vì vậy phải đi qua bản đồ câu của
từng cặp (mục §1 trong 20 file phân tích).

---

## C. Bất thường dữ liệu nguồn cần lưu ý khi dùng số liệu

Tổng hợp từ mục §8 của 20 file phân tích:

1. **P20 không có URL nguồn** trong file gốc (bất thường duy nhất về nguồn);
   một số cặp có hàng lede VI tự sinh không đối ứng EN (P20) hoặc hàng EN
   không đối ứng VI (P02 — dòng Wiradjuri).
2. **Câu artifact đã loại khỏi đánh dấu**: caption pull-quote, câu lặp nguyên
   văn (P01, P07 S056, P10), chú thích biên tập (P07 S071), hàng "(1)/(?)"
   (P15, 5 hàng) — không dùng làm bằng chứng cấp câu.
3. **Lỗi nguồn hai phía**: typo EN ("outh Korea" P13, "Australia English"
   P07, "The fisherman have" P20), typo VI ("đối phó vơi" P11, "chắc chắc"
   P20), thiếu dấu cách (P07 S024/S055, P20 S003/S039), "IIU" thay "IUU" ở
   **cả hai phía** P20; một số bản dịch sai nghĩa (P07 S022 "làm tăng độ tin
   cậy" — ngược nghĩa gốc).
4. **Segmenter chẻ câu tại dấu viết tắt/điểm dừng bất thường** (Mr., Jr., U.S.,
   dấu nháy kép tách rời P11 S051): các quyết định [LC]/[TC] và "câu kề" đã tính
   lại theo câu thật theo quy ước phiên, có ghi chú trong từng analysis.

## D. Hạn chế của phiên phân tích

- Số đếm phụ thuộc **chính sách đánh dấu L của phiên**. Phiên này dùng chính
  sách **v2 (2026-11-05)**: chuỗi gồm cả từ đơn nội dung; đánh dấu lặp cùng
  dạng ở cả câu kề; chuỗi động từ attribution; tái lập tại điểm nối diễn
  ngôn; 1 mark/câu/chuỗi — các nghiên cứu dùng chính sách khác sẽ ra số
  khác; cần trích kèm quy ước khi so sánh. (Bản pilot hẹp hơn được thay
  thế; số pilot vẫn lưu trong lịch sử git.)
- Phân tích manual-first một luồng, mỗi hàng có conf (high/med/low) và alt
  (phương án mã khác đã cân nhắc); các hàng bridging/conf thấp đã ghi rõ.
- Lớp [TC] ({tc_en + tc_vi} hàng toàn bộ) chỉ mang tính bổ sung mô tả, không kết luận được
  gì về liên kết liên câu.
- 20 cặp đều là tin tức/báo chí Úc–Việt hiện đại; kết luận không nên ngoại suy
  sang thể loại tự sự dài, học thuật hay văn học.

---

*Báo cáo này được tổng hợp từ 20 file phân tích chi tiết (`work/analysis/
P01–P20_semantic.md`, mỗi file 9 mục, mục §6.4 và §9 cập nhật theo chính sách
v2) và số liệu tie đã qua cổng QC của pipeline; số liệu thô tại
`out/appendix2/appendix2_stats.json` và `out/appendix1/match_stats.json`.*
"""

out = ROOT / 'out/appendix2/Appendix2.md'
out.write_text(md)
print(f"Wrote {out} ({len(md)} chars)")
print(f"EN ties {te} / VI ties {tv}; EN-heavier {len(en_heavier)} pairs {en_heavier}")
print(f"VI-heavier {len(vi_heavier)} pairs {vi_heavier}; equal {equal}")
