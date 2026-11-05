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

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn có nội dung thực, tên riêng,
    # thuật ngữ đa từ, động từ attribution, lặp câu kề — 36 hàng mới; 15 hàng
    # L cũ giữ nguyên. Bỏ theo ĐỌC HIỂU (không bịa): "bao gồm" S010 ≠ "liên
    # quan đến" S006 (VI dịch bằng hai động từ khác nhau — chuỗi include của
    # EN không tái lập bên VI); "cửa khẩu biên giới" S010 là điểm cửa khẩu ≠
    # "vượt biên" S006 (chuỗi O §6.2); "Tổng thống" S005/S006 trỏ hai người
    # khác nhau (Trump/Biden); "Mỹ" trong "Hải quan Mỹ" S002 lồng trong tên
    # riêng cơ quan, "giấc mơ Mỹ" S003 là thuật ngữ cố định; "hợp pháp" S008
    # lồng trong span hàng cũ; "di cư ồ ạt" S011 gộp 1 mark với "người nhập
    # cư" (quá trình↔người, §6.2 P); "cơ quan này" S002 là quy chiếu (R).
    ("S002", "Ứng dụng", "L", "repetition", "S001: một ứng dụng mới", "high",
     None,
     "v2: từ đơn 'ứng dụng' (chuỗi C §6.2) tái lập từ S001 — cùng thực thể "
     "CBP Home; S002 lần đầu nêu cơ quan chủ quản và tên 'CBP Home'",
     1, None, None, "LC", None),
    ("S003", "Ứng dụng CBP Home", "L", "repetition",
     "S002: Ứng dụng của Cơ quan Bảo vệ Biên giới và Hải quan Mỹ, gọi là "
     "CBP Home", "high", None,
     "v2 bỏ hạn chế 'câu kề': tái lập cả tên 'CBP Home' (chuỗi A §6.2) lẫn "
     "'ứng dụng' (chuỗi C) tại lượt lời mới (trích dẫn Noem)",
     1, None, None, "LC", None),
    ("S003", "cho phép", "L", "repetition",
     "S001: cho phép những người nhập cư", "high", None,
     "'cho phép' tái lập sau 2 câu; khung song song 'ứng dụng + cho phép + "
     "người di cư + V' (S001 tự trục xuất ↔ S003 rời đi và tự trục xuất); "
     "EN đối ứng là 'allow' (S010)",
     1, None, None, "LC", None),
    ("S003", "rời đi", "L", "repetition", "S002: ý định rời đi", "high",
     None,
     "tái lập nguyên dạng 'rời đi' (chuỗi M §6.2) trong trích dẫn Noem; EN "
     "đối ứng leave ~ depart là biến thể đồng nghĩa, VI cùng dạng",
     1, None, None, "LC", None),
    ("S003", "nói", "L", "synonym", "S002: theo tuyên bố của cơ quan này",
     "high", None,
     "chuỗi động từ attribution riêng (§8.1 v): tuyên bố → nói; EN đối ứng "
     "said → said (repetition) — VI là biến thể mới",
     1, None, None, "LC", None),
    ("S003", "hợp pháp", "L", "antonym", "S001: đang ở Mỹ trái phép", "high",
     None,
     "đối nghĩa phái sinh hợp pháp ↔ trái phép; đối lập 'cư trú trái phép' "
     "↔ 'quay lại hợp pháp' là trọng tâm lập luận của Noem; EN đối ứng "
     "legally ↔ illegally",
     1, None, None, "LC", None),
    ("S003", "cơ hội", "L", "collocation", "S002: một sự lựa chọn", "med",
     None,
     "cùng trường 'khả năng ứng dụng mang lại' (sự lựa chọn ~ cơ hội); EN "
     "gộp option–opportunity thành 1 chuỗi ở S003; VI 'cơ hội' = khả năng "
     "quay lại — khác thực thể cụ thể, liên kết trường nghĩa",
     1, None, None, "LC", None),
    ("S004", "trục xuất", "L", "repetition", "S001: chính sách trục xuất",
     "high", None,
     "gốc 'trục xuất' tái lập (chuỗi J §6.2 — trục xuất cưỡng bức, khác "
     "chuỗi 'tự trục xuất' đã đánh dấu ở S003)",
     1, None, None, "LC", None),
    ("S004", "quay lại", "L", "repetition", "S003: quay lại hợp pháp",
     "high", None,
     "tái lập 'quay lại' trong cùng trích dẫn Noem; đối lập 'quay lại hợp "
     "pháp' ↔ 'không bao giờ được quay lại'",
     1, None, None, "LC", None),
    ("S005", "cam kết", "L", "collocation", "S003: Kristi Noem nói", "med",
     None,
     "động từ báo cáo 'cam kết' — cùng trường attribution tuyên bố/nói "
     "(§8.1 v); báo cáo phát ngôn của Trump, không trích trực tiếp; EN đối "
     "ứng 'vowed'",
     1, None, None, "LC", None),
    ("S005", "trục xuất", "L", "repetition", "S004: sẽ trục xuất họ",
     "high", None,
     "lặp kề — v2 cho phép; 'cam kết trục xuất' tiếp chuỗi J (trục xuất "
     "cưỡng bức)",
     1, None, None, "LC", None),
    ("S006", "ông Trump", "L", "repetition", "S005: Tổng thống Trump",
     "high", None,
     "lặp kề — v2 cho phép (v1 ghi chú 'kề → không đánh dấu'); tái lập tên "
     "người dạng danh xưng 'ông' + họ",
     1, None, None, "LC", None),
    ("S006", "trục xuất", "L", "repetition", "S005: cam kết trục xuất",
     "high", None,
     "chuỗi J tiếp tục: 'trục xuất' ×2 trong câu ('Số liệu trục xuất', "
     "'các đợt trục xuất') — 1 mark",
     2, None, None, "LC", None),
    ("S006", "Số liệu", "L", "collocation", "S005: một số lượng kỷ lục",
     "med", None,
     "cùng trường số liệu thống kê, chung gốc 'số' (số lượng ↔ số liệu); "
     "EN đối ứng numbers → numbers là repetition — VI dùng từ khác nên "
     "collocation",
     1, None, None, "LC", None),
    ("S007", "người nhập cư", "L", "repetition", "S003: người nhập cư",
     "high", None,
     "tái lập nguyên từ sau 4 câu (S005 'di dân', S006 'người vượt biên' "
     "cùng chuỗi G đã đánh dấu); v2 tách cụm S007 thành các chuỗi từ đơn",
     1, None, None, "LC", None),
    ("S007", "trái phép", "L", "repetition", "S005: di dân vào Mỹ trái phép",
     "high", None,
     "tái lập 'trái phép' (dạng S005 lồng trong span hàng cũ — chỉ dùng làm "
     "ante); chuỗi legality: trái phép (S001, S005, S007) ↔ hợp pháp (S003, "
     "S010)",
     1, None, None, "LC", None),
    ("S007", "rời khỏi", "L", "repetition", "S003: rời đi ngay", "high",
     None,
     "động từ 'rời' tái lập (chuỗi M: rời đi S002–S003 → rời khỏi), khác "
     "tiểu từ hướng; EN đối ứng 'to leave' (S007)",
     1, None, None, "LC", None),
    ("S007", "nước Mỹ", "L", "repetition", "S005: vào Mỹ", "high", None,
     "chuỗi tên riêng Mỹ (L §6.2): S001 'ở Mỹ' → S005 'vào Mỹ' (lồng trong "
     "span hàng cũ) → S007 'nước Mỹ' → S008 'tại Mỹ' → S011 'vào Mỹ'",
     1, None, None, "LC", None),
    ("S008", "chính quyền Trump", "L", "repetition",
     "S007: Chính quyền Trump", "high", None,
     "lặp kề — v2 cho phép (v1 ghi chú 'S008 kề → không đánh dấu'); tái "
     "lập thuật ngữ tổ chức (chuỗi E §6.2)",
     1, None, None, "LC", None),
    ("S008", "quy định", "L", "collocation", "S007: các biện pháp khác",
     "med", None,
     "cùng trường 'biện pháp của chính quyền': 'quy định' cụ thể hóa một "
     "trong các 'biện pháp' ở câu trước; EN đối ứng 'regulation' ~ 'other "
     "steps'",
     1, None, None, "LC", None),
    ("S008", "đối mặt với", "L", "repetition",
     "S001: đối mặt với khả năng bị bắt giam", "high", None,
     "động từ nội dung 'đối mặt' tái lập sau 7 câu; cùng khung 'đối mặt "
     "với + hình phạt'; EN đối ứng 'face'",
     1, None, None, "LC", None),
    ("S008", "án phạt hoặc án tù", "L", "collocation",
     "S001: khả năng bị bắt giam", "med", None,
     "cùng trường trừng phạt (án phạt/án tù ~ bắt giam); cấu trúc song "
     "song 'đối mặt với X hoặc Y' với S001; EN đối ứng 'fines or jail "
     "time' ~ 'arrest and detention'",
     1, None, None, "LC", None),
    ("S008", "Mỹ", "L", "repetition", "S007: nước Mỹ", "high", None,
     "chuỗi tên riêng Mỹ — lặp kề (v2 cho phép); 'tại Mỹ' không lồng trong "
     "span hàng cũ nào nên đánh dấu được",
     1, None, None, "LC", None),
    ("S009", "ra mắt", "L", "repetition", "S001: ra mắt một ứng dụng mới",
     "high", None,
     "'ra mắt' tái lập sau 8 câu; hai app khác nhau (CBP One cũ ≠ CBP Home "
     "mới) — liên kết từ vựng thuần túy; EN đối ứng rolled out → launched "
     "là synonym, VI cùng dạng nên repetition",
     1, None, None, "LC", None),
    ("S009", "ứng dụng", "L", "repetition", "S003: Ứng dụng CBP Home",
     "high", None,
     "từ đơn 'ứng dụng' (chuỗi C §6.2) tái lập sau 6 câu; câu này lần đầu "
     "xuất hiện tên 'CBP One' (chuỗi B — lần đầu, không đánh dấu)",
     1, None, None, "LC", None),
    ("S010", "Ứng dụng CBP One", "L", "repetition",
     "S009: ứng dụng CBP One", "high", None,
     "tái lập cả 'ứng dụng' (chuỗi C) lẫn tên 'CBP One' (chuỗi B) — gộp 1 "
     "mark kiểu hàng EN S003 'The CBP Home app'; 'của thời Biden' là bổ "
     "nghĩa mới",
     1, None, None, "LC", None),
    ("S010", "Biden", "L", "repetition", "S009: Biden", "high", None,
     "chuỗi tên riêng Biden (F §6.2): S006 'cựu Tổng thống Joe Biden' → "
     "S009 'Biden' → S010 'thời Biden' (dạng thời kỳ, EN đối ứng "
     "'Biden-era'); lặp kề — v2 cho phép",
     1, None, None, "LC", None),
    ("S010", "cho phép", "L", "repetition", "S003: cho phép", "high", None,
     "'cho phép' tái lập sau 7 câu (chuỗi S001 → S003 → S010); khung song "
     "song 'cho phép + người di cư + V' (tự trục xuất ↔ đặt lịch hẹn); EN "
     "đối ứng 'allowed'",
     1, None, None, "LC", None),
    ("S010", "hợp pháp", "L", "repetition",
     "S008: không có giấy tờ hợp pháp", "high", None,
     "chuỗi legality: 'hợp pháp' tái lập (dạng S008 lồng trong span hàng "
     "cũ — chỉ dùng làm ante); đối nghĩa với 'trái phép' S001/S005/S007; "
     "EN đối ứng 'legal' (S010)",
     1, None, None, "LC", None),
    ("S010", "tính năng", "L", "collocation", "S002: một sự lựa chọn",
     "low", None,
     "cùng trường 'chức năng/lựa chọn của ứng dụng' (tính năng ~ sự lựa "
     "chọn); không đồng quy chiếu: tính năng đặt lịch của CBP One ≠ tùy "
     "chọn tự rời của CBP Home — conf thấp; EN đối ứng 'feature'",
     1, None, None, "LC", None),
    ("S011", "cho rằng", "L", "collocation", "S005: cam kết", "med", None,
     "chuỗi attribution (§8.1 v): tuyên bố → nói → cam kết → cho rằng; "
     "ante = lần attribution trước đó; 'chỉ trích' cùng khung phát ngôn "
     "trong câu — 1 mark; EN đối ứng 'saying'",
     1, None, None, "LC", None),
    ("S011", "người nhập cư", "L", "repetition", "S007: người nhập cư",
     "high", None,
     "tái lập nguyên từ sau 4 câu; trong câu còn 'di cư ồ ạt' — quá trình ↔ "
     "người (§6.2 P) — gộp 1 mark cho chuỗi; EN đối ứng 'migrants' + 'mass "
     "migration' gộp",
     1, None, None, "LC", None),
    ("S011", "Mỹ", "L", "repetition", "S008: tại Mỹ", "high", None,
     "chuỗi tên riêng Mỹ — thành viên cuối (S001, S005 lồng hàng cũ, S007 "
     "'nước Mỹ', S008 'tại Mỹ', S011 'vào Mỹ'); EN đối ứng 'the United "
     "States' (S011)",
     1, None, None, "LC", None),
    ("S012", "đóng", "L", "antonym", "S009: ra mắt", "high", None,
     "CBP One được 'ra mắt' (S009) ↔ bị 'đóng' (S012) — cùng thực thể, "
     "hành động đối ngẫu mở ↔ đóng; EN đối ứng 'shut down' ↔ 'launched'",
     1, None, None, "LC", None),
    ("S012", "di dân", "L", "repetition", "S010: di dân ở Mexico", "high",
     None,
     "'các di dân có lịch hẹn chưa giải quyết' = nhóm người dùng CBP One "
     "(S010) — nhóm con của chuỗi người di cư; S011 'người nhập cư' cùng "
     "chuỗi; ante = dạng 'di dân' gần nhất",
     1, None, None, "LC", None),
    ("S012", "ứng dụng", "L", "repetition", "S010: Ứng dụng CBP One",
     "high", None,
     "từ đơn 'ứng dụng' (chuỗi C) tái lập; tên 'CBP One' đã có hàng riêng "
     "trong câu (chuỗi B) — hai chuỗi, hai span kề nhau, không lồng nhau",
     1, None, None, "LC", None),
]
