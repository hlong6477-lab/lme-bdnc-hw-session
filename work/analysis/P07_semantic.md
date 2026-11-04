# P07 — Phân tích ngữ nghĩa liên kết (COHESION BEYOND THE SENTENCE LEVEL)

> **Khung:** EN — Halliday & Hasan (1976): reference, substitution, ellipsis,
> conjunction, lexical cohesion. VI — Trần Ngọc Thêm (1985; 2006, dẫn theo
> Nguyễn Thanh Tùng 2020): phép lặp, phép đối, phép thế đẳng nghĩa, phép liên
> tưởng, phép tuyến tính; phép thế đại từ (khiếm diện/dự báo/hồi quy), phép
> tỉnh lược, phép nối. Mã R/S/E/C/L theo `references/en-vi-mapping.md`.
> **Quy ước:** `[LC]` liên câu (đơn vị chính); `[TC]` trong câu (lớp bổ sung
> S/E); `[TD]` tiêu đề (không đánh dấu, chỉ nói ở §8). `∅` = thành phần bị
> lược; `{…}` = phần bù hồi phục bằng ngữ nghĩa.

**ST (EN):** *Is Australian English different from English?* — SBS English (tin tính năng, 73 câu S001–S073).
**TT (VI):** *Tiếng Anh Úc có khác với tiếng Anh không?* — SBS Tiếng Việt (73 câu S001–S073).

---

## 1. Tổng quan nội dung, thể loại, bản đồ câu

**Thể loại/nguồn:** tin tính năng (news feature) văn hóa – ngôn ngữ học song ngữ
của SBS, bài giới thiệu loạt phim *Weird and Wonderful Aussie English* của
Tiến sĩ Howie Manns. Lối viết tự sự – giải thích ngôi thứ nhất ("we" = người
Úc, bao gồm cả tác giả và độc giả), giàu ví dụ từ vựng (grouse, mate, crikey,
larrikin, dinkum, arvo, bloody, currency/sterling, fair go/fair dinkum, sanger,
Tim Tams, galah, pink-atoo), một trích dẫn Mark Twain, một đoạn hội thoại cha –
con (S060–S068), kết bằng chú thích biên tập về loạt phim (S071) + tiểu sử tác
giả (S072–S073). Câu hỏi tít ([TD], không đánh dấu) được lặp lại trong bài ở
S003 và S056 như bám sát vấn đề.

**Cấu trúc:** deck/standfirst (S001–S002) → câu hỏi nêu vấn đề + dẫn (S003–S004)
→ khối ví dụ slang kiểu caption kèm chú thích trong ngoặc (S005–S009) + bình
luận (S010–S011) → subhead *The limits of "English" and its stories* (S012) +
mục 1 (S013–S025) → subhead *Embracing and creating Australia's English
stories* **dính với câu body đầu tiên** trong cùng một đơn vị sentmap (S026) +
mục 2 (S027–S055) → subhead *The future of Australian English* **dính với câu
hỏi lặp nguyên văn câu mở S003** (S056) + mục 3 (S057–S070) → chú thích biên tập
trong ngoặc (S071) + tiểu sử (S072–S073). Theo CONVENTIONS §1, các hàng subhead
và chú thích được đọc như hàng body bình thường; bản chất hàng ghi ở §1 này và
để §8 tổng hợp.

**Bản đồ câu:** 73 câu EN ↔ 73 câu VI, **toàn bộ "giữ" (đối ứng 1–1)** — không
gộp, không tách, không cắt, không câu VI tự sinh. Đây là cặp đối ứng đầy đủ hiếm
gặp (rows.json 33 hàng, không ô trống nào). Các điểm "dính" (caption pull-quote
S025, subhead + body S026/S056) nằm ở đúng cùng vị trí hai bên nên không tạo
lệch chỉ số câu. Hệ quả: mọi phân tích cấp câu của cặp này đều có đối ứng hai
phía — không có khối một bên.

**Các chuỗi/trường nghĩa chi phối liên kết (mô tả; đánh dấu L thuộc §6):**
(i) tên tiếng Anh/nước — EN dao động *English / Australian English / Australia
English (lỗi nguồn S070) / Aussie / Aussies / Australians / Australia*, VI hội
tụ *tiếng Anh / tiếng Anh Úc / người Úc / nước Úc*; (ii) trường "câu chuyện" —
*story/stories/tale/tall tales/yarns* ↔ *câu chuyện/chuyện kể/câu chuyện cổ
tích*; (iii) slang/thành ngữ/từ — *slang/idioms/words* ↔ *tiếng lóng/thành
ngữ/từ ngữ*; (iv) kho từ ví dụ giữ nguyên dạng Anh hai bên, VI chèn gloss
tiếng Việt trong ngoặc (dinkum, larrikin, bloody, tall tales, currency,
sterling, fair go, sanger, Tim Tams, galah, pink-atoo, cockatoo…); (v) nhân
vật: Mark Twain, Kevin Rudd, Dr Howie Manns, cặp "tôi – con trai" (đoạn tự sự
S060–S069); (vi) đối chiều quốc gia: British/Britain – French – American –
Chinese ↔ người Anh/Anh – Pháp – Mỹ – Trung Quốc; (vii) mỏ vàng:
goldfields/goldminers ↔ mỏ vàng/thợ đào vàng.

**Bảng bản đồ câu ST ↔ TT** (giữ = dịch gần 1–1; chi tiết dịch chuyển ghi ở cột Ghi chú):

| ST | TT | Ghi chú |
|---|---|---|
| S001 | S001 | giữ — deck/standfirst; EN "This article" ↔ VI "Bài viết này" (tự trỏ bài viết, ref=E) |
| S002 | S002 | giữ — deck; "this is the tale" ↔ "đây là câu chuyện"; "their own"/"của riêng mình" (trong câu, không đánh dấu) |
| S003 | S003 | giữ — câu hỏi nêu vấn đề; được lặp nguyên văn ở S056 (echo tu từ) |
| S004 | S004 | giữ — "this question"/"câu hỏi này" (R demonstrative ← S003) |
| S005 | S005 | giữ — ví dụ slang #1 "grouse" (caption kèm chú thích ngoặc) |
| S006 | S006 | giữ — EN "it" → VI ∅ chủ ngữ (R→E, xem §2) |
| S007 | S007 | giữ — ví dụ #2 "mate" |
| S008 | S008 | giữ — EN tỉnh lược "anyone can be ∅"; VI lấp đầy "là "mate"" (E chỉ EN, §2) |
| S009 | S009 | giữ — ví dụ #3 "Crikey"; VI gloss "(Trời ơi)" |
| S010 | S010 | giữ — EN "This is confusing" → VI "Đúng là khó hiểu thật" (mất hình thức quy chiếu, §4.3) |
| S011 | S011 | giữ — But/Nhưng (C 1–1); EN "it" → VI "đó" |
| S012 | S012 | giữ — subhead; EN "its" trong câu → VI không hiện thực sở hữu |
| S013 | S013 | giữ — EN "it"/VI "đó" quy chiếu trong câu (không đánh dấu) |
| S014 | S014 | giữ — EN "we"×2 → VI ∅ chủ ngữ (vế nếu) + "chúng ta" (E [TC], §2) |
| S015 | S015 | giữ — "We"/"Chúng ta" (chuỗi we) |
| S016 | S016 | giữ — "We"/"Chúng ta" |
| S017 | S017 | giữ — "themselves…its"/"chính mình…ngôn ngữ này" trong câu |
| S018 | S018 | giữ — "English speakers"/"người nói tiếng Anh" (neo cho "us" S019); VI chèn gloss "scare" |
| S019 | S019 | giữ — "gave us"/"cho chúng ta" |
| S020 | S020 | giữ — "gave us"/"cho chúng ta"; VI gloss "(tall tales)" |
| S021 | S021 | giữ — "we"/"chúng ta"; "Like tall tales"/"Giống như…" (trong câu) |
| S022 | S022 | giữ — VI dịch ngược nghĩa "stretched the credibility" → "làm tăng độ tin cậy" (§8); EN "more than most" → VI hiện thực "hơn bất kỳ ngôn ngữ nào khác" |
| S023 | S023 | giữ — attribution dẫn trích dẫn Mark Twain |
| S024 | S024 | giữ — trích dẫn Twain; "but"/"mà" trong câu; thiếu dấu cách sau "…" hai bên |
| S025 | S025 | giữ — caption "Mark Twain" dính đầu câu (artifact, §8); "those stories"/"đó" trong câu |
| S026 | S026 | giữ — subhead + câu body dính một đơn vị sentmap; EN "our"×2 → VI lược sở hữu (bất đối xứng chuỗi we, §4.3) |
| S027 | S027 | giữ |
| S028 | S028 | giữ — "At first"/"Ban đầu" (không đánh dấu, xem §5) |
| S029 | S029 | giữ — EN "them" → VI "họ" (R ← S028) |
| S030 | S030 | giữ — "themselves"/"mình" trong câu |
| S031 | S031 | giữ — But/Thế nhưng (C); "their"/"của mình" trong câu |
| S032 | S032 | giữ — "this obsession"/"nỗi ám ảnh…này" (bridging, conf low); "Over the next 100 years"/"tiếp theo sau đó" (temporal C) |
| S033 | S033 | giữ — đề tài hoá "The word "afternoon"?"/"Từ "buổi chiều"…" |
| S034 | S034 | giữ — hai bên cùng tỉnh lược "∅ Too long"/"∅ Quá dài" (§2) |
| S035 | S035 | giữ — đề tài hoá như S033 |
| S036 | S036 | giữ — EN "it's" → VI tái cấu trúc "Ta nói" (mất đại từ; "ta" khái quát) |
| S037 | S037 | giữ — VI "đó" neo trong câu ("trải nghiệm của người Úc") |
| S038 | S038 | giữ — "it"×2/"nó"×2 trong câu; "Where…"/"Trong khi… thì… lại" trong câu |
| S039 | S039 | giữ — mở cặp đối lập Anh/Úc không connector (§5) |
| S040 | S040 | giữ — "but"/"nhưng" trong câu; VI "nó" trong câu |
| S041 | S041 | giữ — "This embrace"/"Sự đón nhận…này" (bridging, conf low) |
| S042 | S042 | giữ — "These stories"/"Những câu chuyện này"; VI tự sinh "giúp bạn hiểu" ("bạn" ref=E) |
| S043 | S043 | giữ — "We…our…them"/"Chúng ta…của riêng mình" (chuỗi we; "them" trong câu) |
| S044 | S044 | giữ — "British word" → "từ tiếng Anh" (đổi nhãn British→English) |
| S045 | S045 | giữ — "these British origins"/"nguồn gốc Anh này"; VI tự sinh "Thế nhưng" (C, §5) |
| S046 | S046 | giữ — EN "it" → VI "từ này"; VI "trở nên bắt nguồn" lủng củng (§8) |
| S047 | S047 | giữ — "Another story"/"Một câu chuyện khác" (comparative); "it"/"từ này" |
| S048 | S048 | giữ — "These goldfields stories"/"Những câu chuyện về mỏ vàng này" |
| S049 | S049 | giữ — However/Tuy nhiên (C); EN "that accuracy" bất thường (§8); "we've"/"chúng ta" |
| S050 | S050 | giữ — "it"/"từ ngữ đó" trong câu |
| S051 | S051 | giữ — And/Và (C); "they" trong câu; "we"/"chúng ta" |
| S052 | S052 | giữ |
| S053 | S053 | giữ — "you"/"bạn" (ref=E); VI tự sinh mệnh đề "– đều có nghĩa là chơi đẹp" |
| S054 | S054 | giữ — "These humorous idioms"/"Những thành ngữ hài hước này" |
| S055 | S055 | giữ — "but…they…that person"/"nhưng…người đó" trong câu |
| S056 | S056 | giữ — subhead dính + câu hỏi lặp nguyên văn S003 (echo tu từ; để §6/§8 quyết định) |
| S057 | S057 | giữ — câu trả lời tỉnh lược hai bên (§2) |
| S058 | S058 | giữ — "its" trong câu; "but most of all"/"nhưng trên hết" trong câu |
| S059 | S059 | giữ — "And, yet"/"Tuy nhiên" (C); "us – new Australians and old" đồng vị tự định nghĩa |
| S060 | S060 | giữ — mở đoạn tự sự ngôi 1; "my"/"của tôi" (ref=E) |
| S061 | S061 | giữ — EN "He" → VI "Nó" (đại từ vô tri cho trẻ em, §4.3) |
| S062 | S062 | giữ — "I"/"Tôi"; "Yep" → "Phải" |
| S063 | S063 | giữ — "He"/"Nó"; "that"/"điều này" (quy chiếu mở rộng ← S061) |
| S064 | S064 | giữ — EN "wouldn't ∅" (E) → VI lấp đầy "không biết"; "them"/"họ" |
| S065 | S065 | giữ — "My"/"của tôi"; "That's"/"Đó" (← S064) |
| S066 | S066 | giữ — "They're…our"/"Chúng…chúng ta" (attribution nằm ở câu trước S065) |
| S067 | S067 | giữ — But…also/Nhưng…cũng (C); "he"/"nó"; "that bird"/"con chim đó" ← S060; "I"/"Con" (attribution cùng câu) |
| S068 | S068 | giữ — "It"/"Nó" ← "that bird"/"con chim đó" (S067) |
| S069 | S069 | giữ — "I"/"Tôi" (chuỗi người kể chuyện) |
| S070 | S070 | giữ — But/Nhưng (C); EN "Australia English" thiếu -n (§8); EN "its" → VI lặp "của tiếng Anh Úc" |
| S071 | S071 | giữ — dòng chú thích biên tập trong ngoặc (§8: không đánh dấu tie) |
| S072 | S072 | giữ — EN "is linguist" thiếu mạo từ (§8) |
| S073 | S073 | giữ — "He's" → VI "Ông" (honorific) |

## 2. Phép tỉnh lược (ellipsis)

### 2.1. Bảng tỉnh lược EN (4 hàng, toàn bộ [LC])

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-EN1 | ST S008 | "anyone can be ∅)." | tỉnh lược danh từ (bổ ngữ predicative của "be"): hồi phục {a mate}, tiền trạm S007 "Who's a "mate"?"; VI lấp đầy "bất kỳ ai cũng có thể là "mate"" → phía VI không có hàng E | [LC] |
| E-EN2 | ST S034 | "∅ Too long - Australians say "arvo"." | tỉnh lược mệnh đề (mảnh đáp không chủ–vị): hồi phục {It is / The word "afternoon" is}, tiền trạm S033 "The word "afternoon"?"; VI cũng tỉnh lược (E-VI3) — hai bên đồng cấu trúc | [LC] |
| E-EN3 | ST S057 | "∅ Almost certainly." | tỉnh lược mệnh đề (câu trả lời cho câu hỏi S056): hồi phục {It is (English)}, tiền trạm S056 "Is Australian English really English?"; VI cũng tỉnh lược (E-VI4) | [LC] |
| E-EN4 | ST S064 | "Most of them wouldn't ∅"." | tỉnh lược động từ (trợ động từ "would" + phủ định, lược VP): hồi phục {know that}, tiền trạm S063 "Do Americans know that?"; VI lấp đầy "Hầu hết họ đều không biết" → E chỉ phía EN | [LC] |

### 2.2. Bảng tỉnh lược VI (4 hàng: 3 [LC] + 1 [TC])

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-VI1 | TT S006 | "(∅ nghĩa là rất tốt)" | zero chủ ngữ, hồi phục {nó / "grouse"}, tiền trạm TT S005 ""Grouse" là gì?"; đọc *thế đại từ khiếm diện* (theo dõi thực thể "grouse", không phải lược wording) — vẫn một hàng E, không thêm hàng R; EN đối ứng dùng đại từ "it" (R-EN4) → dịch chuyển EN R → VI E | [LC] |
| E-VI2 | TT S014 | "Nếu ∅ lắng nghe tiếng Anh kỹ lưỡng, chúng ta sẽ…" | zero chủ ngữ vế điều kiện, hồi phục {chúng ta} — tiền trạm "chúng ta" nằm ngay trong câu (vế chính); EN "If we listen" tường minh → EN không có E đối ứng | [TC] |
| E-VI3 | TT S034 | "∅ Quá dài - người Úc nói "arvo"." | tỉnh lược mệnh đề (mảnh đáp không chủ–vị), hồi phục {Từ "buổi chiều" thì}, tiền trạm TT S033; đồng cấu trúc với E-EN2 | [LC] |
| E-VI4 | TT S057 | "∅ Gần như chắc chắn rồi." | tỉnh lược mệnh đề (câu trả lời cho câu hỏi TT S056), hồi phục {Thật vậy, (là tiếng Anh)}; đồng cấu trúc với E-EN3 | [LC] |

### 2.3. Chỗ trống đã cân nhắc nhưng KHÔNG đánh dấu

- **ST S022 "more than most ∅"** — so sánh cụt; phần hồi phục {other words/other
  cases} chỉ mang tính khái quát ngoài văn bản, không truy hồi được tiền trạm
  xác định → không đủ điều kiện theo H&H. VI hiện thực hóa "hơn bất kỳ ngôn ngữ
  nào khác" (explicitation) — ghi nhận là dịch chuyển, không bịa ∅.
- **ST S033/S035 "The word "afternoon"?" / "The word "Australian"?"** — mảnh
  đề tài hoá; hai bên đồng cấu trúc (TT "Từ "buổi chiều"…ư?"), phần "bình luận"
  do câu SAU cung cấp (xử lý ở E-EN2/E-VI3) — bản thân mảnh đề tài không có
  phần hồi phục ổn định.
- **TT S010 "Đúng là khó hiểu thật."** — không chủ ngữ, nhưng là câu cảm thán
  đánh giá (CTN theo Trần Ngọc Thêm), chủ ngữ mang tính tình huống, không truy
  hồi một tiền trạm xác định; EN đối ứng "This is confusing" là quy chiếu mở
  rộng (R-EN5) — mất hình thức khi dịch, không phải tỉnh lược.
- **TT S036 "– Ta nói "Aussie" thôi."** — EN "it's" (R ← S035) được tái cấu
  trúc thành "Ta nói…"; "ta" là chủ ngữ khái quát một lần, không truy hồi.
- Các liên từ bổ ngữ zero ("cho rằng ∅", "không chắc ∅ rằng") hai phía: cấu trúc
  cú pháp thông thường, không phải thiết bị liên kết liên câu.

**Nhận định:** tỉnh lược của cặp này tập trung ở hai vị trí tu từ đặc trưng:
(i) **mảnh đáp/đoạn ngắn** (S034, S057) — hai bên cùng giữ tính tỉnh lược, giữ
nhịp khẩu ngữ của caption và lời đáp; (ii) **lời nói gián tiếp tách câu**
(S008, S064) — EN tỉnh lược thì VI lấp đầy đầy đủ, đúng dự báo của Nguyễn
Thanh Tùng (2020) về ellipsis là phép khó chuyển nhất. Chiều ngược VI→EN có 2
zero chủ ngữ (E-VI1 [LC], E-VI2 [TC]) đối ứng đại từ/hoàn chỉnh tường minh của
EN. E-VI1 là trường hợp *thế đại từ khiếm diện* điển hình (zero theo dõi nhân
vật/vật "grouse"), ghi một hàng E duy nhất theo quy ước.

## 3. Phép thế (substitution)

**Kết quả đọc hiểu: cặp P07 KHÔNG có phép thế nào ([LC] lẫn [TC]) ở cả hai
phía** — không có pro-form nào thay thế *wording* (EN: không "one/ones/do
so/the same/not" thay thế; VI: không "như vậy/làm vậy/thế/vậy" pro-form). Bảng
dưới liệt kê toàn bộ ứng viên đã kiểm tra và lý do loại, để agent tie table và
§6–§9 đối chiếu.

| # | Ngôn ngữ | Nguyên văn | Vì sao KHÔNG phải phép thế | Cấp nếu đánh dấu |
|---|---|---|---|---|
| S-? | EN | "their own" (S002 "made the English language their own") | đại từ sở hữu + "own" = quy chiếu sở hữu (H&H §2.3 personal), tiền trạm "Australians" nằm CÙNG CÂU → không đủ [LC]; VI "của riêng mình" tương tự (trong câu) | — (R trong câu) |
| S-? | EN | "One story" (S046) | số từ "One" + danh từ "story" hiện diện → không thay thế wording; quan hệ với "a few yarns" (S045) là từ vựng (story ↔ yarn, §6) + chọn thành viên từ tập, không phải thế danh từ | — (xem §4.3) |
| S-? | EN | "so commonly used … that" (S038) | "so…that" là cấu trúc mức độ, không phải pro-form "so" (clausal substitution) | — |
| S-? | EN | "those born in the Australian colony" (S028) | "those" + mệnh đề quan hệ giới thiệu thực thể mới lần đầu (prerequisite) → không truy hồi, không phải thế | — |
| S-? | EN | "anyone can be ∅" (S008), "wouldn't ∅" (S064) | substitution bằng zero = tỉnh lược (E-EN1, E-EN4), không có pro-form | E (đã ghi §2) |
| S-? | EN | "more than most" (S022) | so sánh cụt khái quát, không hồi phục được wording (xem §2.3) | — |
| S-? | VI | "ra sao" (S002 "…thành ngôn ngữ của riêng mình ra sao") | từ hỏi "how" mở mệnh đề quan hệ, không thay thế wording đã có trong văn bản | — |
| S-? | VI | "của riêng mình" (S002), "mình" (S030), "của mình" (S031) | phản thân/sở hữu quy chiếu trong câu, không phải pro-form | — (R trong câu) |
| S-? | VI | "Thế nhưng" (S031, S045) | "thế" đã ngưng kết (fossilized) trong liên từ, không thay thế wording | — (C, §5) |
| S-? | VI | "thôi" (S036), "ư" (S033/S035), "rồi" (S057) | tiểu từ cuối câu/khắc khẩu — theo quy ước không phải tie | — |
| S-? | VI | "Gần như chắc chắn rồi" (S057) | không có pro-form; đây là tỉnh lược mệnh đề (E-VI4) | E (đã ghi §2) |

**Nhận định:** con số S = 0/0 của cặp này không phải do đọc sót: chức năng
"thay thế cách diễn đạt" trong P07 được đảm nhiệm bằng (i) **danh ngữ
demonstrative + danh từ tổng quát** ("từ này", "Những câu chuyện này",
"Những thành ngữ hài hước này" — quy chiếu, §4) và (ii) **lặp danh từ/
gloss tiếng Anh** (dinkum, larrikin, fair dinkum giữ nguyên dạng hai bên).
Cấu trúc liệt kê ví dụ slang (S005–S009, S053, S055) mỗi lần nêu một từ mới,
không tái diễn đạt cùng một wording → không tạo điều kiện cho thế. Đây là
bằng chứng bổ sung cho nhận định contrastive: tiếng Việt trong bản dịch này
ưu tiên hiện thực hóa/giữ nguyên danh từ thay vì dùng pro-form.

## 4. Phép quy chiếu (reference)

### 4.1a. Bảng quy chiếu EN (43 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-EN1 | S001 | This article | E | ngoài văn bản (chính bài viết) | tự trỏ bài viết (deck); VI "Bài viết này" đối ứng |
| R-EN2 | S002 | this | A | S001: This article | "this is the tale" — quy chiếu mở rộng tới bài viết/chuỗi larrikin–dinkum; conf med |
| R-EN3 | S004 | this question | A | S003: Is Australian English really English? | demonstrative + danh từ tổng quát "question" |
| R-EN4 | S006 | it | A | S005: "grouse" | đại từ chỉ từ ("grouse") — metalinguistic; VI ∅ (E-VI1) |
| R-EN5 | S010 | This | A | S005–S009: chuỗi ví dụ slang (neo gần nhất S009) | quy chiếu mở rộng (this = đống ví dụ vừa nêu); conf med |
| R-EN6 | S011 | it | A | S004: The unique way Australians communicate | "But it is definitely English" — đọc tiếp chuỗi quy chiếu mở rộng qua "This" (S010); conf med |
| R-EN7 | S014 | we | E | ngoài văn bản (we khái quát: người viết + độc giả) | "we"×2 trong câu — 1 mark; chuỗi we mở đầu, xem chính sách §4.3 |
| R-EN8 | S015 | We | A | S014: we | cụm song song "We hear…" |
| R-EN9 | S016 | We | A | S015: We | tiếp cụm song song |
| R-EN10 | S019 | us | A | S018: English speakers | "gave us" — neo về NP trong văn bản tốt hơn là we ngoại văn bản; us = người nói tiếng Anh (bao gồm tác giả); conf med |
| R-EN11 | S020 | us | A | S019: us | cấu trúc song song "gave us" câu kề |
| R-EN12 | S021 | we | A | S020: us | "what we are willing to accept" — câu kề |
| R-EN13 | S026 | our | A | S021: we | "our history and our relationships" — our×2, 1 mark; xa 5 câu qua trích dẫn Twain (far-away vẫn A); VI lược sở hữu → không đối ứng |
| R-EN14 | S029 | them | A | S028: those born in the Australian colony | |
| R-EN15 | S032 | this obsession | A | S031: Aussies soon took pride in their status (mốc S027: rejecting British formality) | demonstrative + danh từ đánh giá bao trùm S027–S031 — cầu nối (bridging): "obsession" là nhận định của tác giả → conf low; phương án L (danh từ mới) đã cân nhắc, chọn R vì "this" là liên kết duy nhất |
| R-EN16 | S041 | This embrace | A | S040: the "larrikin" … evolved into a fun, likeable person | bridging tương tự R-EN15 → conf low |
| R-EN17 | S042 | These stories | A | S041: an underdog story | |
| R-EN18 | S043 | We | A | S026: our | "We even tell yarns about our English words…" — We + our trong câu, 1 mark; khoảng cách xa (17 câu) nhưng theo en-vi-mapping §3.3 vẫn A |
| R-EN19 | S045 | these British origins | A | S044: started off as British word | gốc Anh được nêu tường minh ở S044 → conf med |
| R-EN20 | S046 | it | A | S045: "dinkum" | |
| R-EN21 | S047 | it | A | S045: "dinkum" | tiếp chuỗi qua S046; "it" thứ hai trong câu ("as it was reputedly said") trỏ "fair dinkum" cùng câu → không ghi |
| R-EN22 | S047 | Another story | A | S046: One story | comparative (another); "One story" S046 không đánh dấu (xem §4.3) |
| R-EN23 | S048 | These goldfields stories | A | S047: Another story (gồm S046: One story) | |
| R-EN24 | S049 | we've | A | S043: We | tiếp chuỗi we sau 6 câu, cùng mục |
| R-EN25 | S051 | we | A | S049: we've | "how we relate to one another" |
| R-EN26 | S053 | you | E | ngoài văn bản (you khái quát) | thành ngữ "(if you ask …)"; VI "bạn" giữ 1–1 |
| R-EN27 | S054 | These humorous idioms | A | S053: "fair crack of the whip", "fair suck of the sav", "fair shake of the sauce bottle" | |
| R-EN28 | S059 | us…we | A | S051: we | "defined by us - new Australians and old" — "us" được đồng vị tự định nghĩa → mark đại diện cho "we" cuối câu; 1 mark/câu |
| R-EN29 | S060 | my | E | ngoài văn bản (người kể chuyện) | đoạn tự sự ngôi 1 mở đầu; VI "của tôi" 1–1 |
| R-EN30 | S061 | He | A | S060: my young son | |
| R-EN31 | S062 | I | A | S060: my (người kể chuyện) | |
| R-EN32 | S063 | He | A | S061: He | tiếp chuỗi con trai (gốc S060) |
| R-EN33 | S063 | that | A | S061: "Isn't galah a way of saying stupid?" | quy chiếu mở rộng tới sự thật trong trích dẫn câu trước (trong lời thoại của con); conf med |
| R-EN34 | S064 | them | A | S063: Americans | "Most of them wouldn't" — lời đáp của người kể |
| R-EN35 | S065 | My | A | S062: I (người kể chuyện) | "My 9-year-old" — danh ngữ mới chỉ con trai (quan hệ từ vựng để §6) |
| R-EN36 | S065 | That's | A | S064: Most of them wouldn't | quy chiếu mở rộng (that = chuyện người khác không biết từ Úc); conf med |
| R-EN37 | S066 | They're | A | S065: Australian words | trong trích dẫn; "them" cuối câu cùng chuỗi → 1 mark |
| R-EN38 | S066 | our | A | S065: My 9-year-old smiled (attribution ở câu trước) | đại từ ngôi 1 trong trích dẫn đủ điều kiện [LC] theo CONVENTIONS §1 (attribution câu trước) |
| R-EN39 | S067 | he | A | S065: My 9-year-old | "But he also added" |
| R-EN40 | S067 | that bird | A | S060: a "galah" | demonstrative trong trích dẫn, khoảng cách 7 câu; conf high |
| R-EN41 | S068 | It | A | S067: that bird | tiếp trích dẫn |
| R-EN42 | S069 | I | A | S065: My (người kể chuyện) | |
| R-EN43 | S073 | He's | A | S072: Dr Howie Manns | |

### 4.1b. Bảng quy chiếu VI (41 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-VI1 | S001 | này (Bài viết này) | E | ngoài văn bản (chính bài viết) | đối ứng R-EN1 |
| R-VI2 | S002 | đây | A | S001: Bài viết này | "đây là câu chuyện" — quy chiếu mở rộng; conf med |
| R-VI3 | S004 | này (câu hỏi này) | A | S003: Tiếng Anh Úc có thực sự là tiếng Anh không? | đối ứng R-EN3 |
| R-VI4 | S011 | đó | A | S004: Cách giao tiếp độc đáo của người Úc | "chắc chắn đó là tiếng Anh"; TT S010 không có hình thức quy chiếu → VI phải neo thẳng về S004 (bất đối xứng với EN); conf med |
| R-VI5 | S014 | chúng ta | E | ngoài văn bản (chúng ta = người viết + độc giả/người Úc) | đối ứng R-EN7; vế "Nếu ∅ lắng nghe" là E-VI2 [TC] riêng |
| R-VI6 | S015 | Chúng ta | A | S014: chúng ta | cụm song song |
| R-VI7 | S016 | Chúng ta | A | S015: Chúng ta | |
| R-VI8 | S019 | chúng ta | A | S018: người nói tiếng Anh | "mang đến cho chúng ta"; conf med |
| R-VI9 | S020 | chúng ta | A | S019: chúng ta | |
| R-VI10 | S021 | chúng ta | A | S020: chúng ta | |
| R-VI11 | S029 | họ | A | S028: những người sinh ra ở thuộc địa Úc | đối ứng R-EN14 |
| R-VI12 | S032 | này (nỗi ám ảnh…này) | A | S031: người Úc… tự hào về địa vị "currency lads" (mốc S027: bác bỏ sự trang trọng) | bridging như R-EN15 → conf low |
| R-VI13 | S041 | này (Sự đón nhận từ "larrikin" này) | A | S040: "larrikin"… trở thành một người vui vẻ, dễ mến | bridging → conf low |
| R-VI14 | S042 | này (Những câu chuyện này) | A | S041: các câu chuyện về những kẻ yếu | |
| R-VI15 | S042 | bạn | E | ngoài văn bản (bạn = độc giả khái quát) | **VI tự sinh**: "là chìa khóa giúp bạn hiểu…" — EN S042 không có đại từ ("key to the Aussie experience"); explicitation |
| R-VI16 | S043 | Chúng ta | A | S021: chúng ta | khoảng cách 22 câu (TT S026 lược sở hữu "our" nên chuỗi VI phải nhảy xa hơn EN — xem §4.3); "của riêng mình" cùng câu gộp 1 mark |
| R-VI17 | S045 | này (nguồn gốc Anh này) | A | S044: một từ tiếng Anh (gốc Anh) | conf med |
| R-VI18 | S046 | từ này | A | S045: "dinkum" | demonstrative + danh từ tổng quát "từ" — hiện thực hóa EN "it" |
| R-VI19 | S047 | từ này | A | S045: "dinkum" | tiếp chuỗi qua S046 |
| R-VI20 | S047 | khác (Một câu chuyện khác) | A | S046: Một câu chuyện | comparative, đối ứng R-EN22 |
| R-VI21 | S048 | này (Những câu chuyện về mỏ vàng này) | A | S047: Một câu chuyện khác (gồm S046) | |
| R-VI22 | S049 | chúng ta | A | S043: Chúng ta | |
| R-VI23 | S051 | chúng ta | A | S049: chúng ta | "cách chúng ta giao tiếp" |
| R-VI24 | S053 | bạn | E | ngoài văn bản (bạn khái quát) | "nếu bạn tham khảo cựu Thủ tướng Kevin Rudd"; đối ứng R-EN26 |
| R-VI25 | S054 | này (Những thành ngữ hài hước này) | A | S053: "fair crack of the whip"… | |
| R-VI26 | S059 | chúng ta | A | S051: chúng ta | "chính chúng ta - những người Úc mới và cũ" — đồng vị tự định nghĩa, 1 mark cho "chúng ta"×2 trong câu |
| R-VI27 | S060 | của tôi | E | ngoài văn bản (người kể chuyện) | đối ứng R-EN29 |
| R-VI28 | S061 | Nó | A | S060: con trai nhỏ của tôi | **"nó" [+người] dùng như đại từ vô tri cho trẻ em** — xem §4.3 |
| R-VI29 | S062 | Tôi | A | S060: của tôi (người kể chuyện) | |
| R-VI30 | S063 | Nó | A | S061: Nó | tiếp chuỗi (gốc S060) |
| R-VI31 | S063 | điều này | A | S061: "Chẳng phải galah có nghĩa là ngớ ngẩn sao?" | quy chiếu mở rộng trong trích dẫn; conf med |
| R-VI32 | S064 | họ | A | S063: Người Mỹ | "Hầu hết họ đều không biết" |
| R-VI33 | S065 | của tôi | A | S062: Tôi (người kể chuyện) | "Cậu con trai 9 tuổi của tôi" |
| R-VI34 | S065 | Đó | A | S064: Hầu hết họ đều không biết | quy chiếu mở rộng; conf med |
| R-VI35 | S066 | Chúng | A | S065: các từ ngữ Úc | "Chúng là từ của chúng ta"; "chúng" tân ngữ cuối câu cùng chuỗi → 1 mark |
| R-VI36 | S066 | chúng ta | A | S065: Cậu con trai 9 tuổi… mỉm cười (attribution câu trước) | EN "our" → VI "chúng ta" (sở hữu → đại từ) |
| R-VI37 | S067 | nó | A | S065: Cậu con trai 9 tuổi | "Nhưng nó cũng nói thêm" |
| R-VI38 | S067 | con chim đó | A | S060: một con "galah" | demonstrative "đó", khoảng cách 7 câu |
| R-VI39 | S068 | Nó | A | S067: con chim đó | "Nó trông giống như…" — "nó" vô tri cho con chim |
| R-VI40 | S069 | Tôi | A | S065: của tôi (người kể chuyện) | |
| R-VI41 | S073 | Ông | A | S072: Tiến sĩ Howie Manns | **honorific** — EN "He's" trung tính |

### 4.2. Hướng A/C/E

- **A (hồi quy) áp đảo:** EN 39/43 hàng, VI 36/41 hàng. Mọi đại từ/danh ngữ
  demonstrative đều truy hồi được về câu trước.
- **C (tiền chỉ): không có hàng nào** hai phía. Ứng viên duy nhất là TT S037
  "cuốn vào đó" — "đó" đọc được là trỏ tới "trải nghiệm của người Úc" xuất
  hiện SAU nó trong cùng câu, nhưng đây là quan hệ trong câu (không [LC]) và
  cũng đọc là trỏ khái quát; không đánh dấu.
- **E (ngoại văn bản): EN 4 hàng** (S001 This article; S014 we; S053 you;
  S060 my), **VI 5 hàng** (S001 này; S014 chúng ta; S042 bạn — tự sinh; S053
  bạn; S060 của tôi). Tỷ lệ ref=E cao hơn P01 là đặc trưng thể loại: bài tự
  sự – giáo dục viết bằng ngôi "we" tập thể (người Úc), đối thoại trực tiếp
  với độc giả ("you"/"bạn"), và đoạn hồi tưởng cá nhân ("my"/"của tôi").

### 4.3. Hệ đại từ / danh xưng / [±người]

**Chính sách chuỗi "we/us/our" – "chúng ta" của cặp này (chốt để tie table
theo):** điểm neo của chuỗi (tác giả = người Úc) nằm NGOÀI văn bản → hàng đầu
tiên ref=E (S014). Các lần tái lập QUÁ RANH GIỚI CÂU đều được đánh dấu 1
mark/câu, tiền trạm = thành viên chuỗi gần nhất trong văn bản (khoảng cách xa
vẫn là A theo en-vi-mapping §3.3): S015, S016 (cụm song song "We hear");
S019 neo về NP "English speakers" (S018); S020, S021; S026 "our"×2; S043
We+our; S049; S051; S059 (us có đồng vị tự định nghĩa "new Australians and
old", mark đại diện "we"). VI tương tự: S014–S021, S043, S049, S051, S059.
**Bất đối xứng có chủ ý:** EN S026 "our history and our relationships" → TT
S026 lược hoàn toàn sở hữu ("gắn liền với lịch sử và các mối quan hệ") → phía
VI không có hàng S026, và "Chúng ta" (S043) phải neo ngược về S021 (22 câu)
thay vì S026 như phía EN.

**[±người] và hiện tượng đáng chú ý:**
- **VI "nó" cho con trai nhỏ** (S061, S063, S067): trẻ em [+người] nhưng được
  theo dõi bằng đại từ vô tri "nó" — thói quen khẩu ngữ tiếng Việt với thân
  nhân nhỏ; EN dùng "He/he" trung tính mọi chỗ. S068 "Nó" = con galah (vô tri
  chuẩn). Đây là phân hóa hệ [±người] VI không có ở EN.
- **Honorific:** TT S073 "Ông là giảng viên cao cấp…" cho Tiến sĩ Howie Manns;
  EN "He's". VI thêm danh xưng chức vị "Tiến sĩ" (S071, S072) so với "Dr" EN —
  khoảng cách xã hội được mã hoá từ vựng ở VI.
- **"chúng ta" bao gồm (inclusive):** toàn bộ "we/us" của bài được dịch
  "chúng ta", không có "chúng tôi" — tác giả tự đặt mình vào cộng đồng
  người Úc và kéo cả độc giả vào; không có phân hóa chúng tôi/chúng ta như
  một số cặp khác.
- **Ngôi xưng hô gia đình trong hội thoại:** TT S067 "Con nghĩ con chim đó…"
  (EN "I think…"), TT S062 "Phải" (EN "Yep") — hệ con–cha; "Con"/"I" không
  đánh dấu vì attribution ("nó cũng nói thêm"/"Tôi cười và nói") nằm cùng câu.
- **Demonstrative gánh chức năng xác định:** EN dùng đại từ trần (it, they) và
  mạo từ "the"; VI chuyển thành danh ngữ demonstrative + danh từ tổng quát:
  "từ này" (S046, S047 ← EN it), "điều này" (S063 ← EN that), "con chim đó"
  (S067 ← EN that bird), "Những câu chuyện này" (S042), "nguồn gốc Anh này"
  (S045). Thống kê tiểu loại: EN personal 29 / demonstrative 13 / comparative
  1; VI personal 25 / demonstrative 15 / comparative 1 — VI dịch 4 vị trí
  personal EN thành demonstrative, chỉ 1 vị trí ngược lại (S066 our → chúng
  ta).

**Quy chiếu trong câu đã kiểm tra và KHÔNG đưa vào tie table (R chỉ [LC]):**
EN S002 "their own" (← Australians), S012 "its" (← "English"), S013 "it"
(← English), S017 "themselves…its", S022 "its" (← Australia), S030
"themselves" (← The British), S031 "their" (← Aussies), S038 "it"×2 (← a word
like "bloody"), S043 "them" (← our English words), S050 "it" (← a
word), S053 "which" (← "fair go"), S055 "they…that person" (← Aussies/a
person), S058 "its" (← Australian English), S066 "them" (← our words), S067
"I" (attribution cùng câu), S070 "its" (← Australia English); TT S002 "của
riêng mình", S013 "đó" (← tiếng Anh), S017 "chính mình…ngôn ngữ này" (← tiếng
Anh), S030 "mình", S031 "của mình", S037 "đó" (← trải nghiệm của người Úc),
S038 "nó"×2, S040 "nó", S043 "của riêng mình", S050 "từ ngữ đó", S053 "mà",
S055 "người đó", S067 "Con" (attribution cùng câu). Đại từ ngôi 1/2 trong
trích dẫn chỉ đủ điều kiện khi attribution ở câu trước: EN/VI S066 ("our"/
"chúng ta" ← attribution S065) là trường hợp duy nhất được đánh dấu.

**Comparative:** mỗi bên 1 hàng — EN "Another story" (S047) ↔ VI "Một câu
chuyện khác" (S047), giữ 1–1. EN S066 "other people" đối lập với "our" trong
cùng câu → không đánh dấu. **S046 "One story" ← S045 "a few yarns"** đã cân
nhắc: đọc là chọn một thành viên từ tập yarns; chọn không đánh dấu R (quan hệ
chính là từ vựng story ↔ yarn, giao cho §6; "One" là số từ, không phải thiết
bị quy chiếu theo H&H §2.5) — đối chiếu bắt buộc với "Another story" S047
được đánh dấu.

**Bridging (conf low, đã nêu cả hai phương án):** S032 "this obsession"/"nỗi
ám ảnh…này" và S041 "This embrace"/"Sự đón nhận…này" — danh từ bao trùm
(obsession, embrace) là đánh giá mới của tác giả, không lặp từ vựng tiền trạm;
chọn R (demonstrative là liên kết duy nhất), phương án L ghi trong ghi chú.

## 5. Phép nối (conjunction)

### 5.1. Bảng nối EN (8 hàng, toàn bộ [LC])

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-EN1 | S011 | But | adversative | S010: This is confusing | tương phản "khó hiểu ↔ nhưng chắc chắn là tiếng Anh" |
| C-EN2 | S031 | But | adversative | S028–S030: người Anh chế nhạo/gọi "currency"/"sterling" | "But Aussies soon took pride…" — "soon" là thời gian, gộp vào một mark; cặp với "At first" (S028, không đánh dấu riêng — xem 5.3) |
| C-EN3 | S032 | Over the next 100 years | temporal | S031: Aussies soon took pride in their status | "the next" mặc định mốc thời gian vừa kể (kỷ nguyên thuộc địa); conf med |
| C-EN4 | S049 | However | adversative | S048: These goldfields stories are almost certainly not true | tương phản "chuyện không thật ↔ độ chính xác không quan trọng" |
| C-EN5 | S051 | And | additive | S050: the more stories… the more likely it is to survive | thêm luận điểm về vai trò của từ/câu chuyện; conf med |
| C-EN6 | S059 | And, yet | adversative | S058: defined by its past stories | "And" + "yet" gộp một mark; tương phản "quá khứ ↔ cũng do chúng ta hiện tại" |
| C-EN7 | S067 | But … also | adversative | S066: They're our words and other people don't know them | "But he also added" — But là tín hiệu chính, "also" gộp; lời khen ↔ lời đùa bổ sung; conf med |
| C-EN8 | S070 | But | adversative | S069: I am not sure that "pink-atoo" will ever catch on | "pink-atoo" có thể không thịnh hành ↔ tiếng Anh Úc sẽ tiếp tục phát triển |

### 5.2. Bảng nối VI (9 hàng, toàn bộ [LC])

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-VI1 | S011 | Nhưng | adversative | S010: Đúng là khó hiểu thật | đối ứng C-EN1, giữ 1–1 |
| C-VI2 | S031 | Thế nhưng | adversative | S028–S030: người Anh chế giễu/gọi "tiền tệ"/"bảng Anh" | đối ứng C-EN2, giữ 1–1; "chẳng bao lâu sau" = "soon" gộp |
| C-VI3 | S032 | tiếp theo sau đó | temporal | S031: người Úc… tự hào về địa vị "currency lads" | "Trong 100 năm tiếp theo sau đó" — đối ứng C-EN3; VI hiện thực hóa tường minh bằng liên từ thời gian "sau đó" |
| C-VI4 | S045 | Thế nhưng | adversative | S044: "Dinkum"… ban đầu là một từ tiếng Anh | **VI tự sinh**: EN S045 không có connector liên câu — quan hệ ngầm nằm trong cụm nhượng bộ "Not content with these British origins" (trong câu); VI tách ra thành connector câu |
| C-VI5 | S049 | Tuy nhiên | adversative | S048: Những câu chuyện về mỏ vàng này… không có thật | đối ứng C-EN4, giữ 1–1 |
| C-VI6 | S051 | Và | additive | S050: càng có nhiều câu chuyện… khả năng tồn tại càng cao | đối ứng C-EN5, giữ 1–1 |
| C-VI7 | S059 | Tuy nhiên | adversative | S058: Tiếng Anh Úc được định nghĩa bởi những câu chuyện trong quá khứ | đối ứng C-EN6, giữ kiểu adversative; đổi hình thức ("And, yet" → "Tuy nhiên"), mất sắc thái additive của "And" |
| C-VI8 | S067 | Nhưng … cũng | adversative | S066: Chúng là từ của chúng ta và người khác không biết chúng | đối ứng C-EN7, giữ 1–1 ("cũng" = "also") |
| C-VI9 | S070 | Nhưng | adversative | S069: Tôi không chắc từ "pink-atoo" sẽ bao giờ được ưa chuộng | đối ứng C-EN8, giữ 1–1 |

### 5.3. Ứng viên đã cân nhắc nhưng KHÔNG đánh dấu (C chỉ [LC])

- **EN S028 "At first" / TT S028 "Ban đầu"** — tổ chức diễn ngôn HƯỚNG TỚI (cặp
  với "soon"/"chẳng bao lâu sau" ở S031), không nối về một mệnh đề trước; quan
  hệ tương phản của cặp "At first… But soon" đã được xử tại C-EN2/C-VI2.
- **EN S038 "Where… , it became…" / TT S038 "Trong khi… thì… nó lại…"** — quan
  hệ tương phản/nhượng bộ hoàn toàn TRONG CÂU (đáng chú ý: VI hiện thực hóa
  tường minh "Trong khi… thì… lại" hơn EN).
- **EN S024 "but" / TT S024 "mà"** (trong trích dẫn Twain), **S040 "but"/
  "nhưng"**, **S055 "but"/"nhưng"**, **S058 "but most of all"/"nhưng trên
  hết"** — tất cả trong câu.
- **EN S013 "not just… - it is…" / TT S013 "không chỉ… - đó là…"** — tương
  phản ngầm trong câu.
- **EN S014 "If we listen…, we hear…" / TT S014 "Nếu…, … sẽ…"** — điều kiện
  trong câu.
- **EN S021 "Like tall tales" / TT S021 "Giống như…"** — so sánh trong câu
  (quan hệ từ vựng tall tales → §6).
- **EN S060 "A few years ago" / TT S060 "Vài năm trước"** — khởi cảnh đoạn tự
  sự, không có tiền trạm trước đó.
- **Cặp S039 "In Britain…" / S040 "In Australia…"** — tương phản ngầm GIỮA HAI
  CÂU không được hiện thực hóa bằng connector ở cả hai bên → không có hàng C
  nào (nối ngầm hai phía, ghi nhận là đặc trưng cặp đối lập địa danh).
- **TT S008 "cũng"** — additive trong câu ("bất kỳ ai cũng có thể là…").
- **TT S053 "– đều có nghĩa là chơi đẹp"** — mệnh đề tóm lược danh sách VI TỰ
  SINH, nằm trong cùng câu → không tạo quan hệ liên câu (mô tả dịch chuyển ở
  §1/§7).

**Nhận định:** tổng C: EN 8 – VI 9. Cấu trúc: (i) **giữ 1–1** 8 cặp
(But/Những 3 cặp S011/S070 + Thế nhưng S031 + However/Tuy nhiên S049 + And/Và
S051 + And-yet/Tuy nhiên S059 + But-also/Nhưng-cũng S067 + temporal S032) —
tỷ lệ giữ kiểu rất cao, không có trường hợp EN có connector liên câu mà VI
lược; (ii) **VI tự sinh** 1 (Thế nhưng S045 — hiện thực hóa quan hệ ngầm của
EN); (iii) **đổi hình thức giữ kiểu** 1 (S059: "And, yet" → "Tuy nhiên", mất
sắc "And" thêm vào); (iv) adversative thống trị (EN 6/8, VI 7/9), temporal 1,
additive 1 mỗi bên — phù hợp mạch lập luận "tương phản – xoay chuyển" (Anh ↔
Úc, không thật ↔ không quan trọng, quá khứ ↔ hiện tại) của bài. Các connector
trong câu (but, and, if, while, or, "mà", "và", "hoặc", "trong khi") không
đánh dấu vì C chỉ lấy [LC].

## 6. Liên kết từ vựng (lexical cohesion)

### 6.1. Chính sách đánh dấu L của cặp này (theo CONVENTIONS §8.1)

Chuỗi định nghĩa **hẹp theo tổ hợp từ vựng** (multi-word item): mỗi thuật ngữ
("Australian English", "tall tales", "fair go", "the Aussie experience",
"currency lads"…) là một chuỗi riêng. Danh từ/đại từ đơn lẻ quá tản mát hoặc
lặp dày — "English"/"tiếng Anh" trần (chuỗi B), "Australia/Aussie/
Australians"/"người Úc/nước Úc" (chuỗi L), "words"/"từ", "history"/"lịch sử",
verba dicendi (asked/hỏi), verba communicandi (communicate/relate/interact ↔
giao tiếp/trò chuyện) — chỉ ghi inventory (bảng §6.2), không đánh dấu.

**Đánh dấu [LC] khi:** (i) hạng mục là **biến thể mới** vào chuỗi (đồng nghĩa,
trái nghĩa, thượng vị, general word, gia đình hình thái, rút gọn/clipping,
thêm/bớt bổ ngữ) — kể cả ở câu kề nếu là hạng mục từ vựng mới thật sự (tiền lệ
thực hành P05/P17); (ii) **tái lập chuỗi** sau khoảng cách ≥ 2 câu hoặc tại
**điểm nối diễn ngôn** (mở mục sau subhead, câu body đầu tiên sau trích dẫn,
lượt lời mới); (iii) lặp tên người nói trong attribution sau khoảng cách.
**Không đánh dấu:** lặp cùng dạng ở câu kề ngay trước; vùng chuỗi liên tục dày
(S044–S048 "dinkum"; S049–S051 "story"); câu artifact (caption S025, câu hỏi
lặp nguyên văn S056, chú thích biên tập S071 — xem §8); thành viên đã mang mã
R trong cùng câu ("These stories" S042, "Another story" S047, "These
goldfields stories" S048, "these British origins" S045, "These humorous
idioms" S054) — quy tắc **một mark/câu/chuỗi**. Chuỗi "we/us/our" ↔ "chúng
ta" và các chuỗi nhân vật theo dõi bằng đại từ đã xử ở §4 (R), không lặp lại
ở đây. Trích dẫn dưới đây chuẩn hoá dấu ngoặc thẳng như §1–§5; khi ghi tie
table lấy nguyên văn từng ký tự từ sentmap.

### 6.2. Kho chuỗi hai phía (inventory — gồm cả thành viên không đánh dấu)

| Chuỗi | Thành viên EN | Thành viên VI | Đánh dấu |
|---|---|---|---|
| **A.** Australian English (tên ngôn ngữ Úc) | Australian English (S003); The future of Australian English (S056, subhead); Australian English (S058, S059); Australia English (S070 — lỗi nguồn thiếu -n, §8); Aussie English (S071 — tên loạt phim, artifact §8) | Tiếng Anh Úc (S003); tiếng Anh Úc (S022); Tương lai của tiếng Anh Úc (S056, subhead); Tiếng Anh Úc (S058, S059); tiếng Anh Úc (S070 ×2); Tiếng Anh Úc Độc lạ và Thú vị (S071 — artifact) | EN: S058, S070 · VI: S022, S058, S070 |
| **B.** "English" trần (tên ngôn ngữ) | "English" (S001); the English language (S002); English (S011); "English" (S012 subhead); English (S013 ×2, S014, S017); English speakers (S018); new English words (S021); English (S022) | "tiếng Anh" (S001, S002, S003, S011, S012 subhead, S013, S014, S017, S021, S022 ×2, S037, S044); người nói tiếng Anh (S018); ngôn ngữ này (S013, S017) | không (tản mát, lặp dày S011–S022; VI còn hút 2 vị trí "British" EN tại S037/S044 — xem K) |
| **C.** story/tale/tall tales/yarns (câu chuyện) | the tale (S002); its stories (S012 subhead); a collection of stories (S013); "tall tales" + colourful stories (S020); tall tales (S021); stories ×2 (S025 — phần body sau caption); Australia's English stories (S026 subhead); an underdog story (S041); These stories - or yarns (S042, R-EN17); yarns (S043); a few yarns (S045); One story (S046); Another story (S047, R-EN22); These goldfields stories (S048, R-EN23); a story (S049); stories (S050, S051); its past stories (S058); its collection of stories (S070) | câu chuyện (S002); các câu chuyện (S012 subhead); những câu chuyện (S013); "những câu chuyện cổ tích" (tall tales) + những câu chuyện đầy màu sắc (S020); những câu chuyện cổ tích (S021); những câu chuyện (S025); những câu chuyện tiếng Anh của Úc (S026 subhead); các câu chuyện về những kẻ yếu (S041); Những câu chuyện này + "yarns" + những chuyện kể (S042, R-VI14); các câu chuyện (S043); một vài câu chuyện (S045); Một câu chuyện (S046); Một câu chuyện khác (S047, R-VI20); Những câu chuyện về mỏ vàng này (S048, R-VI21); một câu chuyện (S049); câu chuyện (S050, S051); những câu chuyện trong quá khứ (S058); bộ sưu tập các câu chuyện (S070) | EN: S020, S025, S041, S045, S046, S058, S070 · VI: S020, S025, S041, S045, S058, S070 (S042/S047/S048 mã R; S046 VI lặp kề cùng dạng) |
| **D.** slang (tiếng lóng) | Aussie slang (S001); Aussie slang (S048); Australian slang (S071 — artifact); Australian slang (S073) | tiếng lóng và thành ngữ Úc (S001); tiếng lóng (S048); tiếng lóng Úc (S071 — artifact; S073) | EN: S048, S073 · VI: S048, S073 |
| **E.** idioms (thành ngữ) | idioms (S001); colourful idioms (S052); These humorous idioms (S054, R-EN27) | thành ngữ (S001); những thành ngữ đầy màu sắc (S052); Những thành ngữ hài hước này (S054, R-VI25) | EN: S052 · VI: S052 (S054 đã mã R) |
| **F.** Aussie/Australian words (từ ngữ Úc) | Aussie words (S025); Aussie words (S051); Australian words (S065) | các từ ngữ Úc (S025); những từ ngữ và câu chuyện của người Úc (S051); các từ ngữ Úc (S065) | EN: S051, S065 · VI: S051, S065 |
| **G.** dinkum | "dinkum" (S002, S044, S045, S048); "ding kam" (S046 — cụm tiếng Quảng Đông nguồn gốc, chỉ inventory) | "dinkum" (S002); Từ "Dinkum" (S044); "dinkum" (S045, S046, S048) | EN: S044 · VI: S044 (S045–S048 vùng dày liên tục) |
| **H.** larrikin | "larrikin" (S002, S039, S040); the "larrikin" (S041 — trong NP mã R-EN16) | "larrikin" (S002, S039, S040, S041) | EN: S039 · VI: S039 |
| **I.** fair (fair dinkum/fair drinking/fairness/fair go ↔ công bằng) | "fair drinking", "fair dinkum" (S047); a sense of fairness (S052); "fair go", "fair crack of the whip", "fair suck of the sav", "fair shake of the sauce bottle" (S053); fair (S058) | "fair drinking" (uống rượu công bằng), "fair dinkum" (S047); tinh thần công bằng (S052); "fair go" (chơi đẹp) + 3 thành ngữ + "– đều có nghĩa là chơi đẹp" (S053 — mệnh đề VI tự sinh); công bằng (S058) | EN: S052, S053, S058 · VI: S052, S053, S058 |
| **J.** goldfields/goldminers (mỏ vàng) | the goldfields (S045); Chinese goldminers (S046); goldfields gamblers (S047); These goldfields stories (S048, R-EN23) | các mỏ vàng (S045); những thợ đào vàng Trung Quốc (S046); những kẻ đào vàng (S047); Những câu chuyện về mỏ vàng này (S048, R-VI21) | EN: S046 · VI: S046 (S047–S048 chuỗi liên tục/đã mã R) |
| **K.** British/Britain (người Anh/Anh) | British formality (S027); the British (S028); The British (S029, S030); the British Empire (S030); British words (S037); in Britain (S038); In Britain (S039); British word (S044); these British origins (S045, R-EN19); not British (S058) | người Anh (S027, S028); Người Anh + Đế quốc Anh (S029, S030); "ở Anh" (S038); "Ở Anh" (S039); nguồn gốc Anh (S045, R-VI17); kiểu cách Anh (S058) — VI dịch "British" ở S037/S044 thành "tiếng Anh" (chuyển sang chuỗi B) | EN: S037, S044, S058 · VI: S058 (S038–S039 lặp kề; S045 mã R) |
| **L.** Australia/Aussie/Australians (Úc/người Úc/nước Úc) | Australians (S002, S004); Australia's (S026 subhead); the Australian colony (S028); Aussies (S031); Australia (S032); Australians (S034); Australia + the great Australian adjective (S038); In Australia (S040); Aussies (S041, S045, S053, S054); a more Aussie feel (S043); classic Aussie ×2 (S055); new Australians and old (S059) | người Úc (S002, S004, S027, S031, S034, S037, S041, S042, S045, S048, S051, S052, S053, S054, S055 ×2); của Úc (S026 subhead); thuộc địa Úc (S028); nước Úc (S032, S038); Ở Úc (S040); kiểu Úc (S043); người Úc mới đến (S004); người Úc mới và cũ (S059) | KHÔNG (tên quốc gia/dân tộc danh lặp dày gần như mỗi câu — §8.1; các tổ hợp đa từ tách thành chuỗi riêng: A, D, F, M, Q, Y) |
| **M.** the Aussie experience (trải nghiệm của người Úc) | the Australian experience (S027); the Aussie experience (S037, S042) | trải nghiệm của người Úc (S027, S037, S042) | EN: S037, S042 · VI: S037, S042 |
| **N.** currency/sterling (tiền tệ/bảng Anh) | "currency" (S029); "sterling" (S030); "currency lads" (S031) | "tiền tệ" – "currency" (S029); "bảng Anh" – "sterling" (S030); "những chàng trai tiền tệ" – "currency lads" (S031) | EN: S030, S031 · VI: S030, S031 |
| **O.** true/accuracy (thật/chính xác/chắc chắn) | to be true (S020); as true (S021); credibility (S022 — lỗi dịch VI §8, chỉ inventory); almost certainly not true (S048); accuracy (S049); accurate or not (S050); Almost certainly (S057) | là sự thật (S020, S021); độ tin cậy (S022 — lỗi); gần như chắc chắn không có thật (S048); tính chính xác (S049); chính xác (S050); Gần như chắc chắn (S057) | EN: S048, S057 · VI: S048, S057 (S049–S050 lặp kề) |
| **P.** formality/informal (trang trọng) | British formality (S027); being informal (S032) | sự trang trọng (S027); tính cách bất cần trang trọng (S032) | EN: S032 · VI: S032 |
| **Q.** relationships (mối quan hệ) | our relationships (S026); Aussie relationships (S052) | các mối quan hệ (S026); Các mối quan hệ của người Úc (S052) | EN: S052 · VI: S052 |
| **R.** national identity (bản sắc) | national identity (S001); identity (S073) | bản sắc dân tộc (S001); bản sắc nước Úc (S073) | EN: S073 · VI: S073 |
| **S.** Vikings | Viking axes and swords (S014); Rampaging Vikings (S018) | rìu và kiếm Viking (S014); Những người Viking hung hãn (S018) | EN: S018 · VI: S018 |
| **T.** French (Pháp) | fancy French feasts (S015); "Fancy" French "nobles" (S019) | bữa tiệc xa hoa kiểu Pháp (S015); Những "quý tộc" (nobles) Pháp "sang trọng" (fancy) (S019) | EN: S019 · VI: S019 |
| **U.** American cowboys (cao bồi Mỹ) | a galloping American cowboy (S016); American cowboys (S020); Americans (S063 — khác thực thể, đơn từ, chỉ inventory) | một chàng cao bồi Mỹ (S016); Những chàng cao bồi Mỹ (S020); Người Mỹ (S063 — inventory) | EN: S020 · VI: S020 |
| **V.** galah/cockatoo/pink-atoo (chim + wordplay) | a "galah" (S060); galah (S061); that bird (S067, R-EN40); 'pink-atoo' (S067); a pink 'cockatoo' (S068 — thượng vị của galah, gộp trong R-EN41); "pink-atoo" (S069) | một con "galah" (S060); galah (S061); con chim đó (S067, R-VI38); 'pink-atoo' (S067); một con 'cockatoo' màu hồng (S068 — gộp trong R-VI39); "pink-atoo" (S069) | EN: S069 · VI: S069 |
| **W.** con trai (my young son / 9-year-old) | my young son (S060); He (S061, S063 — R); My 9-year-old (S065 — "My" mã R-EN35); he (S067 — R) | con trai nhỏ của tôi (S060); Nó (S061, S063 — R); Cậu con trai 9 tuổi của tôi (S065 — "của tôi" mã R-VI33); nó (S067 — R) | EN: S065 ("9-year-old") · VI: S065 ("Cậu con trai 9 tuổi") |
| **X.** silly/stupid (ngớ ngẩn/ngu ngốc) | "silly" or "stupid" (S055); stupid (S061) | "ngớ ngẩn"(silly) hay "ngu ngốc" (stupid) (S055); ngớ ngẩn (S061) | EN: S061 · VI: S061 |
| **Y.** cặp rút gọn (clipping): afternoon→arvo; Australian→Aussie | The word "afternoon" (S033) → "arvo" (S034); The word "Australian" (S035) → "Aussie" (S036) | Từ "buổi chiều" – "afternoon" (S033) → "arvo" (S034); Từ "người Úc" – "Australian" (S035) → "Aussie" (S036) | EN: S034, S036 · VI: S034, S036 |
| **Z.** tên riêng nhân vật (Mark Twain, Kevin Rudd, Howie Manns) | US writer Mark Twain (S023 — attribution); Mark Twain (S025 — caption artifact §8.2, KHÔNG dùng); former Prime Minister, Kevin Rudd (S053); Dr Howie Manns (S071 — chú thích biên tập, artifact); Dr Howie Manns (S072 — lần đầu trong flow); He's (S073 — R-EN43) | Nhà văn Mỹ Mark Twain (S023); Mark Twain (S025 — artifact); cựu Thủ tướng Kevin Rudd (S053); Tiến sĩ Howie Manns (S071 — artifact); Tiến sĩ Howie Manns (S072); Ông (S073 — R-VI41) | KHÔNG (S025/S071 artifact; S072 prerequisite; S073 mã R; Rudd/Monash chỉ một lần) |
| **Khác** (chỉ inventory — tản mát hoặc một lần) | words (S017, S021, S022, S043, S050); The word (S033, S035); a word like "bloody" (S038); language (S002, S013, S072); history (S024 ×2, S026, S071, S073); asked (S061, S063 — kề); communicate/relate/interact (S004, S051, S054, S059); smile/laughed (S025, S062, S065); humorous/fun/funny (S051, S054, S058); colourful (S020, S052); grouse, mate, Crikey, bloody, sanger, Tim Tams, hee-haw, scare, cuisine, ding kam, Monash University, hierarchy, underdog (trong C), keep growing | từ/từ ngữ (S033/S035 "Từ", S038, S017, S021, S043, S050; "từ này" S046/S047, "từ ngữ đó" S050 — trong câu/R); ngôn ngữ/ngôn ngữ này (S002, S013, S017, S072); lịch sử (S024 ×2, S026, S071, S073); hỏi (S061, S063 — kề); giao tiếp/trò chuyện (S004, S051, S054, S059); cười/mỉm cười (S062, S065); hài hước/vui nhộn (S051, S054, S058); đầy màu sắc (S020, S052); "grouse", "mate", "Crikey", "bloody", sanger, Tim Tam, "hee-haw", "nỗi sợ hãi"-scare, "ẩm thực"-cuisine, "ding kam", Đại học Monash, thứ bậc, kẻ yếu (trong C), phát triển | KHÔNG |

### 6.3. Các hàng L ghi vào tie table (cat=L, level=[LC])

**EN — 40 hàng:**

| # | Câu | Nguyên văn | sub | Tiền trạm (mã câu + nguyên văn) | Ghi chú |
|---|---|---|---|---|---|
| L-EN1 | S018 | "Rampaging Vikings" | repetition | S014 "Viking axes and swords" | tái lập sau 4 câu (cụm "We hear" → "gave") |
| L-EN2 | S019 | ""Fancy" French "nobles"" | repetition | S015 "fancy French feasts" | gap 4; lặp cả "fancy" lẫn "French" (wordplay dấu ngoặc) |
| L-EN3 | S020 | ""tall tales" - colourful stories" | synonym | S013 "a collection of stories" | gap 7; thành ngữ "tall tales" mới vào chuỗi; "colourful stories" cùng câu gộp 1 mark |
| L-EN4 | S020 | "American cowboys" | repetition | S016 "a galloping American cowboy" | gap 4 |
| L-EN5 | S025 | "stories" | synonym | S021 "Like tall tales" | gap 4; occ 2 ("those stories" quy chiếu trong câu, §4); tại điểm trở lại giọng tác giả sau trích dẫn Twain; caption "Mark Twain" đầu câu là artifact (§8) |
| L-EN6 | S030 | ""sterling"" | antonym | S029 ""currency"" | câu kề; cặp đối lập trong trường "đơn vị tiền tệ" (vô giá trị ↔ có giá trị) — phép đối, hạng mục mới thật sự |
| L-EN7 | S031 | ""currency lads"" | repetition | S029 ""currency"" | gap 2; biến thể thành ngữ mới |
| L-EN8 | S032 | "informal" | antonym | S027 "British formality" | gap 5; trái nghĩa phái sinh (formality ↔ in-formal), cùng gia đình hình thái |
| L-EN9 | S034 | ""arvo"" | repetition | S033 "The word "afternoon"?" | câu kề; biến thể rút gọn (clipping) — hạng mục mới thật sự, hiện tượng trung tâm của bài |
| L-EN10 | S036 | ""Aussie"" | repetition | S035 "The word "Australian"?" | câu kề; clipping Australian → Aussie (cặp wordplay; "Aussie" rải rác khác thuộc chuỗi L — inventory) |
| L-EN11 | S037 | "British words" | repetition | S030 "The British called themselves "sterling"" | gap 7 |
| L-EN12 | S037 | "the Aussie experience" | repetition | S027 "the Australian experience" | gap 10; biến thể hình thái Australian → Aussie |
| L-EN13 | S039 | "the "larrikin"" | repetition | S002 ""larrikin"" | gap 37; từ deck vào thân bài |
| L-EN14 | S041 | "an underdog story" | repetition | S026 "Australia's English stories" (subhead) | gap 15; biến thể mới (bổ ngữ "underdog") |
| L-EN15 | S042 | "the Aussie experience" | repetition | S037 "the Aussie experience" | gap 5; lặp nguyên tổ hợp |
| L-EN16 | S044 | ""Dinkum"" | repetition | S002 ""dinkum"" | gap 42; khung mở (deck) → thân bài |
| L-EN17 | S044 | "British word" | repetition | S039 "In Britain" | gap 5; Britain → British |
| L-EN18 | S045 | "a few yarns" | repetition | S043 "yarns" | gap 2 |
| L-EN19 | S046 | "One story" | synonym | S045 "a few yarns" | câu kề; story ↔ yarns — chọn một thành viên từ tập yarns (§4.3 giao §6) |
| L-EN20 | S046 | "Chinese goldminers" | collocation | S045 "the goldfields" | câu kề; lặp thành tố "gold", cùng trường mỏ vàng; hạng mục mới thật sự |
| L-EN21 | S048 | "Aussie slang" | repetition | S001 "Aussie slang and idioms" | gap 47 |
| L-EN22 | S048 | "not true" | repetition | S021 "willing to accept as true" | gap 27; lặp "true" ở dạng phủ định |
| L-EN23 | S051 | "Aussie words" | repetition | S025 "Aussie words tell stories" | gap 26 |
| L-EN24 | S052 | "colourful idioms" | repetition | S001 "Aussie slang and idioms" | gap 51 |
| L-EN25 | S052 | "a sense of fairness" | repetition | S047 ""fair drinking", or "fair dinkum"" | gap 5; fair → fairness (gia đình hình thái) |
| L-EN26 | S052 | "Aussie relationships" | repetition | S026 "our history and our relationships" | gap 26 |
| L-EN27 | S053 | ""fair go"" | repetition | S052 "a sense of fairness" | câu kề; thành ngữ mới thật sự; 3 thành ngữ "fair…" cùng câu gộp 1 mark |
| L-EN28 | S057 | "Almost certainly" | repetition | S048 "almost certainly not true" | gap 9; câu đáp tỉnh lược dùng lại nguyên cụm; cùng câu có E-EN3 (tỉnh lược mệnh đề) — hai hàng khác nhau, text E = None |
| L-EN29 | S058 | "Australian English" | repetition | S056 "The future of Australian English" (subhead) | gap 2; câu hỏi lặp nguyên văn trong cùng S056 là artifact, không dùng (§8) |
| L-EN30 | S058 | "its past stories" | repetition | S051 "Aussie words and stories" | gap 7; câu body đầu tiên của mục 3 |
| L-EN31 | S058 | "fair" | repetition | S053 ""fair go"" | gap 5 |
| L-EN32 | S058 | "not British" | repetition | S045 "these British origins" | gap 13 |
| L-EN33 | S061 | "stupid" | repetition | S055 ""silly" or "stupid"" | gap 6; trong trích dẫn của con trai |
| L-EN34 | S065 | "9-year-old" | synonym | S060 "my young son" | gap 5; đổi bổ ngữ young → 9-year-old; "My" cùng câu mã R-EN35 (chuỗi người kể — khác chuỗi) |
| L-EN35 | S065 | "Australian words" | repetition | S051 "Aussie words" | gap 14; Aussie → Australian |
| L-EN36 | S069 | ""pink-atoo"" | repetition | S067 "'pink-atoo'" | gap 2; từ chơi chữ của con trai được người kể nhắc lại |
| L-EN37 | S070 | "Australia English" | repetition | S059 "Australian English" | gap 11; biến thể lỗi nguồn thiếu -n (§8) — trích nguyên văn |
| L-EN38 | S070 | "its collection of stories" | repetition | S058 "its past stories" | gap 12; "collection of stories" hồi âm S013 "a collection of stories" |
| L-EN39 | S073 | "Australian slang" | repetition | S048 "Aussie slang" | gap 25; Aussie → Australian; S071 (artifact) chỉ inventory |
| L-EN40 | S073 | "identity" | repetition | S001 "national identity" | gap 72; rút gọn — khung mở–đóng của bài |

**VI — 38 hàng:**

| # | Câu | Nguyên văn | sub | Tiền trạm (mã câu + nguyên văn) | Ghi chú |
|---|---|---|---|---|---|
| L-VI1 | S018 | "Những người Viking" | repetition | S014 "rìu và kiếm Viking" | gap 4 |
| L-VI2 | S019 | "Những "quý tộc" (nobles) Pháp "sang trọng" (fancy)" | repetition | S015 "bữa tiệc xa hoa kiểu Pháp" | gap 4; "Pháp" lặp; fancy/nobles giữ nguyên gloss tiếng Anh |
| L-VI3 | S020 | "những câu chuyện cổ tích" (tall tales) | repetition | S013 "một tập hợp của những câu chuyện" | gap 7; biến thể thêm "cổ tích" (lệch nghĩa so với tall tales, §8) |
| L-VI4 | S020 | "Những chàng cao bồi Mỹ" | repetition | S016 "một chàng cao bồi Mỹ" | gap 4 |
| L-VI5 | S022 | "tiếng Anh Úc" | repetition | S003 "Tiếng Anh Úc có thực sự là tiếng Anh không?" | gap 19; EN đối ứng S022 "Australia and its words" — VI hội tụ thuật ngữ, không có hàng EN |
| L-VI6 | S025 | "những câu chuyện" | repetition | S021 "những câu chuyện cổ tích" | gap 4; sau caption artifact "Mark Twain" |
| L-VI7 | S030 | ""bảng Anh"- "sterling"" | antonym | S029 ""tiền tệ" – "currency"" | câu kề; phép đối |
| L-VI8 | S031 | ""những chàng trai tiền tệ" – "currency lads"" | repetition | S029 ""tiền tệ" – "currency"" | gap 2 |
| L-VI9 | S032 | "bất cần trang trọng" | antonym | S027 "sự trang trọng" | gap 5; lặp thành tố "trang trọng" ở dạng phủ định |
| L-VI10 | S034 | ""arvo"" | repetition | S033 "Từ "buổi chiều" – "afternoon" ư?" | câu kề; clipping; giữ nguyên tiếng Anh |
| L-VI11 | S036 | ""Aussie"" | repetition | S035 "Từ "người Úc" – "Australian" ư?" | câu kề; clipping |
| L-VI12 | S037 | "trải nghiệm của người Úc" | repetition | S027 "trải nghiệm của người Úc" | gap 10; lặp nguyên tổ hợp |
| L-VI13 | S039 | "larrikin" | repetition | S002 ""larrikin"" | gap 37 |
| L-VI14 | S041 | "các câu chuyện về những kẻ yếu" | repetition | S026 "những câu chuyện tiếng Anh của Úc" (subhead) | gap 15 |
| L-VI15 | S042 | "trải nghiệm của người Úc" | repetition | S037 "trải nghiệm của người Úc" | gap 5 |
| L-VI16 | S044 | "Từ "Dinkum"" | repetition | S002 ""dinkum"" | gap 42; khung mở (deck) → thân bài |
| L-VI17 | S045 | "một vài câu chuyện" | repetition | S043 "kể các câu chuyện" | gap 2 |
| L-VI18 | S046 | "những thợ đào vàng Trung Quốc" | collocation | S045 "các mỏ vàng" | câu kề; lặp "vàng"; hạng mục mới thật sự |
| L-VI19 | S048 | "tiếng lóng" | repetition | S001 "tiếng lóng và thành ngữ Úc" | gap 47 |
| L-VI20 | S048 | "không có thật" | repetition | S021 "chấp nhận là sự thật" | gap 27 |
| L-VI21 | S051 | "những từ ngữ và câu chuyện của người Úc" | repetition | S025 "các từ ngữ Úc" | gap 26 |
| L-VI22 | S052 | "những thành ngữ đầy màu sắc" | repetition | S001 "tiếng lóng và thành ngữ Úc" | gap 51 |
| L-VI23 | S052 | "tinh thần công bằng" | repetition | S047 ""fair drinking" (uống rượu công bằng)" | gap 5; "công bằng" nằm trong gloss VI tự sinh |
| L-VI24 | S052 | "Các mối quan hệ của người Úc" | repetition | S026 "lịch sử và các mối quan hệ" | gap 26 |
| L-VI25 | S053 | ""fair go" (chơi đẹp)" | repetition | S052 "tinh thần công bằng" | câu kề; thành ngữ giữ nguyên tiếng Anh; mệnh đề tự sinh "– đều có nghĩa là chơi đẹp" cùng câu cùng chuỗi |
| L-VI26 | S057 | "Gần như chắc chắn" | repetition | S048 "gần như chắc chắn không có thật" | gap 9; cùng câu có E-VI4 (tỉnh lược mệnh đề) — hai hàng khác nhau |
| L-VI27 | S058 | "Tiếng Anh Úc" | repetition | S056 "Tương lai của tiếng Anh Úc" (subhead) | gap 2; câu hỏi lặp nguyên văn trong S056 là artifact, không dùng (§8) |
| L-VI28 | S058 | "những câu chuyện trong quá khứ" | repetition | S051 "những từ ngữ và câu chuyện của người Úc" | gap 7 |
| L-VI29 | S058 | "công bằng" | repetition | S053 ""fair go" (chơi đẹp)" | gap 5 |
| L-VI30 | S058 | "kiểu cách Anh" | repetition | S045 "nguồn gốc Anh này" | gap 13 |
| L-VI31 | S061 | "ngớ ngẩn" | repetition | S055 ""ngớ ngẩn"(silly)" | gap 6; trong trích dẫn của con trai |
| L-VI32 | S065 | "Cậu con trai 9 tuổi" | repetition | S060 "con trai nhỏ của tôi" | gap 5; lặp "con trai" + bổ ngữ tuổi; "của tôi" cùng câu mã R-VI33 (chuỗi người kể — khác chuỗi) |
| L-VI33 | S065 | "các từ ngữ Úc" | repetition | S051 "những từ ngữ và câu chuyện của người Úc" | gap 14 |
| L-VI34 | S069 | "từ "pink-atoo"" | repetition | S067 "'pink-atoo'" | gap 2 |
| L-VI35 | S070 | "tiếng Anh Úc" | repetition | S059 "tiếng Anh Úc" | gap 11; occ 2 ("tiếng Anh Úc" ×2 trong câu) |
| L-VI36 | S070 | "bộ sưu tập các câu chuyện" | repetition | S058 "những câu chuyện trong quá khứ" | gap 12; hồi âm S013 "tập hợp của những câu chuyện" |
| L-VI37 | S073 | "tiếng lóng Úc" | repetition | S048 "tiếng lóng "dinkum" của người Úc" | gap 25; S071 (artifact) chỉ inventory |
| L-VI38 | S073 | "bản sắc nước Úc" | repetition | S001 "bản sắc dân tộc" | gap 72; biến thể "dân tộc" → "nước Úc" — khung mở–đóng |

### 6.4. Nhận định

- **Quy mô:** 26 chuỗi có tên + nhóm "Khác"; L-EN 40 hàng / L-VI 38 hàng.
  Chuỗi dày nhất là **C (câu chuyện)** — EN 7 hàng, VI 6 hàng — đúng vai trò
  xương sống của bài ("English is not just a language - it is a collection of
  stories"); kế đến **I (fair/công bằng)** và **A (tiếng Anh Úc)**, mỗi bên 3
  hàng. S058 hội tụ 4 chuỗi trong một câu (A, C, I, K) — đỉnh dày liên kết từ
  vựng ở câu tổng kết mục 3.
- **Hội tụ khi dịch (VI có hàng, EN không):** TT S022 "Nước Úc và **tiếng Anh
  Úc** đã làm tăng…" kéo thuật ngữ chủ đề quay lại sau 19 câu (L-VI5) trong
  khi EN S022 chỉ viết "Australia and its words" — bản dịch làm đậm thuật ngữ
  sớm hơn nguyên văn.
- **Phân rã khi dịch (EN có hàng, VI không):** (i) hai vị trí "British" (S037
  "British words", S044 "British word") được VI dịch "từ tiếng Anh" — chuỗi K
  phía VI chỉ còn 1 hàng (S058) so với 3 hàng EN; (ii) EN S046 "One story" ←
  "a few yarns" là quan hệ đồng nghĩa story↔yarn (L-EN19) nhưng VI dịch cả hai
  vị trí là "câu chuyện" → lặp kề cùng dạng, không đánh dấu. Bù lại, các gloss
  VI tự sinh ("uống rượu công bằng", "chơi đẹp") lại trở thành thành viên
  chuỗi I phía VI (L-VI23, L-VI25).
- **Khung mở–đóng:** deck S001–S002 mở bằng "national identity", "Aussie
  slang", "dinkum", "larrikin", "the tale" — tất cả tái lập ở khoảng cách
  37–72 câu (L-EN13, L-EN16, L-EN39, L-EN40; VI tương ứng L-VI13, L-VI16,
  L-VI37, L-VI38); "its collection of stories" (S070) hồi âm "a collection of
  stories" (S013); "Almost certainly" (S057) hồi âm nguyên cụm "almost
  certainly not true" (S048) — câu đáp tỉnh lược dùng lại đúng cụm của tiền
  trạm.
- **Ảnh hưởng chọn từ đến số đếm:** hai chuỗi dày nhất bài — L
  (Australia/Aussie/người Úc, có mặt gần như mỗi câu) và B (English/tiếng Anh
  trần) — chỉ inventory theo §8.1, nếu đánh dấu lặp thông thường thì số L sẽ
  vượt trội; các tổ hợp đa từ (F "Aussie words", M "the Aussie experience", Q
  "relationships") tách thành chuỗi riêng có mark. Tiểu loại: EN 33
  repetition + 4 synonym + 2 antonym + 1 collocation; VI 35 repetition + 2
  antonym + 1 collocation — VI lặp nguyên dạng nhiều hơn EN (EN xoay vòng
  synonym như tale↔story↔yarn, young son↔9-year-old; VI hội tụ về một dạng),
  trùng quan sát verba communicandi (EN communicate→relate→interact; VI đều là
  "giao tiếp/trò chuyện" — chỉ inventory).

## 7. Các dịch chuyển liên kết nổi bật (tổng hợp)

| Kiểu dịch chuyển | Số lần | Ví dụ nguyên văn hai đầu |
|---|---:|---|
| EN đại từ → VI ∅ chủ ngữ (R→E) | 2 (1 [LC] + 1 [TC]) | EN S006 "(it means very good)" ↔ VI "(∅ nghĩa là rất tốt)" [LC, E-VI1]; EN S014 "If we listen closely enough to English" ↔ VI "Nếu ∅ lắng nghe tiếng Anh kỹ lưỡng" [TC, E-VI2] |
| EN quy chiếu → VI danh ngữ demonstrative (giữ R, đổi dạng) | 4 | EN S046/S047 "links it"/"attributes it" ↔ VI "liên hệ từ này"/"từ này bắt nguồn"; EN S063 "Do Americans know that?" ↔ VI "Người Mỹ có biết điều này không?"; EN S067 "that bird" ↔ VI "con chim đó" |
| EN quy chiếu → VI tái cấu trúc (mất hình thức quy chiếu) | 2 | EN S010 "This is confusing." ↔ VI "Đúng là khó hiểu thật."; EN S036 "- it's "Aussie"." ↔ VI "– Ta nói "Aussie" thôi." |
| EN đại từ trong câu → VI danh ngữ demonstrative trong câu (không đánh dấu) | 2 | EN S050 "the more likely it is to survive" ↔ VI "khả năng từ ngữ đó tồn tại"; EN S055 "they might say that person is" ↔ VI "họ có thể nói rằng người đó" |
| EN đại từ sở hữu → VI lặp danh ngữ | 1 | EN S070 "its collection of stories" ↔ VI "bộ sưu tập các câu chuyện của tiếng Anh Úc" |
| EN đại từ sở hữu → VI lược hẳn (bất đối xứng chuỗi we) | 1 | EN S026 "wrapped up in our history and our relationships" ↔ VI "gắn liền với lịch sử và các mối quan hệ" ("our"×2 mất → R-VI16 phải neo về S021, cách 22 câu) |
| EN tỉnh lược → VI lấp đầy (E chỉ phía EN) | 2 | EN S008 "anyone can be ∅" ↔ VI "bất kỳ ai cũng có thể là "mate""; EN S064 "Most of them wouldn't ∅" ↔ VI "Hầu hết họ đều không biết" |
| Hai bên cùng tỉnh lược (E giữ 1–1) | 2 | S034 "∅ Too long - Australians say "arvo"" ↔ "∅ Quá dài - người Úc nói "arvo""; S057 "∅ Almost certainly." ↔ "∅ Gần như chắc chắn rồi." |
| Phép thế | 0 hai phía | §3: không có pro-form nào ("one/ones/do so/như vậy/làm vậy"); chức năng thế đảm nhiệm bằng danh ngữ demonstrative ("từ này") và lặp danh từ/gloss |
| EN nối ngầm → VI hiện thực hóa (C VI tự sinh) | 1 | TT S045 "Thế nhưng không bằng lòng với nguồn gốc Anh này…" (EN "Not content with these British origins" — nhượng bộ nằm trong câu) |
| Nối ngầm giữ ngầm hai phía (không connector) | 1 cặp | EN S039 "In Britain, the "larrikin"…" / S040 "In Australia, the "larrikin"…" ↔ VI S039 "Ở Anh…" / S040 "Ở Úc…" — tương phản cặp địa danh không hiện thực ở cả hai bên |
| VI tự sinh đại từ/mệnh đề hướng độc giả (explicitation) | 2 | TT S042 "là chìa khóa giúp **bạn** hiểu về trải nghiệm của người Úc" (EN "have been key to the Aussie experience"); TT S053 "– đều có nghĩa là chơi đẹp" (EN không có mệnh đề tóm lược) |
| VI hiện thực hóa so sánh cụt | 1 | EN S022 "stretched the credibility of English more than most" ↔ VI "hơn bất kỳ ngôn ngữ nào khác" |
| Giữ connector liên câu 1–1 (kể cả đổi hình thức) | 8 cặp | But/Nhưng (S011, S070); But/Thế nhưng (S031); However/Tuy nhiên (S049); And/Và (S051); "And, yet"/Tuy nhiên (S059 — đổi hình thức, mất sắc additive); But…also/Nhưng…cũng (S067); "Over the next 100 years"/"Trong 100 năm tiếp theo sau đó" (S032 — VI thêm liên từ "sau đó") |
| Đổi hệ [±người] ("nó" vô tri cho trẻ em) | 3 | EN "He asked" ↔ VI "Nó hỏi" (S061, S063); EN "But he also added" ↔ VI "Nhưng nó cũng nói thêm" (S067); đối chiếu S068 "It"/"Nó" cho con galah — chuẩn vô tri |
| Honorific | 1 | EN S073 "He's a senior lecturer" ↔ VI "Ông là giảng viên cao cấp" (+ VI thêm "Tiến sĩ" ở S071/S072 so với "Dr") |
| Giữ ngôi 1 tập thể 1–1 (we ↔ chúng ta) | 11 ↔ 10 hàng R | R-EN7–13, 18, 24, 25, 28 ↔ R-VI5–10, 16, 22, 23, 26; toàn bộ "we/us/our" dịch "chúng ta" (không có "chúng tôi"); VI thiếu hàng S026 do lược "our" |
| VI giữ nguyên từ mượn + chèn gloss tiếng Việt | ~12 mục | dinkum, larrikin, Aussie, arvo, yarns, fair go, fair drinking, currency lads, galah, cockatoo, pink-atoo, sanger, Tim Tams — giữ nguyên dạng hai phía (quy ước §1); một số gloss VI tự sinh trở thành thành viên chuỗi (L-VI23 "uống rượu công bằng", L-VI25 "chơi đẹp") |
| L hội tụ/phân rã bất đối xứng | 1 hội tụ + 3 phân rã | VI hội tụ: S022 "tiếng Anh Úc" ← S003 (EN: "Australia and its words" — không có hàng); EN có mà VI không: S037/S044 "British" → VI "từ tiếng Anh", S046 "One story"↔"yarns" → VI đều là "câu chuyện" (lặp kề) |

## 8. Bất thường dữ liệu nguồn (cần ghi chú khi thống kê)

- **(a) Caption pull-quote S025 (hai bên):** "Mark Twain" (2 từ) dính vào đầu
  câu body "If Aussie words tell stories, those stories are told with a sly
  wink and smile." / "Nếu các từ ngữ Úc có thể kể chuyện, thì đó là những câu
  chuyện được kể bằng…". Caption là artifact (CONVENTIONS §8.2): chuỗi Mark
  Twain (Z) chỉ inventory, **không dùng "Mark Twain" S025 làm bằng chứng cấp
  câu** (tránh nhân đôi attribution S023); phần body sau caption đọc như câu
  bình thường (L-EN5/L-VI6 đánh dấu trên body).
- **(b) Subhead dính body S026 (hai bên):** "Embracing and creating Australia's
  English stories" / "Nắm bắt và tạo ra những câu chuyện tiếng Anh của Úc" dính
  với câu body đầu mục 2 trong cùng một đơn vị sentmap. Subhead được dùng làm
  thành viên chuỗi (C — tiền trạm của L-EN14/L-VI14) và làm điểm neo bối cảnh,
  nhưng **không phát sinh mark riêng**; body "Aussie ways of speaking…" đọc
  bình thường.
- **(c) Subhead + câu hỏi lặp nguyên văn S056 (hai bên):** "The future of
  Australian English Is Australian English really English?" / "Tương lai của
  tiếng Anh Úc Tiếng Anh Úc có thực sự là tiếng Anh không?" — câu hỏi lặp
  NGUYÊN VĂN câu mở S003 (echo tu từ). Câu hỏi lặp là artifact (§8.2):
  **không đánh dấu tie, không dùng làm bằng chứng cấp câu** (S003 đã mang chức
  năng đó); chỉ phần subhead "The future of Australian English" được dùng làm
  tiền trạm của L-EN29/L-VI27.
- **(d) Chú thích biên tập S071 (hai bên):** dòng trong ngoặc "(Weird and
  Wonderful Aussie English is a 5-part video series…)" / "Tiếng Anh Úc Độc lạ
  và Thú vị là loạt phim gồm 5 phần…" — theo CONVENTIONS §8.2 **không đánh dấu
  tie**; "Dr Howie Manns"/"Tiến sĩ Howie Manns", "Australian slang"/"tiếng lóng
  Úc" tại đây chỉ inventory (chuỗi Z, D), không làm tiền trạm cho hàng nào.
- **(e) Lỗi nguồn EN:** S070 "Australia English" (thiếu -n, phải là
  "Australian English") — hàng L-EN37 trích nguyên văn kèm lỗi, ghi chú trong
  note; S072 "Dr Howie Manns is linguist" (thiếu mạo từ "a"); S049 "sometimes
  that accuracy of a story" ("that" bất thường, có thể lỗi đánh máy của "the"
  hoặc vẩn đọng cấu trúc "not that important" cuối cùng câu) — không ảnh hưởng
  mã (C-EN4 giữ); S044 "started off as British word" (thiếu mạo từ "a" — bổ
  sung mới, cùng loại với S072).
- **(f) Lỗi dịch VI:** S022 "đã làm tăng độ tin cậy của tiếng Anh" — **ngược
  nghĩa** với EN "stretched the credibility of English" (kéo căng/làm quá tải,
  không phải tăng); thành phần "credibility/độ tin cậy" vì thế chỉ inventory
  (chuỗi O), không đánh dấu; S046 ""dinkum" trở nên bắt nguồn từ một cụm từ
  tiếng Quảng Đông" — cụm lai cấu trúc ("trở nên bắt nguồn" — dịch nửa vời
  "deriving from"); không ảnh hưởng các hàng L quanh đó (L-VI18 đánh dấu trên
  "thợ đào vàng", không dính lỗi).
- **(g) Lệch nghĩa nhẹ:** S020 EN "tall tales" (chuyện phóng đại khó tin) được
  dịch "câu chuyện cổ tích" (fairy tale) — lựa chọn từ thay đổi sắc thái chuỗi
  C; mã L giữ (lặp "câu chuyện"), ghi chú trong L-VI3.
- **(h) Thiếu dấu cách/dấu gạch:** S024 hai bên "Australian history...does not
  read" / "Lịch sử Úc...không giống" (thiếu dấu cách sau "…"); TT S055
  ""ngớ ngẩn"(silly)" (thiếu dấu cách trước ngoặc mở — hàng L-VI31 trích kèm
  lỗi); TT S030 ""bảng Anh"- "sterling"" (gạch ngang dính, không cách — hàng
  L-VI7 trích nguyên văn).
- **(i) VI tự sinh (không phải lỗi, ghi nhận làm dịch chuyển):** S042 "giúp
  bạn hiểu" (EN không có đại từ — "bạn" thành R-VI15 ref=E); S053 mệnh đề tóm
  lược "– đều có nghĩa là chơi đẹp"; S022 "hơn bất kỳ ngôn ngữ nào khác"
  (hiện thực hóa so sánh cụt "more than most"); S045 "Thế nhưng" (C-VI4).
- **(j) Dấu trích lẫn kiểu:** nguồn trộn ngoặc thẳng và cong (EN S005 "grouse"
  thẳng ↔ S009 "Crikey" cong; VI S005 "Grouse" thẳng ↔ S009 "Crikey" cong) —
  chỉ là kiểu gõ, không ảnh hưởng ranh giới câu; phân tích chuẩn hoá ngoặc
  thẳng, tie table lấy nguyên văn sentmap.
- **(k) Segmenter/đối ứng:** không có trường hợp chẻ câu tại dấu viết tắt
  (Jr./Mr./U.S.); 73 câu EN ↔ 73 câu VI đối ứng 1–1 trọn vẹn (rows.json 33
  hàng, không ô trống, không khối cắt) — mọi phân tích cấp câu đều có đối ứng
  hai phía.
- **(l) Tiêu đề [TD]:** "Is Australian English different from English?" /
  "Tiếng Anh Úc có khác với tiếng Anh không?" — không nằm trong flow ST/TT,
  không có tie; chỉ so sánh định tính (VI dịch "different from" → "có khác…
  không", trung tính so với câu hỏi trong bài S003 "really English" → "có thực
  sự là tiếng Anh không").
- **Tổng kết "không dùng làm bằng chứng cấp câu":** caption "Mark Twain" (S025,
  hai bên), câu hỏi lặp nguyên văn (S056, hai bên), toàn bộ dòng chú thích biên
  tập (S071, hai bên), và hàng [TC] duy nhất E-VI2 (TT S014). Mọi hàng R/C/L
  và E còn lại đều [LC].

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table

| Chỉ số | Đọc tay | Đã ghi tie table | Ghi chú |
|---|---:|---:|---|
| EN — R | 43 | 43 | §4.1a (R-EN1–43): 39 hướng A + 4 hướng E; tiểu loại personal 29 / demonstrative 13 / comparative 1 |
| EN — S | 0 | 0 | §3: không có phép thế nào ([LC] lẫn [TC]) |
| EN — E | 4 | 4 | §2.1 (E-EN1–4), toàn bộ [LC] |
| EN — C | 8 | 8 | §5.1 (C-EN1–8), toàn bộ [LC] (6 adversative, 1 additive, 1 temporal) |
| EN — L | 40 | 40 | §6.3 (L-EN1–40) theo chính sách §6.1 (33 repetition, 4 synonym, 2 antonym, 1 collocation) |
| VI — R | 41 | 41 | §4.1b (R-VI1–41): 36 A + 5 E; tiểu loại personal 25 / demonstrative 15 / comparative 1; 1 hàng tự sinh (R-VI15 "bạn") |
| VI — S | 0 | 0 | §3: không có phép thế nào |
| VI — E | 4 | 4 | §2.2 (E-VI1–4): 3 [LC] + 1 [TC] (E-VI2, S014) |
| VI — C | 9 | 9 | §5.2 (C-VI1–9), toàn bộ [LC]; 1 hàng tự sinh (C-VI4, S045) |
| VI — L | 38 | 38 | §6.3 (L-VI1–38) theo chính sách §6.1 (35 repetition, 2 antonym, 1 collocation) |

**Tổng đọc tay:** EN 95 tie (R43/S0/E4/C8/L40) trên 73 câu ≈ 1,30 tie/câu;
VI 92 tie (R41/S0/E4/C9/L38) ≈ 1,26 tie/câu.

**Kết luận:**

- **Thiết bị chủ lực là quy chiếu + từ vựng** (EN 43+40 = 88% tổng; VI 41+38 =
  86%): bài tự sự – giải thích ngôi "we" với chuỗi đại từ dày (11↔10 hàng
  "chúng ta") và hệ thống thuật ngữ – thành ngữ chịu tải thông tin. C gần đối
  xứng 8↔9 (VI tự sinh 1 adversative S045); E hiếm (4↔4), tập trung ở mảnh
  đáp (S034, S057) và lời nói gián tiếp tách câu (S008, S064); **S = 0 hai
  phía** — chức năng thế được đảm nhiệm bằng danh ngữ demonstrative ("từ này")
  và lặp danh từ/gloss tiếng Anh.
- **Mật độ 1,30/1,26 tie/câu — thấp hơn P01 (≈1,6) dù bài dài hơn 73 câu:**
  kho ví dụ slang của P07 phần lớn chỉ xuất hiện một lần (grouse, mate,
  Crikey, bloody, sanger… → inventory), và hai chuỗi dày nhất (Australia/
  Aussie/người Úc; English/tiếng Anh trần) chỉ inventory theo §8.1.
- **Bất đối xứng nổi bật:** (i) VI hiện thực hóa 4 vị trí đại từ EN thành danh
  ngữ demonstrative, thêm honorific "Ông" (S073) và "nó" vô tri cho trẻ em
  (S061/S063/S067) — VI ưa neo danh ngữ; (ii) EN S026 "our"×2 bị VI lược →
  chuỗi "chúng ta" phía VI phải nhảy 22 câu (R-VI16 ← S021 thay vì S026);
  (iii) L: VI hội tụ "tiếng Anh Úc" (S022, không có hàng EN) nhưng phân rã
  chuỗi "British" (S037/S044 → "tiếng Anh") và mất biến thể story↔yarn (S046)
  — EN 40 / VI 38.
- **Hàng [TC] duy nhất là E-VI2 (TT S014, zero chủ ngữ vế điều kiện)** — không
  dùng làm bằng chứng cho bất kỳ kết luận nào về liên kết liên câu; mọi hàng
  R/C/L và 3/4 hàng E đều [LC].
- **Các vị trí artifact đã loại khỏi số đếm:** caption "Mark Twain" (S025), câu
  hỏi lặp nguyên văn S003 (S056), dòng chú thích biên tập (S071) — không phát
  sinh tie (§8); số đếm tay ở trên đã loại đúng các vị trí này, sẵn sàng cho
  bước tie table đối chiếu.
