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
