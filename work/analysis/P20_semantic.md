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

*(Hết §5. §6–§9 — liên kết từ vựng, dịch chuyển, bất thường nguồn, đối chiếu
số đếm — do task kế tiếp viết nối vào file này.)*
