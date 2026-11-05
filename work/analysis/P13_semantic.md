# P13 — Phân tích ngữ nghĩa liên kết (COHESION BEYOND THE SENTENCE LEVEL)

> **Khung:** EN — Halliday & Hasan (1976): reference, substitution, ellipsis,
> conjunction, lexical cohesion. VI — Trần Ngọc Thêm (1985; 2006, dẫn theo
> Nguyễn Thanh Tùng 2020): phép lặp, phép đối, phép thế đẳng nghĩa, phép liên
> tưởng, phép tuyến tính; phép thế đại từ (khiếm diện/dự báo/hồi quy), phép tỉnh
> lược, phép nối. Mã R/S/E/C/L theo `references/en-vi-mapping.md`.
> **Quy ước:** `[LC]` liên câu (đơn vị chính); `[TC]` trong câu (lớp bổ sung
> cho S/E); `[TD]` tiêu đề (chỉ nói ở §8, không đánh dấu). `∅` = lược; `{…}` = hồi phục.

**ST (EN):** *Seoul working for pope visit to N.Korea, Vatican agency says* — Reuters, 8/7/2021 (13 câu S001–S013; tiêu đề lấy từ dòng standalone, không nằm trong flow).
**TT (VI):** *Hàn Quốc tìm cách thu xếp cho chuyến thăm của Giáo hoàng tới Triều Tiên* — VOA Tiếng Việt (8 câu S001–S008).

---

## 1. Tổng quan nội dung, thể loại, bản đồ câu

**Thể loại/nguồn:** tin quốc tế ngắn (news brief) về ngoại giao – tôn giáo:
nỗ lực thu xếp chuyến thăm Triều Tiên của Giáo hoàng Francis do giám đốc cơ
quan tình báo Hàn Quốc Park Jie-won công bố qua hãng tin Fides. Cấu trúc: lede
thông báo (S001) → nền tôn giáo Triều Tiên (S002–S003) → chi tiết nguồn Fides
(S004–S005) → định danh Park (S006) → kiểm chứng độc lập (S007–S008) → nền
2018 (Moon – Kim Jong Un – Vatican, S009–S013). EN 13 câu; VI 8 câu: VI cắt
toàn bộ khối nền 2018 (rows 9–11 của `rows.json` có `vi` rỗng) — không có câu
VI tự sinh, không có gộp/tách: khối dùng chung ánh xạ 1–1.

**Các chuỗi/trường nghĩa chi phối liên kết:** (i) chuyến thăm Giáo hoàng
(visit/trip ↔ chuyến thăm); (ii) chuỗi Triều Tiên (North Korea / the reclusive
state / Pyongyang / North Korean / the two Koreas ↔ Triều Tiên / Bình Nhưỡng);
(iii) chuỗi Hàn Quốc (outh Korea's / South Korea / Seoul / South Korean ↔ Hàn
Quốc / Seoul); (iv) chuỗi Giáo hoàng (Pope Francis / a pope / papal / the pope
↔ Giáo hoàng Francis); (v) cơ quan tình báo (intelligence chief / National
Intelligence Service / intelligence agency ↔ cơ quan tình báo / Cơ quan Tình
báo Quốc gia); (vi) hãng tin nguồn (Catholic news agency / Fides ↔ hãng thông
tấn / Fides); (vii) thư mời (invitation); (viii) bình luận – xác nhận
(comments / confirmed ↔ bình luận / xác nhận); (ix) trường Công giáo (Catholic,
Mass, priests, faith, Vatican, Archbishop — phép liên tưởng); (x) verba
dicendi (said / told / cho biết / đưa tin / nói).

**Bản đồ câu ST ↔ TT** (giữ = dịch gần 1–1):

| ST | TT | Ghi chú |
|---|---|---|
| S001 | S001 | giữ; EN typo "outh Korea's" (mất chữ S, §8a); EN "he" [TC] ↔ VI "ông" [TC] (tiền trạm cùng câu) |
| S002 | S002 | giữ; EN "the reclusive state" (R) → VI lặp tên "Triều Tiên" (R→L); EN E "the first ∅" → VI lấp "lần đầu tiên" |
| S003 | S003 | giữ; EN "its citizens" (R) → VI "công dân Triều Tiên" (hiện thực hóa danh ngữ) |
| S004 | S004 | giữ; "on Monday" → "hôm 5/7" (§8c); "the announcement" (R) ↔ "thông báo này" (R) |
| S005 | S005 | giữ; EN "a possible papal visit to Pyongyang" → VI "khả năng Giáo hoàng Francis tới Bình Nhưỡng" (danh từ → mệnh đề; "papal" → tên riêng) |
| S006 | S006 | giữ; câu định danh Park (đối ứng hai bên đều là hàng L) |
| S007 | S007 | giữ; "On Thursday" → "Hôm 8/7" (§8c); EN chủ ngữ dùng chung qua "but" ↔ VI zero chủ ngữ vế tọa hợp [TC] |
| S008 | S008 | giữ; "The intelligence agency in Seoul" ↔ "Cơ quan tình báo ở Seoul" (L + L hai phía) |
| S009 | — | VI cắt (khối rỗng) |
| S010 | — | VI cắt |
| S011 | — | VI cắt |
| S012 | — | VI cắt |
| S013 | — | VI cắt |

## 2. Phép tỉnh lược (ellipsis)

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-EN1 | ST S002 | "…would be the first ∅ by a pope to the reclusive state" | tỉnh lược danh từ sau ordinal "the first"; hồi phục {visit} ← "Any visit" cùng câu (kiểu "two ∅" của H&H); VI lấp bằng tổ hợp "lần đầu tiên" (danh từ tổng quát "lần") — dịch chuyển EN E → VI hiện thực hóa | [TC] |
| E-VI1 | TT S007 | "…và ∅ đã xác nhận sự tham dự của ông nhưng ∅ không xác nhận…" | lược chủ ngữ vế tọa hợp sau "và" (zero kéo dài đến vế "nhưng"); hồi phục {một người} ← "một người đã trả lời…" cùng câu; đọc thêm *thế đại từ khiếm diện* (zero theo dõi nhân vật "một người" — vẫn một hàng E, CONVENTIONS §2); EN đối ứng dùng chủ ngữ dùng chung qua phối từ, không có khe ∅ theo H&H | [TC] |

**EN, các ứng viên đã kiểm tra và loại:**
- S007 "confirmed his attendance but would not confirm…" — chủ ngữ "a person"
  dùng chung cho cả vế "but" (phối thành phần, không phải tỉnh lược theo H&H);
  bất đối xứng với VI được giải thích bằng khung TNT (vế tọa hợp = tỉnh lược
  chủ ngữ) — xem §7;
- S012 "It was not clear…" — "It" là chủ ngữ hình thức (expletive), không
  quy chiếu, không phải tỉnh lược;
- S001 "he is working", S005 "he would meet", S007 "his" ×2 — đại từ, không
  phải zero.

**VI, các chỗ trống đã cân nhắc nhưng không đánh dấu:**
- S005 "để thảo luận về…" — cấu trúc mục đích với chủ ngữ điều khiển ("ông"),
  không phải khe ∅ đọc được;
- S002 "nơi không cho phép…" — chủ ngữ "nơi" hiện diện; S003 "họ" hiện diện;
- S002 "lần đầu tiên của một vị giáo hoàng…" — slot danh từ đã được lấp bằng
  "lần" (đối ứng với E-EN1), không có zero phía VI.

**Nhận định:** mỗi phía đúng 1 hàng E và cả hai đều [TC] — không có tỉnh lược
liên câu nào trong cặp này. Chiều EN→VI ở S002 là lấp đầy (E-EN ↔ từ vựng
"lần đầu tiên"); chiều VI→EN ở S007 là zero [TC] không có đối ứng hình thức
bên EN (EN dùng phối từ với chủ ngữ dùng chung).

## 3. Phép thế (substitution)

| # | Ngôn ngữ | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| — | — | — | không có phép thế nào ở cả hai phía | — |

**Các ứng viên gần đúng đã cân nhắc và loại:**
- EN S013 "such a trip" — "such" là determiner tổng quát hóa đứng cạnh danh
  từ đồng nghĩa mới "trip"; quan hệ trội là từ vựng (trip ↔ visit) → mã L
  (đồng nghĩa), khả năng "R: such" ghi vào `alt` (mapping §3.9, §2 quy tắc
  "the"); không phải thế vì không thay thế wording đủ điều kiện kiểu
  one/do/so/the same;
- EN S002 "the first" — xem §2: tỉnh lược (E), không phải thế;
- VI S002 "Bất kỳ… nào" — lượng từ, không phải pro-form; VI S002 "lần đầu
  tiên" — danh từ tổng quát lấp chỗ EN tỉnh lược, không phải thế;
- Không có "one/ones/do/so/not/the same" (EN) hay "như vậy/làm vậy/thế/vậy"
  (VI) nào trong văn bản.

**Nhận định:** cặp P13 không có phép thế — mọi chỗ "rỗng" về diễn đạt được EN
giải quyết bằng tỉnh lược (the first ∅) và VI giải quyết bằng hiện thực hóa từ
vựng (lần đầu tiên; công dân Triều Tiên). Đây là khác biệt loại hình rõ so với
P01 (nơi "do the same"/"làm như vậy" giữ pro-form hai phía).

## 4. Phép quy chiếu (reference)

### 4.1. Bảng quy chiếu EN (4 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-EN1 | S002 | the reclusive state | A | S001: North Korea | danh ngữ mô tả mới; "the" là liên kết duy nhất tại vị trí; VI đối ứng lặp tên "Triều Tiên" (R→L, lặp kề → không đánh dấu VI) |
| R-EN2 | S003 | its | A | S002: the reulsive state (North Korea) | "its citizens" = công dân Triều Tiên; VI hiện thực hóa "công dân Triều Tiên" |
| R-EN3 | S004 | the announcement | A | S001: nội dung phát biểu ("has said") | quy chiếu mở rộng (extended reference); danh từ "announcement" mới nên "the" là liên kết duy nhất; conf med |
| R-EN4 | S013 | They | A | S011: Vatican officials | [+người, số nhiều]; câu thuộc khối VI cắt (§8b) |

### 4.2. Bảng quy chiếu VI (1 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-VI1 | S004 | thông báo này | A | S001: nội dung phát biểu của Giám đốc cơ quan tình báo | demonstrative "này" + danh từ mới "thông báo"; quy chiếu mở rộng; đối ứng song song EN "the announcement" (R-EN3) — khác P01 ở chỗ VI dùng chỉ từ tường minh nơi EN chỉ có mạo từ |

### 4.3. Hướng A/C/E và hệ đại từ / danh xưng / [±người]

- **A (hồi quy) áp đảo:** 4/4 hàng EN, 1/1 hàng VI. Không đọc được hướng C
  (tiền chỉ) nào ở cấp câu body; cũng **không có ref=E** — khác P01 (we/you):
  P13 không có đại từ ngôi 1/2 nào, mọi phát ngôn đều là lời gián tiếp với
  attribution cùng câu.
- **Đại từ trong lời gián tiếp (quy ước CONVENTIONS §1):** mọi attribution
  ("a Catholic news agency… says", "Fides… said", "ông Park nói với…") đều
  nằm **cùng câu** với đại từ đi kèm (EN "he" S001/S005, "his" ×2 S007; VI
  "ông" S001/S005/S007) → toàn bộ [TC], không hàng nào đủ điều kiện [LC].
  Hàng đại từ liên câu duy nhất là "They" S013 ← "Vatican officials" S011
  (attribution ở câu trước đúng 2 câu). Đây là điểm khác P01 dày attribution
  gián đoạn ("ông nói"/"he says").
- **[±người] và danh xưng:** EN chỉ có "They" [+người, số nhiều] và "its"
  [−người, quốc gia]; "the reclusive state"/"the announcement" là quy chiếu
  mở rộng tới thực thể/sự kiện. VI phân tầng "ông" (honorific [+người]) —
  đứng cạnh tên ("ông Park Jie-won") hoặc thay thế trong câu — nhưng như đã
  nói đều [TC]; VI "này/đó" ("thông báo này", "ở đó") chỉ có một hàng liên
  câu, còn lại [TC].
- **Hành vi "the" (EN):** 2 hàng R riêng (the reclusive state, the
  announcement) — vị trí sự xác định là liên kết duy nhất; các "the" khác
  xử lý theo CONVENTIONS §1: "the Mass" S005, "the pope" S009/S013, "The
  intelligence agency" S008 → phép lặp từ vựng là liên kết chính (hàng L,
  alt "R: the"); "the church" S007 được giải quyết bằng mệnh đề quan hệ cùng
  câu → không tie; "the two Koreas" S013 → hàng L với alt "R: the two".
- **Đã kiểm tra và loại:** S012 "It" (expletive); S010 "Kim and Moon" (tên
  riêng rút gọn, lặp kề S009 → inventory §6); S002 "there" (trạng từ chỉ chỗ,
  tiền trạm cùng câu [TC]); S003 "they/their" (← "its citizens" cùng câu,
  [TC]); S013 "it" (← "such a trip" cùng câu, [TC]).
- **Zero VI S007 (E-VI1):** đọc *thế đại từ khiếm diện* (zero theo dõi nhân
  vật "một người") — phân tích này bổ sung cho §2, mã vẫn là E.

## 5. Phép nối (conjunction)

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-EN1 | S010 | a month earlier | temporal | S009: Moon Jae-in verbally relayed an invitation | quá khứ hoàn thành + mốc "earlier" neo cuộc gặp Kim–Moon về trước sự kiện chuyển thư mời 2018 |
| C-EN2 | S011 | afterwards | temporal | S010: Kim and Moon had met a month earlier | nối thời gian ở vị trí giữa câu nhưng neo liên câu về chuỗi sự kiện 2018; conf med |
| C-EN3 | S012 | since then | temporal | S009: In 2018 (thời điểm chuyển thư mời) | "then" hồi quy thời điểm 2018 |

**VI: không có hàng nối nào** (C-VI = 0).

**Nhận định:** cả 3 nối EN đều temporal và đều nằm trong khối nền 2018
(S009–S013) mà VI cắt — mất cân bằng EN 3 / VI 0 hoàn toàn do khối cắt, không
phải do lược từng connector. Trong khối dùng chung (S001–S008), hai phía đều
không có nối liên câu: các liên từ "or" S003, "and" S005, "but" S007 (EN) /
"hoặc" S003, "và"/"nhưng" S007 (VI) đều nối vế trong cùng câu → không đủ điều
kiện [LC] (C chỉ đánh dấu liên câu). "On Thursday"/"on Monday" (→ "Hôm
8/7"/"hôm 5/7") là khung thời gian ngoại cảnh (exophoric), không truy hồi
được textual antecedent → không phải tie (xem §8c).

## 6. Liên kết từ vựng (lexical cohesion)

### 6.1. Chính sách đánh dấu L (áp dụng CONVENTIONS §8.1 như P01 §6.1)

Chuỗi định nghĩa hẹp theo tổ hợp từ vựng (multi-word item): mỗi thuật ngữ /
tên riêng là một chuỗi; từ đơn tản mát (Catholic, visit đứng đơn lẻ, verba
dicendi) và tên riêng lặp kề nhau chỉ ghi inventory. **Đánh dấu [LC] khi:**
(i) hạng mục là biến thể mới vào chuỗi (đồng nghĩa / trái nghĩa / thượng vị /
general word / gia đình hình thái / đảo tổ hợp / liên tưởng thủ đô↔quốc gia);
(ii) tái lập chuỗi sau khoảng cách ≥ 2 câu hoặc tại điểm nối diễn ngôn (mở
đoạn, lượt attribution mới); (iii) lặp tên người nói trong attribution.
**Không đánh dấu:** lặp cùng dạng ở câu kề ngay trước (Fides S004→S005; Park
S004–S008; Triều Tiên VI S001→S003; Thánh lễ S004→S005; comments S007→S008);
thành phần trong tên riêng (Pontifical, Giáo hoàng trong "Hiệp hội Truyền
giáo Giáo hoàng"). Một mark/câu/chuỗi.

### 6.2. Kho chuỗi hai phía (inventory — gồm cả thành viên không đánh dấu)

| Chuỗi | Thành viên EN | Thành viên VI | Đánh dấu |
|---|---|---|---|
| A. chuyến thăm Giáo hoàng | a possible visit by Pope Francis (S001) · Any visit (S002) · a possible papal visit (S005) · such a trip (S013) | chuyến thăm (S001) · Bất kỳ chuyến thăm nào (S002) · [S005 hiện thực hóa thành mệnh đề "Giáo hoàng Francis tới Bình Nhưỡng" — bỏ danh từ] | EN: S005, S013; VI: không (S002 lặp kề; S005 đổi loại hình) |
| B. Triều Tiên (Bắc) | North Korea (S001) · the reclusive state (S002, R) · Pyongyang (S005) · North Korean (S009) · the two Koreas (S013) | Triều Tiên (S001–S003) · Bình Nhưỡng (S005) | EN: S005, S009, S013; VI: S005; VI lặp "Triều Tiên" S002–S003 kề nhau → không |
| C. Hàn Quốc (Nam) | outh Korea's (S001, typo §8a) · South Korea (S004, S005) · Seoul (S008) · South Korean (S009) | Hàn Quốc (S001, S004, S005) · Seoul (S008) | EN: S008; VI: S008; "South Korean" S009 kề "Seoul" S008 → không |
| D. Giáo hoàng | Pope Francis (S001) · a pope (S002, generic) · papal (S005) · the pope (S009, S013) | Giáo hoàng Francis (S001) · một vị giáo hoàng (S002, generic) · Giáo hoàng Francis (S005) | EN: S005 (gộp trong "a possible papal visit"), S009, S013; VI: S005 |
| E. cơ quan tình báo | outh Korea's intelligence chief (S001) · director of the National Intelligence Service (S006) · The intelligence agency (S008) | Giám đốc cơ quan tình báo Hàn Quốc (S001) · giám đốc của Cơ quan Tình báo Quốc gia (S006) · Cơ quan tình báo (S008) | EN: S006, S008; VI: S006, S008 |
| F. hãng tin nguồn | a Catholic news agency (S001) · the official agency (S004) · Fides (S004, S005) | một hãng thông tấn Công giáo (S001) · hãng tin chính thức (S004) · Fides (S004, S005) | EN: S004; VI: S004; "Fides" lặp kề → không |
| G. thư mời | an invitation (S009) · an official written invitation (S011) · any invitation (S012) | — (khối cắt) | EN: S011; S012 lặp đầu từ kề S011 → không |
| H. bình luận – xác nhận | his comments (S007) · Park's comments (S008) · confirmed/would not confirm (S007) · confirmed (S008) | bình luận nào của ông (S007) · bình luận của ông Park (S008) · xác nhận (S007 ×2, S008) | không (lặp đầu từ ở câu kề) |
| I. nhân vật | Park Jie-won/Park (S004–S008, mỗi câu) · Kim Jong Un/Kim (S009–S010) · Moon Jae-in/Moon (S009–S010) · Kim Hee-jung, Alfred Xuereb (S005) | ông Park Jie-won/ông Park (S004–S008, mỗi câu) · Kim Hee-jung, Alfred Xuereb (S005) | không — tên Park lặp liên tục 5 câu không khoảng trống (khác P01: attribution tái lập sau khoảng cách) |
| J. trường Công giáo (phép liên tưởng) | Catholic (S001, S003) · a Mass/the Mass (S004–S005) · priests (S002) · faith (S003) · Pontifical (S004, trong tên riêng) · Vatican (S001, S005, S011) · Archbishop (S005 ×2) | Công giáo (S001, S003) · thánh lễ/Thánh lễ (S004–S005) · linh mục (S002) · đức tin (S003) · Giáo hoàng (S004, trong tên riêng) · Vatican (S001, S005) · Tổng giám mục (S005 ×2) | không (từ đơn / lặp kề / trong tên riêng); liên tưởng thủ đô↔quốc gia (Pyongyang, Seoul) được đánh dấu ở chuỗi B, C |
| K. verba dicendi | has said/says (S001) · said (S004, S005, S011, S013) · told (S005) | cho biết (S001 ×2, S004) · đưa tin (S005) · nói (S005, S007) | không (động từ báo dẫn quá phổ biến, kiểu "water" §8.1) |

### 6.3. Các hàng L ghi vào tie table

**EN — 12 hàng** (câu | dạng | kiểu | tiền trạm):
S004 the official agency, lặp ← S001 a Catholic news agency (biến thể "news
agency" → "official agency"; Fides đồng quy chiếu với hãng tin S001) · S005 a
possible papal visit, lặp ← S001 a possible visit by Pope Francis (biến thể
thêm "papal", tái lập sau 4 câu; "papal" đồng thời tái lập chuỗi D) · S005
Pyongyang, liên tưởng ← S001 North Korea (thủ đô ↔ quốc gia) · S006 director
of the National Intelligence Service, đồng nghĩa ← S001 outh Korea's
intelligence chief ("director" ↔ "chief" + "Intelligence" gia đình hình thái;
câu định danh Park; nguyên văn typo §8a) · S008 The intelligence agency, lặp ←
S006 the National Intelligence Service (biến thể "Service" → "agency"; alt
"R: The") · S008 Seoul, liên tưởng ← S005 South Korea · S009 North Korean,
lặp ← S001 North Korea (tính từ hóa — gia đình hình thái; mở đoạn nền 2018) ·
S009 the pope, lặp ← S001 Pope Francis ("Pope" lặp từ trở + mạo từ; S002 "a
pope" là generic không tính; alt "R: the") · S011 an official written
invitation, lặp ← S009 an invitation (biến thể thêm bổ nghĩa) · S013 the
pope, lặp ← S009 the pope (tái lập sau 4 câu, trong lời Vatican officials;
alt "R: the") · S013 the two Koreas, lặp ← S009 South Korean President Moon
Jae-in và North Korean leader Kim Jong Un (gộp hai chuỗi Nam–Bắc đã thiết
lập; alt "R: the two") · S013 such a trip, đồng nghĩa ← S005 a possible papal
visit ("trip" ↔ "visit"; alt "R: such").

**VI — 6 hàng** (câu | dạng | kiểu | tiền trạm):
S004 hãng tin chính thức, lặp ← S001 một hãng thông tấn Công giáo (biến thể
rút gọn "hãng thông tấn" → "hãng tin") · S005 Giáo hoàng Francis, lặp ← S001
Giáo hoàng Francis (tái lập chuỗi nhân vật sau 4 câu; EN đối ứng "papal") ·
S005 Bình Nhưỡng, liên tưởng ← S001 Triều Tiên (thủ đô ↔ quốc gia) · S006
giám đốc của Cơ quan Tình báo Quốc gia, lặp ← S001 Giám đốc cơ quan tình báo
Hàn Quốc (câu định danh Park; đảo tổ hợp với "của"; tái lập sau 5 câu) · S008
Cơ quan tình báo, lặp ← S006 Cơ quan Tình báo Quốc gia (biến thế "Quốc gia" →
"ở Seoul"; theo §3.9 lặp danh từ VI = L) · S008 Seoul, liên tưởng ← S005 Hàn
Quốc (thủ đô ↔ quốc gia).

### 6.4. Nhận định

- **L-EN (12) gấp đôi L-VI (6)** vì hai lý do: (i) khối cắt S009–S013 chứa 6
  hàng L EN (North Korean, the pope, an official written invitation, the pope,
  the two Koreas, such a trip); (ii) phía VI lặp tên kề nhau dày (Triều Tiên
  S001–S003, ông Park S004–S008, Thánh lễ S004–S005, Fides S004–S005) — theo
  chính sách §6.1 không đánh dấu lặp kề.
- **EN phân rã, VI hội tụ** ở chuỗi B: EN dùng 4 biến thể từ vựng (North
  Korea / the reclusive state / Pyongyang / North Korean / the two Koreas)
  trong khi VI ổn định quanh "Triều Tiên" + 1 lần "Bình Nhưỡng" — cùng hướng
  dịch chuyển với chuỗi A của P01. Ngược lại chuỗi D: EN dao động Pope Francis
  / papal / the pope còn VI giữ nguyên danh "Giáo hoàng Francis".
- Liên tưởng thủ đô ↔ quốc gia (phép liên tưởng của TNT) được đánh dấu L
  collocation ở cả hai phía cho Pyongyang/Bình Nhưỡng (S005) và Seoul (S008) —
  hai vị trí này là biến thể mới duy nhất của chuỗi B, C tại điểm tái lập.
- Tên nhân vật Park/ông Park xuất hiện ở 5 câu liên tiếp (S004–S008) nên
  không phát sinh hàng attribution nào — trái với P01 nơi tên người nói tái
  lập sau khoảng cách được đánh dấu theo §8.1(iii).
- Số đếm L phụ thuộc trực tiếp chính sách §6.1: nếu đánh dấu mọi lặp kề, VI
  sẽ vượt 15 hàng; mọi thành viên vẫn nằm trong kho §6.2 để kiểm tra.

### 6.4. Bổ sung L theo chính sách v2 (2026-11-05)

Theo chỉ thị giảng viên (phân tích kỹ hơn, đánh dấu nhiều hơn), chính
sách L được nới rộng (CONVENTIONS §8.1 v2): lặp cùng dạng kể cả câu kề,
từ đơn có nội dung thực, chuỗi động từ attribution, tái lập tại điểm nối
diễn ngôn. Kho chuỗi §6.2 được rà lại; các hàng L mới là quyết định đọc
hiểu tay (không regex/word-list), mỗi hàng 1 mark/câu/chuỗi, ante luôn
nằm trước. Danh sách hàng bổ sung (đối soát 2 cổng QC PASS):

Phía EN — 33 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S002 | Any visit | repetition | S001: a possible visit by Pope Francis |
| 2 | S002 | priests | collocation | S001: a Catholic news agency |
| 3 | S003 | Catholic | repetition | S001: a Catholic news agency |
| 4 | S004 | South Korea | repetition | S001: outh Korea's |
| 5 | S004 | said | repetition | S001: has said |
| 6 | S004 | a Mass | collocation | S003: Catholic |
| 7 | S004 | the Pontifical Mission Societies | synonym | S001: Pope Francis |
| 8 | S005 | Fides | repetition | S004: Fides |
| 9 | S005 | said | repetition | S004: said |
| 10 | S005 | Park | repetition | S004: Park Jie-won |
| 11 | S005 | the Mass | repetition | S004: a Mass |
| 12 | S005 | the Vatican's | repetition | S001: the Vatican |
| 13 | S005 | South Korea | repetition | S004: South Korea |
| 14 | S005 | Archbishop | collocation | S004: a Mass |
| 15 | S006 | Park | repetition | S005: Park |
| 16 | S007 | Park | repetition | S006: Park |
| 17 | S007 | the church | collocation | S005: the Mass |
| 18 | S007 | spoke | synonym | S005: told |
| 19 | S007 | comments | synonym | S004: the announcement |
| 20 | S007 | attendance | collocation | S005: the Mass |
| 21 | S008 | Park's | repetition | S007: Park |
| 22 | S008 | confirmed | repetition | S007: confirmed |
| 23 | S008 | comments | repetition | S007: comments |
| 24 | S009 | South Korean | repetition | S005: South Korea |
| 25 | S009 | an invitation | collocation | S005: a possible papal visit |
| 26 | S009 | relayed | synonym | S005: told |
| 27 | S010 | Kim and Moon | repetition | S009: Kim Jong Un và Moon Jae-in |
| 28 | S011 | Vatican officials | repetition | S005: the Vatican's |
| 29 | S011 | said | repetition | S005: said |
| 30 | S012 | any invitation | repetition | S011: an official written invitation |
| 31 | S013 | said | repetition | S011: said |
| 32 | S013 | consider | repetition | S011: considered |
| 33 | S013 | made | repetition | S004: made the announcement |


Phía VI — 30 hàng bổ sung:

| # | sent | text | sub | ante |
|---:|---|---|---|---|
| 1 | S002 | chuyến thăm | repetition | S001: chuyến thăm (trong 'thực hiện chuyến thăm tới Triều Tiên') |
| 2 | S002 | Triều Tiên | repetition | S001: Triều Tiên |
| 3 | S002 | linh mục | collocation | S001: Công giáo (trong 'hãng thông tấn Công giáo') |
| 4 | S003 | Triều Tiên | repetition | S002: Triều Tiên |
| 5 | S003 | Công giáo | repetition | S001: Công giáo (trong 'hãng thông tấn Công giáo') |
| 6 | S003 | tín đồ | collocation | S002: linh mục |
| 7 | S003 | đức tin | collocation | S001: Công giáo |
| 8 | S004 | cho biết | repetition | S001: cho biết |
| 9 | S004 | Hàn Quốc | repetition | S001: Hàn Quốc (trong 'cơ quan tình báo Hàn Quốc') |
| 10 | S004 | thánh lễ | collocation | S003: Công giáo |
| 11 | S004 | Hiệp hội Truyền giáo Giáo hoàng | synonym | S001: Giáo hoàng Francis |
| 12 | S004 | Mokpo | collocation | S001: Hàn Quốc |
| 13 | S005 | Fides | repetition | S004: Fides |
| 14 | S005 | đưa tin | synonym | S004: cho biết |
| 15 | S005 | Park | repetition | S004: Park Jie-won |
| 16 | S005 | Thánh lễ | repetition | S004: thánh lễ |
| 17 | S005 | Tổng giám mục | collocation | S004: thánh lễ |
| 18 | S005 | Vatican | repetition | S001: Vatican |
| 19 | S005 | Hàn Quốc | repetition | S004: Hàn Quốc |
| 20 | S005 | khả năng | repetition | S001: khả năng (trong 'làm việc về khả năng') |
| 21 | S005 | Gwangju | collocation | S004: Hàn Quốc |
| 22 | S006 | Park | repetition | S005: Park |
| 23 | S007 | Park | repetition | S006: Park |
| 24 | S007 | nhà thờ | collocation | S005: Thánh lễ |
| 25 | S007 | nói chuyện | repetition | S005: nói (trong 'ông Park nói với những người tham dự') |
| 26 | S007 | bình luận | synonym | S004: thông báo (trong 'đưa ra thông báo này') |
| 27 | S007 | tham dự | repetition | S005: tham dự (trong 'những người tham dự Thánh lễ') |
| 28 | S008 | Park | repetition | S007: Park |
| 29 | S008 | xác nhận | repetition | S007: xác nhận |
| 30 | S008 | bình luận | repetition | S007: bình luận |

Số đếm §9 dưới đây đã gộp toàn bộ phần bổ sung này. Các kết luận §6.5
(nếu có) của bản pilot về "chọn lọc lặp kề" không còn áp dụng — thay
bằng chính sách v2.

## 7. Các dịch chuyển liên kết nổi bật (tổng hợp)

| Kiểu dịch chuyển | Số lần | Ví dụ nguyên văn |
|---|---:|---|
| EN quy chiếu mô tả → VI lặp tên riêng / danh ngữ (R→L hoặc R→∅ hàng) | 2 | EN S002 "the reclusive state" → VI S002 "tới Triều Tiên" (lặp kề → không có hàng VI); EN S003 "its citizens" → VI S003 "công dân Triều Tiên" |
| EN tỉnh lược → VI lấp bằng danh từ tổng quát | 1 | EN S002 "the first ∅ by a pope" → VI S002 "đánh dấu lần đầu tiên của một vị giáo hoàng" |
| EN "the" → VI "này" (giữ chức năng R hai phía) | 1 | EN S004 "made the announcement" ↔ VI S004 "đưa ra thông báo này" |
| EN danh từ → VI mệnh đề + hiện thực hóa tên riêng | 1 | EN S005 "to discuss a possible papal visit to Pyongyang" → VI S005 "để thảo luận về khả năng Giáo hoàng Francis tới Bình Nhưỡng" ("papal" → "Giáo hoàng Francis") |
| EN chủ ngữ dùng chung ↔ VI zero chủ ngữ [TC] | 1 | EN S007 "confirmed his attendance but would not confirm…" ↔ VI S007 "và ∅ đã xác nhận… nhưng ∅ không xác nhận…" |
| EN đại từ [TC] → VI giữ đại từ [TC] | 2 | EN S003 "how they practice their faith" → VI "cách họ thực hành đức tin"; EN S007 "his attendance" → VI "sự tham dự của ông" |
| EN nối temporal → nằm trong khối bị VI cắt | 3 | "a month earlier" (S010), "afterwards" (S011), "since then" (S012) — không có đối ứng VI |
| VI cắt khối câu | 5 câu | ST S009–S013 (toàn bộ nền 2018: Moon – Kim Jong Un – Vatican) |
| EN thứ → VI ngày (explicitation thời gian) | 2 | EN S004 "on Monday" → VI "hôm 5/7"; EN S007 "On Thursday" → VI "Hôm 8/7" |
| VI explicitation khác | 3 | VI S002 thêm động từ "đánh dấu"; VI S003 "how many" → "số lượng"; VI S005 thêm "thành phố" (Gwangju) |
| Tiêu đề [TD]: VI bỏ mệnh đề nguồn, bỏ metonym | 1 | EN "Seoul working for pope visit to N.Korea, Vatican agency says" → VI "Hàn Quốc tìm cách thu xếp cho chuyến thăm của Giáo hoàng tới Triều Tiên" (bỏ "Vatican agency says"; "Seoul" → "Hàn Quốc") |

## 8. Bất thường dữ liệu nguồn (cần ghi chú khi thống kê)

- **(a) Typo lede EN:** S001 bắt đầu bằng "outh Korea's intelligence chief"
  (mất chữ "S" đầu — "South"). Nguyên văn giữ nguyên khi trích dẫn; hàng
  L-EN S006 dẫn tiền trạm "S001: outh Korea's intelligence chief". Bối cảnh
  và bản VI ("Hàn Quốc") xác nhận đọc dự định; không ảnh hưởng quyết định tie.
- **(b) Khối cắt phía VI:** rows 9–11 của `rows.json` có `vi` rỗng — ST
  S009–S013 (nền 2018) không có đối ứng. Đánh dấu tie bên EN (R-EN4, C-EN1–3,
  6 hàng L), bên VI để trống; `TT.txt`/`TT_seg.json` còn 3 đoạn rỗng cuối
  (artifact của khối cắt, không phải câu).
- **(c) Quy đổi thời gian:** EN dùng thứ ("on Monday", "On Thursday"), VI
  dùng ngày ("hôm 5/7", "Hôm 8/7") — nhất quán với ngày phát 8/7/2021
  (thứ Năm) của URL Reuters. Hai mốc này là khung exophoric, **không dùng làm
  bằng chứng cấp câu** (không phải tie, đã loại ở §5).
- **(d) Tiêu đề standalone:** lấy từ `meta.json` (dòng SL:/TL:), không nằm
  trong flow ST/TT → [TD], không có tie table; chỉ so sánh định tính ở §7.
  EN title viết thường "pope", dùng viết tắt "N.Korea" và metonym "Seoul";
  VI title bỏ hẳn mệnh đề attribution "Vatican agency says".
- **(e) Không có câu artifact** kiểu caption pull-quote / câu lặp nguyên văn
  (khác P01) — mọi câu S001–S013 / S001–S008 đều là câu body thật, dùng được
  làm bằng chứng cấp câu. S006 ("Park is director…") là câu định danh chuẩn
  văn phong Reuters, không phải artifact.
- **(f) Tên riêng giữ nguyên:** "Fides", "Mokpo", "Gwangju" không dịch;
  "Pontifical Mission Societies" → "Hiệp hội Truyền giáo Giáo hoàng" (dịch
  tên tổ chức, "Giáo hoàng" trong tên riêng không lập chuỗi D — xem §6.2 J).

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table (cập nhật v2 2026-11-05)

| Chỉ số | Phân tích | Tie table | Ghi chú |
|---|---:|---:|---|
| EN — R | 4 | 4 | §4 |
| EN — S | 0 | 0 | §3 |
| EN — C | 3 | 3 | §5 |
| EN — E | 1 | 1 | §2 |
| EN — L | 45 | 45 | §6 (pilot 12 + v2 33) |
| VI — R | 1 | 1 | §4 |
| VI — S | 0 | 0 | §3 |
| VI — C | 0 | 0 | §5 |
| VI — E | 1 | 1 | §2 |
| VI — L | 36 | 36 | §6 (pilot 6 + v2 30) |

- Tổng tie: EN **53** / VI **38** (pilot: EN 20 / VI 8).
- Bổ sung v2 (33 EN + 30 VI hàng) theo chỉ thị giảng viên
  2026-11-05 (CONVENTIONS §8.1 v2): lặp câu kề, từ đơn nội dung, động từ
  attribution; đã PASS 2 cổng QC `pipeline.annotate` + `pipeline.render`.
- Liên kết từ vựng giữ vai trò chủ lực: L-EN 45 (85%),
  L-VI 36 (95%).
- L-EN (45) > L-VI (36): bản EN phân tán chuỗi từ vựng
  (biến thể/đại từ thay thế) trong khi VI hội tụ lặp danh từ.
- Quy chiếu EN 4 / VI 1 (EN ưa đại từ, VI ưa danh ngữ lặp);
  tỉnh lược EN 1 / VI 1; thế EN 0 / VI 0;
  nối EN 3 / VI 0.
- Các hàng chỉ [TC] không dùng làm bằng chứng cho kết luận liên kết liên câu.
