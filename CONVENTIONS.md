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
