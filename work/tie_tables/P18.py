# P18 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P18_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)

ST = [
    # ---------- R (reference) — 7 hàng, §4.1 ----------
    ("S003", "the group", "R", "demonstrative", "S002: UNICEF", "high", None,
     "danh ngữ mô tả mới; 'the' là liên kết duy nhất (CONVENTIONS §1); VI đối "
     "ứng 'tổ chức này' cùng câu → [TC], không đánh dấu", 1, None, None,
     "LC", "A"),
    ("S007", "the area", "R", "demonstrative", "S006: Rakhine", "high", None,
     "'the' + danh từ tổng quát mới; VI hiện thực hóa 'những vùng có bạo "
     "động' (R→L)", 1, None, None, "LC", "A"),
    ("S015", "other", "R", "comparative",
     "S014: we as an organization", "med", None,
     "so sánh chung (H&H): 'other agencies' ≠ tổ chức của người nói; VI 'khác' "
     "đối ứng; 'also still' gộp nghĩa phụ gia của 'And'", 1, None, None,
     "LC", "A"),
    ("S016", "this", "R", "demonstrative",
     "S014: deliver this life-saving support that we … provide to children "
     "(S015: doing the same thing)", "med", None,
     "quy chiếu mở rộng tới hoạt động cứu trợ; VI 'việc này' đối ứng",
     1, None, None, "LC", "A"),
    ("S020", "those concerns", "R", "demonstrative",
     "S018: some regions are still struggling to recover in the Philippines "
     "(S019: children are still affected by decades of conflict)", "high",
     None,
     "demonstrative số nhiều gom hai mối lo ngại Philippines; VI 'Những mối "
     "quan tâm đó'", 1, None, None, "LC", "A"),
    ("S021", "This", "R", "demonstrative",
     "S020: UNICEF looking to raise $11 million (chuỗi kêu gọi S004/S012)",
     "med", None,
     "quy chiếu mở rộng tới tổng thể các khoản kêu gọi theo nước; VI hiện thực "
     "hóa 'Những khoản quyên góp vừa kể'", 1, None, None, "LC", "A"),
    ("S022", "the money", "R", "demonstrative",
     "S021: a global appeal totaling $3.1 billion", "med", None,
     "'the' + danh từ tổng quát mới 'money' — liên kết duy nhất; VI 'khoản "
     "tiền đó'", 1, None, None, "LC", "A"),

    # ---------- S (substitution) — 1 hàng [LC], §3 ----------
    ("S015", "the same thing", "S", "nominal",
     "S014: deliver this life-saving support … provide to children", "high",
     None,
     "[LC] thế danh từ thay wording hoạt động cứu trợ; đối ứng VI 'những việc "
     "như vậy'; H&H cũng đọc 'same' là so sánh — chọn S theo tiền lệ P01 'do "
     "the same'", 1, None, None, "LC", None),

    # ---------- E (ellipsis) — 1 hàng [TC], §2 ----------
    ("S021", None, "E", "nominal", "S021: a global appeal (trong câu)", "high",
     "L: 'the largest ever' danh từ hóa",
     "[TC] tỉnh lược danh từ sau so sánh cao nhất ('the largest ∅ ever'); hồi "
     "phục {appeal} ← 'a global appeal' cùng câu; VI lấp đầy 'khoản tiền kêu "
     "gọi quyên góp … lớn nhất'", 1, "the largest", "{appeal}", "TC", None),

    # ---------- C (conjunction) — 3 hàng [LC], §5 ----------
    ("S014", "But", "C", "adversative",
     "S013: everything … in DPRK (North Korea) is very much led by the "
     "government", "high", None,
     "trong trích dẫn 2: đối lập 'chính phủ dẫn đầu mọi thứ' ↔ 'phải tự tìm "
     "kênh + đối thoại'; VI 'Nhưng' (S016) đối ứng 1–1", 1, None, None,
     "LC", None),
    ("S015", "And", "C", "additive",
     "S014: you need to continue to look for the avenues and the dialogue",
     "high", None,
     "phụ gia tiếp diễn trong trích dẫn; VI 'Và' (S017) đối ứng 1–1",
     1, None, None, "LC", None),
    ("S016", "So", "C", "causal",
     "S015: there are fortunately also still some other agencies that are "
     "doing the same thing", "high", None,
     "hệ quả: vì có cơ quan khác cùng làm → làm chung; VI S018 lược nối "
     "(nối ngầm)", 1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 24 hàng [LC], §6.3 ----------
    ("S002", "UNICEF", "L", "repetition",
     "S001: The United Nations Childrens' Fund", "high", None,
     "biến thể viết tắt sau tên đầy đủ (kề nhưng dạng mới); VI S001 đã có "
     "'(UNICEF)' trong ngoặc → S002 VI lặp kề, không đánh dấu", 1, None, None,
     "LC", None),
    ("S004", "children under the age of five", "L", "repetition",
     "S001: nearly a quarter of a million children", "high", None,
     "thêm định ngữ tuổi; VI 'các em bé dưới 5 tuổi' (đổi đồng nghĩa trẻ "
     "em→em bé)", 1, None, None, "LC", None),
    ("S005", "more than 240,000 children", "L", "repetition",
     "S001: nearly a quarter of a million children", "high", None,
     "hồi quy số lượng (~250.000 = 240.000 — cùng nhóm trẻ em); VI '240.000 "
     "ngàn trẻ em' (lỗi 'ngàn' §8c)", 1, None, None, "LC", None),
    ("S005", "humanitarian support", "L", "repetition",
     "S001: humanitarian support", "high", None,
     "tái lập nguyên tổ hợp sau 4 câu", 1, None, None, "LC", None),
    ("S006", "inter-communal violence", "L", "synonym",
     "S005: protracted emergencies in Kachin, northern Shan and Rakhine "
     "states", "med", None,
     "đồng nghĩa cùng tình huống khủng hoảng; VI hội tụ 'xung đột' (S006/S007)",
     1, None, None, "LC", None),
    ("S008", "the communities", "L", "repetition",
     "S006: inter-communal violence", "med", "R: the",
     "gia đình hình thái communal→communities; lượt lời mới mở trích dẫn 1",
     1, None, None, "LC", None),
    ("S009", "life-saving support", "L", "repetition",
     "S001: humanitarian support", "high", None,
     "đổi định ngữ (humanitarian→life-saving); trong trích dẫn 1",
     1, None, None, "LC", None),
    ("S011", "the group", "L", "repetition", "S003: the group", "high",
     "R: the",
     "tái lập danh ngữ mô tả sau 8 câu; nội dung 'nhóm trung lập' bị VI cắt "
     "(§8g)", 1, None, None, "LC", None),
    ("S012", "reclusive North Korea", "L", "repetition",
     "S003: North Korea", "high", None,
     "thêm định ngữ 'reclusive', tái lập sau 9 câu; VI 'Bắc Triều Tiên nghèo "
     "khó'", 1, None, None, "LC", None),
    ("S013", "DPRK", "L", "repetition",
     "S012: reclusive North Korea", "high", None,
     "biến thể viết tắt; gloss '(North Korea)' lặp kề cùng câu; lượt lời mới "
     "mở trích dẫn 2", 1, None, None, "LC", None),
    ("S013", "flooding situations", "L", "repetition",
     "S012: recurring floods", "high", None,
     "gia đình hình thái flood→flooding; kề nhưng qua ranh giới "
     "attribution→trích dẫn; VI 'lũ lụt' lặp nguyên dạng kề → không đánh dấu",
     1, None, None, "LC", None),
    ("S014", "this life-saving support", "L", "repetition",
     "S009: life-saving support", "high", "R: this",
     "lặp nguyên tổ hợp sau 5 câu", 1, None, None, "LC", None),
    ("S014", "children", "L", "repetition",
     "S005: more than 240,000 children", "high", None,
     "rút gọn, tái lập sau 9 câu trong trích dẫn 2; VI 'các em bé'",
     1, None, None, "LC", None),
    ("S016", "van Heese", "L", "repetition", "S012: Van Heese said", "high",
     None,
     "lặp tên người nói trong attribution khép trích dẫn, sau 4 câu (§8.1 "
     "iii); VI đảo attribution lên S015", 1, None, None, "LC", None),
    ("S017", "appeal", "L", "repetition",
     "S002: the U.N. organization's largest-ever funding appeal", "high",
     None,
     "rút gọn 'funding appeal'→'appeal', tái lập sau 15 câu, mở đoạn",
     1, None, None, "LC", None),
    ("S017", "life-saving humanitarian assistance", "L", "repetition",
     "S014: this life-saving support", "high", None,
     "ghép 3 thành viên chuỗi: life-saving (S009/S014) + humanitarian (S001) "
     "+ assistance (S004); mở đoạn sau khối trích dẫn", 1, None, None,
     "LC", None),
    ("S017", "North Korea", "L", "repetition",
     "S013: DPRK (North Korea)", "high", None,
     "nguyên dạng tái lập sau 4 câu", 1, None, None, "LC", None),
    ("S018", "the Philippines", "L", "repetition",
     "S003: the Philippines", "high", "R: the",
     "tái lập sau 15 câu, mở đoạn Philippines; VI S009/S010 là bản sao "
     "artifact (§8a) — bản thật S020", 1, None, None, "LC", None),
    ("S019", "The organization", "L", "repetition",
     "S002: the U.N. organization's largest-ever funding appeal", "med",
     "R: The",
     "rút gọn 'the U.N. organization'→'The organization' sau 17 câu; đọc "
     "khác: R ← 'UNICEF' S018 kề — chọn L theo CONVENTIONS §1 (đầu ngữ lặp từ "
     "vựng)", 1, None, None, "LC", None),
    ("S019", "children", "L", "repetition",
     "S014: provide to children", "high", None,
     "tái lập sau 5 câu, mở đoạn", 1, None, None, "LC", None),
    ("S020", "raise", "L", "repetition",
     "S004: the goal is to raise $25 million", "high", None,
     "tái lập động từ sau 16 câu — khung kêu gọi theo nước (25 triệu ↔ 11 "
     "triệu); VI 'kêu gọi quyên góp' (S022)", 1, None, None, "LC", None),
    ("S021", "a global appeal", "L", "repetition",
     "S002: the U.N. organization's largest-ever funding appeal", "high",
     None,
     "khung mở–đóng: kêu gọi lớn nhất (S002) ↔ kêu gọi toàn cầu 3,1 tỉ, sau "
     "19 câu; S017 'appeal' tái lập giữa chừng", 1, None, None, "LC", None),
    ("S022", "The organization", "L", "repetition",
     "S019: The organization", "high", "R: The",
     "lặp cùng dạng sau 3 câu", 1, None, None, "LC", None),
    ("S022", "62 million children", "L", "repetition",
     "S020: allow children access to education", "high", None,
     "tái lập với lượng từ mới '62 million' (khung đóng toàn cầu); VI '62 "
     "triệu em bé'", 1, None, None, "LC", None),

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): chuỗi gồm cả từ đơn nội dung (danh/
    # động/tính/trạng từ), thuật ngữ đa từ, tên riêng, động từ attribution;
    # lặp cùng dạng kể cả câu kề; 1 mark/câu/chuỗi; occ đếm tay. Bỏ có chủ ý
    # (đọc hiểu, §8.1): S007 'aid organizations' (từ 'organization' trỏ lớp
    # chung viện trợ ≠ UNICEF S002), S018 'regions'/'natural disasters'
    # (Philippines ≠ Myanmar — khác thực thể), S002 'the U.N. organization's'
    # (chuỗi 'organization' khởi tại S002; chuỗi tên tại S002 đã có 1 mark —
    # hàng UNICEF), S005 'in need of' (gộp trong span hàng 'humanitarian
    # support' cùng câu), 'this year'/'last year' (deictic thời gian),
    # 'million'/'billion' (số từ). Không dùng regex/danh sách từ.
    ("S002", "says", "L", "repetition", "S001: Childrens' Fund says", "high",
     None, "chuỗi động từ attribution (§8.1 v); lặp nguyên dạng câu kề",
     1, None, None, "LC", None),
    ("S002", "Myanmar", "L", "repetition", "S001: in Myanmar", "high", None,
     "lặp tên riêng câu kề (§8.1 i); 'Burma' biến thể cùng câu — không đánh "
     "dấu riêng", 1, None, None, "LC", None),
    ("S003", "funding priorities", "L", "repetition",
     "S002: regional priorities", "high", None,
     "lặp đầu từ 'priorities' câu kề (+ 'funding' từ 'funding appeal' S002)",
     1, None, None, "LC", None),
    ("S004", "Myanmar", "L", "repetition", "S002: Myanmar", "high", None,
     "tái lập tên riêng sau 2 câu, mở đoạn mục tiêu Myanmar", 1, None, None,
     "LC", None),
    ("S004", "assistance", "L", "synonym", "S001: humanitarian support",
     "high", None,
     "từ đơn nội dung (§8.1); 'assistance' ~ 'support' — biến thể mới vào "
     "chuỗi hỗ trợ", 1, None, None, "LC", None),
    ("S005", "UNICEF", "L", "repetition", "S002: UNICEF", "high", None,
     "tái lập sau 3 câu, mở đoạn khủng hoảng", 1, None, None, "LC", None),
    ("S005", "said", "L", "repetition", "S002: says", "high", None,
     "attribution (§8.1 v); đổi thì says→said", 1, None, None, "LC", None),
    ("S005", "states", "L", "repetition", "S001: several states", "high",
     None,
     "lặp 'states' sau 4 câu; cùng nhóm bang (S001 'several states' = "
     "Kachin, Shan, Rakhine)", 1, None, None, "LC", None),
    ("S006", "Rakhine", "L", "repetition", "S005: Rakhine states", "high",
     None, "tái lập tên riêng câu kề (§8.1 i), chủ ngữ mở câu", 1, None,
     None, "LC", None),
    ("S008", "challenges", "L", "repetition", "S007: posed a challenge",
     "high", None,
     "gia đình hình thái challenge→challenges; câu kề — lời trích dẫn diễn "
     "đạt lại tường thuật", 1, None, None, "LC", None),
    ("S008", "access", "L", "repetition", "S007: Getting access", "high",
     None, "lặp 'access' câu kề (§8.1 i), mở trích dẫn 1", 1, None, None,
     "LC", None),
    ("S010", "said", "L", "repetition", "S005: UNICEF said", "high", None,
     "attribution khép trích dẫn 1 (§8.1 v), sau 5 câu", 1, None, None,
     "LC", None),
    ("S011", "Carmen van Heese", "L", "repetition", "S010: said van Heese",
     "high", None,
     "lặp tên người nói câu kề (§8.1 iv), lần đầu đủ tên đệm 'Carmen'",
     1, None, None, "LC", None),
    ("S011", "UNICEF's", "L", "repetition", "S005: UNICEF", "high", None,
     "tái lập sau 6 câu, dạng sở hữu trong chức danh", 1, None, None,
     "LC", None),
    ("S011", "emergency advisor", "L", "repetition",
     "S005: protracted emergencies", "med", None,
     "gia đình hình thái emergencies→emergency trong chức danh (§8.1 ii)",
     1, None, None, "LC", None),
    ("S011", "stressed", "L", "synonym", "S010: said", "high", None,
     "attribution (§8.1 v); 'stressed' ~ 'said'", 1, None, None, "LC",
     None),
    ("S011", "provide", "L", "repetition",
     "S009: providing life-saving support", "med", None,
     "tái lập động từ sau 2 câu (trích dẫn 1 → attribution)", 1, None, None,
     "LC", None),
    ("S011", "aid", "L", "repetition", "S007: aid organizations", "high",
     None,
     "lặp 'aid' (định ngữ S007 → danh từ trần); đồng thời biến thể chuỗi hỗ "
     "trợ (S009 'life-saving support')", 1, None, None, "LC", None),
    ("S012", "Van Heese", "L", "repetition", "S011: Carmen van Heese",
     "high", None,
     "lặp tên người nói câu kề (§8.1 iv), rút gọn bỏ tên đệm", 1, None,
     None, "LC", None),
    ("S012", "said", "L", "synonym", "S011: stressed", "high", None,
     "attribution (§8.1 v); 'said' ~ 'stressed', mở đoạn Bắc Triều Tiên",
     1, None, None, "LC", None),
    ("S012", "needed", "L", "repetition", "S005: in need of", "med", None,
     "gia đình hình thái need→needed; nối chuỗi nhu cầu (S001/S005 'in need "
     "of')", 1, None, None, "LC", None),
    ("S012", "assistance", "L", "repetition", "S004: expand assistance",
     "high", None,
     "tái lập 'assistance' sau 8 câu; chuỗi hỗ trợ (S009 'life-saving "
     "support', S011 'aid')", 1, None, None, "LC", None),
    ("S012", "emergency stocks", "L", "repetition",
     "S011: emergency advisor", "med", None,
     "lặp 'emergency' câu kề (§8.1 i), định ngữ kho dự trữ", 1, None, None,
     "LC", None),
    ("S012", "affected", "L", "repetition", "S006: has been affected",
     "med", None,
     "lặp mục từ cùng nghĩa 'bị ảnh hưởng'; khác sự kiện (bạo động Rakhine ↔ "
     "lũ NK) — lặp từ vựng theo H&H", 1, None, None, "LC", None),
    ("S014", "organization", "L", "repetition",
     "S002: the U.N. organization's", "high", None,
     "tái lập sau 12 câu trong trích dẫn 2; cùng thực thể UNICEF ('we as an "
     "organization'); chuỗi organization S019/S022 tiếp nối", 1, None, None,
     "LC", None),
    ("S014", "provide", "L", "repetition", "S011: provide aid", "med", None,
     "tái lập động từ sau 3 câu trong trích dẫn 2", 1, None, None, "LC",
     None),
    ("S015", "agencies", "L", "synonym", "S007: aid organizations", "med",
     None,
     "'agencies' ~ 'organizations'; 'other agencies' = lớp cơ quan viện trợ "
     "(S007); 'other' đã là hàng R riêng", 1, None, None, "LC", None),
    ("S016", "said", "L", "repetition", "S012: Van Heese said", "high",
     None, "attribution khép trích dẫn 2 (§8.1 v), sau 4 câu", 1, None,
     None, "LC", None),
    ("S017", "UNICEF’s", "L", "repetition", "S011: UNICEF's", "high", None,
     "tái lập sau 6 câu, dạng sở hữu, mở đoạn sau khối trích dẫn", 1, None,
     None, "LC", None),
    ("S017", "said", "L", "repetition", "S016: said van Heese", "high",
     None,
     "attribution câu kề (§8.1 v); chủ ngữ vật 'UNICEF's appeal said'",
     1, None, None, "LC", None),
    ("S017", "critical need", "L", "repetition", "S012: is needed", "med",
     None,
     "gia đình hình thái needed→need; chuỗi nhu cầu cứu trợ", 1, None, None,
     "LC", None),
    ("S017", "nutrition", "L", "repetition",
     "S004: severe acute malnutrition", "med", None,
     "cùng gốc 'dinh dưỡng' (bỏ tiền tố mal-); S004 tình trạng ↔ S017 lĩnh "
     "vực", 1, None, None, "LC", None),
    ("S018", "UNICEF", "L", "repetition", "S017: UNICEF’s", "high", None,
     "lặp tên riêng câu kề (§8.1 i); khung 'According to' không có động từ "
     "attribution", 1, None, None, "LC", None),
    ("S019", "said", "L", "repetition", "S017: appeal said", "high", None,
     "attribution (§8.1 v), sau 2 câu", 1, None, None, "LC", None),
    ("S019", "affected", "L", "repetition", "S012: may be affected", "med",
     None,
     "lặp mục từ 'affected'; khác sự kiện (lũ NK ↔ xung đột Mindanao) — lặp "
     "từ vựng", 1, None, None, "LC", None),
    ("S019", "conflict", "L", "synonym", "S006: inter-communal violence",
     "med", None,
     "'conflict' ~ 'violence'; VI hội tụ 'xung đột'; Mindanao ≠ Rakhine — "
     "biến thể cùng trường nghĩa (tiền lệ TT S021)", 1, None, None, "LC",
     None),
    ("S019", "the southern Philippines", "L", "repetition",
     "S018: the Philippines", "high", "R: the",
     "lặp tên riêng câu kề (§8.1 i), thêm định ngữ 'southern' (Mindanao)",
     1, None, None, "LC", None),
    ("S020", "UNICEF", "L", "repetition", "S018: According to UNICEF",
     "high", None,
     "tái lập sau 2 câu trong khung 'have UNICEF looking to raise'", 1,
     None, None, "LC", None),
    ("S020", "the Philippines", "L", "repetition",
     "S019: the southern Philippines", "high", "R: the",
     "lặp tên riêng câu kề (§8.1 i); TT S022 ghi chú pilot ngược — v2 đánh "
     "dấu", 1, None, None, "LC", None),
    ("S020", "children", "L", "repetition", "S019: children", "high", None,
     "lặp câu kề; 'child morbidity' cùng chuỗi (child←children) cùng câu — "
     "1 mark (§8.1)", 1, None, None, "LC", None),
    ("S020", "access", "L", "repetition", "S008: challenges on access",
     "med", None,
     "tái lập 'access' sau 12 câu; mở rộng nghĩa: lui tới vùng ↔ đến trường",
     1, None, None, "LC", None),
    ("S020", "education", "L", "repetition", "S017: hygiene and education",
     "high", None,
     "tái lập sau 3 câu; S017 liệt kê lĩnh vực ↔ S020 mục tiêu cụ thể", 1,
     None, None, "LC", None),
    ("S020", "violence", "L", "repetition", "S006: inter-communal violence",
     "med", None,
     "tái lập 'violence' sau 14 câu; khác sự kiện (Rakhine ↔ bảo vệ trẻ em "
     "Philippines) — lặp mục từ", 1, None, None, "LC", None),
    ("S021", "largest", "L", "repetition",
     "S002: largest-ever funding appeal", "high", None,
     "khung mở–đóng 'lớn nhất' (S002 ↔ S021), sau 19 câu; text 'largest' "
     "nằm gọn trong gap_after 'the largest' của hàng E — không chồng marker",
     1, None, None, "LC", None),
    ("S021", "UNICEF", "L", "repetition", "S020: UNICEF", "high", None,
     "lặp tên riêng câu kề (§8.1 i), 'the largest ever by UNICEF'", 1,
     None, None, "LC", None),
    ("S021", "funding needs", "L", "repetition",
     "S003: funding priorities", "high", None,
     "lặp 'funding' sau 18 câu (S002 'funding appeal', S003 'funding "
     "priorities'); 'needs' nối chuỗi nhu cầu (S017)", 1, None, None,
     "LC", None),
    ("S022", "says", "L", "repetition", "S019: The organization said",
     "high", None,
     "attribution (§8.1 v); đổi thì said→says, khép bài", 1, None, None,
     "LC", None),
    ("S022", "assist", "L", "repetition",
     "S017: humanitarian assistance", "high", None,
     "gia đình hình thái assistance→assist, động từ hoá; chuỗi hỗ trợ khép "
     "bài", 1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 8 hàng, §4.2 ----------
    ("S012", "Chúng tôi", "R", "personal",
     "S011: attribution (Bà Carmen van Heese, cố vấn của UNICEF…, cho biết "
     "như sau)", "high", None,
     "ngôi 1 loại trừ trong trích dẫn 1; attribution ở câu trước "
     "(CONVENTIONS §1); 'chúng tôi' ×2 trong câu — 1 mark", 1, None, None,
     "LC", "A"),
    ("S016", "chúng tôi", "R", "personal",
     "S015: attribution (Bà van Heese nói)", "high", None,
     "ngôi 1 trong trích dẫn 2; attribution câu trước; ×3 trong câu — 1 mark "
     "(occ 1)", 1, None, None, "LC", "A"),
    ("S017", "khác", "R", "comparative",
     "S016: chúng tôi, trong tư cách là một tổ chức", "med", None,
     "so sánh: 'cơ quan khác' ≠ tổ chức của người nói; đối ứng EN 'other' "
     "(S015); 'cũng' gộp nghĩa phụ gia của 'Và'", 1, None, None, "LC", "A"),
    ("S018", "việc này", "R", "demonstrative",
     "S016: cung cấp sự giúp đỡ vô cùng cần thiết … cho các em bé", "high",
     None,
     "chỉ từ + danh từ tổng quát 'việc'; quy chiếu mở rộng tới hoạt động; đối "
     "ứng EN 'this' (S016)", 1, None, None, "LC", "A"),
    ("S021", "Tổ chức này", "R", "demonstrative", "S020: Theo UNICEF", "high",
     None,
     "chỉ từ + danh từ tổng quát; đối ứng EN 'The organization' (S019 — bên "
     "EN là L, bất đối xứng có chủ ý)", 1, None, None, "LC", "A"),
    ("S022", "Những mối quan tâm đó", "R", "demonstrative",
     "S020: một số khu vực ở Philippines vẫn đang chật vật để phục hồi sau "
     "một loạt các thiên tai (S021: trẻ em vẫn còn bị tác động bởi cuộc xung "
     "đột kéo dài nhiều thập niên)", "high", None,
     "gom hai mối quan tâm Philippines; đối ứng EN 'those concerns' (S020)",
     1, None, None, "LC", "A"),
    ("S024", "tổ chức này", "R", "demonstrative",
     "S023: khoản tiền kêu gọi quyên góp lớn nhất của UNICEF", "high", None,
     "câu gãy nguồn (§8b) nhưng danh ngữ nguyên vẹn; đối ứng EN 'The "
     "organization' (S022 — bên EN là L)", 1, None, None, "LC", "A"),
    ("S024", "khoản tiền đó", "R", "demonstrative",
     "S023: lời kêu gọi quyên góp toàn cầu tổng cộng 3,1 tỉ đô la", "high",
     None,
     "chỉ từ + lặp đầu từ 'khoản tiền' (S023); đối ứng EN 'the money' (S022)",
     1, None, None, "LC", "A"),

    # ---------- S (substitution) — 2 hàng, §3 ----------
    ("S011", "như sau", "S", "clausal",
     "S011: khối trích dẫn sau dấu hai chấm (trong câu)", "med",
     "R: như sau (text reference)",
     "[TC] pro-form dẫn nhập thay wording khối trích dẫn đứng ngay sau "
     "(tiền chỉ trong câu); VI tự sinh — EN mở trích dẫn trực tiếp",
     1, None, None, "TC", None),
    ("S017", "những việc như vậy", "S", "nominal",
     "S016: cung cấp sự giúp đỡ vô cùng cần thiết … cho các em bé", "high",
     None,
     "[LC] thế danh từ; đối ứng EN 'the same thing' (S015)", 1, None, None,
     "LC", None),

    # ---------- C (conjunction) — 2 hàng [LC], §5 ----------
    ("S016", "Nhưng", "C", "adversative",
     "S015: khi xảy ra lũ lụt … mọi thứ ở Bắc Triều Tiên đều do chính phủ "
     "dẫn đầu", "high", None,
     "đối ứng EN 'But' (S014) 1–1", 1, None, None, "LC", None),
    ("S017", "Và", "C", "additive",
     "S016: chúng tôi cần phải tiếp tục tìm kiếm những phương thức và tiến "
     "hành những cuộc đối thoại", "high", None,
     "đối ứng EN 'And' (S015) 1–1", 1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 24 hàng [LC], §6.3 ----------
    ("S004", "Quỹ Nhi đồng Liên hiệp quốc", "L", "repetition",
     "S001: Quĩ Nhi đồng Liên hiệp quốc (UNICEF)", "high", None,
     "biến thể chính tả Quĩ→Quỹ (§8d), tái lập tên đầy đủ sau 3 câu; EN không "
     "có (UNICEF viết tắt kề)", 1, None, None, "LC", None),
    ("S004", "những nước ưu tiên", "L", "repetition",
     "S002: các quốc gia ưu tiên trong khu vực", "high", None,
     "đổi đầu ngữ quốc gia→nước, rút gọn, sau 2 câu", 1, None, None, "LC",
     None),
    ("S005", "các em bé dưới 5 tuổi", "L", "repetition",
     "S001: gần 250.000 trẻ em", "high", None,
     "đổi đồng nghĩa trẻ em→em bé + định ngữ tuổi; đối ứng EN 'children under "
     "the age of five' (S004)", 1, None, None, "LC", None),
    ("S005", "chương trình trợ giúp", "L", "repetition",
     "S001: sự hỗ trợ nhân đạo", "med", None,
     "biến thể gia đình hình thái hỗ trợ→trợ giúp; EN 'assistance' trần → "
     "không đánh dấu EN", 1, None, None, "LC", None),
    ("S006", "240.000 ngàn trẻ em", "L", "repetition",
     "S001: gần 250.000 trẻ em", "high", None,
     "hồi quy số lượng; lỗi nguồn 'ngàn' thừa (§8c)", 1, None, None, "LC",
     None),
    ("S006", "sự trợ giúp nhân đạo", "L", "repetition",
     "S001: sự hỗ trợ nhân đạo", "high", None,
     "lặp tổ hợp với đổi hỗ→trợ, sau 5 câu", 1, None, None, "LC", None),
    ("S008", "những vùng có bạo động", "L", "synonym",
     "S007: những vụ xung đột kéo dài hai năm nay giữa các cộng đồng", "med",
     None,
     "đồng nghĩa bạo động ~ xung đột; hiện thực hóa EN 'the area' (R→L)",
     1, None, None, "LC", None),
    ("S011", "khó khăn trong việc lui tới", "L", "repetition",
     "S008: khó khăn trong việc lui tới", "high", None,
     "lặp nguyên tổ hợp sau 3 câu (cách nhau 2 câu artifact §8a); EN "
     "'challenges on access' kề S007 → không đánh dấu", 1, None, None, "LC",
     None),
    ("S011", "các cộng đồng đó", "L", "repetition",
     "S007: giữa các cộng đồng", "high", "R: đó",
     "lặp đầu từ sau 4 câu; chỉ từ 'đó' ghi alt; đối ứng EN 'the communities' "
     "(S008)", 1, None, None, "LC", None),
    ("S012", "những sự trợ giúp để cứu sống mạng người", "L", "repetition",
     "S006: sự trợ giúp nhân đạo", "high", None,
     "biến thể mới 'cứu sống mạng người' (~EN life-saving), sau 6 câu",
     1, None, None, "LC", None),
    ("S014", "Bà van Heese", "L", "repetition",
     "S011: Bà Carmen van Heese", "high", None,
     "lặp tên người nói trong attribution sau 3 câu, rút gọn bỏ tên đệm "
     "(§8.1 iii); EN đối ứng kề (S011→S012) → không đánh dấu", 1, None,
     None, "LC", None),
    ("S014", "Bắc Triều Tiên nghèo khó", "L", "repetition",
     "S004: Bắc Triều Tiên", "high", None,
     "thêm định ngữ 'nghèo khó', tái lập sau 10 câu; đối ứng EN 'reclusive "
     "North Korea' (S012)", 1, None, None, "LC", None),
    ("S016", "các em bé", "L", "repetition",
     "S005: các em bé dưới 5 tuổi", "high", None,
     "lặp 'em bé' sau 11 câu trong trích dẫn 2; đối ứng EN 'children' (S014)",
     1, None, None, "LC", None),
    ("S016", "sự giúp đỡ vô cùng cần thiết", "L", "repetition",
     "S012: những sự trợ giúp để cứu sống mạng người", "high", None,
     "biến thể trợ giúp→giúp đỡ; đối ứng EN 'this life-saving support' (S014)",
     1, None, None, "LC", None),
    ("S019", "Lời kêu gọi quyên góp", "L", "repetition",
     "S002: lời kêu gọi quyên góp lớn nhất từ trước tới nay của UNICEF",
     "high", None,
     "tái lập tổ hợp sau 17 câu; đối ứng EN 'appeal' (S017)", 1, None, None,
     "LC", None),
    ("S019", "viện trợ nhân đạo", "L", "repetition",
     "S006: sự trợ giúp nhân đạo", "high", None,
     "biến thế viện trợ, sau 13 câu; đối ứng EN 'life-saving humanitarian "
     "assistance' (S017)", 1, None, None, "LC", None),
    ("S019", "Bắc Triều Tiên", "L", "repetition",
     "S015: ở Bắc Triều Tiên", "high", None,
     "nguyên dạng tái lập sau 4 câu; đối ứng EN 'North Korea' (S017)",
     1, None, None, "LC", None),
    ("S020", "Philippines", "L", "repetition", "S004: Philippines", "high",
     None,
     "tái lập sau 16 câu, mở đoạn Philippines; S009/S010 là bản sao artifact "
     "(§8a) — không tính", 1, None, None, "LC", None),
    ("S021", "trẻ em", "L", "repetition",
     "S006: 240.000 ngàn trẻ em", "high", None,
     "tái lập sau 15 câu; đối ứng EN 'children' (S019)", 1, None, None,
     "LC", None),
    ("S021", "cuộc xung đột kéo dài nhiều thập niên", "L", "repetition",
     "S007: những vụ xung đột kéo dài hai năm nay", "high", None,
     "tái lập tổ hợp 'xung đột kéo dài' sau 14 câu (Mindanao ≠ Rakhine — lặp "
     "wording, không cùng sự kiện); EN phân rã (violence→conflict) → không có "
     "hàng EN", 1, None, None, "LC", None),
    ("S022", "kêu gọi quyên góp", "L", "repetition",
     "S019: Lời kêu gọi quyên góp của UNICEF", "high", None,
     "tái lập sau 3 câu; khung quyên góp theo nước: S005 (25 triệu) ↔ S022 "
     "(11 triệu); đối ứng EN 'raise' (S020)", 1, None, None, "LC", None),
    ("S022", "Philippines", "L", "repetition",
     "S020: một số khu vực ở Philippines", "high", None,
     "tái lập sau 2 câu (beneficiary); EN 'for the Philippines' kề S019 → "
     "không đánh dấu", 1, None, None, "LC", None),
    ("S023", "lời kêu gọi quyên góp toàn cầu", "L", "repetition",
     "S002: lời kêu gọi quyên góp lớn nhất từ trước tới nay của UNICEF",
     "high", None,
     "khung mở–đóng toàn bài, tái lập sau 21 câu (+ khung 'lớn nhất từ trước "
     "tới nay' cùng câu); S022 kề không tính; đối ứng EN 'a global appeal' "
     "(S021)", 1, None, None, "LC", None),
    ("S024", "62 triệu em bé", "L", "repetition",
     "S022: tử suất trẻ em, tăng tỉ lệ trẻ em tới trường và bảo vệ cho các em",
     "high", None,
     "tái lập sau 2 câu với lượng từ '62 triệu', đổi dạng em bé←các em; đối "
     "ứng EN '62 million children' (S022)", 1, None, None, "LC", None),
]
