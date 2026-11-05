# P14 — Phân tích ngữ nghĩa liên kết (COHESION BEYOND THE SENTENCE LEVEL)

> **Khung:** EN — Halliday & Hasan (1976): reference, substitution, ellipsis,
> conjunction, lexical cohesion. VI — Trần Ngọc Thêm (1985; 2006, dẫn theo
> Nguyễn Thanh Tùng 2020): phép lặp, phép đối, phép thế đẳng nghĩa, phép liên
> tưởng, phép tuyến tính; phép thế đại từ (khiếm diện/dự báo/hồi quy), phép tỉnh
> lược, phép nối. Mã R/S/E/C/L theo `references/en-vi-mapping.md`.
> **Quy ước:** `[LC]` liên câu (đơn vị chính); `[TC]` trong câu (lớp bổ sung
> cho S/E); `[TD]` tiêu đề (chỉ nói ở §1/§8, không đánh dấu). `∅` = lược;
> `{…}` = hồi phục.

**ST (EN):** *Trump administration launches new 'self-deportation' app* — Reuters, 10/3/2025 (12 câu S001–S012; tiêu đề từ `meta.json`, không nằm trong flow).
**TT (VI):** *Chính quyền Trump ra mắt ứng dụng 'tự động trục xuất'* — VOA Tiếng Việt (12 câu S001–S012).

---

## 1. Tổng quan nội dung, thể loại, bản đồ câu

**Thể loại/nguồn:** tin chính trị – di trú: chính quyền Trump ra mắt ứng dụng
CBP Home cho phép người nhập cư trái phép "tự trục xuất". Cấu trúc: lede thông
báo (S001) → chi tiết app + nguồn cơ quan CBP (S002) → trích dẫn trực tiếp Bộ
trưởng An ninh Nội địa Kristi Noem kéo dài 2 câu, attribution cuối S003
(S003–S004) → nền chính sách: cam kết của Trump + so sánh số liệu thời Biden
(S005–S006) → các biện pháp tạo áp lực khác (S007–S008) → nền CBP One dưới thời
Biden + chỉ trích của đảng Cộng hòa (S009–S011) → đóng: Trump đóng CBP One
(S012). EN 12 câu / VI 12 câu: **ánh xạ 1–1 hoàn toàn** — 9/9 hàng `rows.json`
đều có đủ EN + VI, không gộp, không tách, không cắt, không câu VI tự sinh
(đối chiếu §8b).

**Các chuỗi/trường nghĩa chi phối liên kết:** (A) CBP Home; (B) CBP One — app
cũ; (C) app/ứng dụng (từ đơn); (D) Trump (người); (E) chính quyền Trump;
(F) Biden; (G) người di cư trái phép (immigrants / aliens / migrants / border
crossers / people lacking legal status ↔ người nhập cư / di dân / người vượt
biên); (H) đảng phái (a Republican / Democrat / Republicans ↔ đảng viên Cộng
hòa); (I) self-deport / tự trục xuất; (J) deport / trục xuất (từ đơn); (K)
lịch hẹn; (L) Mỹ / the United States (từ đơn); (M) leave / rời (từ đơn); (N)
verba dicendi + allow/cho phép + rolled out–launched/ra mắt; (O) biên giới;
(P) mass migration / di cư ồ ạt (danh từ chỉ quá trình). Kho đầy đủ ở §6.2.

**Bản đồ câu ST ↔ TT** (giữ = dịch gần 1–1):

| ST | TT | Ghi chú |
|---|---|---|
| S001 | S001 | giữ; "on Monday" → "ngày 10/3" (§8e); EN "self deport" (2 từ, ngoặc thẳng) ↔ VI 'tự trục xuất' (ngoặc đơn cong) |
| S002 | S002 | giữ; EN "the agency said" → VI "theo tuyên bố của cơ quan này" (danh từ hóa + chỉ từ, đều [TC] §4); EN "someone" → VI "người dùng" (hiện thực hóa) |
| S003 | S003 | giữ; EN "the option" (lặp kề S002) → VI động từ hóa "cho phép"; EN "aliens" (biến thể mới) ↔ VI "người nhập cư" (lặp từ đã có) |
| S004 | S004 | giữ; hai câu thật — chẻ tại "statement." đúng ranh giới câu (§8f); EN "don't" + ∅ ↔ VI "làm vậy" (E↔S); they/we ↔ họ/chúng tôi |
| S005 | S005 | giữ; VI thêm danh xưng "Tổng thống"; EN "migrants in the U.S. illegally" ↔ VI "di dân vào Mỹ trái phép" |
| S006 | S006 | giữ; EN "Democrat Joe Biden" → VI "cựu Tổng thống Joe Biden" (lược đảng — mất phép đối §6/§7; thêm "cựu") |
| S007 | S007 | giữ; EN "other steps" (R so sánh) ↔ VI "cũng … khác" (C phụ gia); VI "rời khỏi nước Mỹ" |
| S008 | S008 | giữ; EN "people lacking legal status" → VI mở rộng "đang có mặt tại Mỹ mà không có giấy tờ hợp pháp" |
| S009 | S009 | giữ; mở đoạn nền CBP One; tái lập CBP Home, Biden |
| S010 | S010 | giữ; EN "The Biden-era app" (mô tả, lặp kề) ↔ VI "Ứng dụng CBP One" (lặp tên); VI thêm "phỏng vấn" |
| S011 | S011 | giữ; EN "the Biden program" ↔ VI "chương trình của thời Biden" (đồng thời tái lập chuỗi đảng Cộng hòa) |
| S012 | S012 | giữ; EN "Trump" ↔ VI "Ông Trump" (thêm danh xưng); "unsure of next steps" → "không biết phải làm sao" |

## 2. Phép tỉnh lược (ellipsis)

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-EN1 | ST S004 | "If they don’t ∅, we will find them…" | tỉnh lược vị ngữ sau trợ động từ phủ định "don’t" (kiểu "John can ∅" của mapping §1); hồi phục {leave now and self-deport} ← S003 (câu trước, phần đầu trích dẫn Noem); VI không lấp bằng mệnh đề đầy đủ mà bằng pro-form "làm vậy" (S-VI1) — dịch chuyển E→S, không còn khe trống phía VI | [LC] |

**EN, các ứng viên đã kiểm tra và loại:**
- S003 "the option to leave now and self-deport", "to return legally… and
  live the American dream" — tọa hợp VP dùng chung một chủ ngữ điều khiển
  (aliens); theo H&H là phối thành phần, không có khe ∅;
- S011 "it facilitated mass migration… and did not adequately vet migrants" —
  chủ ngữ "it" dùng chung qua "and" (phối từ);
- S001 "rather than face possible arrest and detention" — chủ ngữ điều khiển
  (immigrants), cấu trúc "rather than" + VP;
- S010 "some one million" — số từ, không phải tỉnh lược (bẫy "one", xem §3).

**VI, các ứng viên vế tọa hợp đã cân nhắc và loại (cùng một kiểu):**
- S003 "người nhập cư rời đi ngay và ∅ tự trục xuất";
- S003 "họ có thể… quay lại hợp pháp… và ∅ sống giấc mơ Mỹ";
- S008 "phải đăng ký… hoặc ∅ đối mặt với án phạt hoặc án tù";
- S012 "khiến các di dân… rơi vào tình thế bị mắc kẹt và ∅ không biết phải làm sao".

Lý do loại: cả bốn vế sau "và/hoặc" là **VP trần nằm trong phạm vi một động từ
khuyết thiếu/nhân quả ở vế lớn hơn** ("cho phép", "có thể", "phải", "khiến…
rơi vào tình thế…") — một chủ ngữ/đối tượng điều khiển chi phối cả cụm ghép,
không phải mệnh đề độc lập có khe ∅ đọc được. Tỉnh lược chủ ngữ vế tọa hợp theo
TNT (như P13 S007 "và ∅ đã xác nhận…") áp dụng cho tọa hợp **mệnh đề** (vế có
đánh dấu thời/đối số riêng); bốn vị trí này đối ứng EN cũng là tọa hợp VP
("leave now and self-deport"; "register… or face…") — không bịia ∅ (cấm #3).
Ngoài ra VI S001 "thay vì đối mặt với khả năng bị bắt giam" — chủ ngữ điều
kiển, loại như P13 đã loại "để thảo luận về…".

**Nhận định:** EN 1 hàng E ([LC]) / VI 0 hàng. Chiều EN→VI duy nhất: khe ∅
sau "don’t" được VI hiện thực hóa bằng pro-form "làm vậy" (mapping §5:
clausal/verbal ellipsis → filled; ở đây lấp bằng phép thế chứ không phải mệnh
đề đầy đủ). Không có tỉnh lược nào ở cấp [TC] đủ điều kiện ghi.

## 3. Phép thế (substitution)

| # | Ngôn ngữ | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| S-VI1 | VI S004 | "Nếu họ không làm vậy, …" | "làm vậy" = do so — thế động từ: thay thế toàn bộ hành động "rời đi ngay và tự trục xuất" (S003, câu trước); EN đối ứng "don’t" + ∅ là tỉnh lược (E-EN1) | [LC] |

**Các ứng viên gần đúng đã cân nhắc và loại:**
- EN S004 "If they don’t" — có cân nhắc mã S (thế động từ "do") nhưng "don’t"
  là trợ động từ phủ định đứng trước khe ∅ vị ngữ (đúng khuôn "John can ∅"),
  chứ không phải pro-verb thay thế wording → mã E; đọc "thế" chỉ nêu ở đây,
  một dạng một hàng (mapping §3.13);
- EN S010 "some one million migrants" — "one" là thành phần của số từ "one
  million", KHÔNG phải thế danh từ kiểu "the red one" — bẫy cơ khí đã loại
  (đếm occ không cứu được sai chức năng);
- Không còn one/ones/do so/the same nào trong ST; VI không có
  "như vậy/thế/vậy" nào ngoài "làm vậy".

**Nhận định:** phép thế chỉ xuất hiện một phía (VI), đúng vị trí EN dùng tỉnh
lược — cặp E-EN1 ↔ S-VI1 minh họa "function, not form, across languages"
(mapping §3.12): cùng một chức năng (tránh lặp hành động đã nêu) hiện thực hóa
bằng hai thiết bị khác nhau hai phía.

## 4. Phép quy chiếu (reference)

### 4.1. Bảng quy chiếu EN (3 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-EN1 | S004 | they | A | S003: aliens | [+người, số nhiều]; tiếp chuỗi "aliens" ở phần đầu trích dẫn Noem (câu trước); cùng chuỗi trong câu: "them" ×2, "they" lần 2 — 1 mark |
| R-EN2 | S004 | we | A | S003: attribution (Homeland Security Secretary Kristi Noem said) | đại từ ngôi 1 trong trích dẫn; attribution nằm ở câu trước → đủ điều kiện [LC] (CONVENTIONS §1); "we" = phía chính quyền/bộ trưởng; mô hình giống P01 S028 |
| R-EN3 | S007 | other | A | S001: rolled out a new app (bước đi trước của chính quyền) | quy chiếu so sánh loại trừ ("other steps" — "steps" là từ mới, không lặp); presuppose bước trước đó = việc mở app; đọc phụ gia ghi ở alt; VI đối ứng "cũng … khác" (C-VI1) |

### 4.2. Bảng quy chiếu VI (2 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-VI1 | S004 | họ | A | S003: người nhập cư | [+người]; hồi quy "người nhập cư" ở phần đầu trích dẫn (câu trước); "họ" ×3 trong câu — 1 mark |
| R-VI2 | S004 | chúng tôi | A | S003: attribution (Bộ trưởng An ninh Nội địa Kristi Noem nói) | đại từ ngôi 1 trong trích dẫn; attribution câu trước → [LC]; "chúng tôi" ×2 — 1 mark; đối ứng song song EN "we" (R-EN2) |

### 4.3. Hướng A/C/E và hệ đại từ / danh xưng / [±người]

- **A áp đảo:** 3/3 hàng EN, 2/2 hàng VI. Không đọc được hướng C (tiền chỉ)
  nào ở body. **Không có ref=E:** mọi đại từ ngôi 1 đều nằm trong trích dẫn
  Noem với attribution ở câu trước (đủ điều kiện [LC], tiền trạm =
  attribution) — giống P01 ("we" ← attribution Khan), khác P13 (P13 không có
  đại từ ngôi 1/2 nào).
- **[±người]:** EN chỉ có "they/them" và "we" [+người, số nhiều]; VI "họ",
  "chúng tôi" [+người]. Không có đại từ [−người] liên câu nào hai phía
  (khác P13 "its citizens").
- **Danh xưng VI:** VI thêm honorific/chức danh — "Tổng thống Trump" (S005),
  "ông Trump" (S006), "cựu Tổng thống Joe Biden" + "ông Biden" (S006), "Ông
  Trump" (S012) — đều là danh ngữ/kề câu chứ không phải đại từ; "ông Biden"
  S006 cùng câu với tên đầy đủ → [TC] không ghi.
- **Các ứng viên [TC] đã kiểm tra và loại** (R chỉ đánh dấu [LC] theo
  CONVENTIONS §1): EN S002 "their" ← someone (cùng câu); EN S002 "the agency"
  ← U.S. Customs and Border Protection (cùng câu); EN S003 "they" ← aliens
  (cùng câu); EN S006 "Biden's" ← Joe Biden (cùng câu); EN S011 "it" ← the
  Biden program (cùng câu); VI S002 "cơ quan này" ← Cơ quan Bảo vệ Biên giới
  và Hải quan Mỹ (cùng câu — đối ứng EN "the agency"); VI S003 "họ" ← người
  nhập cư (cùng câu); VI S011 "nó" ← chương trình của thời Biden (cùng câu);
  EN S001/S009 "that" là đại từ quan hệ (cấu trúc), không phải quy chiếu liên
  kết theo H&H.
- **Hành vi "the" (EN):** không có "the" nào là liên kết duy nhất ở cấp liên
  câu (khác P13 "the reclusive state"). Các "the" đối chiếu được rơi vào: (i)
  đầu ngữ lặp từ vựng của câu kề trước → phép lặp là liên kết chính, không
  đánh dấu hàng riêng (S002 "The U.S. Customs and Border Protection app" ←
  S001 "a new app"; S003 "The CBP Home app" ← S002 "CBP Home"; S003 "the
  option" ← S002 "an option"; S010 "The Biden-era app" ← S009 "an app");
  (ii) xác định giải quyết cùng câu → [TC] (S002 "the agency"; S006 "the
  monthly average" ← deportation numbers cùng câu). Khả năng "R: the" của
  các vị trí (i) ghi nhận ở đây và trong note hàng L tương ứng chuỗi app
  (S011 "the Biden program" có alt "R: the").

## 5. Phép nối (conjunction)

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-VI1 | TT S007 | "cũng" | additive | S001: ra mắt một ứng dụng mới (hành động trước của chính quyền) | [LC] phó từ nối phụ gia: biện pháp khác cộng thêm với việc mở app; EN đối ứng hiện thực hóa quan hệ phụ gia bằng "other steps" (R-EN3) — một vị trí, hai mã theo hai khung |

**EN: không có hàng nối nào (C-EN = 0).** Các liên từ/phản từ đã kiểm tra đều
nối vế trong cùng câu: "rather than" (S001, chọn lựa), "so" (S003, hệ quả),
"and" (S004, S011), "although" (S006, nhượng bộ — quan hệ đối lập S005↔S006
chỉ hiện thực hóa bằng phép đảo bố cục, hai phía đều không có liên từ liên
câu → không bịa C theo mapping §3.8), "or" (S008 ×2), "hours after"
(S008/S012, trong câu). VI tương tự: "thay vì" (S001), "và" (S003 ×2, S004,
S012), "để" (S003), "mặc dù" (S006), "hoặc" (S008), "khiến" (S012) — toàn bộ
trong câu.

**Nhận định:** quan hệ liên câu duy nhất đọc được là phụ gia "thêm bước mới"
(S007): EN mã hóa bằng quy chiếu so sánh "other steps" (R), VI bằng phép nối
phụ gia "cũng" + "khác" (C) — không "sửa cho cân" (CONVENTIONS §1). Các mốc
thời gian "on Monday"/"ngày 10/3" là khung exophoric, không truy hồi được
textual antecedent → không phải tie (§8e).

## 6. Liên kết từ vựng (lexical cohesion)

### 6.1. Chính sách đánh dấu L (áp dụng CONVENTIONS §8.1 như P01 §6.1, P13 §6.1)

Chuỗi định nghĩa **hẹp theo tổ hợp từ vựng**: mỗi thuật ngữ/tên riêng/cụm danh
ngữ định danh là một chuỗi riêng (CBP Home; CBP One; The Trump
administration/chính quyền Trump; Trump; Biden; đảng phái; người di cư;
self-deport/tự trục xuất; lịch hẹn). **Đánh dấu [LC] khi:** (i) hạng mục là
biến thể mới vào chuỗi (từ/cách diễn đạt chưa từng xuất hiện trong chuỗi:
đồng nghĩa, trái nghĩa, liên tưởng, gia đình hình thái); (ii) tái lập chuỗi
(kể cả cùng dạng) sau khoảng cách ≥ 2 câu, hoặc tại điểm nối diễn ngôn (mở
đoạn) khi chuỗi đã ngắt quãng. **Không đánh dấu:** lặp ở câu kề ngay trước
(kể cả mở đoạn nếu chuỗi liên tục); từ đơn tản mát thuộc từ vựng đề tài
(deport/trục xuất; leave/rời; app/ứng dụng; Mỹ/the United States;
allow/cho phép; said/nói; rolled out–launched/ra mắt); thành phần trong tên
riêng; quan hệ quá trình↔người (mass migration ~ migrants). P14 không có
trường hợp (iii) lặp tên người nói trong attribution (Noem chỉ xuất hiện một
lần duy nhất). **Một mark/câu/chuỗi.**

### 6.2. Kho chuỗi hai phía (inventory — gồm cả thành viên không đánh dấu)

| Chuỗi | Thành viên EN | Thành viên VI | Đánh dấu |
|---|---|---|---|
| A. CBP Home | called CBP Home (S002) · The CBP Home app (S003) · CBP Home (S009) | gọi là CBP Home (S002) · Ứng dụng CBP Home (S003) · CBP Home (S009) | EN: S009; VI: S009 (S002→S003 lặp kề) |
| B. CBP One (app cũ) | an app known as CBP One (S009, lần đầu) · The Biden-era app (S010) · the Biden program (S011) · CBP One (S012) | ứng dụng CBP One (S009, lần đầu) · Ứng dụng CBP One của thời Biden (S010) · chương trình của thời Biden (S011) · CBP One (S012) | EN: S011 (biến thể "program"), S012 (trở lại tên riêng); VI: S011, S012 (S009→S010 lặp kề) |
| C. app/ứng dụng (từ đơn) | a new app (S001) · app (S002, S003, S009, S010) | một ứng dụng mới (S001) · Ứng dụng/ứng dụng (S002, S003, S009, S010) | không (từ đơn tản mát; các mốc tên riêng đã đánh dấu ở A/B) |
| D. Trump (người) | President Donald Trump's (S001) · Trump (S005) · Trump's (S006) · Trump (S012) | Tổng thống Donald Trump (S001) · Tổng thống Trump (S005) · ông Trump (S006) · Ông Trump (S012) | EN: S005, S012; VI: S005, S012 (S006 kề S005; "Trump" trong "Trump administration" là thành phần tên riêng chuỗi E) |
| E. chính quyền Trump | The Trump administration (S001) · The Trump administration (S007) · A Trump administration regulation (S008) | Chính quyền Trump (S001) · Chính quyền Trump (S007) · chính quyền Trump (S008) | EN: S007; VI: S007 (S008 kề S007) |
| F. Biden | Democrat Joe Biden (S006) · Biden's (S006, cùng câu) · Biden (S009) · Biden-era (S010) · the Biden program (S011, gộp chuỗi B) | cựu Tổng thống Joe Biden (S006) · ông Biden (S006, cùng câu) · Biden (S009) · thời Biden (S010, S011) | EN: S009; VI: S009 (S010/S011 lặp kề) |
| G. người di cư trái phép | immigrants in the United States illegally (S001) · aliens (S003) · migrants in the U.S. illegally (S005) · recent border crossers (S006) · immigrants in the United States illegally (S007) · people lacking legal status (S008) · migrants in Mexico (S010) · migrants (S011) · migrants with pending appointments (S012) | những người nhập cư đang ở Mỹ trái phép (S001) · người nhập cư (S003) · di dân vào Mỹ trái phép (S005) · người vượt biên gần đây (S006) · người nhập cư trái phép (S007) · (người) không có giấy tờ hợp pháp (S008) · di dân ở Mexico (S010) · người nhập cư (S011) · di dân có lịch hẹn (S012) | EN: S003, S005, S006, S008, S010; VI: S003, S005, S006, S008, S010 (S007/S011/S012 lặp kề dạng đã có trong kho) |
| H. đảng phái | a Republican (S005) · Democrat (S006) · Republicans (S011) | một đảng viên Cộng hòa (S005) · — (VI lược "Democrat") · Các đảng viên Cộng hòa (S011) | EN: S006 (trái nghĩa), S011; VI: S011 |
| I. self-deport | "self deport" (S001) · self-deport (S003) | 'tự trục xuất' (S001) · tự trục xuất (S003) | EN: S003; VI: S003 (tái lập thuật ngữ sau 2 câu) |
| J. deport/trục xuất (từ đơn) | deportation push (S001) · deport (S004, S005) · deportation numbers, deportations (S006) | chính sách trục xuất (S001) · trục xuất (S004, S005) · Số liệu trục xuất, các đợt trục xuất (S006) | không (từ đơn tản mát 5–6 lần mỗi phía, như verba dicendi P13 §6.2 K) |
| K. lịch hẹn | an appointment (S010) · pending appointments (S012) | lịch hẹn (S010) · lịch hẹn (S012) | EN: S012; VI: S012 (tái lập gap 2) |
| L. Mỹ/the United States (từ đơn) | the United States (S001, S007, S011) · the U.S. (S005; S002 trong tên cơ quan) | Mỹ (S001, S005, S007 ×2, S008 ×2, S011) | không (từ đơn tản mát 7 lần phía VI; nhiều vị trí lồng trong cụm đã đánh dấu chuỗi G — tránh trùng span) |
| M. leave/rời (từ đơn) | intent to depart (S002) · leave now (S003) · to leave (S007) | ý định rời đi (S002) · rời đi ngay (S003) · rời khỏi nước Mỹ (S007) | không (từ đơn; S002→S003 kề, S007 lồng trong ngữ cảnh chuỗi G) |
| N. verba dicendi + allow + launch | said (S002, S003) · saying (S011) · rolled out (S001) · launched (S009) · allow (S001) | theo tuyên bố (S002) · nói (S003) · cho rằng (S011) · ra mắt (S001, S009) · cho phép (S001? không — S003, S010) | không (động từ quá phổ biến; hai sự kiện "rolled out"/"launched" khác nhau) |
| O. biên giới | border crossers (S006, đã tính chuỗi G) · a legal border crossing (S010) | vượt biên (S006, chuỗi G) · cửa khẩu biên giới hợp pháp (S010) | không (S006 đã đánh dấu ở G; "border crossing" S010 là điểm cửa khẩu — loại tham chiếu khác, từ đơn "border" chung) |
| P. quá trình di cư | mass migration (S011) | sự di cư ồ ạt (S011) | không (danh từ chỉ quá trình; gia đình hình thái với migrants/di dân nhưng gốc từ tản mát — inventory) |

### 6.3. Các hàng L ghi vào tie table

**EN — 16 hàng** (câu | dạng | kiểu | tiền trạm):
S003 "aliens", đồng nghĩa ← S001 immigrants in the United States illegally
(thuật ngữ hành chính — biến thể mới, trong trích dẫn Noem) · S003
"self-deport", lặp ← S001 "self deport" (tái lập thuật ngữ then chốt sau 2
câu, biến thể gạch nối) · S005 "Trump", lặp ← S001 President Donald Trump's
(tái lập sau 4 câu, rút còn họ) · S005 "migrants in the U.S. illegally", đồng
nghĩa ← S001 immigrants in the United States illegally (biến thể
migrants + viết tắt U.S.; chuỗi ngắt quãng từ S003) · S006 "border crossers",
collocation ← S005 migrants in the U.S. illegally (liên tưởng cùng trường di
cư; nhóm con "recent") · S006 "Democrat", trái nghĩa ← S005 a Republican
(phép đối; VI lược — §7) · S007 "The Trump administration", lặp ← S001 The
Trump administration (tái lập sau 6 câu, mở đoạn) · S008 "people lacking
legal status", đồng nghĩa ← S007 immigrants in the United States illegally
(diễn đạt mới) · S009 "CBP Home", lặp ← S003 The CBP Home app (tái lập sau 6
câu, mở đoạn nền CBP One) · S009 "Biden", lặp ← S006 Democrat Joe Biden (tái
lập sau 3 câu, rút còn họ) · S010 "migrants in Mexico", lặp ← S005 migrants
in the U.S. illegally (lặp từ "migrants" sau chuỗi liên tục S005–S008; nhóm
tham chiếu khác — quan hệ từ vựng) · S011 "the Biden program", đồng nghĩa ←
S010 The Biden-era app ("program" — cách gọi mới của app CBP One; alt
"R: the") · S011 "Republicans", lặp ← S005 a Republican (tái lập sau 6 câu,
mở đoạn; biến thể số nhiều) · S012 "Trump", lặp ← S006 Trump's (tái lập sau 6
câu, mở đoạn kết) · S012 "CBP One", lặp ← S009 an app known as CBP One (trở
lại tên riêng sau 2 câu dùng mô tả app/program) · S012 "appointments", lặp ←
S010 schedule an appointment (tái lập sau 2 câu).

**VI — 15 hàng** (câu | dạng | kiểu | tiền trạm):
S003 "người nhập cư", lặp ← S001 những người nhập cư đang ở Mỹ trái phép (tái
lập sau 2 câu trong trích dẫn; EN đối ứng là biến thể mới "aliens") · S003 "tự
trục xuất", lặp ← S001 'tự trục xuất' (tái lập thuật ngữ sau 2 câu) · S005
"Tổng thống Trump", lặp ← S001 Tổng thống Donald Trump (tái lập sau 4 câu,
rút tên — giữ danh xưng) · S005 "di dân vào Mỹ trái phép", đồng nghĩa ← S001
những người nhập cư đang ở Mỹ trái phép (biến thể "di dân") · S006 "người
vượt biên", collocation ← S005 di dân vào Mỹ trái phép (liên tưởng; nhóm con
"vượt biên gần đây") · S007 "Chính quyền Trump", lặp ← S001 Chính quyền Trump
(tái lập sau 6 câu, mở đoạn) · S008 "không có giấy tờ hợp pháp", đồng nghĩa ←
S007 những người nhập cư trái phép (paraphrase "trái phép") · S009 "CBP Home",
lặp ← S003 Ứng dụng CBP Home (tái lập sau 6 câu) · S009 "Biden", lặp ← S006
cựu Tổng thống Joe Biden (tái lập sau 3 câu) · S010 "di dân ở Mexico", lặp ←
S005 di dân vào Mỹ trái phép (lặp "di dân" sau chuỗi S005–S008) · S011
"chương trình của thời Biden", đồng nghĩa ← S010 Ứng dụng CBP One của thời
Biden ("chương trình" — cách gọi mới) · S011 "Các đảng viên Cộng hòa", lặp ←
S005 một đảng viên Cộng hòa (tái lập sau 6 câu, mở đoạn) · S012 "Ông Trump",
lặp ← S006 ông Trump (tái lập sau 6 câu, mở đoạn kết; danh xưng + họ) · S012
"CBP One", lặp ← S010 Ứng dụng CBP One (tái lập sau 2 câu — S011 dùng
"chương trình") · S012 "lịch hẹn", lặp ← S010 đặt lịch hẹn (tái lập sau 2 câu).

### 6.4. Nhận định

- **L-EN (16) ≈ L-VI (15)** — gần cân vì ánh xạ câu 1–1 và chuỗi định danh
  (tên riêng, thuật ngữ) chi phối hai phía như nhau. Chênh 1 hàng do EN có
  "Democrat" (phép đối với "a Republican" S005) mà VI lược mất (S006 VI chỉ
  còn "cựu Tổng thống Joe Biden").
- **EN phân rã, VI hội tụ** ở chuỗi G: EN dùng 5 cách nói (immigrants /
  aliens / migrants / border crossers / people lacking legal status) còn VI
  xoay quanh 2 nhãn chính (người nhập cư / di dân) + 1 biến thể (người vượt
  biên). Tại S003 cùng một vị trí: EN đánh dấu vì "aliens" là biến thể mới,
  VI đánh dấu vì "người nhập cư" tái lập sau gap 2 — cùng số hàng, khác lý do
  (bất đối xứng chuẩn mực EN→VI: R/đa dạng từ → lặp từ, mapping §5).
- **Chuỗi B ngược lại:** EN tránh lặp tên ("The Biden-era app" S010, "the
  Biden program" S011) còn VI lặp tên "Ứng dụng CBP One" (S010) — lặp danh từ
  VI là liên kết chuẩn theo TNT (mapping §3.9), EN chuộng diễn đạt lại.
- Từ đơn đề tài (deport/trục xuất ×5–6, Mỹ ×7, app/ứng dụng, leave/rời,
  allow/cho phép, said/nói) chỉ nằm trong inventory — nếu đánh dấu mọi lặp kề
  VI sẽ vượt 20 hàng L; mọi thành viên vẫn liệt kê ở §6.2 để kiểm tra được.
- Chuỗi phụ "lịch hẹn" (S010→S012, gap 2) được đánh dấu như chuỗi "thư mời"
  của P13 — cùng quy tắc tái lập.

### 6.4. Bổ sung L theo chính sách v2 (2026-11-05)

Theo chỉ thị giảng viên (phân tích kỹ hơn, đánh dấu nhiều hơn), chính
sách L được nới rộng (CONVENTIONS §8.1 v2): lặp cùng dạng kể cả câu kề,
từ đơn có nội dung thực, chuỗi động từ attribution, tái lập tại điểm nối
diễn ngôn. Kho chuỗi §6.2 được rà lại; các hàng L mới là quyết định đọc
hiểu tay (không regex/word-list), mỗi hàng 1 mark/câu/chuỗi, ante luôn
nằm trước. Danh sách hàng bổ sung (đối soát 2 cổng QC PASS):

Phía EN — 34 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S002 | The U.S. Customs and Border Protection app | repetition | S001: a new app |
| 2 | S003 | The CBP Home app | repetition | S002: The U.S. Customs and Border Protection app, called CBP Home |
| 3 | S003 | gives | synonym | S002: will offer an option |
| 4 | S003 | the option | repetition | S002: an option |
| 5 | S003 | leave | synonym | S002: intent to depart |
| 6 | S003 | said | repetition | S002: the agency said |
| 7 | S003 | legally | antonym | S001: in the United States illegally |
| 8 | S004 | deport | repetition | S001: deportation push |
| 9 | S004 | return | repetition | S003: to return legally |
| 10 | S005 | vowed | collocation | S003: said in a statement |
| 11 | S005 | deport | repetition | S004: we will deport them |
| 12 | S006 | Trump's | repetition | S005: Trump |
| 13 | S006 | deportation | repetition | S001: deportation push |
| 14 | S006 | numbers | repetition | S005: record numbers |
| 15 | S007 | immigrants | repetition | S001: immigrants in the United States illegally |
| 16 | S007 | the United States | repetition | S005: the U.S. |
| 17 | S007 | illegally | repetition | S005: in the U.S. illegally |
| 18 | S007 | to leave | repetition | S003: the option to leave now |
| 19 | S008 | Trump administration | repetition | S007: The Trump administration |
| 20 | S008 | regulation | collocation | S007: other steps |
| 21 | S008 | face | repetition | S001: rather than face possible arrest and detention |
| 22 | S008 | fines or jail time | collocation | S001: arrest and detention |
| 23 | S009 | launched | synonym | S001: rolled out a new app |
| 24 | S010 | app | repetition | S009: an app known as CBP One |
| 25 | S010 | Biden-era | repetition | S009: under Biden |
| 26 | S010 | included | repetition | S006: Biden's deportations included |
| 27 | S010 | allowed | repetition | S001: will allow |
| 28 | S010 | legal | repetition | S008: legal status |
| 29 | S010 | feature | collocation | S003: the option |
| 30 | S011 | saying | repetition | S005: has vowed |
| 31 | S011 | the United States | repetition | S007: the United States |
| 32 | S011 | migrants | repetition | S010: migrants in Mexico |
| 33 | S012 | migrants | repetition | S011: vet migrants |
| 34 | S012 | shut down | antonym | S009: was launched under Biden |


Phía VI — 36 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S002 | Ứng dụng | repetition | S001: một ứng dụng mới |
| 2 | S003 | Ứng dụng CBP Home | repetition | S002: Ứng dụng của Cơ quan Bảo vệ Biên giới và Hải quan Mỹ, gọi là CBP Home |
| 3 | S003 | cho phép | repetition | S001: cho phép những người nhập cư |
| 4 | S003 | rời đi | repetition | S002: ý định rời đi |
| 5 | S003 | nói | synonym | S002: theo tuyên bố của cơ quan này |
| 6 | S003 | hợp pháp | antonym | S001: đang ở Mỹ trái phép |
| 7 | S003 | cơ hội | collocation | S002: một sự lựa chọn |
| 8 | S004 | trục xuất | repetition | S001: chính sách trục xuất |
| 9 | S004 | quay lại | repetition | S003: quay lại hợp pháp |
| 10 | S005 | cam kết | collocation | S003: Kristi Noem nói |
| 11 | S005 | trục xuất | repetition | S004: sẽ trục xuất họ |
| 12 | S006 | ông Trump | repetition | S005: Tổng thống Trump |
| 13 | S006 | trục xuất | repetition | S005: cam kết trục xuất |
| 14 | S006 | Số liệu | collocation | S005: một số lượng kỷ lục |
| 15 | S007 | người nhập cư | repetition | S003: người nhập cư |
| 16 | S007 | trái phép | repetition | S005: di dân vào Mỹ trái phép |
| 17 | S007 | rời khỏi | repetition | S003: rời đi ngay |
| 18 | S007 | nước Mỹ | repetition | S005: vào Mỹ |
| 19 | S008 | chính quyền Trump | repetition | S007: Chính quyền Trump |
| 20 | S008 | quy định | collocation | S007: các biện pháp khác |
| 21 | S008 | đối mặt với | repetition | S001: đối mặt với khả năng bị bắt giam |
| 22 | S008 | án phạt hoặc án tù | collocation | S001: khả năng bị bắt giam |
| 23 | S008 | Mỹ | repetition | S007: nước Mỹ |
| 24 | S009 | ra mắt | repetition | S001: ra mắt một ứng dụng mới |
| 25 | S009 | ứng dụng | repetition | S003: Ứng dụng CBP Home |
| 26 | S010 | Ứng dụng CBP One | repetition | S009: ứng dụng CBP One |
| 27 | S010 | Biden | repetition | S009: Biden |
| 28 | S010 | cho phép | repetition | S003: cho phép |
| 29 | S010 | hợp pháp | repetition | S008: không có giấy tờ hợp pháp |
| 30 | S010 | tính năng | collocation | S002: một sự lựa chọn |
| 31 | S011 | cho rằng | collocation | S005: cam kết |
| 32 | S011 | người nhập cư | repetition | S007: người nhập cư |
| 33 | S011 | Mỹ | repetition | S008: tại Mỹ |
| 34 | S012 | đóng | antonym | S009: ra mắt |
| 35 | S012 | di dân | repetition | S010: di dân ở Mexico |
| 36 | S012 | ứng dụng | repetition | S010: Ứng dụng CBP One |

Số đếm §9 dưới đây đã gộp toàn bộ phần bổ sung này. Các kết luận §6.5
(nếu có) của bản pilot về "chọn lọc lặp kề" không còn áp dụng — thay
bằng chính sách v2.

## 7. Các dịch chuyển liên kết nổi bật (tổng hợp)

| Kiểu dịch chuyển | Số lần | Ví dụ nguyên văn |
|---|---:|---|
| EN tỉnh lược vị ngữ → VI pro-form (E→S) | 1 | EN S004 "If they don’t ∅, we will find them" → VI S004 "Nếu họ không làm vậy, chúng tôi sẽ truy tìm" |
| EN quy chiếu so sánh → VI phép nối phụ gia | 1 | EN S007 "has taken other steps" → VI S007 "cũng đã thực hiện các biện pháp khác" |
| EN đại từ → VI đại từ (giữ) | 2 | EN S004 "If they don’t"/"we will" ↔ VI "Nếu họ"/"chúng tôi sẽ" (they↔họ; we↔chúng tôi) |
| EN biến thể từ vựng → VI lặp từ đã có | 1 | EN S003 "aliens" → VI S003 "người nhập cư" (lặp S001) |
| EN trái nghĩa đảng phái → VI lược | 1 | EN S006 "under Democrat Joe Biden" → VI S006 "dưới thời cựu Tổng thống Joe Biden" |
| EN danh từ → VI động từ hóa | 1 | EN S003 "gives aliens the option to leave" → VI S003 "cho phép người nhập cư rời đi" ("the option" mất) |
| EN diễn đạt mô tả → VI lặp tên riêng | 1 | EN S010 "The Biden-era app" → VI S010 "Ứng dụng CBP One của thời Biden" |
| EN lượng từ bất định → VI hiện thực hóa | 1 | EN S002 "an option for someone to signal their intent" → VI S002 "một sự lựa chọn để người dùng thông báo" |
| EN attribution động từ → VI danh từ hóa + chỉ từ | 1 | EN S002 "the agency said" → VI S002 "theo tuyên bố của cơ quan này" |
| Thứ → ngày (explicitation thời gian, exophoric) | 1 | EN S001 "on Monday" → VI S001 "ngày 10/3" (§8e) |
| VI thêm danh xưng/chức danh | 3 | "Tổng thống Trump" (S005); "cựu Tổng thống Joe Biden" (S006); "Ông Trump" (S012) |
| VI mở rộng paraphrase | 2 | EN S008 "people lacking legal status" → VI "những người đang có mặt tại Mỹ mà không có giấy tờ hợp pháp"; EN S010 "to schedule an appointment" → VI "đặt lịch hẹn phỏng vấn" |
| Tiêu đề [TD]: thuật ngữ bị thêm "động" | 1 | EN title "'self-deportation'" → VI title "'tự động trục xuất'" (thân bài VI đúng là "tự trục xuất" — §8a) |

## 8. Bất thường dữ liệu nguồn (cần ghi chú khi thống kê)

- **(a) Tiêu đề VI lệch thuật ngữ:** EN title "…new 'self-deportation' app"
  ↔ VI title "Chính quyền Trump ra mắt ứng dụng 'tự động trục xuất'" — VI
  thêm "động" ('tự động trục xuất' = tự động hóa việc trục xuất) trong khi
  thân bài VI S001/S003 dùng đúng 'tự trục xuất'. Tiêu đề là [TD], không nằm
  trong flow ST/TT → không có tie table; chỉ mô tả ở §1/§7/đây. Không dùng
  tiêu đề làm bằng chứng cấp câu.
- **(b) Ghi chú nguồn về "khối VI=none":** ghi chú nguồn phiên làm việc
  (SESSION.md) nhắc P14 có "nhiều hàng VI=none (khối 2018)". Kiểm tra thực tế:
  `rows.json` của P14 có 9/9 hàng đều đủ EN + VI, sentmap 12/12 câu, 9/9 đoạn
  hai bên — **không có hàng VI=none nào, không có khối cắt** (anomalie "khối
  2018" là của P13, mang sang P14 do nhầm ghi chú). Phân tích này dựa hoàn
  toàn trên dữ liệu thực tế trong `work/pairs/P14/`; không có chỗ nào phải
  "đánh dấu bên EN, bỏ trống bên VI".
- **(c) Dấu ngoặc kép lai (EN):** S003 mở bằng “ (U+201C) nhưng đóng bằng "
  (thẳng); S004 mở " (thẳng), đóng ” (U+201D). VI dùng ngoặc đơn ‘…’ (S001,
  S002) và ngoặc kép “…” (S003, S004) không đồng nhất. Giữ nguyên văn từng ký
  tự khi trích (ảnh hưởng việc tra text/occ).
- **(d) Apostrophe cong:** EN S004 "don’t" dùng ’ (U+2019) — `gap_after`
  của hàng E-EN1 phải dùng đúng ký tự này.
- **(e) Quy đổi thời gian:** EN "on Monday" → VI "ngày 10/3" (thứ → ngày),
  nhất quán với thứ Hai 10/3/2025 theo URL Reuters. Mốc exophoric, không dùng
  làm bằng chứng cấp câu (không phải tie — đã loại ở §5).
- **(f) Ranh giới câu S003/S004:** trích dẫn Noem + attribution nằm gọn cuối
  S003, câu trích thứ hai ("If they don't…") là S004 — chẻ tại "statement."
  là ranh giới câu THẬT (không phải chẻ tại dấu viết tắt như §8.3
  CONVENTIONS) → các hàng [LC] ở S004 (they/we/∅, họ/chúng tôi/làm vậy) hợp lệ.
- **(g) "one million" không phải thế:** EN S010 "some one million migrants" —
  "one" thuộc số từ, đã loại ở §3; không dùng làm bằng chứng cho phép thế.
- **(h) Bất đối xứng inventory EN/VI:** EN "Democrat" (S006) không có đối ứng
  VI; VI thêm "cựu Tổng thống"/"Tổng thống"/"Ông" — mô tả ở §6.4/§7, không
  "sửa cho cân" (CONVENTIONS §1).
- **(i) Không có câu artifact** (caption pull-quote, câu lặp nguyên văn, dòng
  chú thích biên tập) — 12 câu hai bên đều là câu body thật, dùng được làm
  bằng chứng cấp câu. Không có câu nào bị segmenter chẻ tại dấu viết tắt
  (không có Jr./Mr./U.S. cuối câu).

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table (cập nhật v2 2026-11-05)

| Chỉ số | Phân tích | Tie table | Ghi chú |
|---|---:|---:|---|
| EN — R | 3 | 3 | §4 |
| EN — S | 0 | 0 | §3 |
| EN — C | 0 | 0 | §5 |
| EN — E | 1 | 1 | §2 |
| EN — L | 50 | 50 | §6 (pilot 16 + v2 34) |
| VI — R | 2 | 2 | §4 |
| VI — S | 1 | 1 | §3 |
| VI — C | 1 | 1 | §5 |
| VI — E | 0 | 0 | §2 |
| VI — L | 51 | 51 | §6 (pilot 15 + v2 36) |

- Tổng tie: EN **54** / VI **55** (pilot: EN 20 / VI 19).
- Bổ sung v2 (34 EN + 36 VI hàng) theo chỉ thị giảng viên
  2026-11-05 (CONVENTIONS §8.1 v2): lặp câu kề, từ đơn nội dung, động từ
  attribution; đã PASS 2 cổng QC `pipeline.annotate` + `pipeline.render`.
- Liên kết từ vựng giữ vai trò chủ lực: L-EN 50 (93%),
  L-VI 51 (93%).
- L-VI (51) > L-EN (50): bản VI lặp danh từ/tên riêng
  trực tiếp dày hơn (Trần Ngọc Thêm: phép lặp), EN thay bằng đại từ.
- Quy chiếu EN 3 / VI 2 (EN ưa đại từ, VI ưa danh ngữ lặp);
  tỉnh lược EN 1 / VI 0; thế EN 0 / VI 1;
  nối EN 0 / VI 1.
- Các hàng chỉ [TC] không dùng làm bằng chứng cho kết luận liên kết liên câu.
