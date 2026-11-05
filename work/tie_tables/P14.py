# P14 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P14_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)

ST = [
    # ---------- R (reference) — 3 hàng, §4.1 ----------
    ("S004", "they", "R", "personal", "S003: aliens", "high", None,
     "hồi quy 'aliens' ở phần đầu trích dẫn Noem (câu trước); cùng chuỗi "
     "trong câu: 'them' ×2 + 'they' lần 2 — 1 mark", 1, None, None, "LC",
     "A"),
    ("S004", "we", "R", "personal",
     "S003: attribution (Homeland Security Secretary Kristi Noem said)",
     "high", None,
     "đại từ ngôi 1 trong trích dẫn; attribution ở câu trước → đủ điều kiện "
     "[LC] (CONVENTIONS §1); 'we' = phía chính quyền; ×2 trong câu — 1 mark",
     1, None, None, "LC", "A"),
    ("S007", "other", "R", "comparative",
     "S001: rolled out a new app (bước đi trước của chính quyền)", "med",
     "C: additive",
     "so sánh loại trừ: 'other steps' presuppose bước trước = việc mở app; "
     "'steps' là từ mới (không lặp); VI đối ứng 'cũng … khác' (C-VI1)",
     1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 1 hàng [LC], §2 ----------
    ("S004", None, "E", "verbal", "S003: leave now and self-deport", "high",
     None,
     "[LC] tỉnh lược vị ngữ sau trợ động từ phủ định (kiểu 'John can ∅'); "
     "hồi phục {leave now and self-deport} ← S003; VI đối ứng dùng pro-form "
     "'làm vậy' (S-VI1) — dịch chuyển E→S", 1, "don’t",
     "{leave now and self-deport}", "LC", None),

    # ---------- L (lexical cohesion) — 16 hàng [LC], §6.3 ----------
    ("S003", "aliens", "L", "synonym",
     "S001: immigrants in the United States illegally", "high", None,
     "biến thể mới vào chuỗi người di cư (thuật ngữ hành chính), trong trích "
     "dẫn Noem; VI đối ứng lặp 'người nhập cư' (tái lập)",
     1, None, None, "LC", None),
    ("S003", "self-deport", "L", "repetition", "S001: self deport", "high",
     None,
     "tái lập thuật ngữ then chốt sau 2 câu (biến thể gạch nối); chuỗi từ "
     "khóa của bài (tiêu đề [TD] — §8a)", 1, None, None, "LC", None),
    ("S005", "Trump", "L", "repetition",
     "S001: President Donald Trump's", "high", None,
     "tái lập tên người sau 4 câu, rút còn họ; S006 'Trump's' kề → không "
     "đánh dấu", 1, None, None, "LC", None),
    ("S005", "migrants in the U.S. illegally", "L", "synonym",
     "S001: immigrants in the United States illegally", "high", None,
     "biến thể mới ('migrants' ~ 'immigrants') + viết tắt 'U.S.'; chuỗi ngắt "
     "quãng từ S003 'aliens'", 1, None, None, "LC", None),
    ("S006", "border crossers", "L", "collocation",
     "S005: migrants in the U.S. illegally", "med", None,
     "liên tưởng cùng trường di cư; nhóm con 'recent border crossers' của "
     "chuỗi; VI đối ứng 'người vượt biên'", 1, None, None, "LC", None),
    ("S006", "Democrat", "L", "antonym", "S005: a Republican", "med", None,
     "phép đối Republican ↔ Democrat (cặp hạng mục xác định được); VI lược "
     "'Democrat' ('cựu Tổng thống Joe Biden') — bất đối xứng §6.4/§7",
     1, None, None, "LC", None),
    ("S007", "The Trump administration", "L", "repetition",
     "S001: The Trump administration", "high", "R: The",
     "tái lập thuật ngữ tổ chức sau 6 câu, mở đoạn; S008 kề → không đánh dấu",
     1, None, None, "LC", None),
    ("S008", "people lacking legal status", "L", "synonym",
     "S007: immigrants in the United States illegally", "high", None,
     "diễn đạt mới (paraphrase) vào chuỗi người di cư; VI mở rộng 'đang có "
     "mặt tại Mỹ mà không có giấy tờ hợp pháp'", 1, None, None, "LC", None),
    ("S009", "CBP Home", "L", "repetition", "S003: The CBP Home app",
     "high", None,
     "tái lập tên app sau 6 câu, mở đoạn nền CBP One; S002→S003 lặp kề → "
     "không đánh dấu", 1, None, None, "LC", None),
    ("S009", "Biden", "L", "repetition", "S006: Democrat Joe Biden", "high",
     None, "tái lập tên người sau 3 câu, rút còn họ", 1, None, None, "LC",
     None),
    ("S010", "migrants in Mexico", "L", "repetition",
     "S005: migrants in the U.S. illegally", "high", None,
     "lặp từ 'migrants' sau chuỗi liên tục S005–S008; bổ nghĩa mới 'in "
     "Mexico' — nhóm tham chiếu khác (quan hệ từ vựng, không phải quy chiếu)",
     1, None, None, "LC", None),
    ("S011", "the Biden program", "L", "synonym",
     "S010: The Biden-era app", "high", "R: the",
     "'program' — cách gọi mới (tổng quát) của app CBP One; 'the' xác định "
     "nhưng từ vựng là liên kết chính (CONVENTIONS §1)", 1, None, None,
     "LC", None),
    ("S011", "Republicans", "L", "repetition", "S005: a Republican", "high",
     None,
     "tái lập chuỗi đảng phái sau 6 câu, mở đoạn; biến thể số nhiều",
     1, None, None, "LC", None),
    ("S012", "Trump", "L", "repetition", "S006: Trump's", "high", None,
     "tái lập tên người sau 6 câu, mở đoạn kết", 1, None, None, "LC", None),
    ("S012", "CBP One", "L", "repetition",
     "S009: an app known as CBP One", "high", None,
     "trở lại tên riêng sau 2 câu dùng mô tả ('The Biden-era app', 'the "
     "Biden program')", 1, None, None, "LC", None),
    ("S012", "appointments", "L", "repetition",
     "S010: schedule an appointment", "high", None,
     "tái lập chuỗi lịch hẹn sau 2 câu (S011 không có thành viên chuỗi)",
     1, None, None, "LC", None),

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn nội dung, tên riêng, thuật ngữ
    # đa từ, động từ attribution, lặp câu kề — 34 hàng mới; 16 hàng L cũ giữ
    # nguyên. Bỏ theo ĐỌC HIỂU (không bịa): "next steps" S012 ≠ "other steps"
    # S007 (khác thực thể); "leaving" S012 ≠ "leave" rời đi (khác nghĩa);
    # "border crossing" S010 là điểm cửa khẩu ≠ "border crossers" S006; "mass
    # migration" S011 gộp 1 mark với "migrants" (quá trình↔người, §6.2 P);
    # S005 "the U.S."/"illegally" và S008 "legal status" lồng trong span của
    # hàng cũ — tránh trùng marker.
    ("S002", "The U.S. Customs and Border Protection app", "L", "repetition",
     "S001: a new app", "high", "R: The",
     "v2: từ đơn 'app' (chuỗi C §6.2) tái lập từ S001 — cùng thực thể CBP "
     "Home; lần đầu nêu cơ quan chủ quản và tên 'CBP Home'",
     1, None, None, "LC", None),
    ("S003", "The CBP Home app", "L", "repetition",
     "S002: The U.S. Customs and Border Protection app, called CBP Home",
     "high", "R: The",
     "v2 bỏ hạn chế 'câu kề': tái lập cả tên 'CBP Home' (chuỗi A §6.2) lẫn "
     "'app' (chuỗi C) tại lượt lời mới (trích dẫn Noem)",
     1, None, None, "LC", None),
    ("S003", "gives", "L", "synonym", "S002: will offer an option", "high",
     None,
     "gives ~ offer — biến thể mới vào chuỗi 'đưa ra lựa chọn'; khung song "
     "song 'app + give/offer + option' (§6.2 N)",
     1, None, None, "LC", None),
    ("S003", "the option", "L", "repetition", "S002: an option", "high",
     "R: the",
     "lặp kề — v2 cho phép; tái lập chuỗi tại lượt lời mới; 'opportunity' "
     "trong câu cùng chuỗi — 1 mark",
     1, None, None, "LC", None),
    ("S003", "leave", "L", "synonym", "S002: intent to depart", "high", None,
     "leave ~ depart — biến thể mới vào chuỗi rời đi (M §6.2), trong trích "
     "dẫn Noem",
     1, None, None, "LC", None),
    ("S003", "said", "L", "repetition", "S002: the agency said", "high", None,
     "chuỗi động từ attribution riêng (§8.1 v): said → said; ante = lần "
     "attribution trước đó",
     1, None, None, "LC", None),
    ("S003", "legally", "L", "antonym",
     "S001: in the United States illegally", "high", None,
     "đối nghĩa phái sinh legally ↔ illegally; đối lập 'cư trú trái phép' ↔ "
     "'quay lại hợp pháp' là trọng tâm lập luận của Noem",
     1, None, None, "LC", None),
    ("S004", "deport", "L", "repetition", "S001: deportation push", "high",
     None,
     "gốc 'deport' tái lập (chuỗi J §6.2 — trục xuất cưỡng bức, khác chuỗi "
     "self-deport tự nguyện đã đánh dấu ở S003)",
     1, None, None, "LC", None),
    ("S004", "return", "L", "repetition", "S003: to return legally", "high",
     None,
     "tái lập 'return' trong cùng trích dẫn; đối lập 'return legally' ↔ "
     "'never return'",
     1, None, None, "LC", None),
    ("S005", "vowed", "L", "collocation", "S003: said in a statement", "med",
     None,
     "động từ báo cáo 'vowed' — cùng trường attribution said/saying (§8.1 "
     "v); báo cáo phát ngôn của Trump, không trích trực tiếp",
     1, None, None, "LC", None),
    ("S005", "deport", "L", "repetition", "S004: we will deport them",
     "high", None,
     "lặp kề — v2 cho phép; 'vowed to deport' tiếp chuỗi trục xuất cưỡng bức",
     1, None, None, "LC", None),
    ("S006", "Trump's", "L", "repetition", "S005: Trump", "high", None,
     "lặp kề — v2 cho phép (v1 ghi chú 'kề → không đánh dấu'); tái lập tên "
     "người dạng sở hữu",
     1, None, None, "LC", None),
    ("S006", "deportation", "L", "repetition", "S001: deportation push",
     "high", None,
     "danh từ 'deportation' tái lập nguyên dạng S001 (S004–S005 'deport' "
     "cùng chuỗi J); 'deportations' cuối câu cùng chuỗi — 1 mark; occ=1 vì "
     "'deportation' còn nằm trong 'deportations'",
     1, None, None, "LC", None),
    ("S006", "numbers", "L", "repetition", "S005: record numbers", "high",
     None,
     "từ đơn nội dung (v2): 'numbers' tái lập từ 'record numbers' câu kề — "
     "chuỗi số liệu trục xuất",
     1, None, None, "LC", None),
    ("S007", "immigrants", "L", "repetition",
     "S001: immigrants in the United States illegally", "high", None,
     "tái lập nguyên từ sau 6 câu (v1 bỏ vì 'lặp kề dạng cũ' §6.2 G); v2 tách "
     "cụm S007 thành các chuỗi từ đơn: immigrants (G), the United States "
     "(L), illegally (legality)",
     1, None, None, "LC", None),
    ("S007", "the United States", "L", "repetition", "S005: the U.S.",
     "high", "R: the",
     "chuỗi tên riêng Mỹ (L §6.2): S001 nguyên dạng → S005 viết tắt 'the "
     "U.S.' (lồng trong cụm chuỗi G đã đánh dấu) → S007 nguyên dạng",
     1, None, None, "LC", None),
    ("S007", "illegally", "L", "repetition", "S005: in the U.S. illegally",
     "high", None,
     "trạng từ nội dung (v2): tái lập 'illegally'; chuỗi legality: illegally "
     "(S001, S005) ↔ legally (S003, đối nghĩa) → legal (S008, S010)",
     1, None, None, "LC", None),
    ("S007", "to leave", "L", "repetition", "S003: the option to leave now",
     "high", None,
     "tái lập 'leave' sau 4 câu (chuỗi M §6.2: depart → leave → leave); S012 "
     "'leaving' khác nghĩa (khiến mắc kẹt) — không đánh dấu",
     1, None, None, "LC", None),
    ("S008", "Trump administration", "L", "repetition",
     "S007: The Trump administration", "high", None,
     "lặp kề — v2 cho phép; tái lập thuật ngữ tổ chức (chuỗi E §6.2); "
     "'regulation' là hạng mục mới trong cụm",
     1, None, None, "LC", None),
    ("S008", "regulation", "L", "collocation", "S007: other steps", "med",
     None,
     "cùng trường 'biện pháp của chính quyền': 'regulation' cụ thể hóa một "
     "trong các 'steps' được nêu ở câu trước",
     1, None, None, "LC", None),
    ("S008", "face", "L", "repetition",
     "S001: rather than face possible arrest and detention", "high", None,
     "động từ nội dung 'face' tái lập sau 7 câu; cùng khung 'face + hình "
     "phạt'",
     1, None, None, "LC", None),
    ("S008", "fines or jail time", "L", "collocation",
     "S001: arrest and detention", "med", None,
     "cùng trường trừng phạt (fines/jail time ~ arrest/detention); cấu trúc "
     "song song 'face X or/and Y' với S001",
     1, None, None, "LC", None),
    ("S009", "launched", "L", "synonym", "S001: rolled out a new app",
     "med", None,
     "launched ~ rolled out — biến thể đồng nghĩa vào chuỗi 'triển khai "
     "app' (§6.2 N); hai sự kiện khác app (CBP One cũ ≠ CBP Home mới) — liên "
     "kết từ vựng thuần túy",
     1, None, None, "LC", None),
    ("S010", "app", "L", "repetition", "S009: an app known as CBP One",
     "high", "R: the",
     "từ đơn 'app' (chuỗi C §6.2) tái lập câu kề, cùng thực thể CBP One; "
     "'Biden-era' là bổ nghĩa mới; bẫy occ (§8.3): 'app' ⊂ 'appointment' — "
     "chỉ đếm từ thật, occ=1",
     1, None, None, "LC", None),
    ("S010", "Biden-era", "L", "repetition", "S009: under Biden", "high",
     None,
     "chuỗi tên riêng Biden (F §6.2): Biden (S009) → tính từ hóa "
     "'Biden-era'; v1 bỏ vì lặp kề — v2 đánh dấu",
     1, None, None, "LC", None),
    ("S010", "included", "L", "repetition",
     "S006: Biden's deportations included", "med", None,
     "động từ nội dung 'include' tái lập sau 4 câu (v2: từ đơn là chuỗi)",
     1, None, None, "LC", None),
    ("S010", "allowed", "L", "repetition", "S001: will allow", "high", None,
     "'allow' tái lập sau 9 câu; khung song song 'allow + người di cư + to "
     "V' (S001 tự trục xuất ↔ S010 đặt lịch hẹn)",
     1, None, None, "LC", None),
    ("S010", "legal", "L", "repetition", "S008: legal status", "high", None,
     "chuỗi legality: 'legal' tái lập (S008 'legal status' lồng trong cụm "
     "chuỗi G, chưa đánh dấu riêng); ante = dạng gần nhất theo từ",
     1, None, None, "LC", None),
    ("S010", "feature", "L", "collocation", "S003: the option", "low", None,
     "cùng trường 'chức năng/tùy chọn ứng dụng' (option ~ feature); không "
     "đồng quy chiếu: tính năng đặt lịch của CBP One ≠ tùy chọn tự rời của "
     "CBP Home — conf thấp",
     1, None, None, "LC", None),
    ("S011", "saying", "L", "repetition", "S005: has vowed", "high", None,
     "chuỗi attribution (§8.1 v): said → said → vowed → saying; ante = lần "
     "attribution trước đó; 'criticized' cùng khung phát ngôn trong câu — "
     "1 mark",
     1, None, None, "LC", None),
    ("S011", "the United States", "L", "repetition",
     "S007: the United States", "high", "R: the",
     "chuỗi tên riêng Mỹ — thành viên thứ 4 (S001, S005 viết tắt, S007, "
     "S011); không trùng span hàng nào trong câu",
     1, None, None, "LC", None),
    ("S011", "migrants", "L", "repetition", "S010: migrants in Mexico",
     "high", None,
     "lặp kề — v2 cho phép; trong câu còn 'mass migration' cùng gốc migrat- "
     "(quan hệ quá trình↔người, §6.2 P) — 1 mark cho chuỗi",
     1, None, None, "LC", None),
    ("S012", "migrants", "L", "repetition", "S011: vet migrants", "high",
     None,
     "lặp kề — v2 cho phép; 'migrants with pending appointments' = nhóm "
     "người dùng CBP One (S010) — nhóm con của chuỗi người di cư",
     1, None, None, "LC", None),
    ("S012", "shut down", "L", "antonym",
     "S009: was launched under Biden", "high", None,
     "CBP One được 'launched' (S009) ↔ bị 'shut down' (S012) — cùng thực "
     "thể, hành động đối ngẫu mở ↔ đóng; đối lập thêm với 'rolled out' (S001)",
     1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 2 hàng, §4.2 ----------
    ("S004", "họ", "R", "personal", "S003: người nhập cư", "high", None,
     "hồi quy 'người nhập cư' ở phần đầu trích dẫn Noem (câu trước); "
     "'họ' ×3 trong câu — 1 mark", 1, None, None, "LC", "A"),
    ("S004", "chúng tôi", "R", "personal",
     "S003: attribution (Bộ trưởng An ninh Nội địa Kristi Noem nói)",
     "high", None,
     "đại từ ngôi 1 trong trích dẫn; attribution ở câu trước → đủ điều kiện "
     "[LC]; 'chúng tôi' = phía chính quyền Noem; ×2 trong câu — 1 mark",
     1, None, None, "LC", "A"),

    # ---------- S (substitution) — 1 hàng [LC], §3 ----------
    ("S004", "làm vậy", "S", "verbal",
     "S003: rời đi ngay và tự trục xuất", "high", None,
     "[LC] 'làm vậy' = do so — thế động từ, thay thế hành động 'rời đi ngay "
     "và tự trục xuất' ở câu trước; EN đối ứng 'don’t' + ∅ là tỉnh lược "
     "(E-EN1)", 1, None, None, "LC", None),

    # ---------- C (conjunction) — 1 hàng [LC], §5 ----------
    ("S007", "cũng", "C", "additive",
     "S001: ra mắt một ứng dụng mới (hành động trước của chính quyền)",
     "high", None,
     "[LC] phó từ nối phụ gia: biện pháp khác cộng thêm với việc mở app ở "
     "S001; EN đối ứng 'other steps' (R-EN3) — một vị trí, hai mã theo hai "
     "khung; 'khác' cùng trường nghĩa, gộp trong ghi chú",
     1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 15 hàng [LC], §6.3 ----------
    ("S003", "người nhập cư", "L", "repetition",
     "S001: những người nhập cư đang ở Mỹ trái phép", "high", None,
     "tái lập chuỗi sau 2 câu trong trích dẫn Noem; EN đối ứng là biến thể "
     "mới 'aliens' — bất đối xứng lý do đánh dấu", 1, None, None, "LC",
     None),
    ("S003", "tự trục xuất", "L", "repetition", "S001: tự trục xuất",
     "high", None,
     "tái lập thuật ngữ then chốt sau 2 câu; đối ứng EN 'self-deport'; tiêu "
     "đề VI lại là 'tự động trục xuất' (§8a)", 1, None, None, "LC", None),
    ("S005", "Tổng thống Trump", "L", "repetition",
     "S001: Tổng thống Donald Trump", "high", None,
     "tái lập sau 4 câu, rút tên — VI giữ danh xưng 'Tổng thống'; S006 'ông "
     "Trump' kề → không đánh dấu", 1, None, None, "LC", None),
    ("S005", "di dân vào Mỹ trái phép", "L", "synonym",
     "S001: những người nhập cư đang ở Mỹ trái phép", "high", None,
     "biến thể mới 'di dân' (đồng nghĩa với 'người nhập cư')", 1, None,
     None, "LC", None),
    ("S006", "người vượt biên", "L", "collocation",
     "S005: di dân vào Mỹ trái phép", "med", None,
     "liên tưởng cùng trường di cư; nhóm con 'vượt biên gần đây'; đối ứng EN "
     "'border crossers'", 1, None, None, "LC", None),
    ("S007", "Chính quyền Trump", "L", "repetition",
     "S001: Chính quyền Trump", "high", None,
     "tái lập sau 6 câu, mở đoạn; S008 kề → không đánh dấu",
     1, None, None, "LC", None),
    ("S008", "không có giấy tờ hợp pháp", "L", "synonym",
     "S007: những người nhập cư trái phép", "high", None,
     "diễn đạt mới (paraphrase 'trái phép'); VI mở rộng thêm 'đang có mặt "
     "tại Mỹ'", 1, None, None, "LC", None),
    ("S009", "CBP Home", "L", "repetition", "S003: Ứng dụng CBP Home",
     "high", None,
     "tái lập tên app sau 6 câu, mở đoạn nền CBP One", 1, None, None, "LC",
     None),
    ("S009", "Biden", "L", "repetition",
     "S006: cựu Tổng thống Joe Biden", "high", None,
     "tái lập tên người sau 3 câu", 1, None, None, "LC", None),
    ("S010", "di dân ở Mexico", "L", "repetition",
     "S005: di dân vào Mỹ trái phép", "high", None,
     "lặp 'di dân' sau chuỗi liên tục S005–S008; bổ nghĩa 'ở Mexico' — nhóm "
     "tham chiếu khác (quan hệ từ vựng)", 1, None, None, "LC", None),
    ("S011", "chương trình của thời Biden", "L", "synonym",
     "S010: Ứng dụng CBP One của thời Biden", "high", None,
     "'chương trình' — cách gọi mới (tổng quát) của ứng dụng CBP One; EN đối "
     "ứng 'the Biden program' (alt 'R: the' ở hàng EN)", 1, None, None,
     "LC", None),
    ("S011", "Các đảng viên Cộng hòa", "L", "repetition",
     "S005: một đảng viên Cộng hòa", "high", None,
     "tái lập chuỗi đảng phái sau 6 câu, mở đoạn; biến thể số nhiều",
     1, None, None, "LC", None),
    ("S012", "Ông Trump", "L", "repetition", "S006: ông Trump", "high", None,
     "tái lập sau 6 câu, mở đoạn kết; danh xưng 'Ông' + họ (VI thêm danh "
     "xưng)", 1, None, None, "LC", None),
    ("S012", "CBP One", "L", "repetition",
     "S010: Ứng dụng CBP One của thời Biden", "high", None,
     "tái lập tên app sau 2 câu (S011 dùng 'chương trình')",
     1, None, None, "LC", None),
    ("S012", "lịch hẹn", "L", "repetition",
     "S010: đặt lịch hẹn phỏng vấn", "high", None,
     "tái lập chuỗi lịch hẹn sau 2 câu; VI thêm 'phỏng vấn' ở S010 (§7)",
     1, None, None, "LC", None),
]
