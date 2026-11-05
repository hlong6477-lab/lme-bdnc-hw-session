# P08 — Phân tích ngữ nghĩa liên kết (COHESION BEYOND THE SENTENCE LEVEL)

> **Khung:** EN — Halliday & Hasan (1976): reference, substitution, ellipsis,
> conjunction, lexical cohesion. VI — Trần Ngọc Thêm (1985; 2006, dẫn theo
> Nguyễn Thanh Tùng 2020): phép lặp, phép đối, phép thế đẳng nghĩa, phép liên
> tưởng, phép tuyến tính; phép thế đại từ (khiếm diện/dự báo/hồi quy), phép tỉnh
> lược, phép nối. Mã R/S/E/C/L theo `references/en-vi-mapping.md`.
> **Quy ước:** `[LC]` liên câu (đơn vị chính); `[TC]` trong câu (lớp bổ sung cho
> S/E); `[TD]` tiêu đề. `∅` = lược; `{…}` = hồi phục.

**ST (EN):** *Revealed: Australian suburbs with the biggest home price falls* —
SBS News (40 câu S001–S040). S001 là hàng **dek/subhead** "State-by-state: …"
(đọc như hàng body theo CONVENTIONS §1); 5 hàng khác cũng dính subhead đầu câu:
S011 "Sydney slows down", S014 "Gold Coast prices take a dip", S017 "First-home
buyers in Melbourne", S029 "Hobart and Canberra: Mixed results", S033 "Will it
be a buyer's market in 2025?".
**TT (VI):** *Những khu vực có giá nhà giảm mạnh nhất tại Úc trong năm 2024* —
SBS Tiếng Việt (38 câu S001–S038). S001 là **headline VI** (trùng `title_vi`
trong meta.json) ghép với dek EN; VI giữ 5 subhead tương ứng (S010 "Giá nhà
Sydney giảm", S013, S016, S027, S031), **cắt trọn khối S022–S023** (para 17
rỗng), **gộp** EN S010+S011 → VI S010, **tách** EN S017 → VI S016+S017.

---

## 1. Tổng quan nội dung, thể loại, bản đồ câu

**Thể loại/nguồn:** tin kinh tế – bất động sản của SBS News (Úc, tháng 1/2025)
dựa trên phúc trình giá nhà quý 4/2024 của Domain: điểm danh các khu vực có giá
giảm mạnh nhất toàn Úc theo từng bang — Sydney (Crows Nest −22,1%), Gold Coast
(Biggera Waters −22,4%, Clear Island Waters −21,1%), Melbourne/first-home
buyers (căn hộ +2,1%; Chadstone −33,3%, Sunshine −18,9%, Barwon Heads −20,5%,
Warracknabeal −19,6%), Hobart (căn hộ −1,5% nhưng nhà +4,6%), Canberra (đứng
yên; Denman Prospect −22,2%) — kết bằng triển vọng "thị trường của người mua"
2025. Cấu trúc: dek (S001) → lede + bối cảnh thị trường (S002–S005) → khối
trích dẫn Nicola Powell (S006–S009) → mục Sydney (S010–S013) → mục Gold Coast
(S014–S016) → mục Melbourne (S017–S023) → các khu vực Melbourne + vùng
(S024–S028) → mục Hobart–Canberra (S029–S032) → mục triển vọng 2025
(S033–S040).

**Các chuỗi/trường nghĩa chi phối liên kết:** (i) **trường giá** — home/house/
unit prices, property values, median (giá nhà, giá căn hộ, giá cả, giá trị,
giá bất động sản); (ii) **thị trường** (property/housing market ↔ thị trường
địa ốc/nhà ở); (iii) **người mua** (buyers, first-home buyers ↔ người mua nhà,
người mua nhà lần đầu); (iv) **nhu cầu** (demand ↔ nhu cầu); (v) **chi trả –
áp lực** (affordability pressures, accessible, affordable ↔ áp lực tài chính,
áp lực giá nhà, chi trả, khả năng chi trả); (vi) **tăng–giảm** (falls,
decline, dip, decrease, increase, growth ↔ giảm, sụt giảm, hạ nhiệt, tăng,
tăng trưởng, gia tăng); (vii) **Powell** (Nicola Powell, Powell said, she ↔
bà Nicola Powell, bà nói, Bà Powell); (viii) **phúc trình – dữ liệu** (Domain
report, the data ↔ Phúc trình, dữ liệu); (ix) **quý** (December quarter ↔ quý
4, quý cuối); (x) **thủ phủ** (capital city/cities ↔ các thủ phủ); (xi)
**khu vực** (suburbs ↔ những khu vực); (xii) **nguồn cung** (housing stock,
Increased supply — chỉ tồn tại phía EN vì VI cắt nửa sau S005); (xiii) **lãi
suất** (interest rate, rate-lifting ↔ lãi suất); (xiv) **các khung mở–đóng**
(interesting, tip the scales, property market ↔ một năm thú vị, cho người mua
nhà trong năm nay, thị trường địa ốc); (xv) **tên riêng** (Domain, Sydney,
Melbourne, Hobart, Canberra, Gold Coast, Queensland, Victoria, Crows Nest,
Biggera Waters, Clear Island Waters, Chadstone, Sunshine, Barwon Heads,
Warracknabeal, Denman Prospect, RBA, 2024/2025) — lặp dày, chỉ inventory.

**Bản đồ câu ST ↔ TT** (giữ = dịch gần 1–1; VI 38 = EN 40 − 2 câu cắt
[S022–S023] + 1 câu tách [S017] − 1 câu gộp [S010+S011]; từ S024 chỉ số VI
lệch −2):

| ST | TT | Ghi chú |
|---|---|---|
| S001 | S001 | dek EN "State-by-state: …" ↔ headline VI (trùng title_vi); đọc như hàng body |
| S002 | S002 | giữ; EN "This year" ↔ VI "năm 2025" (explicitation); EN "one" [TC] ↔ VI "một năm thú vị" |
| S003 | S003 | giữ; VI lược ẩn dụ "the scales" — làm tiền trạm cho khung đóng S032 |
| S004 | S004 | giữ |
| S005 | S005 | VI **cắt nửa sau** (housing stock, homes for sale) → chuỗi nguồn cung chỉ có EN |
| S006 | S006 | giữ; VI cắt "rather than a fall in demand" |
| S007 | S007 | giữ |
| S008 | S008 | giữ; EN "Powell said" (L, tên) ↔ VI "bà nói" (R, đại từ) |
| S009 | S009 | giữ |
| S010 | S010 | **gộp với S011**; VI cắt "second consecutive decline / only capital city" (dồn sang S011); EN "But" [LC] ↔ VI "nhưng" [TC] |
| S011 | S010 | gộp; subhead "Sydney slows down" ↔ "Giá nhà Sydney giảm" |
| S012 | S011 | giữ; VI gộp thêm "liên tiếp trong hai quý" ← ý S010 |
| S013 | S012 | giữ; EN "the city's" (R) ↔ VI hiện thực bằng tên "Sydney"; VI lược "recent report" |
| S014 | S013 | giữ (subhead "Gold Coast prices take a dip" ↔ "Giá nhà Gold Coast hạ nhiệt") |
| S015 | S014 | giữ; VI cắt "a popular suburb on the Gold Coast" |
| S016 | S015 | giữ |
| S017 | S016+S017 | **tách**; EN "while" [TC] ↔ VI "cũng" [LC] (tự sinh); "the same period" [TC] ↔ "cùng giai đoạn" [LC] |
| S018 | S018 | giữ; EN "the unit price growth" (L) ↔ VI "sự gia tăng này" (R) |
| S019 | S019 | giữ |
| S020 | S020 | giữ |
| S021 | S021 | giữ |
| S022 | — | VI **cắt** |
| S023 | — | VI **cắt** (para 17 rỗng, rows.json vi="") |
| S024 | S022 | giữ; VI lược "year-on-year" (chỉ số lệch −2 từ đây) |
| S025 | S023 | giữ |
| S026 | S024 | giữ; VI lược "Victorian" |
| S027 | S025 | giữ; VI lược "Regional" |
| S028 | S026 | giữ |
| S029 | S027 | giữ (subhead "Hobart and Canberra: Mixed results") |
| S030 | S028 | giữ |
| S031 | S029 | giữ; VI lược "at a capital level"; VI **tự sinh** "Trong khi đó" (EN nối ngầm) |
| S032 | S030 | giữ; VI lược "ACT", "bringing the median to" |
| S033 | S031 | giữ (subhead "Will it be a buyer's market in 2025?") |
| S034 | S032 | giữ |
| S035 | S033 | giữ |
| S036 | S034 | giữ |
| S037 | S035 | giữ; VI explicitation "một số yếu tố" |
| S038 | S036 | giữ |
| S039 | S037 | giữ; EN "that" [TC] ↔ VI ∅ chủ ngữ [TC] |
| S040 | S038 | giữ; EN "rate-lifting cycle" ↔ VI "giảm lãi suất" (lệch nghĩa, §8d) |

## 2. Phép tỉnh lược (ellipsis)

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-VI1 | TT S037 | "Các điều kiện yếu đã tích lũy trong năm 2024 và ∅ sẽ ảnh hưởng đến đầu năm 2025." | zero chủ ngữ của vế tọa hợp sau "và"; hồi phục {các điều kiện yếu} — chủ ngữ vế 1 cùng câu; đọc *thế đại từ khiếm diện* (zero theo dõi một participant) nhưng theo quy ước chỉ MỘT hàng E, không thêm hàng R; EN đối ứng đại từ tường minh "that is going to flow" | [TC] |

**EN — các ứng viên đã kiểm tra và loại (E-EN = 0):**
- S002 "an \"interesting\" one" — thế danh từ (S), không phải tỉnh lược (§3);
- S012 "It's the first time…" — "It" đại từ hình thức/cleft, không phải khe ∅;
- S017 "— up 2.1 per cent over the December quarter" — vị ngữ rút gọn dạng
  bổ ngữ appositive (kiểu "(which is) up…"), không hồi phục theo kiểu tỉnh lược
  H&H, ghi nhận inventory;
- S020 "we saw growth" / S023 "we've seen" / S039 "and that is going to flow" —
  mọi mệnh đề đều đủ chủ ngữ, đại từ tường minh;
- S005, S013, S024–S032 — mệnh đề đầy đủ chủ–vị; không có khe "two ∅" hay
  "John can ∅" nào trong văn bản.

**VI — các chỗ trống đã cân nhắc nhưng không đánh dấu:**
- S010 "giá nhà tại đây đã giảm 0,1%" — chủ ngữ hiện diện;
- S017 "Giá nhà cũng tăng 1,6%" — chủ ngữ hiện diện (câu tách riêng khỏi S016);
- S008 "họ chỉ đang trì hoãn" — chủ ngữ "họ" tường minh;
- S032 "có thể tạo điều kiện thuận lợi" — chủ ngữ "khả năng chi trả và triển
  vọng…" hiện diện ở cùng câu;
- S006/S012 — mệnh đề đầy đủ.

**Nhận định:** EN không có tỉnh lược nào ([LC] lẫn [TC]); VI đúng 1 hàng E
[TC] tại vị trí EN dùng đại từ "that" — dịch chuyển **EN đại từ → VI ∅** (R-EN
[TC] không đánh dấu vs E-VI [TC] đánh dấu theo quy ước S/E được ghi [TC]). Không
có cặp nào hai phía cùng tỉnh lược như P17 ("Some ∅"/"Một số ∅").

## 3. Phép thế (substitution)

| # | Ngôn ngữ | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| S-EN1 | EN S002 | "This year will be an \"interesting\" one for Australia's property market" | "one" thế cho danh từ "year" cùng câu ("an interesting one" = "an interesting year") — thế danh từ điển hình của H&H; VI đối ứng hiện thực hóa "một năm thú vị" (lặp "năm", không giữ pro-form) | [TC] |

**Các ứng viên gần đúng đã cân nhắc và loại:**
- EN S007 "What we have seen is…" — "What" là đại từ quan hệ mở đầu pseudo-
  cleft, không thay thế wording có thể viết ra → không phải thế;
- EN S025 "over the same period", S031 "over the same period" — "the same"
  có mặt trong danh sách S của H&H nhưng luôn đi kèm danh từ "period" nên chức
  năng trội là **quy chiếu so sánh** (R comparative, mapping §4); khả năng S
  ghi vào `alt` ("S: the same");
- VI S007 "Những gì chúng tôi thấy" — quan hệ tự do, không phải pro-form thế;
- VI S017/S023/S029 "cùng (giai đoạn)" — như EN "the same period": quy chiếu
  so sánh (R), `alt "S: cùng"`;
- Không có "do/so/not/ones" (EN) hay "như vậy/làm vậy/thế/vậy" thay wording
  (VI) nào trong văn bản.

**Nhận định:** mỗi phía nhiều nhất 1 thiết bị: EN 1 phép thế danh từ [TC]
("one"), VI không có (VI lặp "năm"). Cặp "the same/cùng" được giải bằng quy
chiếu so sánh thay vì thế — quyết định đối xứng hai phía, ghi `alt` để lưu khả
năng kia. Phép thế không phải thiết bị chủ lực của cặp này; các "chỗ rỗng"
diễn đạt được giải quyết bằng quy chiếu mở rộng ("This/That/it/điều đó/này")
hoặc bằng lặp danh từ.

## 4. Phép quy chiếu (reference)

### 4.1. Bảng quy chiếu EN (16 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-EN1 | S001 | These | C | S013: units in the … suburb of Crows Nest (danh sách khu vực bài sẽ điểm: Biggera Waters, Chadstone, Denman Prospect…) | dek; "These" tiến chỉ — các khu vực được liệt kê ở phần thân; conf low, khả năng đọc ngoại văn bản ghi alt (§8b) |
| R-EN2 | S006 | the data | A | S005: this week's Domain's house price report | bridging: mạo từ xác định là liên kết duy nhất tại vị trí (danh từ mới "data"); VI đối ứng danh từ trần "dữ liệu" → L |
| R-EN3 | S008 | That | A | S007: a pullback in buyer demand | quy chiếu mở rộng tới phát ngôn S007; VI "Điều đó" |
| R-EN4 | S009 | This delay | A | S008: people delay their decisions | chỉ từ + danh từ (động từ → danh từ hóa); alt "L: delay ← delay"; VI "Sự trì hoãn này" |
| R-EN5 | S010 | it | C | S011: Sydney slows down Sydney remains… | "it" = thành phố (Sydney) được nêu tên ở câu sau — tiến chỉ hiếm gặp, conf low; nguyên nhân là thứ tự đoạn nguồn (§8e); VI hiện thực bằng tên "Sydney" ngay trong S010 |
| R-EN6 | S013 | the city's | A | S011: Sydney remains Australia's most expensive housing market | "the" + danh từ mới "city"; sự xác định là liên kết chính; VI hiện thực bằng tên "Sydney" |
| R-EN7 | S020 | It's | A | S019: Melbourne has been the surprise | = Melbourne; VI "Thị trường ở đây" |
| R-EN8 | S021 | This | A | S020: we saw growth | quy chiếu mở rộng; VI "Sự tăng trưởng này" (R + lặp danh từ) |
| R-EN9 | S023 | those two movements in price | A | S022: Sydney and Melbourne price cycles | chỉ từ + số từ + danh từ tổng quát; VI cắt khối |
| R-EN10 | S025 | the same period | A | S024: year-on-year | quy chiếu so sánh; VI "cùng giai đoạn"; alt "S: the same" |
| R-EN11 | S027 | these changes | A | S026: house prices … dropped 20.5 per cent (khối giảm S024–S026) | quy chiếu mở rộng tới khối diễn ngôn; VI "những thay đổi này" |
| R-EN12 | S030 | there | A | S029: Hobart recorded the sharpest decline… | phó từ chỉ vị trí hồi quy (tại Hobart); VI "ở đây" |
| R-EN13 | S031 | over the same period | A | S030: over the quarter | quy chiếu so sánh; VI "cùng giai đoạn" |
| R-EN14 | S036 | this trend | A | S035: Increased supply … opportunities to negotiate on price | quy chiếu mở rộng; VI "xu hướng này" |
| R-EN15 | S037 | it | A | S036: Will this trend hold? | quy chiếu mở rộng tới câu hỏi; VI "điều này" |
| R-EN16 | S038 | she said | A | S037: According to Powell | đại từ attribution; tiền trạm ở câu trước; VI "bà nói" |

### 4.2. Bảng quy chiếu VI (15 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-VI1 | S008 | Điều đó | A | S007: nhu cầu của người mua giảm | quy chiếu mở rộng tới phát ngôn; đối ứng EN "That" (R-EN3) |
| R-VI2 | S008 | họ | A | S007: người mua | [+người, số nhiều]; EN đối ứng danh từ tổng quát "people" (L) — dịch chiều ngược: VI đại từ ↔ EN danh từ |
| R-VI3 | S008 | bà nói | A | S006: bà Nicola Powell | đại từ attribution (text "bà nói" tránh bẫy substring); EN đối ứng tên "Powell said" (L) |
| R-VI4 | S009 | Sự trì hoãn này | A | S008: trì hoãn việc ra quyết định | chỉ từ + danh từ hóa; đối ứng EN "This delay" (R-EN4) |
| R-VI5 | S017 | cùng giai đoạn | A | S016: … tăng 2,1% trong quý 4 | quy chiếu so sánh; EN "the same period" nằm [TC] trong S017 (không đánh dấu) — VI tách câu nên thành [LC] |
| R-VI6 | S018 | sự gia tăng này | A | S017: Giá nhà cũng tăng 1,6% | chỉ từ + danh từ hóa mới ("tăng" → "sự gia tăng"); EN đối ứng "the unit price growth" (L) |
| R-VI7 | S020 | Thị trường ở đây | A | S019: Melbourne thật sự gây bất ngờ | chỉ từ vị trí "ở đây" + danh từ chuỗi thị trường; EN đối ứng đại từ thuần "It's" |
| R-VI8 | S021 | Sự tăng trưởng này | A | S020: ghi nhận sự tăng trưởng | chỉ từ "này" + lặp danh từ kề; đối ứng EN "This" (R-EN8) |
| R-VI9 | S023 | cùng giai đoạn | A | S022: Chadstone … giảm 33,3% | đối ứng EN "the same period" (S025); VI lược "year-on-year" nên tiền trạm mô tả |
| R-VI10 | S025 | những thay đổi này | A | S024: giá nhà … Barwon Heads giảm 20,5% (khối S022–S024) | quy chiếu mở rộng; đối ứng EN "these changes" (R-EN11) |
| R-VI11 | S028 | ở đây | A | S027: Hobart … mức giảm giá căn hộ mạnh nhất | chỉ từ vị trí = tại Hobart; đối ứng EN "there" (R-EN12) |
| R-VI12 | S029 | cùng giai đoạn | A | S028: tăng 4,6% trong quý 4 | đối ứng EN "over the same period" (S031) |
| R-VI13 | S034 | xu hướng này | A | S033: Nguồn cung gia tăng … thương lượng về giá | quy chiếu mở rộng; đối ứng EN "this trend" (R-EN14) |
| R-VI14 | S035 | điều này | A | S034: Liệu xu hướng này có tiếp diễn? | danh từ tổng quát "điều" + chỉ từ; đối ứng EN "it" (R-EN15) |
| R-VI15 | S036 | bà nói | A | S035: Theo bà Powell | đại từ attribution, tiền trạm ở câu trước; đối ứng EN "she said" (R-EN16) |

### 4.3. Hướng A/C/E và hệ đại từ / danh xưng / [±người]

- **Hướng:** A áp đảo — 14/16 hàng EN, 15/15 hàng VI. Hai hàng C đều phía EN và
  đều do cấu trúc nguồn: R-EN1 "These" (dek tiến chỉ danh sách khu vực ở phần
  thân) và R-EN5 "it" (S010 nói về Sydney trước khi Sydney được nêu tên ở
  S011 — artifact thứ tự đoạn, §8e). **Không có ref=E**: bài không có đại từ
  ngôi 1/2 nào đủ điều kiện (xem dưới), dateline/dek là khung ngoại cảnh.
- **Đại từ ngôi 1/2 trong trích dẫn — tất cả bị loại theo CONVENTIONS §1**
  (attribution phải ở câu trước): EN "we" S007 (attribution "Powell said" cuối
  S008 — câu sau), S020 ("Powell said" cuối cùng câu), S023 (attribution ở
  S020, cách 3 câu), S040 (attribution ở S038, cách 2 câu); VI "chúng tôi"
  S007/S020, "chúng ta" S038 — hoàn toàn đối xứng. EN "You" (S022) generic
  (người ta), không truy hồi.
- **[±người] và danh xưng:** EN chỉ có 1 đại từ [+người] là "she said" (R-EN16);
  "it/It's/this/that/these/those/there" đều [−người] hoặc quy chiếu mở rộng
  (thành phố, thị trường, tình huống, khoảng thời gian). VI có 3 hàng [+người]
  ("họ", "bà nói" ×2) — VI dùng đại từ ở các vị trí EN dùng tên/danh từ tổng
  quát ("Powell said", "people"). Honorific "bà" chỉ đi kèm chức năng attribution,
  không có "ông ấy/bà ấy" đứng độc lập.
- **Danh từ tổng quát + chỉ từ là khuynh hướng VI:** "Điều đó", "điều này",
  "Sự trì hoãn/gia tăng/tăng trưởng này", "Thị trường ở đây", "xu hướng này",
  "những thay đổi này" — VI neo bằng danh từ (thường lặp/danh từ hóa tiền trạm)
  thay vì đại từ thuần như EN ("That", "This", "It's"); 8/15 hàng R-VI thuộc
  loại này. Nguyên tắc mã: chỉ từ "này/đó" + danh từ **tổng quát** → R thuần;
  chỉ từ + danh từ **lặp/gia đình hình thái** tiền trạm → vẫn R (chỉ từ là dấu
  quy chiếu tường minh) nhưng ghi khả năng L vào `alt`.
- **Hành vi "the" (EN):** 5 hàng L có `alt "R: the"` — "the December quarter"
  (S017), "the unit price growth" (S018), "the quarter" (S030), "the median"
  (S032), "the market overall" (S034): đầu ngữ đều lặp từ vựng tiền trạm nên
  phép lặp là liên kết chính. Hai hàng R riêng cho "the": "the data" (S006,
  danh từ mới — bridging) và "the city's" (S013, danh từ mới) — đúng §1
  CONVENTIONS.
- **Đã kiểm tra và loại (EN):** "This year" S002 (deixis thời gian ngoại cảnh —
  VI hiện thực "năm 2025"); "an economist" S002 (bất định — tiền trạm danh xưng
  của Powell S006, không đánh dấu); "it means" S008, "this hasn't been the case"
  S023, "their strongest" S017, "its lowest level" S034, "that" S039 (đều [TC]
  cùng câu); "It's the first time" S012 và "Will it be" S033 (đại từ hình
  thức); "There is" S023 (tồn tại); "one another" S022 (tương hỗ, cùng câu);
  "as a market" S020 (nghĩa "một thị trường" generic); "Regional and smaller
  markets" S027 (lớp chỉ vật mới, không đồng quy chiếu); "the change" S040
  (nghĩa "yếu tố biến đổi", khác "changes" S027).
- **Đã kiểm tra và loại (VI):** "tại đây" S010 ([TC] — "Sydney" cùng câu);
  "Những gì" S007 (quan hệ tự do); "Các thị trường nhỏ hơn" S025 (lớp mới);
  "một số yếu tố" S035 (tự sinh); "các điều kiện yếu" S037 không truy hồi được
  tiền trạm xác định.

## 5. Phép nối (conjunction)

**EN — 10 hàng** (adversative 5 · additive 4 · temporal 1):

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-EN1 | S010 | But | adversative | S006: a shift in buyer behaviour rather than a fall in demand (S007–S008: demand doesn't go away) | chuyển mạch từ phân tích nhu cầu sang số liệu giá giảm ("nhu cầu không giảm" ↔ "giá đã giảm"); VI đối ứng "nhưng" nằm [TC] trong S010 → không đánh dấu; conf med |
| C-EN2 | S014 | also | additive | S013: units … Crows Nest … decreasing by 22.1 per cent | cộng trường hợp Queensland sau Sydney; VI "cũng" |
| C-EN3 | S016 | Similarly | additive | S015: Biggera Waters … 22.4 per cent year-on-year decrease | liệt kê song song Clear Island Waters; VI "Tương tự" |
| C-EN4 | S025 | also | additive | S024: Chadstone … dropping by 33.3 per cent | cộng Sunshine sau Chadstone; VI "cũng" |
| C-EN5 | S026 | Meanwhile | temporal | S025: Sunshine … an 18.9 per cent decline | chuyển trường hợp cùng kỳ (Barwon Heads); VI "Trong khi đó" |
| C-EN6 | S027 | either | additive | S026: house prices … dropped 20.5 per cent (khối S024–S026) | phần tử cộng thêm trong phủ định ("not been immune … either"); VI "cũng" |
| C-EN7 | S030 | In contrast | adversative | S029: the sharpest decline in unit prices … falling 1.5 per cent | đối lập giảm căn hộ ↔ tăng nhà (Hobart); VI "Tuy nhiên" |
| C-EN8 | S032 | But | adversative | S031: Canberra's housing market was stagnant … no change | tổng thể đứng yên ↔ một khu vực giảm mạnh; VI "Tuy nhiên" |
| C-EN9 | S036 | But | adversative | S035: Increased supply … more opportunities | cơ hội cho người mua ↔ nghi vấn tính bền; conf med; VI "Nhưng" |
| C-EN10 | S040 | But | adversative | S039: Weak conditions … flow into the early parts of 2025 | điều kiện yếu tiếp diễn ↔ yếu tố có thể thay đổi (lãi suất); VI "Tuy nhiên" |

**VI — 11 hàng** (adversative 5 · additive 5 · temporal 1):

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-VI1 | S013 | cũng | additive | S012: giá căn hộ ở Crows Nest … giảm 22,1% | đối ứng C-EN2, giữ 1–1 |
| C-VI2 | S015 | Tương tự | additive | S014: Biggera Waters … giảm 22,4% | đối ứng C-EN3, giữ 1–1 |
| C-VI3 | S017 | cũng | additive | S016: Giá căn hộ ở Melbourne tăng mạnh nhất … 2,1% | **VI tự sinh** (EN "while" nằm [TC] trong S017); VI tách câu nên nối thành [LC] |
| C-VI4 | S023 | cũng | additive | S022: Chadstone … giảm 33,3% | đối ứng C-EN4, giữ 1–1 |
| C-VI5 | S024 | Trong khi đó | temporal | S023: Sunshine … giảm 18,9% | đối ứng C-EN5 ("Meanwhile"), giữ 1–1; thiên đối chiếu, conf med |
| C-VI6 | S025 | cũng | additive | S024: giá nhà … Barwon Heads giảm 20,5% | đối ứng C-EN6 ("either"), giữ 1–1 |
| C-VI7 | S028 | Tuy nhiên | adversative | S027: Hobart … mức giảm giá căn hộ mạnh nhất | đối ứng C-EN7, giữ 1–1 |
| C-VI8 | S029 | Trong khi đó | adversative | S028: giá nhà ở đây lại tăng 4,6% | **VI tự sinh** (EN S031 nối ngầm, không có liên từ); đối chiếu tăng (Hobart) ↔ giữ nguyên (Canberra) |
| C-VI9 | S030 | Tuy nhiên | adversative | S029: thị trường Canberra giữ nguyên | đối ứng C-EN8, giữ 1–1 |
| C-VI10 | S034 | Nhưng | adversative | S033: Nguồn cung gia tăng … cơ hội | đối ứng C-EN9, giữ 1–1 |
| C-VI11 | S038 | Tuy nhiên | adversative | S037: Các điều kiện yếu … đầu năm 2025 | đối ứng C-EN10, giữ 1–1 |

**Nhận định:** nối gần đối xứng 10↔11 với 3 dịch chuyển đáng chú ý: (1) EN
C-EN1 "But" [LC] ↔ VI "nhưng" [TC] (S010) — VI gộp câu khiến phạm vi nối thu
hẹp vào trong câu, mất 1 hàng; (2) VI tự sinh "cũng" (S017) và "Trong khi đó"
(S029) tại hai vị trí EN chỉ có nối [TC] ("while") hoặc nối ngầm — đủ 2 hàng
bù, làm VI nhiều hơn 1; (3) đổi kiểu một cặp: "Meanwhile" ↔ "Trong khi đó"
(S026/S024) cùng temporal, nhưng "Trong khi đó" thứ hai (S029) là adversative.
Các liên từ trong câu không đánh dấu vì C chỉ [LC]: "In addition to" S005,
"rather than" S006, "as" S004/S009, "while" S017, "but" S020, "and" S039–S040
(EN) ↔ "khi" S004/S009, "nhưng" S010/S020, "và" S013/S029/S037, "Mặc dù" S032
(VI).

## 6. Liên kết từ vựng (lexical cohesion)

### 6.1. Chính sách đánh dấu L của cặp này (theo CONVENTIONS §8.1)

Chuỗi định nghĩa hẹp theo tổ hợp từ vựng (multi-word item); từ đơn tản mát
("prices/giá", "market/thị trường" trần, "suburb" đơn lẻ, tên riêng, verba
dicendi, số liệu phần trăm/năm) chỉ ghi inventory. **Đánh dấu [LC] khi:**
(i) hạng mục là biến thể mới vào chuỗi (đồng nghĩa/trái nghĩa/thượng vị/
general word/gia đình hình thái/đảo-rút tổ hợp); (ii) tái lập chuỗi sau khoảng
cách ≥ 2 câu không có thành viên trung gian, hoặc tại điểm nối diễn ngôn
(5 subhead, mở/đóng trích dẫn, attribution mới); (iii) lặp tên người nói
trong attribution sau khoảng cách. **Không đánh dấu:** lặp cùng dạng ở câu kề
ngay trước (trường giá liên tục hiện diện hầu hết các câu của mỗi mục nên
nhiều câu trong mục không phát sinh mark); các trạng ngữ thời gian rút gọn
"the quarter/trong quý" (S010) không đánh dấu riêng vì cùng câu đã đánh dấu
chuỗi giá, chuỗi quý được đánh dấu tại các lần tái lập chính. Một
mark/câu/chuỗi; subhead vừa là thành viên chuỗi vừa là điểm nối.

### 6.2. Kho chuỗi hai phía (inventory — gồm cả thành viên không đánh dấu)

| Chuỗi | Thành viên EN | Thành viên VI | Đánh dấu |
|---|---|---|---|
| A. trường giá | home prices (S001, S005) · property values (S004) · rising prices (S009) · house prices (S010 ×2, S016, S017, S026, S030, S032) · median prices (S013) · Gold Coast prices (S014) · houses prices (S015, typo §8a) · unit prices (S017, S024, S029) · unit price (S025) · unit price growth (S018) · price cycles (S022) · movements in price (S023) · house or unit prices (S031) · the median (S032) · negotiate on price (S035) | giá nhà (S001, S004, S005, S010 ×2, S011, S013, S014, S015, S017, S024, S026, S028, S030) · giá cả (S009) · giá căn hộ (S012, S016, S022, S023, S027) · giá bất động sản (S013) · áp lực giá nhà (S009) · giá nhà trung bình (S026) · giá trị (S021) · thương lượng về giá (S033) | EN 15: S004, S005, S009, S010, S013, S014, S017, S022, S024, S026, S028, S029, S030, S032, S035; VI 14: S004, S005, S009 (giá cả), S010, S012, S013, S016, S017, S022, S024, S026, S027, S028, S033 |
| B. thị trường | Australia's property market (S002) · Australia's housing market (S004) · Australia's most expensive housing market (S011) · as a market (S020) · Regional and smaller markets (S027) · Canberra's housing market (S031) · buyer's market (S033) · the market overall (S034) | thị trường địa ốc Úc (S002) · Thị trường nhà ở Úc (S004) · thị trường nhà ở đắt đỏ nhất nước Úc (S010) · Thị trường ở đây (S020, R) · Các thị trường nhỏ hơn (S025) · thị trường Canberra (S029) · thị trường [của người mua nhà] (S031) · thị trường địa ốc (S032) | EN 5: S004, S011, S031, S033, S034; VI 5: S004, S010, S029, S031, S032 |
| C. tăng – giảm | falls (S001) · fallen (S005) · dropped (S010, S026) · decline (S010 ×2, S012, S025, S028, S029) · take a dip (S014) · decrease (S015) · fall (S016) · increase (S017 ×2) · growth (S018, S020, S034) · improvement (S024) · surged (S030) · drop (S032) | giảm (S001, S005, S010 ×2, S012, S014, S022, S024, S026, S030) · hạ nhiệt (S013) · sụt giảm (S011) · tăng (S016, S017) · gia tăng (S018) · tăng trưởng (S020, S021, S032) · cải thiện (S022) | chọn lọc trong mark của chuỗi A/B (S012, S014 EN; S013, S018/S020 VI); "improvement/cải thiện" trái nghĩa áp lực — chỉ ghi note |
| D. người mua | buyers (S003) · buyer behaviour (S006) · buyer demand (S007) · people (S008) · many buyers (S009) · activating buyers (S020) · first-home buyers (S017, S018, S021) · buyer's market (S033) · buyers (S034) | người mua nhà (S003, S006, S031, S032) · người mua (S007, S021) · họ (S008, R) · người mua nhà lần đầu (S016, S018, S021) | EN 3: S006, S008 (people), S021; VI 3: S006, S021, S031 (S033 EN/S032 VI gộp vào khung/chuỗi B) |
| E. nhu cầu | shifting demand (S004) · demand (S006, S007, S008 ×2) | nhu cầu (S004, S007, S008 ×2) | EN 1: S006; VI 1: S007 (VI cắt "fall in demand" S006 nên mark dời xuống) |
| F. chi trả – áp lực | affordability pressures (S004, S009) · more accessible (S013) · more affordable (S015) · housing affordability (S024) · affordability (S034) | áp lực tài chính (S004) · áp lực giá nhà (S009) · chi trả (S009) · khả năng chi trả nhà ở (S022) · khả năng chi trả (S032) | EN 4: S009, S015, S024, S034; VI 3: S009 (áp lực), S022, S032 |
| G. Powell | Nicola Powell (S006) · Powell said (S008, S018, S020) · Powell (S037) · she said (S038, R) | bà Nicola Powell (S006) · bà nói (S008, R) · Bà Powell (S018) · bà Powell nhận xét (S020) · Theo bà Powell (S035) · bà nói (S036, R) | EN 4: S008, S018, S020, S037; VI 3: S018, S020, S035 |
| H. phúc trình – dữ liệu | Domain's house price report (S005) · the data (S006, R) · Data + Domain's recent report (S013) | Phúc trình quý 4/2024 (S005) · dữ liệu (S006) · Dữ liệu từ Domain (S012) | EN 2 L + 1 R; VI 2 L (S006 — liên tưởng, conf low; S012) |
| I. quý | the December quarter (S005, S017) · over the quarter (S010) · the final quarter of 2024 (S020) · the quarter (S030) | quý 4/2024 (S005) · trong quý (S010) · quý 4 (S016, S028) · quý cuối năm 2024 (S020) | EN 3: S017, S020, S030; VI 3: S016, S020, S028 (S010 hai bên không đánh dấu, §6.1) |
| J. thủ phủ – thành phố | the combined capitals (S005) · the only capital city (S010) · all capital cities (S029) · at a capital level (S031) · major cities (S035) | các thủ phủ (S027) · các thành phố lớn (S033) | EN 2: S029, S035; VI 1: S033 (VI cắt mệnh đề S010 nên "thủ phủ" không có tiền trạm) |
| K. khu vực – suburb | the suburbs (S001) · Queensland suburbs (S014) · a popular suburb (S015) · the ACT suburb (S032) | Những khu vực (S001) · khu vực (S013, S030) | EN 2: S014, S032; VI 2: S013, S030 |
| L. nguồn cung | an increase in housing stock (S005) · homes for sale (S005) · Increased supply (S035) | Nguồn cung (S033 — không có tiền trạm vì VI cắt nửa sau S005) | EN 1: S035; VI 0 |
| M. lãi suất | interest rate adjustments (S034) · rate-lifting cycle (S040) | điều chỉnh lãi suất (S032) · giảm lãi suất (S038) | EN 1: S040; VI 1: S038 (lệch nghĩa tăng/giảm, §8d) |
| N. khung mở–đóng | an "interesting" one (S002) ↔ an interesting year (S038) · the scales be tipped (S003) ↔ tip the scales (S034) · property market (S002) ↔ the market overall (S034) | một năm thú vị (S002 ↔ S036) · cho người mua nhà trong năm nay (S003 ↔ S032) · thị trường địa ốc (S002 ↔ S032) · giá nhà giảm mạnh nhất (S001 ↔ S005) | EN 3: S034 ×2, S038; VI 4: S005, S032 ×2, S036 |
| O. tên riêng + khác | Domain (S005, S006, S013) · Sydney (S011, S012, S022) · Melbourne (S017 ×2, S019, S023) · Hobart/Canberra/Gold Coast/Queensland/Victoria/ACT · các suburb · RBA · seen/experienced/recorded/witnessed ↔ chứng kiến/ghi nhận (verba dicendi + light verbs) · Weak conditions (S039) ↔ Các điều kiện yếu (S037) | tương tự (Sydney S010 ×2, S011, S012; Melbourne S016 ×2, S019, S020; Domain S005, S006, S012) | không (tên riêng lặp dày/kề nhau; light verbs tản mát; "conditions/điều kiện" lần đầu) |

### 6.3. Các hàng L ghi vào tie table

**EN — 49 hàng** (câu | dạng | kiểu | tiền trạm):
S004 Australia's housing market, đồng nghĩa ← S002 Australia's property market
· S004 property values, đồng nghĩa ← S001 home prices · S005 home prices, lặp
← S001 home prices … the biggest falls (echo dek → thân bài) · S006 buyer
behaviour, lặp ← S003 buyers (biến thể thêm danh hạt) · S006 demand, lặp ←
S004 shifting demand (rút gọn, gap 2) · S009 rising prices, lặp ← S005 home
prices have fallen (biến thể 'rising', trái nghĩa rising↔fallen) · S009
affordability pressures, lặp ← S004 affordability pressures (lượt lời Powell)
· S010 house prices, lặp ← S005 home prices ('home'→'house', sau khối trích
dẫn) · S011 Australia's most expensive housing market, lặp ← S004 Australia's
housing market (thêm định ngữ, tại subhead Sydney) · S012 back-to-back
quarterly decline, đồng nghĩa ← S010 the second consecutive decline · S013
Data, lặp ← S006 the data (gap 7) · S013 Domain's recent report, lặp ← S005
Domain's house price report (rút gọn, gap 8) · S013 median prices, lặp ← S010
house prices … a median of $1,645,444 (ghép mới) · S014 Gold Coast prices take
a dip, lặp ← S013 median prices … decreasing (S010 decline) — subhead mục Gold
Coast: 'prices' tái lập + 'take a dip' biến thể chuỗi giảm · S014 suburbs, lặp
← S001 the suburbs (gap 13) · S015 more affordable, đồng nghĩa ← S013 more
accessible · S017 unit prices, lặp ← S013 units … median prices (S016 house
prices) — tổ hợp mới tại subhead Melbourne · S017 the December quarter, lặp ←
S005 the December quarter (gap 12; alt 'R: the') · S018 Powell said, lặp ←
S008 Powell said (attribution, gap 10) · S018 the unit price growth, đồng nghĩa
← S017 their strongest quarterly increase ('unit price' lặp kề; alt 'R: the')
· S020 Powell said, lặp ← S018 Powell said (gap 2) · S020 growth, lặp ← S018
the unit price growth (rút gọn, trong lời Powell) · S020 the final quarter of
2024, đồng nghĩa ← S017 the December quarter · S021 first-home buyers, lặp ←
S018 first-home buyer activity (gap 3) · S021 value, lặp ← S004 property
values (gap 17) · S022 price cycles, lặp ← S017 unit prices … house prices
increase (biến thể 'cycles') · S024 housing affordability, lặp ← S015 more
affordable (gap 9) · S024 unit prices, lặp ← S018 the unit price growth
(gap 6) · S026 house prices, lặp ← S017 house prices increase (tái lập sau
9 câu) · S028 the median house price, lặp ← S026 house prices (thêm 'median')
· S028 Victorian town, lặp ← S026 the Victorian seaside town (gap 2) · S029
unit prices, lặp ← S024 unit prices (gap 5, tại subhead Hobart–Canberra) ·
S029 capital cities, lặp ← S010 the only capital city (gap 19, đơn↔số nhiều)
· S030 house prices, lặp ← S028 the median house price (gap 2) · S030 the
quarter, lặp ← S020 the final quarter of 2024 (rút gọn, gap 10; alt 'R: the')
· S031 Canberra's housing market, lặp ← S011 Australia's most expensive
housing market (gap 20) · S032 the median, lặp ← S028 the median house price
(rút gọn, gap 4; alt 'R: the') · S032 suburb, lặp ← S015 a popular suburb
(gap 17) · S033 buyer's market, lặp ← S031 Canberra's housing market (tổ hợp
mới tại subhead, gộp chuỗi buyers S020) · S034 the market overall, lặp ← S002
Australia's property market (rút gọn — khung mở/đóng; alt 'R: the') · S034
annual growth, lặp ← S020 growth (gap 14) · S034 affordability, lặp ← S024
housing affordability (gap 10) · S034 tip the scales in favour of buyers, lặp
← S003 Could the scales be tipped in favour of buyers? (idiom, gap 31 — khung
đóng) · S035 Increased supply, đồng nghĩa ← S005 an increase in housing stock
(gap 30) · S035 major cities, đồng nghĩa ← S029 all capital cities · S035
negotiate on price, lặp ← S032 drop in house prices (rút gọn 'price', gap 3)
· S037 Powell, lặp ← S020 Powell said (attribution, gap 17) · S038 an
interesting year, lặp ← S002 an "interesting" one (từ khóa 'interesting' +
'year', gap 36 — khung đóng) · S040 rate-lifting cycle, lặp ← S034 interest
rate adjustments ('rate' lặp, gap 6; lệch nghĩa §8d).

**VI — 43 hàng** (câu | dạng | kiểu | tiền trạm):
S004 Thị trường nhà ở Úc, đồng nghĩa ← S002 thị trường địa ốc Úc · S004 giá
nhà, lặp ← S001 giá nhà giảm mạnh nhất (từ khóa headline) · S005 giá nhà giảm
mạnh nhất, lặp ← S001 giá nhà giảm mạnh nhất (lặp nguyên cụm — echo headline →
thân bài) · S006 dữ liệu, liên tưởng (collocation) ← S005 Phúc trình quý 4/2024
của Domain (conf low; EN đối ứng R bridging 'the data') · S006 người mua nhà,
lặp ← S003 người mua nhà (gap 3) · S007 nhu cầu, lặp ← S004 sự thay đổi nhu
cầu (mở trích dẫn, lượt lời mới) · S009 áp lực giá nhà, lặp ← S004 áp lực tài
chính (cùng hạt 'áp lực', đổi định ngữ — VI dịch "affordability" hai cách) ·
S009 giá cả, lặp ← S005 giá nhà (biến thể 'giá cả') · S010 Giá nhà Sydney
giảm, lặp ← S005 giá nhà giảm mạnh nhất (tái lập tổ hợp 'giá nhà…giảm' tại
subhead mở mục Sydney) · S010 thị trường nhà ở đắt đỏ nhất nước Úc, lặp ← S004
Thị trường nhà ở Úc (thêm định ngữ) · S012 Dữ liệu từ Domain, lặp ← S006 dữ
liệu (gap 6) · S012 giá căn hộ, lặp ← S010 giá nhà (biến thể mới 'căn hộ') ·
S013 Giá nhà Gold Coast hạ nhiệt, lặp ← S010 Giá nhà Sydney giảm (subhead đối
song — phép đối: lặp 'Giá nhà' + thế 'giảm'↔'hạ nhiệt') · S013 khu vực, lặp ←
S001 Những khu vực (từ khóa headline, gap 12) · S016 Giá căn hộ, lặp ← S012
giá căn hộ (gap 4, tại subhead Melbourne) · S016 quý 4, lặp ← S005 quý 4/2024
(gap 11) · S017 Giá nhà, lặp ← S011 sụt giảm giá nhà (tái lập 'giá nhà' sau
6 câu) · S018 Bà Powell, lặp ← S006 bà Nicola Powell (attribution, gap 12) ·
S020 sự tăng trưởng, đồng nghĩa ← S018 sự gia tăng (gap 2) · S020 bà Powell
nhận xét, lặp ← S018 Bà Powell (attribution, gap 2) · S020 quý cuối năm 2024,
lặp ← S016 quý 4 (biến thể, gap 4) · S021 người mua nhà lần đầu, lặp ← S018
những người mua nhà lần đầu (gap 3, trong lời Powell) · S021 giá trị, lặp ←
S004 giá nhà (gia đình hình thái 'giá', gap 17) · S022 khả năng chi trả nhà ở,
lặp ← S009 việc chi trả (biến thể, gap 13) · S022 giá căn hộ, lặp ← S016 Giá
căn hộ (gap 6) · S024 giá nhà, lặp ← S017 Giá nhà (gap 7) · S026 giá nhà trung
bình, lặp ← S024 giá nhà (thêm 'trung bình', gap 2) · S027 giá căn hộ, lặp ←
S023 giá căn hộ (gap 4, tại subhead Hobart–Canberra) · S028 giá nhà, lặp ←
S026 giá nhà trung bình (gap 2) · S028 quý 4, lặp ← S020 quý cuối năm 2024
(gap 8) · S029 thị trường Canberra, lặp ← S020 Thị trường ở đây ('thị trường',
gap 9) · S030 khu vực, lặp ← S013 khu vực (gap 17) · S031 thị trường, lặp ←
S029 thị trường Canberra (tại subhead, gap 2) · S031 người mua nhà, lặp ← S021
người mua nhà lần đầu (gap 10, tại subhead) · S032 thị trường địa ốc, lặp ←
S002 thị trường địa ốc Úc (lặp nguyên tổ hợp, gap 30 — khung mở/đóng) · S032
mức tăng trưởng hàng năm, lặp ← S021 Sự tăng trưởng (gap 11) · S032 khả năng
chi trả, lặp ← S022 khả năng chi trả nhà ở (rút gọn, gap 10) · S032 cho người
mua nhà trong năm nay, lặp ← S003 cho người mua nhà trong năm nay (lặp nguyên
cụm, gap 29 — khung đóng; VI lược idiom 'scales') · S033 các thành phố lớn,
đồng nghĩa ← S027 các thủ phủ · S033 thương lượng về giá, lặp ← S030 giá nhà
(rút gọn 'giá', gap 3) · S035 Theo bà Powell, lặp ← S020 bà Powell nhận xét
(attribution, gap 15) · S036 một năm thú vị, lặp ← S002 "một năm thú vị" (lặp
nguyên cụm, gap 34 — khung đóng) · S038 lãi suất, lặp ← S032 điều chỉnh lãi
suất (gap 6; lệch nghĩa §8d).

### 6.4. Nhận định

- **L-EN (49) > L-VI (43)** — ngược P17 (VI đậm hơn): VI cắt khối S022–S023,
  nửa sau S005 và nhiều định ngữ ("recent report", "median", "Victorian",
  "ACT", "year-on-year", "at a capital level") nên mất các điểm tái lập chuỗi
  (nguồn cung, Victorian town, the median, capital cities chỉ còn phía EN).
- **Trường giá (chuỗi A) là xương sống**: EN 15 mark / VI 14 mark, xuất hiện
  gần như mỗi câu của mỗi mục — thể loại listicle thống kê giá nhà; chính sách
  §6.1 (bỏ lặp kề) giữ số mark ở mức có thể đọc được thay vì đánh dấu mọi câu.
- **Hội tụ – phân rã khi dịch**: EN phân rã ở "affordability" ↔ VI tách thành
  áp lực tài chính / áp lực giá nhà / khả năng chi trả (3 nhánh); ngược lại VI
  hội tụ mọi biến thể EN về hạt "giá" (giá nhà / giá cả / giá căn hộ / giá trị /
  giá bất động sản). EN "the city's" (R) ↔ VI lặp tên "Sydney".
- **Khung mở–đóng là điểm nhấn liên kết cấp diễn ngôn**: "interesting one" ↔
  "an interesting year" (S002↔S038) / "một năm thú vị" (S002↔S036);
  "tip the scales in favour of buyers" (S003↔S034) ↔ VI khung riêng "cho người
  mua nhà trong năm nay" (S003↔S032); "property market" ↔ "the market
  overall"/"thị trường địa ốc" (S002↔S034/S032); VI thêm khung "giá nhà giảm
  mạnh nhất" (S001↔S005).
- Số đếm L phụ thuộc trực tiếp chính sách §6.1: "over the quarter/trong quý"
  (S010), "at a capital level" (S031), "sharpest decline" (S029), "houses
  prices" (S015), "sự cải thiện/improvement" (S024/S022), "Weak conditions/Các
  điều kiện yếu" nằm trong kho §6.2 nhưng không đánh dấu.

### 6.4. Bổ sung L theo chính sách v2 (2026-11-05)

Theo chỉ thị giảng viên (phân tích kỹ hơn, đánh dấu nhiều hơn), chính
sách L được nới rộng (CONVENTIONS §8.1 v2): lặp cùng dạng kể cả câu kề,
từ đơn có nội dung thực, chuỗi động từ attribution, tái lập tại điểm nối
diễn ngôn. Kho chuỗi §6.2 được rà lại; các hàng L mới là quyết định đọc
hiểu tay (không regex/word-list), mỗi hàng 1 mark/câu/chuỗi, ante luôn
nằm trước. Danh sách hàng bổ sung (đối soát 2 cổng QC PASS):

Phía EN — 56 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S005 | fallen | repetition | S001: the biggest falls |
| 2 | S005 | housing stock | repetition | S004: Australia's housing market |
| 3 | S006 | Domain's | repetition | S005: this week's Domain's house price report |
| 4 | S006 | fall | repetition | S005: home prices have fallen the most |
| 5 | S006 | economics | repetition | S002: an economist |
| 6 | S007 | buyer demand | repetition | S006: buyer behaviour |
| 7 | S008 | demand | repetition | S007: a pullback in buyer demand |
| 8 | S008 | people | general word | S007: a pullback in buyer demand |
| 9 | S008 | Powell said | repetition | S006: Nicola Powell |
| 10 | S009 | buyers | repetition | S003: in favour of buyers |
| 11 | S010 | dropped | synonym | S005: home prices have fallen the most |
| 12 | S010 | the quarter | repetition | S005: the December quarter |
| 13 | S010 | the only capital city | repetition | S005: across the combined capitals |
| 14 | S011 | slows down | synonym | S010: marking the second consecutive decline |
| 15 | S012 | Sydney | repetition | S011: Sydney slows down Sydney remains… |
| 16 | S013 | shows | repetition | S006: the data shows |
| 17 | S013 | suburb | repetition | S001: the suburbs |
| 18 | S013 | decreasing | synonym | S012: back-to-back quarterly decline |
| 19 | S014 | experienced | repetition | S012: Sydney has experienced |
| 20 | S015 | a popular suburb | repetition | S014: Some Queensland suburbs |
| 21 | S015 | Gold Coast | repetition | S014: Gold Coast prices take a dip |
| 22 | S015 | houses prices | repetition | S010: house prices |
| 23 | S015 | decrease | repetition | S013: decreasing by 22.1 per cent |
| 24 | S016 | house prices | repetition | S015: houses prices |
| 25 | S016 | fall | repetition | S006: a fall in demand |
| 26 | S016 | has seen | repetition | S007: What we have seen |
| 27 | S017 | First-home buyers | repetition | S009: many buyers |
| 28 | S017 | strongest quarterly increase | repetition | S005: an increase in housing stock |
| 29 | S018 | first-home buyer activity | repetition | S017: First-home buyers |
| 30 | S019 | Melbourne | repetition | S017: Melbourne unit prices |
| 31 | S020 | a market | repetition | S011: Australia's most expensive housing market |
| 32 | S020 | saw | repetition | S016: has seen house prices fall |
| 33 | S022 | Sydney | repetition | S012: Sydney has experienced |
| 34 | S022 | Melbourne | repetition | S019: Melbourne has been the surprise |
| 35 | S022 | see | repetition | S020: we saw growth |
| 36 | S023 | Melbourne | repetition | S022: Sydney and Melbourne price cycles |
| 37 | S024 | dropping | repetition | S010: dropped by 0.1 per cent |
| 38 | S024 | year-on-year | repetition | S015: year-on-year decrease |
| 39 | S024 | has seen | repetition | S022: tend to see |
| 40 | S025 | experienced | repetition | S014: have also experienced |
| 41 | S025 | a fall | repetition | S016: house prices fall |
| 42 | S025 | a median unit price | repetition | S024: unit prices |
| 43 | S026 | dropped | repetition | S024: dropping by 33.3 per cent |
| 44 | S027 | markets | repetition | S020: as a market |
| 45 | S028 | decline | repetition | S025: an 18.9 per cent decline |
| 46 | S029 | recorded | repetition | S010: to record a decline |
| 47 | S029 | the sharpest decline | repetition | S028: a 19.6 per cent decline |
| 48 | S030 | surged | synonym | S017: house prices increase 1.6 per cent |
| 49 | S031 | unit prices | repetition | S029: unit prices |
| 50 | S031 | at a capital level | repetition | S029: among all capital cities |
| 51 | S032 | recorded | repetition | S029: Hobart recorded |
| 52 | S032 | drop | repetition | S026: dropped 20.5 per cent |
| 53 | S034 | has seen | repetition | S024: Chadstone has seen |
| 54 | S040 | see | repetition | S034: has seen annual growth slow |
| 55 | S040 | the change | repetition | S027: these changes |
| 56 | S040 | Australia | repetition | S011: Australia's most expensive housing market |


Phía VI — 55 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S002 | Úc | repetition | S001: tại Úc |
| 2 | S002 | năm 2025 | repetition | S001: trong năm 2024 |
| 3 | S003 | năm nay | repetition | S002: năm 2025 |
| 4 | S005 | trên toàn quốc | repetition | S004: trên toàn quốc |
| 5 | S005 | những nơi | general word | S001: Những khu vực |
| 6 | S006 | kinh tế | repetition | S002: nhà kinh tế học |
| 7 | S006 | Domain | repetition | S005: của Domain |
| 8 | S006 | phản ảnh | synonym | S005: đã tiết lộ |
| 9 | S006 | sự thay đổi | repetition | S004: sự thay đổi nhu cầu |
| 10 | S007 | người mua | repetition | S006: người mua nhà |
| 11 | S007 | giảm | repetition | S005: giảm mạnh nhất |
| 12 | S008 | nhu cầu | repetition | S007: nhu cầu của người mua |
| 13 | S009 | người mua | repetition | S007: người mua |
| 14 | S010 | trong quý | repetition | S005: quý 4/2024 |
| 15 | S011 | Sydney | repetition | S010: Giá nhà Sydney giảm |
| 16 | S011 | sụt giảm | synonym | S010: đã giảm 0,1% |
| 17 | S011 | hai quý | repetition | S010: trong quý |
| 18 | S012 | cho thấy | synonym | S006: dữ liệu phản ảnh |
| 19 | S012 | Sydney | repetition | S011: Sydney |
| 20 | S012 | giảm | repetition | S011: sụt giảm |
| 21 | S013 | sự thay đổi lớn | repetition | S006: sự thay đổi |
| 22 | S014 | giá nhà | repetition | S013: Giá nhà Gold Coast hạ nhiệt |
| 23 | S014 | giảm | repetition | S012: đã giảm 22,1% |
| 24 | S015 | giá nhà | repetition | S014: giá nhà |
| 25 | S015 | giảm | repetition | S014: giảm 22,4% |
| 26 | S016 | Người mua nhà lần đầu | repetition | S009: nhiều người mua |
| 27 | S016 | tăng mạnh nhất | repetition | S009: giá cả tăng cao |
| 28 | S017 | tăng | repetition | S016: tăng mạnh nhất |
| 29 | S018 | cho rằng | synonym | S008: bà nói |
| 30 | S018 | người mua nhà lần đầu | repetition | S016: Người mua nhà lần đầu |
| 31 | S019 | Melbourne | repetition | S016: ở Melbourne |
| 32 | S020 | hoạt động | repetition | S018: hoạt động tích cực |
| 33 | S020 | ghi nhận | repetition | S013: ghi nhận |
| 34 | S021 | phản ảnh | repetition | S006: dữ liệu phản ảnh |
| 35 | S022 | chứng kiến | repetition | S011: Sydney chứng kiến |
| 36 | S022 | giảm | repetition | S015: giảm 21,1% |
| 37 | S023 | trải qua | repetition | S004: đang trải qua |
| 38 | S023 | giá căn hộ | repetition | S022: giá căn hộ |
| 39 | S024 | giảm | repetition | S022: giảm 33,3% |
| 40 | S025 | Các thị trường nhỏ hơn | repetition | S020: Thị trường ở đây |
| 41 | S026 | thị trấn | repetition | S024: thị trấn ven biển |
| 42 | S026 | giảm | repetition | S024: giảm 20,5% |
| 43 | S027 | giảm 1,5% | repetition | S026: giảm 19,6% |
| 44 | S028 | tăng | repetition | S020: sự tăng trưởng |
| 45 | S029 | căn hộ | repetition | S027: giá căn hộ |
| 46 | S030 | giảm | repetition | S027: giảm 1,5% |
| 47 | S031 | năm 2025 | repetition | S002: năm 2025 |
| 48 | S032 | chứng kiến | repetition | S022: Chadstone chứng kiến |
| 49 | S033 | gia tăng | synonym | S032: mức tăng trưởng hàng năm |
| 50 | S036 | Năm 2025 | repetition | S031: năm 2025 |
| 51 | S037 | điều kiện | repetition | S032: tạo điều kiện thuận lợi |
| 52 | S037 | tích lũy | repetition | S021: giá trị tích lũy |
| 53 | S037 | năm 2024 | repetition | S020: quý cuối năm 2024 |
| 54 | S038 | thay đổi | repetition | S025: những thay đổi này |
| 55 | S038 | thấy | repetition | S007: chúng tôi thấy |

Số đếm §9 dưới đây đã gộp toàn bộ phần bổ sung này. Các kết luận §6.5
(nếu có) của bản pilot về "chọn lọc lặp kề" không còn áp dụng — thay
bằng chính sách v2.

## 7. Các dịch chuyển liên kết nổi bật (tổng hợp)

| Kiểu dịch chuyển | Số lần | Ví dụ nguyên văn |
|---|---:|---|
| EN tên trong attribution → VI đại từ (L→R) | 1 | EN S008 "…,\" Powell said." ↔ VI S008 "…," bà nói." |
| EN đại từ attribution → VI tên (R→L) | 1 | EN S038 "\"2025 is going to be an interesting year,\" she said." ↔ VI S036 "…," bà nói" (đối ứng tên ở S035 "Theo bà Powell" — hàng L) |
| EN danh từ tổng quát → VI đại từ (L→R) | 1 | EN S008 "it means people delay their decisions" ↔ VI S008 "họ chỉ đang trì hoãn việc ra quyết định" |
| EN đại từ "it" [TC] → VI ∅ chủ ngữ (R→E, cả hai [TC]) | 1 | EN S039 "and that is going to flow into…" ↔ VI S037 "và ∅ sẽ ảnh hưởng đến đầu năm 2025" |
| EN "the city's" (R) → VI lặp tên "Sydney" (không đánh dấu, kề) | 1 | EN S013 "the city's inner northern suburb of Crows Nest" ↔ VI S012 "Crows Nest phía bắc Sydney" |
| EN "it" tiến chỉ (S010) → VI nêu tên Sydney trước (R→L cấu trúc) | 1 | EN S010 "making it the only capital city…" ↔ VI S010 "Sydney vẫn là… nhưng giá nhà tại đây…" |
| EN đại từ thuần → VI danh ngữ chỉ từ + danh từ (R→R, đổi dạng) | 3 | EN S020 "It's underperformed" ↔ VI "Thị trường ở đây"; EN S021 "This reflects" ↔ VI "Sự tăng trưởng này phản ảnh"; EN S037 "it depends" ↔ VI "điều này còn phụ thuộc" |
| EN thế "one" [TC] → VI hiện thực hóa | 1 | EN S002 "an \"interesting\" one" ↔ VI S002 "một năm thú vị" |
| EN nối [LC] → VI nối [TC] (mất hàng) | 1 | EN S010 "But house prices dropped…" ↔ VI S010 "…đắt đỏ nhất nước Úc, nhưng giá nhà tại đây đã giảm…" |
| EN nối [TC]/ngầm → VI nối [LC] tự sinh | 2 | EN S017 "while house prices increase…" ↔ VI S017 "Giá nhà cũng tăng 1,6%…"; EN S031 (không liên từ) ↔ VI S029 "Trong khi đó, thị trường Canberra giữ nguyên…" |
| Khung mở–đóng giữ 1–1 | 3 | "interesting one" (S002) ↔ "an interesting year" (S038) / "một năm thú vị" (S002↔S036); "the scales be tipped in favour of buyers" (S003) ↔ "tip the scales in favour of buyers" (S034), VI thay bằng khung riêng "cho người mua nhà trong năm nay" (S003↔S032); "Australia's property market" (S002) ↔ "the market overall" (S034) / "thị trường địa ốc" (S002↔S032) |
| VI explicitation | 3 | EN S002 "This year" → VI "năm 2025"; EN S037 "it depends" → VI "điều này còn phụ thuộc vào một số yếu tố"; EN S010 (Sydney ẩn trong "it") → VI S010 nêu "Sydney" |
| VI cắt khối câu | 1 (2 câu) | EN S022–S023 (cả para 17: "You tend to see Sydney and Melbourne price cycles… established recovery") — VI không có gì tương ứng |
| VI cắt nửa câu → mất chuỗi một phía | 4 | EN S005 "an increase in housing stock … homes for sale" (chuỗi nguồn cung chỉ EN); EN S010 "the only capital city to record a decline" (chuỗi thủ phủ VI không có tiền trạm); EN S024 "year-on-year" (tiền trạm "cùng giai đoạn" VI phải mô tả); EN S032 "bringing the median to" (mất "the median" VI) |
| VI tách/gộp câu đổi cấp [TC]↔[LC] | 2 | EN S017 (1 câu, "the same period" [TC]) → VI S016+S017 (2 câu, "cùng giai đoạn" [LC]); EN S010+S011 (2 câu, "it" [LC] tiến chỉ) → VI S010 (1 câu, "tại đây" [TC] không đánh dấu) |
| Lệch nghĩa khi dịch (ghi nhận, không phải lỗi tie) | 1 | EN S040 "a rate-lifting cycle from the RBA" ↔ VI S038 "RBA giảm lãi suất" (tăng ↔ giảm, §8d) |

## 8. Bất thường dữ liệu nguồn (cần ghi chú khi thống kê)

- **(a) Lỗi chính tả EN S015:** "with houses prices at $660,000" — thiếu dấu
  sở hữu/số ít (đúng phải là "house prices"); vị trí này không phát sinh hàng
  tie (lặp kề trong mục Gold Coast) nên không ảnh hưởng; giữ nguyên văn khi
  trích.
- **(b) Hàng dek EN S001 là hàng đầu body:** "State-by-state: These are the
  suburbs…" — theo CONVENTIONS §1 đọc như hàng body bình thường. "These" không
  có tiền trạm trước nó trong flow; cách đọc chốt: tiến chỉ (ref=C) tới danh
  sách khu vực ở phần thân (S013 Crows Nest, S015 Biggera Waters, S024
  Chadstone, S032 Denman Prospect…), conf low, khả năng đọc ngoại văn bản
  (danh sách trong phúc trình Domain) ghi `alt`. Tiêu đề [TD] "Revealed:
  Australian suburbs with the biggest home price falls" không nằm trong flow,
  chỉ so sánh định tính.
- **(c) TT S001 là headline VI trùng `title_vi`:** "Những khu vực có giá nhà
  giảm mạnh nhất tại Úc trong năm 2024" — vừa là tiêu đề vừa là hàng đầu flow
  TT; đọc như hàng body (không có tie nào; là tiền trạm của chuỗi "giá nhà giảm
  mạnh nhất"/"khu vực"). Không dùng tiêu đề làm bằng chứng cấp câu.
- **(d) Lệch nghĩa EN S040 ↔ VI S038:** EN "when we start to see a rate-lifting
  cycle from the RBA" (chu kỳ TĂNG lãi suất) ↔ VI "khi chúng ta bắt đầu thấy
  RBA giảm lãi suất" (GIẢM lãi suất) — bối cảnh đầu 2025 RBA được dự báo cắt
  lãi suất; một trong hai phía sai hướng. Hàng L hai phía ("rate-lifting
  cycle"/"lãi suất") vẫn ghi vì quan hệ từ vựng 'rate/lãi suất' là thật; ghi
  chú lệch nghĩa trong note; không dùng làm bằng chứng cho chiều hướng lãi suất.
- **(e) Thứ tự đoạn bất thường quanh S010–S011 (EN):** câu số liệu Sydney
  ("But house prices dropped… making it the only capital city…") đứng TRƯỚC
  subhead "Sydney slows down" (S011) — artifact của cách dàn trang/nạp bài gốc
  (câu này thuộc mục Sydney). Hệ quả: "it" (S010) chỉ đọc được hướng tiến chỉ
  (ref=C, conf low). VI sửa bằng cách gộp hai câu và nêu "Sydney" trước. Không
  dùng S010/S011 (EN) làm bằng chứng cho quan hệ hồi quy thông thường.
- **(f) VI cắt trọn khối EN S022–S023:** `rows.json` có 1 hàng `"vi": ""`, para
  17 trong `TT_seg.json` rỗng — artifact của khối cắt, không phải câu; hai bên
  biên rỗng này không dùng làm bằng chứng cấp câu phía VI. Hệ quả: R-EN9
  ("those two movements in price") và L-EN (S022 "price cycles") không có đối
  ứng VI.
- **(g) Subhead dính body trong 1 hàng sentmap (cả hai phía):** EN S011/S014/
  S017/S029/S033 và VI S010/S013/S016/S027/S031 đều có dạng "Subhead + câu
  body" nối nhau không có dấu câu — đọc subhead như phần đầu hàng body
  (CONVENTIONS §1); các mark tại các hàng này lấy text của subhead hoặc của
  body tùy vị trí chuỗi.
- **(h) Lỗi chính tả VI:** S022 "33,3%xuống" (thiếu dấu cách — không nằm trong
  text đã đánh dấu "giá căn hộ"); "phản ảnh" (S006, S021 — chuẩn là "phản ánh");
  không ảnh hưởng tie.
- **(i) VI tự sinh/lược rải rác (không phải lỗi):** VI tự sinh "cũng" (S017),
  "Trong khi đó" (S029), "một số yếu tố" (S035); VI lược "Regional" (S027→
  S025), "Victorian" (S026→S024), "ACT" + "at a capital level" (S031–S032→
  S029–S030), "year-on-year" (S024→S022), "a popular suburb on the Gold Coast"
  (S015→S014), "(Reserve Bank of Australia)" (S040); EN S005 "this week's
  Domain's house price report" — sở hữu kép gượng gạo của nguồn.
- **(j) Segmenter:** không có trường hợp chẻ câu tại dấu viết tắt (U.S./Mr./Jr.)
  trong cặp này; "per cent" luôn viết nguyên vẹn; các cặp câu trong cùng trích
  dẫn (S007–S008, S019–S020, S022–S023, S039–S040 EN) là câu thật (dấu chấm
  thật trong lời trích), quyết định [LC]/[TC] lấy theo câu thật.

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table (cập nhật v2 2026-11-05)

| Chỉ số | Phân tích | Tie table | Ghi chú |
|---|---:|---:|---|
| EN — R | 16 | 16 | §4 |
| EN — S | 1 | 1 | §3 |
| EN — C | 10 | 10 | §5 |
| EN — E | 0 | 0 | §2 |
| EN — L | 105 | 105 | §6 (pilot 49 + v2 56) |
| VI — R | 15 | 15 | §4 |
| VI — S | 0 | 0 | §3 |
| VI — C | 11 | 11 | §5 |
| VI — E | 1 | 1 | §2 |
| VI — L | 98 | 98 | §6 (pilot 43 + v2 55) |

- Tổng tie: EN **132** / VI **125** (pilot: EN 76 / VI 70).
- Bổ sung v2 (56 EN + 55 VI hàng) theo chỉ thị giảng viên
  2026-11-05 (CONVENTIONS §8.1 v2): lặp câu kề, từ đơn nội dung, động từ
  attribution; đã PASS 2 cổng QC `pipeline.annotate` + `pipeline.render`.
- Liên kết từ vựng giữ vai trò chủ lực: L-EN 105 (80%),
  L-VI 98 (78%).
- L-EN (105) > L-VI (98): bản EN phân tán chuỗi từ vựng
  (biến thể/đại từ thay thế) trong khi VI hội tụ lặp danh từ.
- Quy chiếu EN 16 / VI 15 (EN ưa đại từ, VI ưa danh ngữ lặp);
  tỉnh lược EN 0 / VI 1; thế EN 1 / VI 0;
  nối EN 10 / VI 11.
- Các hàng chỉ [TC] không dùng làm bằng chứng cho kết luận liên kết liên câu.
