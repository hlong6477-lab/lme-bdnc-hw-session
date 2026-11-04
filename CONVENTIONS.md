# QUY ƯỚC GÁN NHÃN LIÊN KẾT EN–VI — ràng buộc cho cả 20 cặp (phiên độc lập này)

> File này là **quy ước chung bắt buộc** của phiên làm việc, chốt bởi điều phối
> viên sau khi đọc `SKILL.md` + `references/`. Mọi agent gán nhãn (mỗi agent
> một cặp) phải tuân theo đúng file này để 20 cặp có thể so sánh với nhau.
> Khi file này mâu thuẫn với một ví dụ trong `examples/mini/`, **file này thắng**.

## 0. Nguyên tắc nền

1. **Manual-first**: mọi tie là một quyết định ĐỌC HIỂU (tiền trạm là gì, vì sao
   là R/S/E/C/L, hướng A/C/E). Cấm sinh tie bằng regex, danh sách đại từ/từ
   nối, đếm chuỗi trùng, so khớp chuỗi, vòng lặp.
2. **Độc lập**: không mang tie/note/số liệu từ bất kỳ nguồn ngoài repo này
   (đặc biệt là bộ benchmark của skill gốc — không có mặt trong repo này).
   Không copy note giữa các cặp.
3. **Chất lượng > tốc độ**: đọc kỹ cả ST lẫn TT trước khi viết hàng nào.

## 1. Đơn vị và phạm vi đánh dấu

| Danh mục | Cấp được đánh dấu |
|---|---|
| R (quy chiếu), C (nối), L (từ vựng) | **chỉ [LC]** — item ở câu N, tiền trạm ở câu M ≠ N |
| S (thế), E (tỉnh lược) | **cả [LC] và [TC]** (lớp bổ sung, đọc kỹ để tìm) |
| [TD] (tiêu đề) | **không** đưa vào tie table (tiêu đề không nằm trong ST/TT); chỉ phân tích trong analysis §8 |

Quy tắc chọn lọc:
- **Prerequisite không đánh dấu**: thực thể nêu lần đầu, chỉ từ chưa neo trong
  văn bản → không có tie; ghi nhận trong analysis.
- **Một chuỗi một mark**: trong cùng một câu, các dạng theo dõi cùng một
  chuỗi (my/me/us; he/his; nó/cô ấy…) chỉ ghi **1 hàng** (chọn đại diện rõ
  nhất, nêu các dạng còn lại trong note).
- **"The" (EN)**: là R theo H&H, nhưng **không đánh dấu riêng** khi đầu ngữ
  lặp lại từ vựng của tiền trạm (lúc đó phép lặp đã là L); ghi khả năng
  `R: the` vào trường `alt` của hàng L tương ứng. Chỉ có hàng R riêng cho
  "the" khi sự xác định là liên kết duy nhất tại vị trí đó.
- **Đại từ ngôi 1/2 trong trích dẫn**: chỉ đủ điều kiện [LC] khi attribution
  (tên người nói) nằm ở **câu trước** (tiền trạm = attribution).
  Attribution cùng câu hoặc ở câu sau → không ghi.
- **Hàng subhead / pull-quote / dek** (vd P01 "'We're at a tipping point'",
  P08 "State-by-state: …", P20 "EU Aims for Public Shaming …"): là hàng body
  bình thường — đọc và quyết định như văn bản thật; ghi bản chất hàng này
  trong §1/§8 của analysis.
- **Khối cắt** (một bên "none"/rỗng): đánh dấu bên có văn bản; bên kia để
  trống — KHÔNG bịa tie đối ứng. Câu VI tự sinh (không có đối ứng EN): tie VI
  đứng độc lập, tiền trạm trong văn bản VI.
- **Bất đối xứng inventory EN/VI là bình thường** (EN "the U.S." lần 2 có thể
  không đánh dấu theo quy ước EN, VI "Hoa Kỳ" lần 2 đánh dấu L…): mỗi bên theo
  quy ước ngôn ngữ mình; mô tả bất đối xứng trong §7/§9, không "sửa cho cân".

## 2. Phân loại — theo bảng quyết định `references/en-vi-mapping.md` §3

Câu hỏi theo thứ tự: **cùng quy chiếu một thực thể? → R**. **Thay thế cách
diễn đạt (wording)? → S**. **Thiếu diễn đạt có thể hồi phục? → E**. **Quan hệ
ngữ nghĩa giữa mệnh đề? → C**. **Quan hệ từ vựng giữa hai hạng mục? → L**.

Phía VI theo Trần Ngọc Thêm (dẫn theo Nguyễn Thanh Tùng 2020):
- **Lặp danh từ/riêng tên = L** (*phép lặp*), không phải R và không phải lỗi.
- **Zero (chủ ngữ/vị ngữ/bổ ngữ) = E**; nếu zero theo dõi một nhân vật thì ghi
  thêm đọc *thế đại từ khiếm diện* trong §2/§4 của analysis — vẫn chỉ MỘT
  hàng E, không thêm hàng R cho cùng zero.
- **Pro-form** (như vậy, làm vậy, thế, vậy) = **S**; nếu nó trỏ sự kiện thì có
  thể là R (text reference) — chọn một mã, giải thích mã còn lại trong analysis.
- ***Phép thế đẳng nghĩa*, *phép liên tưởng* = L** (từ vựng), không phải S.
- ***Phép đối*, *phép tuyến tính*** không tự thân là tie; chỉ ghi L nếu có
  cặp hạng mục từ vựng xác định được.
- Classifier (cái/việc/điều/con/chiếc) đứng alone và tiểu từ cuối câu
  (nhé/ạ/chứ) **không phải tie**.

Dịch chuyển kỳ vọng (đọc trước khi kết luận "thiếu tie"):
EN đại từ → VI lặp từ (R→L); EN "the" → VI chỉ từ/zero/lặp; EN ellipsis mệnh
đề → VI lấp đầy (chỉ E phía EN); VI zero → EN đại từ; nối ngầm một bên → hiện
thực bên kia. Tất cả là **dịch chuyển để ghi nhận**, không phải lỗi hay tie thiếu.

## 3. Hướng quy chiếu A/C/E (chỉ dành cho R)

- `A` hồi quy: tiền trạm truy xuất được **trước** vị trí (thực thể, mệnh đề,
  hoặc attribution ở câu trước).
- `C` tiến chỉ: tiền trạm **sau** vị trí — rất hiếm trong tin tức; chỉ ghi khi
  thật sự đọc được.
- `E` ngoại văn bản: người viết/độc giả/bối cảnh (we-ta tác giả, you-bạn hướng
  độc giả…). Hàng ref=E được miễn "ante có mã câu" (ante chỉ mang tính mô tả).
- **Không bao giờ mặc định.** Mỗi hàng R là một quyết định tay.

## 4. Cơ chế bảng tie — 13 trường

```python
(sent, text, cat, sub, ante, conf, alt, note, occ, gap_after, recovered, level, ref)
```

- `sent`: mã câu trong `ST_seg.json`/`TT_seg.json` (S001…).
- `text`: **nguyên văn từng ký tự** trong câu đó; `None` với E.
- `cat/sub`: R|S|E|C|L; sub theo bảng vocab dưới đây.
- `ante`: `"S003: Singapore"` — **có mã câu**, trừ ref=E và [TC] (với [TC]
  cite cùng câu và ghi "(trong câu)").
- `conf`: high/med/low; bridging → low + note nêu cả hai phương án.
- `alt`: khả năng mã khác đã cân nhắc (vd `'R: the'`).
- `note`: ngắn, tiếng Việt, tiền tố `[LC]`/`[TC]` với hàng S/E.
- `occ`: **bắt buộc tường minh** (1, 2, …) khi chuỗi/gap lặp hơn một lần
  trong câu;annotate sẽ từ chối occ ngầm định khi trùng.
- E: `text=None`, `gap_after` = chuỗi nguyên văn kết thúc **ngay trước** ∅
  (`""` nếu ∅ ở đầu câu), `recovered` = `"{phần hồi phục}"`.
- `level`: LC/TC; `ref`: A/C/E chỉ với R.

Vocab `sub` thống nhất:
- R: `personal` / `demonstrative` / `comparative`
- S: `nominal` / `verbal` / `clausal`
- E: `nominal` / `verbal` / `clausal`
- C: `additive` / `adversative` / `causal` / `temporal` / `continuative`
- L: `repetition` / `synonym` / `antonym` / `superordinate` / `general word` /
  `collocation`

## 5. File phân tích 9 mục (`work/analysis/PXX_semantic.md`)

Theo `templates/analysis_template.md`, viết bằng **tiếng Việt**:
1. tổng quan + **bản đồ câu** ST↔TT (trạng thái mỗi câu: giữ/gộp/tách/bỏ/tự sinh);
2. tỉnh lược (mọi zero, [LC]/[TC], {hồi phục});
3. thế (danh/động/mệnh đề; giữ pro-form hay hiện thực hóa);
4. quy chiếu (bảng + hướng A/C/E + hành vi [±người]/danh xưng/khoảng cách);
5. nối (giữ/lược/tự sinh/đổi kiểu);
6. liên kết từ vựng (chuỗi hội tụ/phân rã khi dịch);
7. bảng dịch chuyển nổi bật (đếm + ví dụ nguyên văn hai đầu);
8. **bất thường dữ liệu nguồn** (câu trùng, thiếu dấu cách, sai số, hàng
   subhead, khối cắt…) + chỗ nào không dùng làm bằng chứng cấp câu;
9. **đối chiếu số đếm tay ↔ tie table** (bảng 10 ô EN/VI × R/S/E/C/L) + kết luận.

Không dùng [TC] làm bằng chứng cho bất kỳ kết luận nào về liên kết liên câu.

## 6. Cổng QC (phải đạt trước khi báo cáo)

```bash
cd /home/z/my-project/lme-bdnc-hw-session
python3 -m pipeline.annotate --work work --pair PXX
python3 -m pipeline.render   --work work --pair PXX
```

Cả hai phía phải in **PASS**. Lỗi thường gặp: text không nguyên văn trong
câu; thiếu occ khi chuỗi lặp; R thiếu ref; ante thiếu mã câu; ante không nằm
trước câu hiện tại (trừ ref=E / [TC]); gap_after không tìm thấy. **Sửa tie
table, không bao giờ sửa pipeline.**

## 7. Danh sách cấm

1. Copy tie/note/số liệu từ cặp khác hoặc từ bất kỳ benchmark nào.
2. Sinh tie bằng regex / danh sách từ / đếm chuỗi.
3. Bịa ∅ khi bản dịch đã lấp đầy chỗ trống; pro-form ghi S, không E.
4. Thêm hàng không có trong analysis; một dạng một hàng (không double-code).
5. Mặc định ref; bỏ qua phân tích thủ công để chạy nhanh.
6. Push git / sửa file ngoài phạm vi cặp của mình
   (`work/analysis/PXX*`, `work/tie_tables/PXX.py`, `work/pairs/PXX/`).

## 8. Hiệu chỉnh từ pilot P01 (BẮT BUỘC cho P02–P20)

### 8.1. Chính sách đánh dấu L — **v2 (nới rộng, có hiệu lực thay thế chính sách pilot hẹp)**

Sau khi hoàn tất 20/20 cặp theo chính sách pilot, điều phối viên rà soát thấy
lexical cohesion bị **đánh dấu thiếu rõ rệt**: lặp cùng dạng ở câu kề và từ
đơn lẻ đều là tie hợp lệ theo Halliday & Hasan (1976) nhưng bị chính sách
pilot loại. Chỉ thị của giảng viên (2026-11-05): phân tích kỹ hơn, đánh dấu
nhiều hơn. Chính sách v2 dưới đây **bổ sung** (không thay thế) các quy tắc
khác của CONVENTIONS.

**Chuỗi từ vựng giờ gồm cả từ đơn lẻ có nội dung thực** (danh từ, động từ,
tính từ, trạng từ nội dung): mỗi thuật ngữ đa từ, tên riêng, và từ đơn nội
dung là một chuỗi riêng.

**Đánh dấu [LC] khi hạng mục xuất hiện ở câu N với tiền trạm ở câu M ≠ N:**
(i) **lặp cùng dạng — kể cả câu kề ngay trước** (bỏ hạn chế "≥ 2 câu" và
"câu kề không đánh dấu" của pilot);
(ii) **biến thể mới** vào chuỗi (đồng nghĩa / trái nghĩa / thượng vị /
general word / biến thể hình thái / word-order);
(iii) tái lập chuỗi tại **điểm nối diễn ngôn** (subhead, attribution/lượt
lời mới, mở đoạn);
(iv) **lặp tên người nói** trong attribution;
(v) **động từ attribution** (says/said/explains… / nói/cho biết/nhấn mạnh…)
— chuỗi khung báo chí: mỗi câu có động từ attribution tái lập chuỗi thì
1 hàng L, ante = lần attribution trước đó.

**Vẫn KHÔNG đánh dấu:** cùng một dạng lặp nhiều lần **trong cùng một câu**
(một mark/câu/chuỗi; occ đếm tay số lần trong câu); từ thuần chức năng
(giới từ, trợ động từ, mạo từ đứng riêng, phó từ bé, đại từ — đại từ thuộc
R); classifier VI đứng alone và tiểu từ cuối câu; caption pull-quote / câu
artifact (xem 8.2); **lần đầu** trong văn bản (prerequisite); hạng mục trỏ
thực thể khác ("water" nước uống ≠ "the waters" vùng biển — quyết định bằng
ĐỌC HIỂU, không phải so chuỗi).

**Thứ tự chống double-code giữ nguyên** (một dạng một hàng, §1, §2): một
hạng mục vừa là biến thể mới vừa tái lập chuỗi → một hàng L với sub của quan
hệ từ vựng chính.

§6 analysis phải có bảng kho chuỗi (inventory) + danh sách hàng được đánh
dấu, để tie table chỉ chứa hàng có trong analysis; §9 đối chiếu lại sau khi
bổ sung. Mật độ định vị của v2 (không phải chỉ tiêu cứng): trung vị L
khoảng 60–70 EN / 55–65 VI mỗi cặp dài; cặp siêu ngắn (vd P12, 2 câu) đánh
dấu theo mức thực tế và nêu rõ lý do trong báo cáo.

### 8.2. Câu artifact không đánh dấu tie

Caption pull-quote (dòng attribution đứng riêng), câu lặp nguyên văn câu
trước, dòng chú thích biên tập: **không** đánh dấu tie; mô tả trong §8 analysis
và ghi rõ "không dùng làm bằng chứng cấp câu".

### 8.3. Bẫy cơ khí (occ) học từ P01

- Đại từ attribution: dùng text **"he says" / "ông nói"** thay vì "he"/"ông"
  riêng lẻ — tránh bẫy substring ("he" ⊂ They/their/scheme/the; "ông" ⊂
  **công** chúng/**công** nghệ). Nếu vẫn dùng dạng ngắn, đếm occ bằng tay theo
  substring thật trong câu.
- Chuỗi VI chứa dấu tiếng Việt: kiểm tra kỹ chữ có dấu (họ ≠ hoạch; khác ≠
  cách) trước khi kết luận occ.
- Bảng đối chiếu vị trí câu (rows.json ↔ sentmap) khi gán nhãn: hai lỗi lệch
  câu của pilot đều do ghi nhầm câu liền kề (S024/S026, S046/S047).
- **Segmenter chẻ câu tại dấu chấm viết tắt** (Jr., Mr., U.S., St.): khi hai
  "câu" sentmap thực chất là MỘT câu thật, lấy **câu thật** làm chuẩn khi quyết
  định [LC]/[TC] và "câu kề" của chính sách L; mã `sent` vẫn theo sentmap;
  ghi chú việc chẻ trong §8 analysis (không bịa tie liên câu từ chủ ngữ chia
  đôi).

### 8.4. Mật độ tham chiếu (không phải chỉ tiêu, chỉ để định vị)

P01 (tin tính năng 55/49 câu): EN 88 tie (R30 S3 E0 C8 L47), VI 67 tie
(R20 S1 E1 C8 L37) ≈ 1,6 tie/câu EN. Cặp ngắn hơn sẽ mật độ thấp hơn — không
ép bằng con số này; chất lượng đọc hiểu vẫn là tiêu chí duy nhất.
