# P20 — Phân tích ngữ nghĩa liên kết (COHESION BEYOND THE SENTENCE LEVEL)

> **Khung:** EN — Halliday & Hasan (1976): reference, substitution, ellipsis,
> conjunction, lexical cohesion. VI — Trần Ngọc Thêm (1985; 2006, dẫn theo
> Nguyễn Thanh Tùng 2020): phép lặp, phép đối, phép thế đẳng nghĩa, phép liên
> tưởng, phép tuyến tính; phép thế đại từ (khiếm diện/dự báo/hồi quy), phép tỉnh
> lược, phép nối. Mã R/S/E/C/L theo `references/en-vi-mapping.md`.
> **Quy ước:** `[LC]` liên câu (đơn vị chính); `[TC]` trong câu (lớp bổ sung
> cho S/E); `[TD]` tiêu đề. `∅` = lược; `{…}` = hồi phục. File này gồm §1–§5
> (task 5-a); §6–§9 do task kế tiếp viết nối.

**ST (EN):** *EU Rolls Out Trade Bans in Global Crackdown on Illegal Fishing*
— tin quốc tế về môi trường – thương mại, văn phong VOA (dateline BANGKOK),
64 câu S001–S064, gồm 4 subhead giữa bài (S012, S022, S040, S056).
**TT (VI):** *EU xúc tiến việc cấm buôn bán hải sản đánh bắt bất hợp pháp* —
44 câu S001–S044; bản rút gọn ≈ 2/3 ST (23 câu EN không dịch), lede VI tự sinh
3 câu (S001–S003) kèm attribution "Thông tín viên Steve Herman… VOA".
**Lưu ý nguồn:** `meta.json` không có URL hai phía (`en_url`/`vi_url` rỗng) —
bất thường đã ghi nhận từ bước chuẩn hóa, không bịa URL (xem §8 sau).

---

## 1. Tổng quan nội dung, thể loại, bản đồ câu

**Thể loại/nguồn:** tin quốc tế (VOA News style, dateline BANGKOK) về chiến
dịch thẻ đỏ/thẻ vàng của EU chống đánh bắt hải sản bất hợp pháp (IUU): đe dọa
thẻ đỏ Nam Triều Tiên; tiền lệ thẻ đỏ Belize–Campuchia–Guinea; trích dẫn Steve
Trent (EJF); nghiên cứu *Marine Policy* của Ganapathiraju về hải sản bất hợp
pháp vào thị trường Mỹ; thỏa thuận Port State Measures (Long/Pew); Connieff về
nhà phân phối; dự báo vai trò Trung Quốc; kết bằng quy định mới (số hiệu nhận
diện tàu, hệ thống vệ tinh).

**Cấu trúc ST:** lede (S001–S005) → trích dẫn Trent 1 (S006–S011) →
[SUBHEAD 1 S012] EJF ghi nhận vi phạm (S013–S015) → Trent 2 về "brand Korea"
(S016–S021) → [SUBHEAD 2 S022] nghiên cứu thị trường Mỹ (S023–S031) → thỏa
thuận cảng + Long (S032–S039) → [SUBHEAD 3 S040] chuỗi cung ứng + Long
(S041–S046) → Conniff về nhà phân phối (S047–S050) → Ganapathiraju về hợp tác
(S051–S055) → [SUBHEAD 4 S056] Trung Quốc (S057–S060) → quy định mới
(S061–S064). **TT** đi song song nhưng: không dịch subhead nào; cắt trọn khối
S016–S021 (Trent 2), S041–S046 (chuỗi cung ứng), S051–S055 (Ganapathiraju 2),
S059–S060 (Conniff về Trung Quốc); tự sinh lede 3 câu đứng trước toàn bộ.

**Các chuỗi/trường nghĩa chính** (inventory chi tiết + hàng đánh dấu thuộc §6):
(i) **EU**: the European Union (S001) · EU (S001, S004, S034…) · the European
Commission (S009) · Europe (S006) ↔ Liên hiệp Châu Âu (S002, S004, S021) · EU
(S004, S007…) · Châu Âu (S008) · Ủy hội Âu châu (S011); (ii) **thẻ phạt**:
"red card" (S001) · "yellow card" (S002) · EU red cards (S004) · The red card
(S005) · a red card (S016) ↔ thẻ đỏ (S004, S007) · thẻ vàng (S005); (iii)
**đánh bắt bất hợp pháp**: illegal fishing (S001…) · pirate fishing (S004) ·
illegally caught fish (S006) · illegal, unreported and unregulated (IIU)
fishing (S023) · IUU fishing (S057) · illegal catches (S028) · illicit catches
(S064) · over-fishing (S045, S054) ↔ đánh bắt cá bất hợp pháp (S002…) · đánh cá
trộm (S007) · đánh trộm cá (S015) · IIU/IUU (S017, S039); (iv) **Nam Triều
Tiên**: South Korea (S001) · Seoul (S001) · [South] Korea (S008) · brand Korea
(S017) · the country (S019) · they (S020) · South Korean-flagged ships (S003) ·
South Korean ships (S013) · South Korean pirates (S014) ↔ Nam Triều Tiên
(S001…) · Seoul (S004) · các ông (S011–S013) · tàu thuyền Nam Triều Tiên
(S006, S014); (v) **hải sản/cá**: seafood · fish · the (sea)food (S049) ·
product (S026, S045) · merchandise (S050) ↔ hải sản · cá (S031) · sản phẩm
(S021) · hàng hóa (S038); (vi) **thị trường/nước nhập khẩu**: EU markets
(S006) · major seafood importing markets (S026) · these markets (S028) · these
importing countries (S028) · major import markets (S031) · big markets (S043) ·
export destinations (S053) ↔ thị trường (S003) · các thị trường này (S021,
S023) · những thị trường nhập khẩu (S021, S026) · những quốc gia này (S024) ·
những nước nhập khẩu (S023); (vii) **tàu thuyền/ngư dân**: boats (S001) · ships
(S003, S013) · vessels (S015, S033, S062–S064) · the boat (S062) · The
fisherman (S036) · local fishermen (S014) ↔ tàu thuyền (S004, S006, S014) ·
con tàu (S015) · nhiều chiếc (S006) · các tàu (S028, S042) · những tàu này
(S042) · ngư dân (S016, S031); (viii) **thỏa thuận cảng**: Port State Measures
agreement (S032) · the pact (S033) · the treaty (S034) · The agreement (S035) ·
Port States Measures agreement (S039) ↔ thỏa thuận các Biện pháp tại Cảng…
(S027) · Thỏa thuận này (S028) · hiệp ước (S029) · thỏa thuận (S030, S034);
(ix) **nghiên cứu/phúc trình**: A new study (S023) · It (S024) · the report
(S026) · his research (S051) ↔ Một cuộc nghiên cứu mới (S017) · Cuộc nghiên
cứu này (S018) · bản phúc trình (S020) · phúc trình (S025); (x) **nhân vật +
tổ chức**: Steve Trent (S006) · he (S009, S019) · the EJF (S013) · The
organization (S014) · It (S015) · the EJF's Trent (S016) · the EJF's Steve
Trent (S057) ↔ Ông Steve Trent (S008, S039) · Tổ chức Tư pháp Môi trường
(S008, S014, S039) · Tổ chức này (S015, S016); Pramod Ganapathiraju (S026) ·
explained Ganapathiraju (S028) · Ganapathiraju at UBC (S051) ↔ ông Pramod
Ganapathiraju (S020) · Ông (S021); Long (S035) · said Anthony Long (S037) ·
Long (S041, S044) · he (S042) · said Long (S045) ↔ Ông Anthony Long (S030);
Richard Conniff (S047) · said Conniff (S048) · Conniff (S059) ↔ Ông Richard
Conniff (S035); (xi) **chế tài/trừng phạt**: sanctions (S003) · warning (S002) ·
penalties (S009, S011) · rebuke (S018) · embargo (S021) ↔ chế tài (S006) ·
cảnh cáo (S005) · trừng phạt (S004, S013) · đe dọa (S009); (xii) **quốc gia**:
the United States (S023) · the U.S. (S026, S032, S043) · this country (S049) ·
China (S026, S057…) · the Chinese government (S058) ↔ Hoa Kỳ (S003, S021,
S025) · nước Mỹ (S017) · nước này (S037) · Trung Quốc (S019, S021, S039).

**Bản đồ câu ST ↔ TT** (64 câu EN ↔ 44 câu VI; lệch số do 3 câu VI tự sinh
đứng đầu, 1 tách, 1 gộp, 23 câu EN bị cắt):

| ST | TT | Trạng thái | Ghi chú |
|---|---|---|---|
| — | S001 | VI tự sinh | lede VI (rows.json hàng 0, ô EN trống); "BANGKOK —" của EN S001 được dời vào đây; "quốc gia đã phát triển đầu tiên" — khẳng định chỉ có VI |
| — | S002 | VI tự sinh | "Điều này" (R-VI1) ← S001; tie VI đứng độc lập |
| — | S003 | VI tự sinh | "Vấn đề này" (R-VI2) ← S002; số liệu "một phần 3" và attribution "Thông tín viên Steve Herman… Đài VOA" không có đối ứng EN (§8) |
| S001 | S004 | giữ 1–1 | EN "it is cracking down"/"its flag" trỏ Seoul [TC], không đánh dấu |
| S002 | S005 | giữ 1–1 | "thẻ vàng" — thuật ngữ mới ở cả hai bên (prerequisite) |
| S003 | S006 | giữ 1–1 | EN "many" E [TC] ↔ VI "nhiều chiếc" (classifier — không tie theo mapping §4) |
| S004 + S005 | S007 | gộp 2→1 | EN S005 "those countries" (R-EN1) ↔ VI lặp tên "Belize, Campuchia và Guinea" (R→L); EN "nor fish" là phối hợp VP chia sẻ "cannot", không phải E |
| S006 | S008 | giữ 1–1 | EN "for Europe/." lỗi nguồn (§8) |
| S007 | S009 | giữ 1–1 | EN "It" (R-EN2) ← regulation ↔ VI chủ ngữ "EU" (danh từ) — R→L |
| S008 | S010 | giữ 1–1 | "And that" ↔ "Và đó" (C-EN1↔C-VI1; R-EN3↔R-VI3) |
| S009 | S011 | giữ 1–1 | VI bỏ "he said"; EN "We" ↔ VI "Chúng ta" (lệch ngôi, §4.4) |
| S010 | S012 | giữ 1–1 | "you"/"us" ↔ "các ông"/"chúng tôi" (honorific + ngôi loại trừ) |
| S011 | S013 | giữ 1–1 | "And" ↔ "Và"; "unless"/"trừ phi" [TC] |
| S012 | — | bỏ | subhead 1 "EU Aims for Public Shaming in Crackdown on Illegal Fishing" — hàng body theo CONVENTIONS §1; VI không dịch subhead nào |
| S013 | S014 | giữ 1–1 | EN "the EJF" (viết tắt, L §6) ↔ VI "Tổ chức Tư pháp Môi trường" (tên đầy đủ) |
| S014 | S015 | giữ 1–1 | EN "The organization" (L general word, alt "R: The") ↔ VI "Tổ chức này" (R-VI6) — mạo từ EN → chỉ từ VI |
| S015 | S016 | giữ 1–1 | EN "It" (R-EN7) ↔ VI "Tổ chức này" lặp cùng dạng câu kề (không ghi); VI tự sinh "cũng" (C-VI3) |
| S016 | — | bỏ | khối cắt: dự báo Trent về repercussion/"brand Korea" |
| S017 | — | bỏ | EN "The other thing" (R-EN8) chỉ có EN |
| S018 | — | bỏ | EN "This" (R-EN9) chỉ có EN |
| S019 | — | bỏ | EN "It"/"he says" (R-EN10, R-EN11) chỉ có EN |
| S020 | — | bỏ | EN "they" (R-EN12) + "their own" (E-EN2) chỉ có EN |
| S021 | — | bỏ | EN "And…that" (C-EN3, R-EN13) chỉ có EN |
| S022 | — | bỏ | subhead 2 "Illegal Foreign Catches Still Enter US Seafood Market" |
| S023 | S017 | giữ 1–1 | "(IIU)" sai chính tả hai phía (đúng: IUU — §8) |
| S024 | S018 | giữ 1–1 | "It" (R-EN14) ↔ "Cuộc nghiên cứu này" (R-VI7) |
| S025 | S019 | giữ 1–1 | "That…also" ↔ "Đây…cũng" (R-EN15↔R-VI8; C-EN4↔C-VI4); EN That (distal) → VI Đây (proximal) |
| S026 | S020 + S021 | tách 1→2 | VI tách câu attribution: "Tác giả đứng đầu…" + "Ông nói…" (R-VI9); hệ quả cấp liên kết: EN "these markets" S028 [LC] ↔ VI "các thị trường này" S021 [TC] |
| S027 | S022 | giữ 1–1 | |
| S028 | S023 | giữ 1–1 | VI bỏ "explained Ganapathiraju"; "these markets" (R-EN16) ↔ "những thị trường này" (R-VI10) |
| S029 | S024 | giữ 1–1 | "So they" ↔ "Do đó những quốc gia này" (C-EN6↔C-VI6; R-EN17↔R-VI11) |
| S030 | S025 | giữ 1–1 | |
| S031 | S026 | giữ 1–1 | "other" ↔ "khác" (R-EN18↔R-VI12, so sánh loại trừ Hoa Kỳ) |
| S032 | S027 | giữ 1–1 | |
| S033 | S028 | giữ 1–1 | "It" (R-EN19) ↔ "Thỏa thuận này" (R-VI13) |
| S034 | S029 | giữ 1–1 | "ratified it" (R-EN20) ↔ "đã phê chuẩn ∅" (E-VI1) — dịch chuyển R→E chủ đạo của cặp |
| S035 | S030 | giữ 1–1 | EN thiếu động từ chính (lỗi nguồn §8); VI dời full intro của Long từ EN S037 lên đây |
| S036 | S031 | giữ 1–1 | EN "The fisherman have" lỗi số (§8); "it" (R-EN21) ↔ "cá" (R→L) |
| S037 | S032 | giữ 1–1 | VI bỏ attribution "said Anthony Long, who runs…" (đã dời lên S030); "that" (R-EN22) ↔ "việc này" (R-VI14); "Therefore"↔"Do đó" |
| S038 | S033 | giữ 1–1 | "It" (R-EN23) ↔ "Việc này" lặp chỉ từ câu kề (không ghi VI); VI "chắc chắc" lỗi chính tả (§8) |
| S039 | S034 | giữ 1–1 | "So"↔"Do đó" (C-EN8↔C-VI8); tái lập thuật ngữ "Port States Measures agreement" ↔ "thỏa thuận về các Biện pháp tại Cảng các Quốc gia" (L §6) |
| S040 | — | bỏ | subhead 3 "Campaign Against Illegal Catches Finds Industry Allies" |
| S041 | — | bỏ | khối cắt: chuỗi cung ứng (Long); EN "Long" tái lập (L §6) |
| S042 | — | bỏ | EN "he said" (R-EN24) chỉ có EN |
| S043 | — | bỏ | EN "your" ref=E (R-EN25) chỉ có EN |
| S044 | — | bỏ | |
| S045 | — | bỏ | |
| S046 | — | bỏ | EN "We're" (R-EN26) chỉ có EN |
| S047 | S035 | giữ 1–1 | tên sách EN đủ phụ đề, VI rút gọn "Người tìm các Chủng loại" (§8) |
| S048 | S036 | giữ 1–1 | VI bỏ "said Conniff" |
| S049 | S037 | giữ 1–1 | "That's" (R-EN27) ↔ "Đó" (R-VI15); "this country" (R-EN28) ↔ "nước này" (R-VI16, conf thấp) |
| S050 | S038 | giữ 1–1 | "the ones" (S-EN1) ↔ "những người" (L general word); "it" (R-EN29) ↔ "tình trạng ấy" (R-VI18); "they" ↔ "họ" (R-VI17) |
| S051 | — | bỏ | khối cắt: Ganapathiraju về hợp tác nhà phân phối; EN "not able obtain" thiếu "to" (§8) |
| S052 | — | bỏ | |
| S053 | — | bỏ | EN "But" (C-EN10) chỉ có EN |
| S054 | — | bỏ | EN "And…they're" (C-EN11, R-EN30) chỉ có EN |
| S055 | — | bỏ | EN "That's the reason" (R-EN31, C-EN12) chỉ có EN |
| S056 | — | bỏ | subhead 4 "Chinese Regulators Expected to Determine Global Approach" |
| S057 | S039 | giữ 1–1 | VI dịch lệch "combating IUU fishing" → "chống lại qui định đánh bắt của IUU"; thiếu dấu cách "tăng- sẽ" (§8) |
| S058 | S040 | giữ 1–1 | VI bỏ "said Trent" |
| S059 | — | bỏ | khối cắt: Conniff về Trung Quốc |
| S060 | — | bỏ | EN "he said" (R-EN32) chỉ có EN |
| S061 | S041 | giữ 1–1 | "Additional" ↔ "thêm" (C-EN13↔C-VI10); "stem the tide" ↔ VI hiện thực hóa "đánh bắt bất hợp pháp" |
| S062 | S042 | giữ 1–1 | EN "the boat" [TC] ↔ VI "những tàu này" [TC] — đều trong câu, không đánh dấu |
| S063 | S043 | giữ 1–1 | "also" ↔ "Cũng" (C-EN14↔C-VI11) |
| S064 | S044 | giữ 1–1 | "It" (R-EN33) ↔ "Hệ thống này" (R-VI19); VI "thay đổi tín hiệu" ↔ EN "switch off beacons" — dịch lệch (§8) |

**Tổng kết bản đồ:** 64 câu EN = **38 giữ 1–1** + **2 gộp** (S004+S005 → VI
S007) + **1 tách** (S026 → VI S020+S021) + **23 bỏ** (19 câu body + 4 subhead,
nằm gọn trong 4 khối: S016–S021, S041–S046, S051–S055, S059–S060, cộng 4
subhead rải rác). 44 câu VI = 41 câu dịch (38 + 1 gộp + 2 tách) + **3 tự sinh**
(S001–S003). `rows.json` có 36 hàng; **15 hàng VI trống** (gộp 2 hàng kề nhau
S016 và S017–S021 thì còn 14 khối cắt — số "14 hàng" của phiếu task đứng trên
cách đếm gộp này). Các tie EN trong khối cắt vẫn đánh dấu đầy đủ; VI để trống,
không bịa tie đối ứng (CONVENTIONS §1).

## 2. Phép tỉnh lược (ellipsis)

| # | Vị trí | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| E-EN1 | ST S003 | "…by South Korean-flagged ships, many ∅ in waters off the coast of West Africa, could bring further sanctions…" | tỉnh lược danh từ sau lượng từ (kiểu "two ∅" của H&H §4.2): "many" giữ vai lượng từ, hạt nhiệm trống, hồi phục {ships} ← "South Korean-flagged ships" **cùng câu**; VI lấp bằng classifier "nhiều chiếc" (S006) — classifier đứng alone không phải tie (mapping §4) nên VI không có hàng | [TC] |
| E-EN2 | ST S020 | "It's saying that they can't look after their own ∅ and their own responsibilities." | tỉnh lược danh từ sau sở hữu + "own" (H&H §4.2): "their own ∅" = người của chính họ (Nam Triều Tiên không trông nổi người/tàu của mình); hồi phục {người dân / ngư dân của họ} từ ngữ cảnh; vế thứ hai "their own responsibilities" là NP đầy đủ — ∅ chỉ ở vế đầu; occ bắt buộc: "their own" ×2 trong câu, ∅ ở lần 1; nằm trong khối cắt nên VI không có đối ứng | [TC] |
| E-VI1 | TT S029 | "10 nước ven biển và EU đã phê chuẩn ∅ nhưng còn cần thêm sự phê chuẩn của 14 nước khác…" | zero bổ ngữ: "đã phê chuẩn" thiếu tân ngữ, hồi phục {thỏa thuận} ← S027 "thỏa thuận các Biện pháp tại Cảng…" / S028 "Thỏa thuận này"; đọc kèm *thế đại từ khiếm diện* (zero theo dõi thực thể) nhưng mã giữ E theo mapping §3.5; EN đối ứng "ratified it" (R-EN20) — dịch chuyển EN đại từ (R) → VI zero (E) | [LC] |

**EN, các ứng viên đã kiểm tra và loại:**
- S005 "cannot sell their seafood in EU countries **nor fish** in member
  countries' waters" — phối hợp VP chia sẻ trợ động từ "cannot" (đối chiếu "can
  sing and dance"), không phải tỉnh lược; VI đối ứng lặp trợ từ "không được…
  và cũng không được…" (hiện thực hóa, không sinh E hai phía);
- S035 "The agreement as an affordable way…, Long argues" — thiếu động từ chính
  do lỗi nguồn (§8); không bịa ∅ từ lỗi nguồn;
- S037 "Therefore to focus on that…" — nguyên mẫu chủ ngữ tổng quát, không truy
  hồi tiền trạm xác định (đối tác VI S032 "cần chú trọng" cũng modal phi nhân);
- S046 "a system that they can use and present to their customers" — phối hợp
  VP chia sẻ tân ngữ, trong câu;
- S051 "not able obtain the same amount of fish" — thiếu "to" là lỗi chính tả
  nguồn (§8);
- S062 "remain the same" — đồng nhất theo thời gian, không truy hồi tiền trạm
  trong văn bản;
- các câu bị động (S004, S030, S061) và câu tồn tại ("There are/There's" S055,
  S060, S063) — thành phần vắng không hồi phục được từ liên văn bản.

**VI, các chỗ trống đã cân nhắc nhưng không đánh dấu:**
- S006 "nhiều **chiếc** hoạt động…" — classifier "chiếc" thay danh từ "tàu
  thuyền": mapping §4 chốt classifier alone không phải tie (đối ứng E-EN1);
- S029 "14 nước **khác**" — so sánh trong cùng câu [TC] (R chỉ [LC]);
- S032 "cần chú trọng" — modal phi nhân không chủ ngữ, không theo dõi nhân vật;
- S042 "đổi tên hay cờ hiệu" — phối hợp chia sẻ động từ "đổi" (đối ứng EN
  "changes names or flags"), không phải E;
- S011 "Các ông làm không đủ" — "làm" không cần tân ngữ nhờ "không đủ" (EN
  "you haven't done enough" cũng vậy);
- bản dịch lấp đầy mọi chỗ EN dùng pro-form/đại từ (S009 chủ ngữ "EU" thay
  "It"; S031 "cá" thay "it"; S038 "những người" thay "the ones") — không bịa ∅
  khi VI đã hiện thực hóa (CONVENTIONS §7.3).

**Nhận định:** tỉnh lược rất hiếm: EN 2 hàng đều **[TC]** (tiền trạm trong
cùng câu — không dùng làm bằng chứng liên kết liên câu), VI 1 hàng **[LC]**
duy nhất ("đã phê chuẩn ∅"). E-VI1 là minh họa chuẩn của dịch chuyển "EN đại
từ → VI zero" (mapping §5); chiều ngược lại (EN lấp đầy chỗ VI zero) không xuất
hiện ở cấp [LC] — VI hầu như hiện thực hóa đầy đủ (lặp danh từ), đúng xu hướng
"ellipsis là chỗ chuyển dịch thất bại nhiều nhất" của Nguyễn Thanh Tùng 2020.

## 3. Phép thế (substitution)

| # | Ngôn ngữ | Nguyên văn | Phân tích | Cấp |
|---|---|---|---|---|
| S-EN1 | EN | "And they are **the ones** who can stop it by insisting that all merchandise be traceable…" (S050) | "the ones" thế danh từ cho **wording** "The distributors" (S048): thay "the ones" bằng "the distributors" vẫn hợp ngữ pháp và cùng referent → thế danh từ (H&H §3.2); khoảng cách 2 câu → [LC]; "they" cùng câu cùng chuỗi nhà phân phối — theo "một chuỗi một mark" chỉ ghi dạng đại diện "the ones" ("they" nêu trong note); VI đối ứng hiện thực hóa bằng danh từ tổng quát "những người" (L general word ← "Các nhà phân phối" S036) + đại từ "họ" (R-VI17) — dịch chuyển S→(L/R) | [LC] |
| — | VI | — | không có pro-form thế nào: không gặp "như vậy/làm vậy/thế/vậy" thay wording trong toàn văn bản | — |

**Các ứng viên đã kiểm tra và loại:**
- EN S025 "That was also the case with…" — "That" truy hồi **mệnh đề** S024
  (phát hiện 40% cá ngừ) → quy chiếu mở rộng, mã R (R-EN15); khả năng đọc
  "the case" là thế danh từ ghi `alt "S: the case"`;
- EN S037 "to focus on **that**" — "that" trỏ sự việc (hành động đưa cá vào
  cảng, S036) → R mở rộng (R-EN22), `alt "S: do that"`;
- EN S051 "the same amount of fish year to year" — so sánh với các năm trước
  (ngoại cảnh thời gian), không truy hồi wording trong văn bản;
- EN S062 "remain the same" — đồng nhất theo thời gian, không phải thế;
- EN S042 "how easy **it** is to manipulate the system" — "it" pro-form vở
  (extraposition/dummy it), không phải tie;
- VI S038 "**những người** có thể chấm dứt tình trạng ấy" — danh từ tổng quát
  (L general word ← "Các nhà phân phối" S036), không phải pro-form thế;
- VI S006 "nhiều **chiếc**" — classifier (đã xử lý ở §2);
- VI "Điều này / Vấn đề này / việc này / tình trạng ấy / Đây / Đó" — demonstrative
  + danh từ tổng quát trỏ sự việc → quy chiếu (mapping §4 "nếu trỏ sự kiện →
  R"), mã R (§4), không phải thế.

**Nhận định:** phép thế gần như vắng mặt ở cặp này: 1 hàng EN duy nhất ("the
ones") và 0 hàng VI. VI không giữ pro-form mà hiện thực hóa bằng danh từ tổng
quát + đại từ ("những người", "họ") — pro-form EN tan vào danh ngữ VI. Cùng xu
hướng với các cặp trước (P13/P17/P19): các "chỗ rỗng" về diễn đạt được giải
quyết bằng quy chiếu mở rộng ("that"/"việc này") hoặc bằng từ vựng (lặp/đồng
nghĩa), không bằng thế. Mật độ thế thấp là đặc trưng thể loại tin tức (vốn ưa
danh từ hóa) cộng thêm xu hướng "VI mang nghĩa ngữ pháp bằng từ vựng" (Nguyễn
Thanh Tùng 2020).

## 4. Phép quy chiếu (reference)

### 4.1. Bảng quy chiếu EN (33 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-EN1 | S005 | those countries | A | S004: Belize, Cambodia and Guinea | demonstrative; nhóm 3 nước câu trước; [−người đơn lẻ, +tập thể quốc gia]; VI đối ứng lặp tên "Belize, Campuchia và Guinea" (S007) — R→L |
| R-EN2 | S007 | It | A | S006: the new tough regulation | personal [−người]; VI đối ứng chủ ngữ "EU" (S009) — R→L (danh từ riêng) |
| R-EN3 | S008 | that | A | S007: "It's beginning to show its teeth." | quy chiếu mở rộng (extended reference) trỏ diễn ngôn "EU bắt đầu ra tay"; VI "đó" (S010, R-VI3) — R↔R |
| R-EN4 | S009 | he said | A | S006: Steve Trent of the Environmental Justice Foundation | đại từ attribution (text đầy đủ "he said" tránh bẫy substring §8.3); gap 3 câu, khép trích dẫn; VI bỏ attribution |
| R-EN5 | S010 | you | A | S009: 'you haven't done enough | ngôi 2 trong trích dẫn nội bộ (Ủy hội nói với Nam Triều Tiên); attribution nội bộ "the European Commission saying" ở câu trước → đủ điều kiện [LC] (CONVENTIONS §1); neo danh riêng: S008 "[South] Korea"; conf med; VI "các ông" (R-VI4) |
| R-EN6 | S010 | us | A | S009: the European Commission saying | ngôi 1 trong trích dẫn nội bộ = người nói (Ủy hội); attribution ở câu trước → đủ điều kiện; VI "chúng tôi" (R-VI5) — ngôi loại trừ |
| R-EN7 | S015 | It says | A | S014: The organization | chuỗi EJF → The organization → It; VI đối ứng "Tổ chức này" (S016) lặp chỉ từ câu kề — không ghi VI |
| R-EN8 | S017 | The other thing | A | S016: repercussions beyond maritime commerce | comparative "other": tác động khác ngoài hệ quả thương mại; conf med; khối cắt |
| R-EN9 | S018 | This | A | S016: If South Korea is given a red card | quy chiếu mở rộng trỏ kịch bản thẻ đỏ; khối cắt |
| R-EN10 | S019 | It | A | S018: This would be an international rebuke | [−người, sự việc]; chuỗi This(S018)–It(S019)–It(S020)–that(S021); khối cắt |
| R-EN11 | S019 | he says | A | S016: the EJF's Trent | đại từ attribution giữa khối trích dẫn (gap 3); khối cắt |
| R-EN12 | S020 | they | A | S019: the country | [+người, tập thể quốc gia]; "their" ×2 cùng câu cùng chuỗi — 1 mark; khối cắt |
| R-EN13 | S021 | that | A | S018: This would be an international rebuke | quy chiếu mở rộng trong khung so sánh "even more damaging… than the embargo"; khối cắt |
| R-EN14 | S024 | It | A | S023: A new study | [−người]; VI "Cuộc nghiên cứu này" (R-VI7) |
| R-EN15 | S025 | That | A | S024: It finds 40 percent of the tuna from Thailand is illegal or unreported | quy chiếu mở rộng trỏ phát hiện 40%; VI "Đây" (R-VI8) — EN distal → VI proximal; alt "S: the case" |
| R-EN16 | S028 | these markets | A | S026: major seafood importing markets | "these importing countries" cùng câu cùng chuỗi — 1 mark; VI "những thị trường này" (R-VI10) |
| R-EN17 | S029 | they | A | S028: these importing countries | "their ports" cùng câu cùng chuỗi — 1 mark; VI "những quốc gia này" (R-VI11) |
| R-EN18 | S031 | other | A | S030: the United States | comparative loại trừ: "most other major import markets" = ngoài Hoa Kỳ; head "import markets" tái lập chuỗi S026 (L, §6) — "other" là liên kết mới tại vị trí; VI "khác" (R-VI12) |
| R-EN19 | S033 | It | A | S032: Port State Measures agreement | [−người]; VI "Thỏa thuận này" (R-VI13) |
| R-EN20 | S034 | it | A | S032: Port State Measures agreement (qua S033 "It") | "ratified it"; VI "đã phê chuẩn ∅" (E-VI1) — R→E |
| R-EN21 | S036 | it | A | S035: illegal fish | [−người]; VI "cá" (S031) — R→L (lặp danh từ) |
| R-EN22 | S037 | that | A | S036: The fisherman have to bring it to port | quy chiếu mở rộng trỏ hành động; VI "việc này" (R-VI14); alt "S: do that" |
| R-EN23 | S038 | It | A | S037: the ports are the obvious place | quy chiếu mở rộng trỏ phương án cảng; VI "Việc này" (S033) lặp chỉ từ câu kề — không ghi VI |
| R-EN24 | S042 | he said | A | S041: Long explains | đại từ attribution câu kề trước; khối cắt |
| R-EN25 | S043 | your | E | (ngoại văn bản — người đọc/người tiêu dùng) | "arrives on your plate": you tổng quát hướng độc giả; attribution ("he said", S042) ở câu trước → đủ điều kiện ghi; referent ngoài văn bản → ref=E; khối cắt; conf med |
| R-EN26 | S046 | We're | A | S045: said Long | ngôi 1 trong trích dẫn, attribution ở câu trước → đủ điều kiện; "we" ("we can build") cùng câu cùng chuỗi — 1 mark; conf med; khối cắt |
| R-EN27 | S049 | That's | A | S048: The distributors are the bottleneck | quy chiếu mở rộng; VI "Đó" (R-VI15) |
| R-EN28 | S049 | this country | A | S043: The U.S. | chỉ từ + danh từ tổng quát; gap 6 câu; conf med; đọc thay thế ref=E (bối cảnh VOA-Mỹ) ghi alt; VI "nước này" (R-VI16, conf thấp) |
| R-EN29 | S050 | it | A | S049: That's where most of the (sea)food comes into this country | quy chiếu mở rộng trỏ dòng hải sản bất hợp pháp; **occ bắt buộc**: "it" ×2 trong S050 (lần 2 "it all be legal" trỏ merchandise — khác chuỗi, [TC]); VI "tình trạng ấy" (R-VI18) |
| R-EN30 | S054 | they're | A | S051: they (received… cooperation from distributors) | [+người] — ngành/nhà cung ứng không đủ cá; chuỗi đại từ gap 3 câu; conf med; khối cắt |
| R-EN31 | S055 | That | A | S054: they're not able to cope with the demand… | quy chiếu mở rộng trỏ mệnh đề nguyên nhân; khối cắt |
| R-EN32 | S060 | he said | A | S059: Conniff said | đại từ attribution câu kề trước; khối cắt |
| R-EN33 | S064 | It | A | S063: a global satellite vessel monitoring system | [−người]; VI "Hệ thống này" (R-VI19) |

### 4.2. Bảng quy chiếu VI (19 hàng)

| # | Câu | Dạng | Hướng | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| R-VI1 | S002 | Điều này | A | S001: Nam Triều Tiên có thể trở thành quốc gia đã phát triển đầu tiên bị cấm bán hải sản cho Châu Âu | danh từ tổng quát "Điều" + chỉ từ "này" trỏ mệnh đề; lede tự sinh — tie VI đứng độc lập (CONVENTIONS §1) |
| R-VI2 | S003 | Vấn đề này | A | S002: nạn đánh bắt cá bất hợp pháp | "Vấn đề" + "này" trỏ vấn nạn (phủ cả S001–S002); tự sinh |
| R-VI3 | S010 | Đó | A | S009: EU bắt đầu đưa ra những lời đe dọa. | chỉ từ "đó" trỏ diễn ngôn S009 (kèm danh từ tổng quát "điều"); EN "that" (R-EN3) — trường hợp hiếm hoi VI **giữ pro-form** thay vì danh ngữ hóa |
| R-VI4 | S012 | các ông | A | S011: 'Các ông làm không đủ | ngôi 2 + honorific "ông" (số nhiều) trong trích dẫn nội bộ; attribution nội bộ "Ủy hội Âu châu nói rằng" ở câu trước → đủ điều kiện; neo danh riêng: S010 "Nam Triều Tiên"; conf med; EN "you" (R-EN5) |
| R-VI5 | S012 | chúng tôi | A | S011: Ủy hội Âu châu nói rằng | ngôi 1 loại trừ = người nói nội bộ (Ủy hội); attribution ở câu trước; EN "us" (R-EN6) |
| R-VI6 | S015 | Tổ chức này | A | S014: Tổ chức Tư pháp Môi trường | lặp danh từ kề + chỉ từ "này" — chỉ từ là liên kết chính; EN đối ứng "The organization" (L general word); "Tổ chức này" S016 lặp cùng dạng câu kề → không ghi (chain continuation) |
| R-VI7 | S018 | Cuộc nghiên cứu này | A | S017: Một cuộc nghiên cứu mới | EN "It" (R-EN14) |
| R-VI8 | S019 | Đây | A | S018: 40% cá ngừ từ Thái Lan là bất hợp pháp hay không được báo cáo | chỉ từ gần trỏ phát hiện; EN "That" (R-EN15) — distal → proximal |
| R-VI9 | S021 | Ông nói | A | S020: ông Pramod Ganapathiraju | đại từ danh xưng "Ông" trong attribution (text "Ông nói" tránh bẫy substring §8.3); EN đối ứng attribution nằm gộp trong S026 (không tách riêng) |
| R-VI10 | S023 | những thị trường này | A | S021: những thị trường nhập khẩu hải sản chính | chỉ từ + lặp danh từ; EN "these markets" (R-EN16); lưu ý "các thị trường này" trong S021 là [TC] (tách câu làm đổi cấp — mô tả §7) |
| R-VI11 | S024 | những quốc gia này | A | S023: tất cả những nước nhập khẩu | chỉ từ + biến thể "quốc gia"←"nước"; EN "they" (R-EN17) — đại từ EN → danh ngữ + chỉ từ VI |
| R-VI12 | S026 | khác | A | S025: Hoa Kỳ | comparative loại trừ: thị trường khác ngoài Hoa Kỳ; EN "other" (R-EN18) |
| R-VI13 | S028 | Thỏa thuận này | A | S027: thỏa thuận các Biện pháp tại Cảng của các Quốc gia | lặp danh từ kề + chỉ từ; EN "It" (R-EN19) |
| R-VI14 | S032 | việc này | A | S031: Ngư dân phải đưa cá vào cảng | danh từ tổng quát + chỉ từ trỏ hành động; EN "that" (R-EN22); "Việc này" S033 lặp cùng dạng câu kề → không ghi (chain continuation) |
| R-VI15 | S037 | Đó | A | S036: Các nhà phân phối là nơi gây tắc nghẽn | chỉ từ trỏ nhận định; EN "That's" (R-EN27) |
| R-VI16 | S037 | nước này | A | S025: Hoa Kỳ | chỉ từ + danh từ tổng quát; gap 12 câu — **conf low**; đọc thay thế ref=E (bối cảnh thị trường Mỹ của cả bài); EN "this country" (R-EN28) |
| R-VI17 | S038 | họ | A | S036: Các nhà phân phối | đại từ nhân xưng ngôi 3 [+người] — ngoại lệ hiếm của văn bản VI; EN "they"/"the ones" (S050) |
| R-VI18 | S038 | tình trạng ấy | A | S037: hầu hết những hải sản vào nước này | danh từ tổng quát + chỉ từ xa "ấy"; EN "it" (R-EN29) |
| R-VI19 | S044 | Hệ thống này | A | S043: một hệ thống theo dõi bằng vệ tinh các tàu thuyền trên thế giới | lặp danh từ kề + chỉ từ; EN "It" (R-EN33) |

### 4.3. Hướng A/C/E

- **A (hồi quy) áp đảo:** EN 32/33, VI 19/19. Mọi quy chiếu đều truy hồi được
  tiền trạm trong văn bản.
- **E (ngoại văn bản):** 1 hàng — R-EN25 (S043 "your plate": bạn đọc/người tiêu
  dùng, theo mô hình you-hướng-độc-giả). R-VI16 "nước này" ghi A nhưng conf
  thấp, alt ref=E (khoảng cách xa). Không có we-ta tác giả đủ điều kiện (EN
  "We" S009 có attribution cùng câu; VI "Chúng ta" S011 không có attribution).
- **C (tiền chỉ):** không đọc được hàng nào; các subhead không tạo cataphora
  cấp câu.

### 4.4. Hệ đại từ / danh xưng / [±người]

- **EN giàu đại từ trong trích dẫn:** It/This/that (quy chiếu mở rộng [−người,
  sự việc] — nhóm lớn nhất: R-EN3/9/10/13/15/22/23/27/29/31), they [+người,
  tập thể] (S020 quốc gia, S029 nước nhập khẩu, S054 ngành), he (attribution
  ×4: R-EN4/11/24/32), ngôi 1/2 (you/us/your/We're — 4 hàng đủ điều kiện).
- **VI gần như bỏ đại từ ngôi 3 cho theo dõi thực thể ngoài trích dẫn:** duy
  nhất "họ" (R-VI17). Mọi theo dõi còn lại bằng **danh từ + chỉ từ** (Tổ chức
  này, Thỏa thuận này, Hệ thống này, Cuộc nghiên cứu này, những quốc gia này,
  những thị trường này) hoặc **danh từ tổng quát + chỉ từ** (Điều này, Vấn đề
  này, việc này, tình trạng ấy, Đây, Đó) — "danh ngữ hóa" như P17/P19.
- **Danh xưng/honorific:** EN xưng nhân vật bằng bare surname (Trent, Long,
  Conniff) hoặc đại từ he; VI luôn "Ông + tên đầy đủ" (S008, S020, S030, S035,
  S039) và một lần "Ông nói" (S021) — khoảng cách trang trọng ổn định. Trong
  trích dẫn nội bộ: EN "you" → VI "các ông" (số nhiều + honorific); EN "us" →
  VI "chúng tôi" (ngôi loại trừ).
- **Lệch ngôi đáng chú ý:** EN S009 "We are seeing" (Trent/EJF) → VI S011
  "Chúng ta đang thấy" (bao gồm người nghe) — dịch chuyển ngôi 1 (độc quyền →
  bao gồm).
- **Deixis:** EN "That" (S025) → VI "Đây" (proximal hóa); EN "That's" (S049) →
  VI "Đó" (giữ distal); EN "it" (S050) → VI "tình trạng ấy" (distal).
- **Đã kiểm tra và loại:** EN "it/its" [TC] (S001 ← Seoul; S016 ← a red card);
  EN "We" S009, "'you" S009 (attribution cùng câu); EN "you" S011, "I" S021
  (attribution cách 2 câu); EN "you" S037 (tổng quát, attribution cùng câu);
  EN "both" S025, "themselves/their" S064 (trong câu); EN "The organization"
  S014, "the report" S026, "the treaty" S034, "The agreement" S035, "these
  other countries" S060, "other destinations" S054, "the pact" S033 (đầu ngữ
  lặp/biến thể từ vựng tiền trạm → L §6, alt "R: the/these/other"); EN "the
  same amount of fish" S051 (so sánh ngoại cảnh); EN "14 others"/"similar
  approval" S034, "all big markets" S043, "the system" S042 (bridging, conf
  thấp); VI "Chúng ta" S011 (VI bỏ attribution "he said" → không đủ điều kiện);
  VI "các ông" S011 (attribution cùng câu), S013 (attribution cách 2 câu); VI
  "Tổ chức này" S016, "Việc này" S033 (lặp cùng dạng câu kề); VI "những tàu
  này" S042, "các thị trường này" S021, "con tàu" S015, "14 nước khác" S029
  (trong câu [TC] — chỉ mô tả, không dùng làm bằng chứng liên câu); VI "nhiều
  chiếc" S006 (classifier); VI "những người" S038 (danh từ tổng quát → L §6).

## 5. Phép nối (conjunction)

### 5.1. Bảng nối EN (14 hàng)

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-EN1 | S008 | And | additive | S007: "It's beginning to show its teeth." | bước tiếp lập luận trong trích dẫn Trent; VI "Và" (C-VI1) |
| C-EN2 | S011 | And | additive | S010: "What you have done doesn't satisfy us." | trích dẫn nội bộ; VI "Và" (C-VI2) |
| C-EN3 | S021 | And | additive | S020: "It's saying that they can't look after their own and their own responsibilities." | khối cắt |
| C-EN4 | S025 | also | additive | S024: It finds 40 percent of the tuna from Thailand is illegal or unreported | cộng thêm phát hiện (cá hồi, cá pôlắc); VI "cũng" (C-VI4) |
| C-EN5 | S028 | But, at the same time | adversative | S027: "The volumes are quite high." | tương phản: khối lượng cao ↔ nhân lực ít; VI "Nhưng đồng thời" (C-VI5), giữ cả hai thành tố |
| C-EN6 | S029 | So | causal | S028: the amount of manpower… is quite low | hệ quả: cần tăng nhân lực; VI "Do đó" (C-VI6) |
| C-EN7 | S037 | Therefore | causal | S036: "The fisherman have to bring it to port." | hệ quả: tập trung vào cảng; VI "Do đó" (C-VI7) |
| C-EN8 | S039 | So | causal | S038: "It's definitely cost effective." | VI "Do đó" (C-VI8) |
| C-EN9 | S050 | And | additive | S049: "That's where most of the (sea)food comes into this country." | VI "Và" (C-VI9) |
| C-EN10 | S053 | But | adversative | S052: "The catches are being depleted." | tương phản: nguồn giảm ↔ cầu tăng; khối cắt |
| C-EN11 | S054 | And | additive | S053: the demand is going up in these export destinations | khối cắt |
| C-EN12 | S055 | the reason | causal | S054: they're not able to cope with the demand because there is so much over-fishing happening… | nhân quả hiện thực bằng **quán từ** "the reason" ("That's the reason they're so open…"), không phải từ nối — vẫn là C theo mapping §3.8 (quan hệ đọc được); khối cắt |
| C-EN13 | S061 | Additional | additive | S032: Port State Measures agreement (và toàn bộ hệ biện pháp đã nêu: thẻ đỏ S004–S005, PSMA S032–S039) | tính từ mang nghĩa cộng thêm mở đoạn kết; conf med; VI "thêm" (C-VI10) |
| C-EN14 | S063 | also | additive | S062: Fishing vessels larger than 100 tons will have to acquire a unique identification number… | VI "Cũng" (C-VI11) |

### 5.2. Bảng nối VI (11 hàng)

| # | Câu | Nguyên văn | Kiểu | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| C-VI1 | S010 | Và | additive | S009: EU bắt đầu đưa ra những lời đe dọa. | đối ứng C-EN1, giữ 1–1 |
| C-VI2 | S013 | Và | additive | S012: Những gì các ông làm không thỏa mãn chúng tôi. | đối ứng C-EN2 |
| C-VI3 | S016 | cũng | additive | S015: Tổ chức này nói Nam Triều Tiên thường xuyên đánh trộm cá… | **VI tự sinh** — EN S015 "It says…" không có "also": nối ngầm EN được hiện thực hóa bằng "cũng" |
| C-VI4 | S019 | cũng | additive | S018: Cuộc nghiên cứu này phát hiện là 40% cá ngừ từ Thái Lan là bất hợp pháp hay không được báo cáo. | đối ứng C-EN4 |
| C-VI5 | S023 | Nhưng đồng thời | adversative | S022: Khối lượng khá cao. | đối ứng C-EN5, giữ 1–1 |
| C-VI6 | S024 | Do đó | causal | S023: số nhân lực cần thiết… thì lại khá thấp trong tất cả những nước nhập khẩu | đối ứng C-EN6 |
| C-VI7 | S032 | Do đó | causal | S031: Ngư dân phải đưa cá vào cảng. | đối ứng C-EN7 |
| C-VI8 | S034 | Do đó | causal | S033: Việc này chắc chắc là giảm bớt tốn kém. | đối ứng C-EN8 |
| C-VI9 | S038 | Và | additive | S037: Đó là nơi hầu hết những hải sản vào nước này. | đối ứng C-EN9 |
| C-VI10 | S041 | thêm | additive | S027: thỏa thuận các Biện pháp tại Cảng… (và toàn bộ hệ biện pháp đã nêu trong bài) | đối ứng C-EN13; nối hiện thực bằng tính từ "thêm" trong "Những thay đổi thêm" |
| C-VI11 | S043 | Cũng | additive | S042: Các tàu đánh cá lớn hơn 100 tấn sẽ phải có một số hiệu nhận diện đặc biệt… | đối ứng C-EN14 |

**Nhận định:**
- **Phần được dịch gần đối xứng:** 10 cặp đối ứng 1–1 giữ nguyên kiểu —
  additive↔additive (6: C-EN1/2/4/9/13/14 ↔ C-VI1/2/4/9/10/11),
  adversative↔adversative (1: C-EN5↔C-VI5), causal↔causal (3: C-EN6/7/8 ↔
  C-VI6/7/8). Chuỗi "So/Therefore" ↔ "Do đó" ×3 (S029↔S024, S037↔S032,
  S039↔S034) tạo nhịp nhân quả dày ở khối thỏa thuận cảng; hai bên đều lặp
  nguyên từ, không đa dạng hóa từ nối.
- **VI tự sinh 1 nối** ("cũng" S016): hiện thực hóa quan hệ cộng thêm còn ngầm
  ở EN (S015 "It says on some of the vessels…" bổ sung tin xấu thứ hai) —
  dịch chuyển "EN nối ngầm → VI hiện thực" (mapping §5).
- **EN-only 4 hàng** (C-EN3, C-EN10, C-EN11, C-EN12) đều nằm trong khối cắt
  (S017–S021, S052–S055) — không phải "mất nối" trong dịch, mà là nội dung bị
  cắt; VI bỏ trống, không bịa tie đối ứng.
- **Không có đổi kiểu nối** trong phần dịch (khác P19 "However"→"Riêng");
  "But, at the same time" ↔ "Nhưng đồng thời" giữ cả hai thành tố (phản thể +
  đồng thời tính). C-EN12 là trường hợp đặc biệt: nhân quả bằng quán từ "the
  reason" thay từ nối — không có đối ứng VI vì khối cắt.
- **Nối trong câu không đánh dấu** (C chỉ [LC]): EN "and" S020/S045/S046, "but"
  S034, "because" S051/S054/S060, "or" S059/S062, "unless" S001/S011, "even
  if" S062, "rather than" S037, "as well as" S054, "in order to" S046, "both…
  and" S026; VI "và cũng không được" S007, "nhưng" S029, "trừ phi" S004/S013,
  "dù… hay" S042, "hay" S044, "và" S019/S038, "hơn là" S032, "thì lại" S023.

*(§6 tiếp theo dưới đây.)*

## 6. Liên kết từ vựng (lexical cohesion)

### 6.1. Chính sách đánh dấu L của cặp này (CONVENTIONS §8.1 + tiền lệ P05/P17)

Chuỗi định nghĩa **hẹp theo tổ hợp từ vựng** (multi-word item): mỗi thuật ngữ
/ tên riêng là một chuỗi riêng ("red card"/"thẻ đỏ", "Port State Measures
agreement", "Tổ chức Tư pháp Môi trường"…). Danh từ đơn **quá tản mát** lặp
dày — "seafood/fish/cá/hải sản" trần (~10 lần mỗi phía), "nations/countries/
nước", "ports/cảng", "fisheries/ngư nghiệp", verba dicendi say/nói/cho biết —
chỉ ghi inventory §6.2, không đánh dấu; riêng **general word/đồng nghĩa mới
vào chuỗi** (the product/sản phẩm, merchandise/hàng hóa) vẫn đánh dấu theo
P17 ("producers"). Quy tắc áp dụng cho P20 (rút từ §8.1 + tiền lệ P05/P17):

1. **Tái lập chuỗi (bất kể cùng dạng hay biến thể) sau khoảng cách ≥ 2 câu**
   → đánh dấu: "the European Union" S026 sau 16 câu; "thẻ đỏ" S007 sau 2 câu;
   "Fishing vessels" S062 sau 25 câu (khung mở–đóng cuối bài); "Trung Quốc"
   S039 sau 17 câu (mở lại chủ đề sau chỗ VI cắt subhead).
2. **Biến thể mới vào chuỗi ở câu kề (gap 0–1)** → chỉ đánh dấu khi là **hạng
   mục từ vựng mới thật sự**: đồng nghĩa (the pact/hiệp ước, penalties/trừng
   phạt, bản phúc trình←study), general word (The organization, những người),
   viết tắt (the EJF, the U.S.), tên lục địa (Europe/Châu Âu), đảo tổ hợp
   (chain of supply, đánh trộm cá←đánh cá trộm), thuật ngữ đầy đủ mới
   ("illegal, unreported and unregulated (IIU) fishing"). **Không** đánh dấu
   khi chỉ rút bớt định ngữ của cùng hạng mục mà chuỗi còn hoạt động ở câu kề
   ("The agreement" S035 ← S032 khi S034 đã có "the treaty"; "thỏa thuận"
   S030 ← S027 khi S029 đã có "hiệp ước" — tiền lệ P05 §6.1 quy tắc 2), và
   khi lặp nguyên dạng câu kề.
3. **Tên riêng**: lặp kề và thành phần liệt kê (South Korea, Trung Quốc trong
   danh sách thị trường S026/S021) → inventory; tái lập chủ thể trung tâm sau
   khoảng cách lớn (Long S041/S044, Conniff S059, Ganapathiraju S051, Trung
   Quốc S039) và **attribution lặp tên người nói sau gap ≥ 2** ("said
   Ganapathiraju" S054) → đánh dấu; attribution kề ("said Conniff" S048,
   "said Trent" S058, "explained Ganapathiraju" S028, "said Long" S045) →
   inventory (tiền lệ P17: Yium S005/S006 kề không đánh dấu).
4. **Bốn subhead EN (S012, S022, S040, S056)** là hàng body (CONVENTIONS §1)
   nhưng theo P17 chỉ là **thành viên inventory**: mỗi subhead được câu body
   đầu đoạn kế tiếp nhận lại chuỗi tương ứng bằng biến thể mới có đánh dấu
   riêng (S013, S023, S041, S057) nên subhead không phát sinh mark riêng,
   tránh đánh dấu hai lần cùng chuỗi tại cùng điểm nối.
5. Một mark/câu/chuỗi; một NP chỉ nhận một hàng (chuỗi đại diện được chọn,
   chuỗi còn lại nêu trong ghi chú — vd "South Korean ships" S013 tính cho
   chuỗi D, thành tố "ships" ghi chú cho chuỗi G). Tiền trạm luôn đứng trước
   câu chứa hàng L.

### 6.2. Kho chuỗi hai phía (inventory — gồm cả thành viên không đánh dấu)

| Chuỗi | Thành viên EN | Thành viên VI | Đánh dấu |
|---|---|---|---|
| A. EU (tổ chức) | the European Union (S001) · the EU fisheries commissioner (S001) · EU red cards (S004 — định ngữ thuộc chuỗi B) · EU countries (S005) · member countries' waters (S005) · EU markets (S006) · for Europe (S006) · the European Commission (S009) · the European Union (S026) · the EU (S034) · The U.S., the European Union (S043) | Châu Âu (S001) · Liên hiệp Châu Âu (S002) · Liên hiệp Châu Âu + ủy viên ngư nghiệp EU (S004) · các nước EU + các nước thành viên EU (S007) · EU (S009) · thị trường EU (S008) · Châu Âu (S008) · Ủy hội Âu châu (S011) · Liên hiệp Châu Âu (S021) · EU (S029) | EN: S006, S009, S026, S034, S043; VI: S002, S007, S008, S011, S021, S029 |
| B. thẻ phạt (red/yellow card) | "red card" (S001) · "yellow card" (S002, thuật ngữ mới — prerequisite) · EU red cards (S004) · The red card (S005, kề) · a red card (S016) | “thẻ đỏ” (S004) · “thẻ vàng” (S005, prerequisite) · thẻ đỏ (S007) | EN: S004, S016; VI: S007 |
| C. đánh bắt bất hợp pháp (IUU) | illegal fishing (S001) · pirate fishing (S004) · illegally caught fish (S006) · Illegal Foreign Catches (S022 subhead) · illegal, unreported and unregulated (IIU) fishing (S023) · illegal or unreported (S024) · illegal catches (S028) · illegal fishing (S033) · illegal fish (S035) · Ending Illegal Fishing Project (S037 — tên riêng dự án) · over-fishing (S045, S054) · illegal fishing (S054) · IUU fishing (S057) · illegal waters (S064) · illicit catches (S064) | đánh bắt cá bất hợp pháp (S002) · đánh bắt bất hợp pháp (S004) · đánh cá trộm (S007) · đánh bắt bất hợp pháp (S008) · đánh trộm cá (S015) · chuyển cá bất hợp pháp (S015 — hành động khác, chỉ inventory) · đánh bắt bất hợp pháp, không báo cáo và không qui định IIU (S017) · bất hợp pháp hay không được báo cáo (S018) · hải sản đánh bắt bất hợp pháp (S023) · Dự án Chấm dứt Đánh bắt bất hợp pháp + cá được đánh bắt bất hợp pháp (S030) · qui định đánh bắt của IUU (S039 — dịch lệch §8j) · đánh bắt bất hợp pháp (S041) · vùng biển bất hợp pháp (S044) · hải sản đánh bắt bất hợp pháp (S044) | EN: S004, S006, S023, S028, S033, S045, S054, S057, S064; VI: S007, S015, S017, S023, S030, S039, S044 |
| D. Nam Triều Tiên | South Korea + Seoul (S001) · South Korean-flagged ships (S003) · [South] Korea (S008) · South Korean ships (S013) · South Korean pirates (S014, kề) · South Korea (S016) · brand Korea (S017) · the country (S019) · they/their (S020, R-EN12) · South Korea (S026 — liệt kê thị trường) | Nam Triều Tiên (S001) · Nam Triều Tiên + Seoul + cờ Nam Triều Tiên (S004) · Nam Triều Tiên (S005, kề) · treo cờ Nam Triều Tiên (S006) · các ông (S011–S013 — ngôi 2 trong trích dẫn, R-VI4) · Nam Triều Tiên (S010) · các tàu thuyền Nam Triều Tiên (S014) · Nam Triều Tiên (S015, kề) · Nam Triều Tiên (S021 — liệt kê thị trường) | EN: S008, S013, S017, S019; VI: S004, S010, S014 |
| E. hải sản/cá (general word) | seafood (S005) · fish (S006) · high-value fish species (S013) · fish (S014) · seafood (S022 subhead, S023) · the product (S026) · seafood imports (S030) · illegal fish (S035) · the fish (S043) · seafood suppliers (S044) · their product (S045) · the (sea)food (S049) · merchandise (S050) · fish (S051) · seafood (S057) — seafood/fish trần tản mát | hải sản (S001) · hải sản nhập khẩu (S003) · hải sản (S007) · hải sản (S017) · nhập khẩu hải sản (S021) · những sản phẩm (S021) · hải sản (S023) · hải sản (S025) · cá (S030, S031) · những hải sản (S037) · hàng hóa (S038) · hải sản (S039) · hải sản (S044) — hải sản/cá trần tản mát | EN: S026 (the product), S050 (merchandise); VI: S021 (sản phẩm), S038 (hàng hóa) |
| F. thị trường/nước nhập khẩu | EU markets (S006) · major seafood importing markets (S026) · these markets + these importing countries (S028, R-EN16) · major import markets (S031) · all big markets (S043) · export destinations (S053) | thị trường EU (S008) · những thị trường nhập khẩu hải sản chính (S021) · các thị trường này (S021, [TC]) · những thị trường này (S023, R-VI10) · tất cả những nước nhập khẩu (S023) · những thị trường nhập khẩu khác (S026) | EN: S026, S031, S043, S053; VI: S021, S026 |
| G. tàu thuyền/ngư dân | boats (S001) · ships (S003) · ships (S013 — tính cho chuỗi D) · local fishermen (S014) · the vessels (S015) · foreign vessels (S033) · The fisherman (S036) · Fishing vessels (S062) · the boat (S062, [TC]) · vessel monitoring system (S063) · vessels (S064, kề) | tàu thuyền (S004) · tàu thuyền + nhiều chiếc (S006 — classifier) · các tàu thuyền Nam Triều Tiên (S014 — tính cho chuỗi D) · con tàu + ngư dân địa phương (S015) · tàu thuyền + các ngư dân trẻ (S016) · các tàu thuyền (S028) · Ngư dân (S031) · các tàu + những tàu này (S042, [TC]) · các tàu thuyền (S043) · những tàu (S044, kề) | EN: S003, S014, S015, S033, S036, S062; VI: S028, S031, S042 |
| H. thỏa thuận cảng (PSMA) | Port State Measures agreement (S032) · It (S033, R-EN19) · the pact (S033) · the treaty (S034) · The agreement (S035) · it (S034, R-EN20) · the Port States Measures agreement (S039) | thỏa thuận các Biện pháp tại Cảng của các Quốc gia (S027) · Thỏa thuận này + ký thỏa thuận (S028, R-VI13) · hiệp ước (S029) · thỏa thuận (S030, rút gọn — inventory) · thỏa thuận về các Biện pháp tại Cảng các Quốc gia (S034) | EN: S033, S034, S039; VI: S029, S034 |
| I. nghiên cứu/phúc trình | A new study (S023) · It (S024, R-EN14) · the report (S026) · A 2009 government report (S030 — tài liệu khác, chỉ inventory) · his research (S051) | một cuộc nghiên cứu mới (S003 — tự sinh) · Một cuộc nghiên cứu mới (S017) · Cuộc nghiên cứu này (S018, R-VI7) · bản phúc trình (S020) · Một phúc trình năm 2009 của chính phủ (S025 — tài liệu khác, chỉ inventory) | EN: S026, S051; VI: S017, S020 |
| J1. Trent + EJF | Steve Trent of the Environmental Justice Foundation (S006) · he said (S009, R-EN4) · the EJF (S013) · The organization (S014) · It says (S015, R-EN7) · the EJF's Trent (S016) · he says (S019, R-EN11) · the EJF's Steve Trent (S057) · said Trent (S058, kề) | Ông Steve Trent thuộc Tổ chức Tư pháp Môi trường (S008) · Tổ chức Tư pháp Môi trường (S014) · Tổ chức này (S015, R-VI6) · Tổ chức này (S016, kề) · ông Steve Trent của Tổ chức Tư pháp Môi trường (S039) | EN: S013, S014, S016, S057; VI: S014, S039 |
| J2. Ganapathiraju | Pramod Ganapathiraju (S026) · explained Ganapathiraju (S028, kề) · Ganapathiraju at UBC (S051) · said Ganapathiraju (S054) | ông Pramod Ganapathiraju (S020) · Ông nói (S021, R-VI9) | EN: S051, S054; VI: — |
| J3. Long | said Anthony Long, who runs the Ending Illegal Fishing Project… (S037) · Long explains (S041) · he said (S042, R-EN24) · Long (S044) · said Long (S045, kề) | Ông Anthony Long (S030 — VI dời attribution lên đây) | EN: S041, S044; VI: — |
| J4. Conniff | Richard Conniff (S047) · said Conniff (S048, kề) · Conniff said (S059) | Ông Richard Conniff (S035) | EN: S059; VI: — |
| K. chế tài/trừng phạt | warning (S002) · further sanctions (S003) · there will be penalties (S011) · an international rebuke (S018) · embargo (S021) | trừng phạt (S004) · cảnh cáo (S005) · chế tài (S006) · lời đe dọa (S009 — inventory) · những trừng phạt (S013) | EN: S003, S011, S018, S021; VI: S005, S006, S013 |
| L. quốc gia (Mỹ, Trung Quốc, nations) | the United States (S023) · the U.S. (S026) · the United States (S030) · The U.S. Senate (S032, kề) · The U.S. (S043) · this country (S049, R-EN28) · China (S025) · China (S026, kề) · China (S057) · the Chinese government (S058, kề) · China (S059, S060, kề) · nations (S033) · other nations (S059) · these other countries (S060) — nations/countries tản mát, chỉ inventory | Hoa Kỳ (S003) · nước Mỹ (S017) · Hoa Kỳ (S021) · Hoa Kỳ (S025) · Thượng viện Hoa Kỳ (S027, kề) · nước này (S037, R-VI16) · Trung Quốc (S019) · Trung Quốc (S021, kề) · Trung Quốc (S039) · chính phủ Trung Quốc (S040, kề) · các nước (S007, S023, S024, S029, S034, S040 — tản mát) | EN: S026, S030, S043, S057; VI: S017, S021, S025, S039 |
| M. nhà phân phối | the distributors (S047) · The distributors (S048, kề) · distributors (S051) | những nơi phân phối (S035) · Các nhà phân phối (S036) · những người (S038, general word) | EN: S051; VI: S036, S038 |
| N. chuỗi cung ứng (EN-only) | the seafood supply chain (S041) · the chain of supply (S043) · the supply chain (S045, kề) · that supply (S043, [TC]) | — (khối cắt) | EN: S043; VI: — |
| O. nhận diện (identification) | identification markings (S014) · a unique identification number (S062) · beacons identifying themselves (S064, kề) | dấu hiệu có thể nhận diện được (S015) · số hiệu nhận diện đặc biệt (S042) · tín hiệu nhận diện hiện tại (S044, kề) | EN: S062; VI: S042 |
| P. quy định (regulation) | the new tough regulation (S006) · Additional regulatory changes (S061) | các qui định nghiêm khắc mới (S008) · qui định đánh bắt của IUU (S039 — dịch lệch, inventory) · Những thay đổi thêm về các qui định (S041) | EN: S061; VI: S041 |
| Q. khác (chỉ inventory) | ports (S030, S033, S036, S037) · tracks/monitoring/surveillance (S006, S029, S063, S064) · fisheries patrols/patrol (S014, S037) · suppliers (S044, S045, S046 — nhóm khác nhà phân phối) · catches (S052) · fisheries (S058, S060) · manpower (S028, S029) · tuna/salmon/pollock (S024) · tên riêng đơn lẻ (Ghana, Curacao, Belize, Cambodia, Guinea, Japan, Thailand, Bangkok, West Africa, Marine Policy, UBC, Pew, U.N. FAO) · verba dicendi · 4 subhead | cảng (S024, S025, S028, S032) · theo dõi/giám sát (S008, S024, S043, S044) · tàu tuần tra/tuần tra (S015, S032) · ngư nghiệp (S004, S015, S020) · cá ngừ/cá hồi/cá pôlắc (S018) · công-ten-nơ (S021) · tên riêng đơn lẻ (Ghana, Curacao, Belize, Campuchia, Guinea, Nhật Bản, Thái Lan, Bangkok, Tây Phi, Chính sách Hàng hải, British Columbia, Pew, Lương Nông Liên hiệp quốc, Steve Herman/VOA S003 tự sinh) · verba dicendi | — |

### 6.3. Các hàng L ghi vào tie table

**EN — 58 hàng** (một mark/câu/chuỗi; tiền trạm luôn đứng trước):

| # | Câu | Nguyên văn | sub | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| L-EN1 | S003 | ships | synonym | S001: boats flying its flag | biến thể boats→ships (gap 1) |
| L-EN2 | S003 | further sanctions | synonym | S002: a "yellow card" warning | đồng nghĩa trường chế tài, câu kề |
| L-EN3 | S004 | EU red cards | repetition | S001: a so-called "red card" | tái lập sau 2 câu + định ngữ EU; alt "R: the" |
| L-EN4 | S004 | pirate fishing | synonym | S001: illegal fishing | đồng nghĩa ẩn dụ; dạng gốc S001 |
| L-EN5 | S006 | for Europe | synonym | S005: EU countries | tên lục địa mới vào chuỗi A; lỗi nguồn "for Europe/." (§8b) |
| L-EN6 | S006 | illegally caught fish | synonym | S004: pirate fishing | tổ hợp participle mới vào chuỗi C |
| L-EN7 | S008 | [South] Korea | repetition | S001: South Korea | rút gọn, tái lập sau 6 câu; ngoặc vuông nguồn (§8p) |
| L-EN8 | S009 | the European Commission | synonym | S006: for Europe | thuật ngữ cơ quan mới vào chuỗi A; conf med |
| L-EN9 | S011 | there will be penalties | synonym | S003: further sanctions | trong trích dẫn nội bộ Ủy hội; tái lập sau 7 câu |
| L-EN10 | S013 | the EJF | repetition | S006: the Environmental Justice Foundation | viết tắt, tái lập sau 6 câu |
| L-EN11 | S013 | South Korean ships | repetition | S008: [South] Korea | tái lập chuỗi D sau 4 câu; "ships" cũng tái lập chuỗi G (gap 9) — một NP một hàng |
| L-EN12 | S014 | The organization | general word | S013: the EJF | alt "R: The" (§1) |
| L-EN13 | S014 | local fishermen | collocation | S013: South Korean ships | biến thể người vào chuỗi G, câu kề |
| L-EN14 | S015 | the vessels | synonym | S013: South Korean ships | vessels mới vào chuỗi G, câu kề |
| L-EN15 | S016 | a red card | repetition | S005: The red card | tái lập sau 10 câu; khối cắt |
| L-EN16 | S016 | the EJF's Trent | repetition | S014: The organization | tái lập tổ chức + người (Trent ← S006); khối cắt |
| L-EN17 | S017 | brand Korea | synonym | S016: South Korea | metonym thương hiệu, câu kề; khối cắt |
| L-EN18 | S018 | an international rebuke | synonym | S011: there will be penalties | tái lập sau 6 câu; khối cắt |
| L-EN19 | S019 | the country | general word | S016: South Korea | đại từ tổng quát hóa quốc gia; khối cắt |
| L-EN20 | S021 | the relatively modest embargo | synonym | S018: an international rebuke | biến thể embargo mới; khối cắt |
| L-EN21 | S023 | illegal, unreported and unregulated (IIU) fishing | repetition | S022: Illegal Foreign Catches (subhead) | thuật ngữ đầy đủ mới; "(IIU)" sai chính tả (§8g); tiền trạm kề là subhead (inventory), dạng gốc S004 |
| L-EN22 | S026 | the European Union | repetition | S009: the European Commission | tái lập sau 16 câu; alt "R: the" |
| L-EN23 | S026 | major seafood importing markets | repetition | S006: EU markets | tái lập chuỗi F sau 19 câu tại attribution |
| L-EN24 | S026 | the product | general word | S023: seafood entering the United States | general word mới vào chuỗi E |
| L-EN25 | S026 | the report | synonym | S023: A new study | đồng nghĩa report←study (§4.4 giao từ R sang L); alt "R: the" |
| L-EN26 | S026 | the U.S. | repetition | S023: the United States | viết tắt, tái lập sau 2 câu |
| L-EN27 | S028 | illegal catches | repetition | S023: illegal, unreported and unregulated (IIU) fishing | biến thể catches, tái lập sau 4 câu |
| L-EN28 | S030 | the United States | repetition | S026: the U.S. | tái lập sau 3 câu; alt "R: the" |
| L-EN29 | S031 | major import markets | repetition | S026: major seafood importing markets | rút gọn + đổi thành tố (importing→import) |
| L-EN30 | S033 | the pact | synonym | S032: Port State Measures agreement | đồng nghĩa mới, câu kề |
| L-EN31 | S033 | foreign vessels | repetition | S015: the vessels | tái lập chuỗi G sau 17 câu |
| L-EN32 | S033 | illegal fishing | repetition | S028: illegal catches | tái lập dạng gốc sau 4 câu |
| L-EN33 | S034 | the treaty | synonym | S033: the pact | đồng nghĩa mới, câu kề; alt "R: the" |
| L-EN34 | S034 | the EU | repetition | S026: the European Union | viết tắt, tái lập sau 7 câu |
| L-EN35 | S036 | The fisherman | repetition | S014: local fishermen | tái lập sau 21 câu; lỗi số nguồn "The fisherman have" (§8e) |
| L-EN36 | S039 | the Port States Measures agreement | repetition | S035: The agreement | tái lập tên gần đầy đủ sau 3 câu; sai chính tả "States" (§8g); alt "R: the" |
| L-EN37 | S041 | Long | repetition | S037: said Anthony Long | tái lập tên sau 3 câu (§1); khối cắt |
| L-EN38 | S043 | The U.S. | repetition | S030: the United States | tái lập sau 12 câu; khối cắt |
| L-EN39 | S043 | the European Union | repetition | S034: the EU | tái lập sau 8 câu; khối cắt |
| L-EN40 | S043 | all big markets | general word | S031: major import markets | big←major (general word); khối cắt |
| L-EN41 | S043 | the chain of supply | repetition | S041: the seafood supply chain | đảo tổ hợp, câu kề; khối cắt |
| L-EN42 | S044 | Long | repetition | S041: Long explains | tái lập tên sau 2 câu; khối cắt |
| L-EN43 | S045 | over-fishing | collocation | S035: illegal fish | biến thể "đánh bắt quá mức" vào chuỗi C sau 9 câu; conf med; khối cắt |
| L-EN44 | S050 | all merchandise | general word | S049: the (sea)food | general word mới, câu kề |
| L-EN45 | S051 | Ganapathiraju at UBC | repetition | S028: explained Ganapathiraju | tái lập tên sau 22 câu; khối cắt |
| L-EN46 | S051 | his research | synonym | S026: the report | đồng nghĩa research←study/report; khối cắt |
| L-EN47 | S051 | distributors | repetition | S048: The distributors | tái lập sau 2 câu; khối cắt |
| L-EN48 | S053 | export destinations | synonym | S043: all big markets | biến thể destinations←markets; khối cắt |
| L-EN49 | S054 | illegal fishing | repetition | S045: over-fishing | tái lập dạng gốc sau 8 câu; "over-fishing" cùng câu cùng chuỗi — 1 mark; khối cắt |
| L-EN50 | S054 | said Ganapathiraju | repetition | S051: Ganapathiraju at UBC | lặp tên người nói trong attribution sau gap 2 (§8.1 iii); khối cắt |
| L-EN51 | S057 | the EJF's Steve Trent | repetition | S016: the EJF's Trent | tái lập người + tổ chức sau 40 câu, mở đoạn (subhead S056 — inventory) |
| L-EN52 | S057 | China | repetition | S026: China | tái lập sau 30 câu, mở đoạn |
| L-EN53 | S057 | IUU fishing | repetition | S023: illegal, unreported and unregulated (IIU) fishing | viết tắt; IIU→IUU biến thể chính tả nguồn (§8g) |
| L-EN54 | S059 | Conniff | repetition | S048: said Conniff | tái lập tên sau 10 câu; khối cắt |
| L-EN55 | S061 | Additional regulatory changes | repetition | S006: the new tough regulation | tái lập trường quy định sau 54 câu — khung mở–đóng của bài |
| L-EN56 | S062 | Fishing vessels | repetition | S033: foreign vessels | tái lập chuỗi G sau 28 câu — khung đóng; "the boat" cùng câu [TC] |
| L-EN57 | S062 | a unique identification number | repetition | S014: identification markings | khung mở–đóng nhận diện sau 47 câu; conf med |
| L-EN58 | S064 | illicit catches | synonym | S057: IUU fishing | illicit←illegal; "illegal waters" cùng câu cùng chuỗi — 1 mark |

**VI — 41 hàng:**

| # | Câu | Nguyên văn | sub | Tiền trạm | Ghi chú |
|---|---|---|---|---|---|
| L-VI1 | S002 | Liên hiệp Châu Âu | synonym | S001: bán hải sản cho Châu Âu | tên đầy đủ mới vào chuỗi A; lede tự sinh — tie VI độc lập (CONVENTIONS §1) |
| L-VI2 | S004 | Nam Triều Tiên | repetition | S001: Nam Triều Tiên có thể trở thành quốc gia đã phát triển đầu tiên | tái lập sau 2 câu; "Seoul" và "cờ Nam Triều Tiên" cùng câu cùng chuỗi |
| L-VI3 | S005 | cảnh cáo | synonym | S004: trừng phạt | đồng nghĩa mới, câu kề |
| L-VI4 | S006 | chế tài | synonym | S005: cảnh cáo | đồng nghĩa mới, câu kề |
| L-VI5 | S007 | các nước EU | repetition | S004: ủy viên ngư nghiệp EU | tái lập sau 2 câu; "các nước thành viên EU" cùng câu |
| L-VI6 | S007 | thẻ đỏ | repetition | S004: “thẻ đỏ” | tái lập sau 2 câu (“thẻ vàng” S005 là thuật ngữ mới — prerequisite, §1) |
| L-VI7 | S007 | đánh cá trộm | synonym | S004: đánh bắt bất hợp pháp | đối ứng EN "pirate fishing" (L-EN4) |
| L-VI8 | S008 | Châu Âu | synonym | S007: các nước EU | tên lục địa mới vào chuỗi A; "thị trường EU" cùng câu (kề, không đánh dấu) |
| L-VI9 | S010 | Nam Triều Tiên | repetition | S006: treo cờ Nam Triều Tiên | tái lập sau 3 câu |
| L-VI10 | S011 | Ủy hội Âu châu | synonym | S008: Châu Âu | thuật ngữ cơ quan mới; đối ứng EN "the European Commission" (L-EN8) |
| L-VI11 | S013 | những trừng phạt | repetition | S006: chế tài | tái lập sau 6 câu (dạng gốc S004) |
| L-VI12 | S014 | Tổ chức Tư pháp Môi trường | repetition | S008: Tổ chức Tư pháp Môi trường | tái lập tên đầy đủ sau 5 câu, mở đoạn (VI cắt subhead EN S012); EN đối ứng viết tắt "the EJF" |
| L-VI13 | S014 | các tàu thuyền Nam Triều Tiên | repetition | S010: Nam Triều Tiên | tái lập chuỗi D sau 3 câu; "tàu thuyền" cũng tái lập chuỗi G (gap 7) — một NP một hàng |
| L-VI14 | S015 | đánh trộm cá | repetition | S007: đánh cá trộm | đảo tổ hợp, tái lập sau 7 câu |
| L-VI15 | S017 | Một cuộc nghiên cứu mới | repetition | S003: một cuộc nghiên cứu mới | tái lập sau 13 câu; tiền trạm nằm trong lede tự sinh |
| L-VI16 | S017 | đánh bắt bất hợp pháp, không báo cáo và không qui định IIU | repetition | S015: đánh trộm cá | thuật ngữ đầy đủ mới (đối ứng L-EN21); "IIU" sai chính tả (§8g) |
| L-VI17 | S017 | nước Mỹ | synonym | S003: Hoa Kỳ | biến thể nước Mỹ←Hoa Kỳ sau 13 câu |
| L-VI18 | S020 | bản phúc trình | synonym | S018: Cuộc nghiên cứu này | đồng nghĩa phúc trình←nghiên cứu (câu cách 1, hạng mục mới) |
| L-VI19 | S021 | Hoa Kỳ | repetition | S017: nước Mỹ | tái lập sau 3 câu (dạng gốc S003) |
| L-VI20 | S021 | những thị trường nhập khẩu hải sản chính | repetition | S008: thị trường EU | tái lập chuỗi F sau 12 câu; "các thị trường này" cùng câu là [TC] (tách câu — §7) |
| L-VI21 | S021 | Liên hiệp Châu Âu | repetition | S011: Ủy hội Âu châu | tái lập sau 9 câu (dạng gốc S002/S004) |
| L-VI22 | S021 | những sản phẩm | general word | S017: hải sản được đưa vào nước Mỹ | general word mới vào chuỗi E (đối ứng L-EN24) |
| L-VI23 | S023 | hải sản đánh bắt bất hợp pháp | repetition | S017: đánh bắt bất hợp pháp, không báo cáo và không qui định IIU | tái lập sau 5 câu |
| L-VI24 | S025 | Hoa Kỳ | repetition | S021: Hoa Kỳ | tái lập sau 3 câu; đối ứng L-EN28 |
| L-VI25 | S026 | những thị trường nhập khẩu khác | repetition | S023: những thị trường này | tái lập sau 2 câu; "tất cả những nước nhập khẩu" cùng câu (R-VI10/11) |
| L-VI26 | S028 | các tàu thuyền | repetition | S016: một số tàu thuyền | tái lập chuỗi G sau 11 câu; đối ứng L-EN31 |
| L-VI27 | S029 | hiệp ước | synonym | S028: Thỏa thuận này | đồng nghĩa mới, câu kề; đối ứng L-EN33 |
| L-VI28 | S029 | EU | repetition | S021: Liên hiệp Châu Âu | viết tắt, tái lập sau 7 câu |
| L-VI29 | S030 | cá được đánh bắt bất hợp pháp | repetition | S023: hải sản đánh bắt bất hợp pháp | tái lập sau 6 câu; occ 2 — "Dự án Chấm dứt Đánh bắt bất hợp pháp" cùng câu cùng chuỗi |
| L-VI30 | S031 | Ngư dân | repetition | S015: ngư dân địa phương | tái lập chuỗi G (dạng người) sau 15 câu; đối ứng L-EN35; "các tàu thuyền" S028 cũng thuộc chuỗi |
| L-VI31 | S034 | thỏa thuận về các Biện pháp tại Cảng các Quốc gia | repetition | S030: thỏa thuận (xem thỏa thuận như là) | tái lập tên đầy đủ sau 3 câu (§1); "thỏa thuận" S030 là rút gọn kề — inventory |
| L-VI32 | S036 | Các nhà phân phối | synonym | S035: những nơi phân phối | biến thể mới, câu kề |
| L-VI33 | S038 | tất cả hàng hóa | general word | S037: những hải sản | general word mới (đối ứng L-EN44) |
| L-VI34 | S038 | những người | general word | S036: Các nhà phân phối | theo §3 (đối ứng S-EN1 "the ones"); "họ" cùng câu là R-VI17 |
| L-VI35 | S039 | ông Steve Trent của Tổ chức Tư pháp Môi trường | repetition | S008: Ông Steve Trent thuộc Tổ chức Tư pháp Môi trường | tái lập người + tổ chức sau 30 câu, mở đoạn; đối ứng L-EN51 |
| L-VI36 | S039 | IUU | repetition | S017: IIU | tái lập sau 21 câu; IIU→IUU (§8g); nằm trong cụm dịch lệch "qui định đánh bắt của IUU" (§8j) |
| L-VI37 | S039 | Trung Quốc | repetition | S021: Trung Quốc | tái lập sau 17 câu, mở đoạn; đối ứng L-EN52 |
| L-VI38 | S041 | Những thay đổi thêm về các qui định | repetition | S008: các qui định nghiêm khắc mới | tái lập trường quy định sau 32 câu — khung đóng; đối ứng L-EN55 |
| L-VI39 | S042 | Các tàu đánh cá | repetition | S031: Ngư dân | tái lập chuỗi G sau 10 câu (dạng tàu ← S028); "những tàu này" cùng câu [TC]; đối ứng L-EN56 |
| L-VI40 | S042 | số hiệu nhận diện đặc biệt | repetition | S015: dấu hiệu có thể nhận diện được | khung mở–đóng nhận diện sau 26 câu; conf med; đối ứng L-EN57 |
| L-VI41 | S044 | hải sản đánh bắt bất hợp pháp | repetition | S039: qui định đánh bắt của IUU | tái lập dạng gốc sau 4 câu; "vùng biển bất hợp pháp" cùng câu cùng chuỗi — 1 mark |

**Các ứng viên đã kiểm tra và loại (không đánh dấu):** "The agreement" S035
(rút định ngữ của S032, chuỗi còn "the treaty" S034 — P05 quy tắc 2); "thỏa
thuận" S030 (tương tự, chuỗi có "hiệp ước" S029); "these other countries"
S060 ← "other nations" S059 và "other destinations" S054 ← S053 (biến thể
kề của trường danh từ đơn tản mát nations/countries/destinations — §4.4 đã
cân nhắc alt "R: these/other", chuyển về inventory); "The red card" S005,
"said Conniff" S048, "said Trent" S058, "explained
Ganapathiraju" S028, "said Long" S045, "the Chinese government" S058,
"China" S059/S060 (lặp kề); "South Korea" S026 / "Trung Quốc" S021 /
"Nam Triều Tiên" S021 (thành phần liệt kê thị trường); "EU" S009, "Tổ chức
này" S016, "Việc này" S033, "Nam Triều Tiên" S005/S006/S015, "tàu thuyền"
S016, "các ngư dân trẻ" S016 (lặp kề nguyên dạng/gia đình hình thái);
"the (sea)food" S049, "their product" S045 (biến thể kiểu gõ/trong câu
product ×2); "the system" S042 (bridging, conf thấp — §4.4); "A 2009
government report" S030 / "Một phúc trình năm 2009" S025 (lặp từ "report/
phúc trình" nhưng **tài liệu khác** — báo cáo chính phủ Mỹ 2009 ≠ nghiên cứu
Marine Policy; không đánh dấu để tránh đọc nhầm đồng quy chiếu); "Ending
Illegal Fishing Project" S037 (tên riêng dự án chứa "Illegal Fishing");
suppliers S044–S046 (nhóm nhà cung ứng ≠ nhà phân phối); seafood/fish/cá/
hải sản trần, nations/countries/nước, ports/cảng, fisheries/ngư nghiệp,
theo dõi/monitoring, tuần tra (danh từ đơn tản mát — quy tắc §6.1); 4
subhead (quy tắc 4).

### 6.4. Nhận định

- **Quy mô:** L-EN 58 hàng / L-VI 41 hàng — hạng mục lớn nhất hai phía
  (54%/57% tổng tie). Mật độ L/câu xấp xỉ (EN 0,91; VI 0,93): VI nén chuỗi
  vào bản dịch ngắn hơn (44 câu) nên đậm tương đương dù mất hẳn 4 khối.
- **Chuỗi chủ đạo:** C (đánh bắt bất hợp pháp/IUU) dày nhất (EN 9, VI 7) và
  **đối xứng từng vị trí dịch** — hai bên giữ ổn định cặp thuật ngữ (illegal
  fishing ↔ đánh bắt bất hợp pháp; pirate fishing ↔ đánh cá trộm; IUU ↔
  IIU/IUU với cùng lỗi chính tả hai phía). Chuỗi A (EU) là nơi VI đa dạng hóa
  danh xưng hơn (Châu Âu → Liên hiệp Châu Âu → EU → Ủy hội Âu châu) nên VI
  6 hàng, EN 5.
- **Ảnh hưởng 4 khối cắt:** 20/58 hàng L-EN nằm gọn trong 4 khối (S016–S021:
  6; S041–S046: 7; S051–S055: 6; S059–S060: 1) — các chuỗi chỉ tồn tại EN
  (rebuke/embargo, chuỗi cung ứng, export destinations, Conniff tái lập)
  không phải "mất liên kết khi dịch" mà là nội dung bị cắt; VI trống, không
  bịa tie đối ứng. Phía VI không có hàng nào không neo được trừ các hàng
  chạm lede tự sinh (L-VI1 ← S001; L-VI15 tiền trạm S003).
- **Hội tụ:** VI hội tụ nơi EN viết tắt ("the EJF" ↔ "Tổ chức Tư pháp Môi
  trường" nguyên dạng; "the U.S." ↔ "Hoa Kỳ") và hai bên cùng giữ hai khung
  mở–đóng lớn: nhận diện (identification markings S014 → a unique
  identification number S062 ↔ dấu hiệu nhận diện S015 → số hiệu nhận diện
  S042) và quy định (the new tough regulation S006 → regulatory changes
  S061 ↔ các qui định nghiêm khắc mới S008 → thay đổi qui định S041).
- **Phân rã có kiểm soát:** chuỗi H hai bên cùng phân rã đồng nghĩa nối tiếp
  (agreement → pact → treaty ↔ thỏa thuận → hiệp ước) — mỗi biến thể mới đều
  có hàng, chuỗi không bao giờ đứt; phân rã duy nhất bất đối xứng là IIU
  (S023) → IUU (S057), VI lặp lại đúng từng lỗi (§8g).
- **Câu đậm nhất:** EN S026 (attribution Ganapathiraju + liệt kê 4 thị
  trường) tái lập đồng thời 5 chuỗi (A, E, F, I, L); VI tách thành S020+S021
  nên 4 hàng tương ứng dồn vào S021 — ví dụ rõ nhất việc tách câu làm dày
  mật độ L/câu phía VI.

*(Hết §6.)*

## 7. Các dịch chuyển liên kết nổi bật (tổng hợp)

| Kiểu dịch chuyển | Số lần | Ví dụ nguyên văn hai đầu |
|---|---:|---|
| EN đại từ [−người] → VI danh từ + chỉ từ (R↔R, "danh ngữ hóa") | 6 | EN S024 "It finds 40 percent of the tuna from Thailand is illegal or unreported" ↔ VI S018 "Cuộc nghiên cứu này phát hiện là 40% cá ngừ từ Thái Lan là bất hợp pháp"; EN S033 "It is designed to keep foreign vessels…" ↔ VI S028 "Thỏa thuận này nhắm mục đích loại trừ các tàu thuyền…"; EN S064 "It would be able to track vessels…" ↔ VI S044 "Hệ thống này sẽ có khả năng theo dõi những tàu…" |
| EN demonstrative/đại từ → VI lặp danh từ (R→L) | 3 | EN S005 "The red card means those countries cannot sell their seafood" ↔ VI S007 "cấm Belize, Campuchia và Guinea không được bán hải sản"; EN S007 "It's beginning to show its teeth" ↔ VI S009 chủ ngữ "EU"; EN S036 "The fisherman have to bring it to port" ↔ VI S031 "Ngư dân phải đưa cá vào cảng" |
| EN đại từ tân ngữ → VI ∅ (R→E) | 1 | EN S034 "Ten coastal countries and the EU have already ratified it" ↔ VI S029 "10 nước ven biển và EU đã phê chuẩn ∅" (E-VI1) |
| Giữ quy chiếu mở rộng pro-form 1–1 | 3 | EN S008 "And that is what is happening with regard to [South] Korea" ↔ VI S010 "Và đó là điều đang xảy ra đối với Nam Triều Tiên"; EN S025 "That was also the case with 70 percent of salmon imports" ↔ VI S019 "Đây cũng là trường hợp của 70% cá hồi nhập khẩu"; EN S049 "That's where most of the (sea)food comes into this country" ↔ VI S037 "Đó là nơi hầu hết những hải sản vào nước này" |
| Đổi khoảng cách deixis (EN distal → VI proximal) | 1 | EN S025 "That was also the case" ↔ VI S019 "Đây cũng là trường hợp" (That→Đây); đối chứng giữ distal: EN S049 "That's" ↔ VI S037 "Đó"; EN S050 "it" ↔ VI S038 "tình trạng ấy" (distal hóa + danh từ tổng quát) |
| EN "the" + đầu ngữ lặp/biến thể → hàng L có alt "R: the" | 6 | EN S014 "The organization" / S026 "the report" / S026 "the European Union" / S030 "the United States" / S034 "the treaty" / S039 "the Port States Measures agreement" ↔ VI "Tổ chức này" (R-VI6) / "bản phúc trình" / "Liên hiệp Châu Âu" / "Hoa Kỳ" / "hiệp ước" / "thỏa thuận về các Biện pháp tại Cảng các Quốc gia" |
| Viết tắt EN ↔ tên đầy đủ VI (bất đối xứng inventory) | 2 | EN S013 "the EJF has documented" ↔ VI S014 "Tổ chức Tư pháp Môi trường đã ghi nhận"; EN S026 "the U.S. and other major seafood importing markets" ↔ VI S021 "Hoa Kỳ và những thị trường nhập khẩu hải sản chính" |
| Nối giữ 1–1 cùng kiểu | 10 | "And"↔"Và" (S008/S010, S011/S013, S050/S038); "also"↔"cũng" (S025/S019, S063/S043); "But, at the same time"↔"Nhưng đồng thời" (S028/S023); "So/Therefore"↔"Do đó" ×3 (S029/S024, S037/S032, S039/S034); "Additional"↔"thêm" (S061/S041) |
| VI tự sinh nối (hiện thực hóa nối ngầm EN) | 1 | EN S015 "It says on some of the vessels, workers as young as 14 are forced…" ↔ VI S016 "Tổ chức này cũng nói trên một số tàu thuyền, các ngư dân trẻ khoảng 14 tuổi bị buộc…" ("cũng" = C-VI3) |
| VI bỏ / dời attribution | 5 | EN S009 "…," he said." (VI S011 bỏ); EN S028 "…," explained Ganapathiraju." (bỏ); EN S037 "…," said Anthony Long, who runs the Ending Illegal Fishing Project for the Pew Charitable Trust." (toàn bộ intro dời lên S030 "Ông Anthony Long, điều hành Dự án…"); EN S048 "…," said Conniff." (bỏ); EN S058 "…," said Trent." (bỏ) |
| VI tách câu attribution → đổi cấp liên kết [LC]→[TC] | 1 | EN S026 một câu attribution ("The lead author of the report… said the U.S. and other major seafood importing markets… see most of the product…") ↔ VI tách S020 "Tác giả đứng đầu bản phúc trình là ông Pramod Ganapathiraju…" + S021 "Ông nói…"; hệ quả: EN "these markets" S028 [LC] (R-EN16) ↔ VI "các thị trường này" S021 [TC] |
| VI tự sinh lede + attribution | 3 câu | VI S001–S003 "BANGKOK — Tháng tới, Nam Triều Tiên có thể trở thành quốc gia đã phát triển đầu tiên bị cấm bán hải sản cho Châu Âu…"; "Thông tín viên Steve Herman thuộc văn phòng Đông Nam Á của Đài VOA ở Bangkok tường trình chi tiết." — không có đối ứng EN; tie VI (R-VI1/2, L-VI1) đứng độc lập |
| Ẩn dụ EN → thuật ngữ VI (hiện thực hóa) | 1 | EN S061 "Additional regulatory changes are being implemented to try to stem the tide." ↔ VI S041 "Những thay đổi thêm về các qui định đang được thực hiện để ngăn chặn việc đánh bắt bất hợp pháp." |
| Lệch ngôi / honorific trong trích dẫn | 3 | EN S009 "We are seeing the European Commission saying" ↔ VI S011 "Chúng ta đang thấy Ủy hội Âu châu nói rằng" (ngôi 1 độc quyền → bao gồm); EN S010 "What you have done doesn't satisfy us." ↔ VI S012 "Những gì các ông làm không thỏa mãn chúng tôi." (you→các ông honorific; us→chúng tôi loại trừ) |
| EN tỉnh lược lượng từ [TC] → VI classifier (không sinh tie VI) | 1 | EN S003 "many ∅ in waters off the coast of West Africa" (E-EN1) ↔ VI S006 "nhiều chiếc hoạt động trong vùng biển ngoài khơi Tây Phi" (classifier — mapping §4) |
| EN cắt khối / subhead (VI trống) | 4 khối + 4 subhead | S016–S021 (Trent 2 "brand Korea"), S041–S046 (chuỗi cung ứng), S051–S055 (Ganapathiraju 2), S059–S060 (Conniff về Trung Quốc) + subhead S012/S022/S040/S056 — 23 câu EN không dịch; 20/58 hàng L-EN và 12/33 hàng R-EN nằm gọn trong 4 khối |

**Nhận định:** phần được dịch gần như "trong suốt" về nối (10/10 đối ứng giữ
kiểu) và giải quyết mọi chỗ rỗng diễn đạt EN bằng **danh ngữ hóa** (danh từ +
chỉ từ) hoặc lặp danh từ — không có chiều ngược "EN lấp đầy chỗ VI zero" nào
ở cấp [LC]. Hai dịch chuyển có tính cấu trúc nhất của cặp: (i) **bỏ
attribution** (5 lần) làm EN giàu hàng R-EN4/11/24/32 + hàng L tên nhân vật
mà VI không có; (ii) **tách S026 → S020+S021** dồn 4 hàng L vào một câu VI,
đảo ngược vị trí đậm nhất của bài.

*(Hết §7.)*

## 8. Bất thường dữ liệu nguồn (cần ghi chú khi thống kê)

- **(a) Không URL nguồn:** `meta.json` có `en_url`/`vi_url` rỗng hai phía —
  bất thường đã ghi nhận từ bước chuẩn hóa (xem phần Lưu ý nguồn đầu file);
  không bịa URL; không ảnh hưởng tie.
- **(b) EN S006 cụt + dấu lạ:** "praised the new tough regulation for
  Europe/." — dấu "/" lạc và câu thiếu vế so với bản dịch (VI S008 "ca ngợi
  các qui định nghiêm khắc mới của Châu Âu"). Không dùng làm bằng chứng về
  ranh giới mệnh đề/câu; từ "Europe" còn nguyên vẹn nên hàng L-EN5 vẫn trích
  được.
- **(c) EN S035 thiếu động từ chính:** "The agreement as an affordable way to
  stop illegal fish from entering the global market, Long argues." — thiếu
  "is"; §2 đã loại không bịa ∅ từ lỗi nguồn. NP "The agreement" và "illegal
  fish" (tiền trạm của L-EN43) còn nguyên — dùng được làm tiền trạm; cấu trúc
  câu không dùng làm bằng chứng cấp câu.
- **(d) EN S037 "draw" khả nghi:** "…you need to patrol out at sea or draw in
  space [satellite] surveillance" — "draw" gần như chắc chắn lỗi gõ của
  "drone"; "[satellite]" là chèn biên tập (VI S032 dịch "theo dõi bằng vệ
  tinh"). Không dùng "draw" làm bằng chứng cấp câu.
- **(e) EN S036 lỗi số:** "The fisherman have to bring it to port." — số ít
  đi với "have". Hàng L-EN35 đánh dấu trên hình thức nguyên văn "The
  fisherman"; ghi chú lỗi, không sửa nguyên văn.
- **(f) EN S051 thiếu "to":** "they are not able obtain the same amount of
  fish year to year" — lỗi nguồn; nằm trong khối cắt nên không ảnh hưởng tie
  VI.
- **(g) Sai chính tả "IIU"/"IUU" hai phía:** EN S023 "(IIU)", VI S017 "IIU"
  (đúng: IUU); EN S057 và VI S039 viết đúng "IUU" — biến thể chính tả của
  chính nguồn, trích nguyên văn kèm lỗi (L-EN21/53, L-VI16/36); tương tự EN
  S039 "Port State**s** Measures" (thiếu dấu so với S032 "Port State
  Measures").
- **(h) VI S033 thiếu dấu:** "Việc này chắc chắc là giảm bớt tốn kém" —
  "chắc chắc" (đúng: chắc chắn); nguyên văn giữ khi trích (đã dẫn trong
  C-VI8).
- **(i) VI thiếu dấu cách:** S003 "…hay không có giấy tờ hợp lệ.Thông tín
  viên Steve Herman…" — hai câu thật dính thành MỘT câu sentmap (ranh giới
  theo sentmap; không dùng ranh giới bên trong S003 làm bằng chứng cấp câu);
  S039 "ngày càng tăng- sẽ" — dấu gạch nối + khoảng trắng lạc.
- **(j) VI dịch lệch nghĩa:** S039 "chống lại qui định đánh bắt của IUU" (EN
  S057: "combating IUU fishing" — đánh bắt kiểu IUU, không phải "qui định
  của IUU"); S044 "thay đổi tín hiệu nhận diện hiện tại" (EN S064: "switch
  off existing beacons" — tắt, không phải thay đổi); S035 tên sách rút phụ
  đề: "Người tìm các Chủng loại" ← "Species Seekers: Heroes, Fools, and the
  Mad Pursuit of Life on Earth". Các hàng tie tại đây (L-VI36, L-VI41…) ghi
  theo nguyên văn VI nhưng **không dùng làm bằng chứng cho nghĩa phía EN**.
- **(k) VI tự sinh số liệu + lede:** S003 "một phần 3 hải sản nhập khẩu được
  đánh bắt bất hợp pháp" — không có đối ứng EN (EN chỉ có 40% / 70% / 45% /
  2% / 85%); cả lede S001–S003 + attribution "Thông tín viên Steve Herman…
  Đài VOA" là khối tự sinh — tie VI tại đây (R-VI1/2, L-VI1) đứng độc lập,
  không dùng làm bằng chứng phía EN.
- **(l) VI bỏ 5 attribution:** "he said" (S009), "explained Ganapathiraju"
  (S028), "said Anthony Long, who runs…" (S037 — nội dung dời lên S030),
  "said Conniff" (S048), "said Trent" (S058) — hệ quả: EN có 4 hàng R
  attribution + 9 hàng L tên nhân vật/tổ chức, VI gần như không có (chỉ
  "Ông nói" S021 = R-VI9).
- **(m) rows.json — đếm lại bằng công cụ (`json.load`):** **35 hàng** (không
  phải 36 như ghi ở §1), ô `vi` trống **14** (khớp phiếu khảo sát 35/14,
  không phải 15): 4 hàng subhead + 10 hàng khối body gộp chứa đúng 19 câu
  body bị cắt; ô `en` trống 1 (hàng 0 — lede VI tự sinh). Số "36 hàng / 15
  hàng VI trống" ở §1 là đếm nhầm; mọi đối chiếu câu–bảng trong §6 dùng
  sentmap (64 câu EN / 44 câu VI) làm chuẩn.
- **(n) 4 subhead EN (S012, S022, S040, S056):** là hàng body theo
  CONVENTIONS §1 nhưng VI cắt toàn bộ; theo chính sách §6.1 chỉ là thành
  viên inventory (chuỗi do câu body đầu đoạn đảm nhiệm), không dùng làm bằng
  chứng cấp câu phía VI.
- **(o) 4 khối cắt (S016–S021, S041–S046, S051–S055, S059–S060):** EN đánh
  dấu đầy đủ (20 hàng L, 12 hàng R, 4 hàng C, 1 hàng E nằm gọn trong khối),
  VI để trống — không bịa tie đối ứng (CONVENTIONS §1).
- **(p) Lỗi gõ nhỏ khác:** EN S008 "[South] Korea" (ngoặc vuông biên tập —
  trích nguyên văn trong L-EN7); EN S009 dấu trích lẫn kiểu ("'you haven't
  done enough," — mở đơn đóng kép); "Curacao" không dấu ç hai phía (S002/
  S005); EN segmenter **không** chẻ câu tại "U.S."/"U.N." (S026, S032 giữ
  nguyên trong câu) — không có trường hợp CONVENTIONS §8.3 phải gộp câu.

*(Hết §8.)*

## 9. Đối chiếu số đếm: phân tích tay ↔ tie table

| Chỉ số | Đọc tay | Đã ghi tie table | Ghi chú |
|---|---:|---:|---|
| EN — R | 33 | | §4.1 (R-EN1–EN33); 32 hướng A + 1 E (R-EN25); 4 hàng attribution "he said/he says"; 12 hàng nằm trong khối cắt |
| EN — S | 1 | | §3 (S-EN1 "the ones", [LC]); không có S [TC] |
| EN — E | 2 | | §2 (E-EN1, E-EN2) — **đều [TC]**, không dùng làm bằng chứng liên câu; E-EN2 trong khối cắt |
| EN — C | 14 | | §5.1 (C-EN1–EN14); 4 hàng trong khối cắt; 10 hàng đối ứng 1–1 với VI |
| EN — L | 58 | | §6.3 theo chính sách §6.1; 6 hàng có alt "R: the"; 20 hàng trong khối cắt; chuỗi đậm nhất: C (9), G (6), J (9), A (5) |
| VI — R | 19 | | §4.2 (R-VI1–VI19); toàn bộ hướng A; 2 hàng neo trong lede tự sinh (R-VI1/2) |
| VI — S | 0 | | §3: không có pro-form thế |
| VI — E | 1 | | §2 (E-VI1 "đã phê chuẩn ∅", [LC]) — minh họa R→E |
| VI — C | 11 | | §5.2 (C-VI1–VI11); 1 hàng tự sinh ("cũng" S016 = C-VI3); 10 hàng đối ứng 1–1 |
| VI — L | 41 | | §6.3 theo chính sách §6.1; chuỗi đậm nhất: C (7), A (6), L (4), D/G/H/K (3) |

**Kết luận:**

- **Từ vựng là thiết bị chủ lực của cặp cắt mạnh nhất này:** L chiếm 58/108
  tie EN (54%) và 41/72 tie VI (57%); mật độ 1,69 tie/câu EN và 1,64 tie/câu
  VI — đậm nhất trong các cặp đã phân tích, phản ánh tin chính sách VOA với
  hệ thuật ngữ dày (thẻ đỏ/thẻ vàng, IUU, PSMA) lặp có chủ đích.
- **Chênh lệch L (58 vs 41) chủ yếu do cắt, không do phân rã khi dịch:**
  20/58 hàng L-EN nằm gọn trong 4 khối cắt; phần được dịch giữ chuỗi gần đối
  xứng từng vị trí (thẻ đỏ S004/S007; thuật ngữ IUU hai phía; chuỗi PSMA
  biến thể đồng nghĩa song song; hai khung mở–đóng nhận diện và quy định được
  VI giữ nguyên vẹn).
- **R→danh ngữ hóa là dịch chuyển hệ thống:** trong 18 cặp R có đối ứng, VI
  chỉ giữ pro-form 3 lần ("đó/Đây/Đó"); 6 cặp đổi sang danh từ + chỉ từ
  ("It" → "Cuộc nghiên cứu này/Thỏa thuận này/Hệ thống này"), 3 cặp R→L, 1
  cặp R→E — đây là nguồn chính của chênh lệch R (33 vs 19) và của việc VI
  gần như không có đại từ ngôi 3 (duy nhất "họ" R-VI17).
- **S/E gần như vắng ở cấp liên câu:** EN S1 [LC] + E2 đều [TC]; VI S0 + E1
  [LC]. Các hiện tượng [TC] (E-EN1/2; VI "các thị trường này" S021, "những
  tàu này" S042, "con tàu" S015, "nhiều chiếc" S006, "14 nước khác" S029)
  chỉ mang tính mô tả, **không dùng làm bằng chứng cho bất kỳ kết luận nào về
  liên kết liên câu** (CONVENTIONS §5).
- Số "Đọc tay" ở trên là chuẩn để lấp tie table (cột "Đã ghi tie table" để
  trống chờ cổng QC `pipeline.annotate`/`render`); lưu ý số liệu đúng của
  `rows.json` là **35 hàng / 14 ô VI trống** (§8m), khác số đếm ghi ở §1 —
  cần hiệu chỉnh khi thống kê khảo sát.

*(Hết §9 — hoàn chỉnh §1–§9 cho P20.)*
