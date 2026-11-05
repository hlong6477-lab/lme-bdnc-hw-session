# P19 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P19_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)

ST = [
    # ---------- R (reference) — 7 hàng, §4.1 ----------
    ("S002", "more", "R", "comparative", "S001: eight airlines", "med", None,
     "so sánh số lượng: 'five more' = thêm 5 hãng ngoài 8 hãng đã bay ở "
     "S001; VI đối ứng 'khác' (S002)", 1, None, None, "LC", "A"),
    ("S002", "the same thing", "R", "comparative", "S001: ticket price-fixing",
     "med", "S: the same",
     "quy chiếu đồng nhất (cùng hành vi lũng đoạn giá vé); VI đối ứng "
     "'một hành vi tương tự' (L)", 1, None, None, "LC", "A"),
    ("S007", "the same players", "R", "comparative",
     "S001: eight airlines (S005: Air France, Cathay Pacific, Japan "
     "Airlines, Malaysia Airlines, Qantas, Singapore Airlines, Thai Airways "
     "and Vietnam Airlines)",
     "med", "L: players (general word)",
     "so sánh đồng nhất: cùng các hãng hoạt động ở cả hai ngành hành khách + "
     "hàng hóa; VI đối ứng 'dịch vụ hàng không' (S008, L)", 1, None, None,
     "LC", "A"),
    ("S010", "that case", "R", "demonstrative",
     "S009: the air cargo price-fixing case", "high", None,
     "chỉ từ trỏ vụ kiện hàng hóa ở câu kề trước; VI đối ứng 'vụ này' (S011)",
     1, None, None, "LC", "A"),
    ("S012", "the period of time", "R", "demonstrative",
     "S001: between 2000 and this year", "med", None,
     "'the' là liên kết duy nhất tại vị trí (danh từ không lặp từ vựng tiền "
     "trạm) → hàng R riêng cho 'the' (CONVENTIONS §1); VI đối ứng 'thời gian "
     "đó' (S013)", 1, None, None, "LC", "A"),
    ("S018", "Those still being sued", "R", "demonstrative",
     "S002: five more air carriers (S004: five more)", "high", None,
     "chỉ từ + cụm phân từ xác định lại nhóm 5 hãng chưa hòa giải; VI đối ứng "
     "'Những hãng' (S019, L — R→L)", 1, None, None, "LC", "A"),
    ("S021", "that", "R", "demonstrative",
     "S020: file a claim form online or by mail", "high",
     "S: do that (thế động từ)",
     "quy chiếu mở rộng tới hành động nộp hồ sơ (text reference); VI đối ứng "
     "'việc này' (S022)", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 1 hàng [TC], §2 ----------
    ("S004", None, "E", "nominal", "S004: eight airlines (trong câu)", "high",
     None,
     "[TC] tỉnh lược danh từ sau lượng từ ('against five more ∅'); hồi phục "
     "{airlines} ← 'eight airlines' cùng câu; VI lấp đầy 'thêm 5 hãng máy "
     "bay nữa' (S005)", 1, "five more", "{airlines}", "TC", None),

    # ---------- C (conjunction) — 5 hàng [LC], §5 ----------
    ("S008", "In fact", "C", "additive",
     "S007: Many of the same players in the air passenger industry also are "
     "air cargo carriers", "med", None,
     "tăng cường lập luận trong trích dẫn; VI 'Trong thực tế' (S009)", 1,
     None, None, "LC", None),
    ("S009", "And", "C", "additive",
     "S008: a lot of the cargo that's carried day to day throughout the "
     "world is carried in the belly of air passenger planes", "med", None,
     "thêm bước lập luận (vụ kiện hàng hóa); VI 'Và' (S010)", 1, None, None,
     "LC", None),
    ("S010", "And", "C", "additive",
     "S009: a very large class action [lawsuit] pending in the eastern "
     "district of New York that pertains to the air cargo price-fixing case",
     "med", None,
     "thêm bước chốt (bị cáo trùng hai vụ); 'as well' cùng câu cùng quan hệ "
     "cộng thêm — 1 mark; VI 'Và' (S011)", 1, None, None, "LC", None),
    ("S018", "also", "C", "additive",
     "S017: The eight airlines which settled deny the allegation and any "
     "liability", "high", None,
     "cộng thêm giữa hai nhóm hãng; VI 'cũng' (S019)", 1, None, None, "LC",
     None),
    ("S019", "However", "C", "adversative",
     "S018: Those still being sued also deny liability", "high", None,
     "tương phosphủ nhận trách nhiệm ↔ nhận tội một phần của ANA; VI 'Riêng' "
     "(S020) — đổi dạng thức nối (đánh dấu ngoại lệ)", 1, None, None, "LC",
     None),

    # ---------- L (lexical cohesion) — 29 hàng [LC], §6.3 ----------
    ("S003", "The case", "L", "synonym", "S001: a class action lawsuit",
     "high", "R: The",
     "biến thể đồng nghĩa (lawsuit → case); VI 'Vụ kiện' (S004) lặp kề S003 "
     "nên chỉ inventory", 1, None, None, "LC", None),
    ("S004", "eight airlines", "L", "repetition", "S001: eight airlines",
     "med", None,
     "tái lập nhóm 8 hãng sau 3 câu (S003 nêu tổng 26 hãng — cùng chuỗi, kề "
     "trước); VI '8 hãng hàng không' (S005)", 1, None, None, "LC", None),
    ("S005", "The carriers which have settled", "L", "repetition",
     "S002: five more air carriers", "high", "R: The",
     "biến thể rút gọn ('air carriers' → 'carriers'), mở đoạn mới; 'settled' "
     "tiếp nối chuỗi Settlements (S004, biến thể lớp từ — chung span, "
     "inventory); VI hiện thực hóa bằng danh sách tên riêng (S006)", 1, None,
     None, "LC", None),
    ("S006", "the case", "L", "repetition", "S003: The case", "high",
     "R: the", "tái lập sau 3 câu; VI đối ứng 'vụ kiện này' (S007, R)", 1,
     None, None, "LC", None),
    ("S006", "price-fixing", "L", "repetition",
     "S001: ticket price-fixing", "high", None,
     "rút gọn (bỏ 'ticket'); ngữ cảnh mở rộng sang ngành hàng hóa; VI "
     "'lũng đoạn giá cả' (S007)", 1, None, None, "LC", None),
    ("S009", "class action", "L", "repetition",
     "S001: a class action lawsuit", "med", None,
     "tái lập thuật ngữ sau 8 câu; '[lawsuit]' là chèn biên tập của nguồn "
     "(§8f); referent khác — vụ kiện hàng hóa; VI 'vụ kiện tập thể' (S010)",
     1, None, None, "LC", None),
    ("S009", "air cargo price-fixing", "L", "repetition",
     "S006: price-fixing in the air cargo industry", "high", None,
     "đảo tổ hợp; VI phân rã 'thay đổi giá cước vận chuyển hàng hóa' (S010) "
     "— không có hàng VI (§8g)", 1, None, None, "LC", None),
    ("S010", "Zapala", "L", "repetition", "S006: Attorney Adam Zapala",
     "high", None,
     "lặp tên người nói trong attribution sau 4 câu (§8.1 iii); VI đối ứng "
     "attribution 'Ông Zapala' (S008)", 1, None, None, "LC", None),
    ("S011", "passengers", "L", "synonym", "S001: Travelers", "high", None,
     "đổi từ 'Travelers' → 'passengers'; VI 'hành khách' (S012)", 1, None,
     None, "LC", None),
    ("S011", "money", "L", "general word", "S005: nearly $40 million", "med",
     None, "danh từ tổng quát cho khoản 40 triệu đôla; VI 'số tiền' (S012)",
     1, None, None, "LC", None),
    ("S012", "People", "L", "general word", "S011: passengers", "med", None,
     "general word cho nhóm hành khách, mở trích dẫn (lượt lời mới); VI "
     "'hành khách' (S013) lặp kề S012 — inventory", 1, None, None, "LC",
     None),
    ("S012", "flights", "L", "repetition",
     "S001: flew on eight airlines across the Pacific", "med", None,
     "biến thể lớp từ (flew → flights), khoảng cách 11 câu; VI 'chuyến bay' "
     "(S013)", 1, None, None, "LC", None),
    ("S013", "the class", "L", "repetition", "S001: a class action lawsuit",
     "med", "R: the",
     "tách danh từ 'class' khỏi tổ hợp 'class action'; referent = nhóm hành "
     "khách nguyên đơn; xuất hiện 2 lần trong câu — 1 mark (occ 1); VI 'vụ "
     "kiện tập thể' (S014)", 1, None, None, "LC", None),
    ("S013", "file claims", "L", "repetition",
     "S011: file applications for claims", "high", None,
     "biến thể rút gọn; VI 'nộp hồ sơ đòi đền bù' (S014)", 1, None, None,
     "LC", None),
    ("S013", "$40 million", "L", "repetition", "S005: nearly $40 million",
     "high", None,
     "tái lập con số sau 8 câu trong trích dẫn; VI '40 triệu đôla' (S014)",
     1, None, None, "LC", None),
    ("S014", "The attorney", "L", "repetition",
     "S006: Attorney Adam Zapala", "high", "R: The",
     "biến thể rút gọn (bỏ tên), khoảng cách 8 câu; VI 'Luật sư Zapala' "
     "(S015)", 1, None, None, "LC", None),
    ("S014", "price-fixing", "L", "repetition",
     "S001: ticket price-fixing (S009: air cargo price-fixing)", "med", None,
     "tái lập dạng trần; VI 'lũng đoạn giá vé' (S015)", 1, None, None, "LC",
     None),
    ("S014", "such legal actions", "L", "general word",
     "S001: a class action lawsuit", "med", "R: such",
     "'legal actions' tổng quát hóa 'lawsuit/class action suit'; VI 'những "
     "vụ kiện như vậy' (S015) — lặp + 'như vậy'", 1, None, None, "LC", None),
    ("S015", "The class action suit", "L", "repetition",
     "S001: a class action lawsuit", "high", "R: The",
     "biến thể 'suit' ↔ 'lawsuit', tái lập sau 14 câu; VI S016 bỏ danh từ "
     "vụ kiện (kể lại như sự thật, §8g) — không có hàng VI", 1, None, None,
     "LC", None),
    ("S015", "airlines", "L", "repetition", "S004: eight airlines", "med",
     None, "tái lập sau 11 câu, sau khối trích dẫn; VI 'Các hãng hàng không "
     "bị kiện' (S016)", 1, None, None, "LC", None),
    ("S015", "fix prices", "L", "repetition", "S001: ticket price-fixing",
     "high", None,
     "đảo tổ hợp + đổi lớp từ (price-fixing → fix prices); VI 'định giá vé' "
     "(S016)", 1, None, None, "LC", None),
    ("S015", "passengers", "L", "repetition", "S011: passengers", "high",
     None, "tái lập sau 4 câu; VI 'hành khách' (S016)", 1, None, None, "LC",
     None),
    ("S017", "The eight airlines", "L", "repetition",
     "S004: eight airlines", "high", "R: The",
     "tái lập nhóm 8 hãng sau 13 câu, mở đoạn mới; VI 'Các hãng hàng không' "
     "(S018)", 1, None, None, "LC", None),
    ("S017", "which settled", "L", "repetition",
     "S004: Settlements have been reached with eight airlines", "med", None,
     "biến thể lớp từ (settlement → settled), tái lập sau 13 câu; VI 'đồng ý "
     "giải quyết' (S018)", 1, None, None, "LC", None),
    ("S017", "the allegation", "L", "synonym",
     "S015: The class action suit claims airlines colluded to fix prices",
     "med", "R: the",
     "đồng nghĩa allegation ↔ claims; VI 'cáo buộc' (S018) là first mention "
     "vì S016 bỏ động từ 'claims' (§8g) — không có hàng VI", 1, None, None,
     "LC", None),
    ("S019", "fixing the prices", "L", "repetition",
     "S015: fix prices on trans-Pacific travel", "high", "R: the",
     "biến thể mở rộng, khoảng cách 4 câu; VI 'lũng đoạn giá cả' (S020)", 1,
     None, None, "LC", None),
    ("S019", "discounted tickets", "L", "repetition", "S003: tickets",
     "high", None,
     "thêm định ngữ 'discounted', tái lập sau 16 câu; VI 'vé giảm giá' "
     "(S020)", 1, None, None, "LC", None),
    ("S020", "eligible for benefits", "L", "repetition",
     "S001: eligible for benefits", "high", None,
     "tái lập nguyên cụm sau 19 câu — khung mở (lede) ↔ đóng (hướng dẫn); VI "
     "đổi dạng 'đủ điều kiện… nhận bồi thường' (S021)", 1, None, None, "LC",
     None),
    ("S020", "claim form", "L", "repetition", "S013: file claims", "med",
     None, "gia đình hình thái (claims → claim form); VI 'nộp hồ sơ đòi bồi "
     "thường' (S021)", 1, None, None, "LC", None),

    # ---------- L v2 bổ sung ----------
    # 36 hàng theo CONVENTIONS §8.1 (chính sách L v2): từ đơn nội dung, lặp ở
    # câu kề, chuỗi động từ attribution; 1 mark/câu/chuỗi; bỏ các trường hợp
    # cùng dạng nhưng trỏ thực thể khác (đọc hiểu từng trường hợp).
    ("S002", "A lawsuit", "L", "repetition",
     "S001: a class action lawsuit", "high", None,
     "biến thể rút gọn (bỏ định ngữ 'class action') ở câu thứ hai của lede",
     1, None, None, "LC", None),
    ("S002", "air carriers", "L", "synonym", "S001: eight airlines", "high",
     None,
     "đồng nghĩa ngành (airline ↔ air carrier); S005 sẽ rút gọn thành "
     "'carriers'", 1, None, None, "LC", None),
    ("S003", "tickets", "L", "repetition", "S001: ticket price-fixing", "med",
     None,
     "biến thể hình thái (ticket → tickets), tách khỏi tổ hợp lede; tiền "
     "trạm của 'discounted tickets' (S019)", 1, None, None, "LC", None),
    ("S003", "airlines", "L", "repetition",
     "S001: eight airlines (S002: air carriers)", "med", None,
     "dùng cấp danh mục ('tổng 26 hãng') — cùng chuỗi từ vựng, nhóm tham "
     "chiếu rộng hơn (đối chiếu note hàng S004)", 1, None, None, "LC", None),
    ("S003", "involves", "L", "repetition",
     "S001: involving ticket price-fixing", "med", None,
     "biến thể hình thái (involving → involves)", 1, None, None, "LC", None),
    ("S004", "a lawsuit", "L", "repetition", "S002: A lawsuit", "high", None,
     "mệnh đề 'a lawsuit continues against five more' tái lập gần nguyên "
     "văn S002 (không nguyên văn cả câu nên vẫn đánh dấu)", 1, None, None,
     "LC", None),
    ("S004", "continues", "L", "repetition", "S002: A lawsuit continues",
     "med", None,
     "lặp động từ nội dung 'continues' trong mệnh đề tái lập từ S002", 1,
     None, None, "LC", None),
    ("S005", "agreed", "L", "synonym",
     "S004: Settlements have been reached", "med", None,
     "đồng nghĩa (thỏa thuận ↔ đồng ý): 'agreed to refund' hiện thực hóa "
     "Settlements ở câu kề", 1, None, None, "LC", None),
    ("S005", "refund", "L", "synonym", "S001: eligible for benefits", "med",
     None,
     "khoản hoàn tiền cụ thể hóa 'benefits' được hứa ở lede", 1, None, None,
     "LC", None),
    ("S007", "industry", "L", "repetition",
     "S006: the air cargo industry", "high", None,
     "lặp 'industry' (air cargo → air passenger), đối lập hai ngành", 1,
     None, None, "LC", None),
    ("S007", "air cargo", "L", "repetition",
     "S006: price-fixing in the air cargo industry", "high", None,
     "tái lập tổ hợp 'air cargo' ở câu kề", 1, None, None, "LC", None),
    ("S007", "carriers", "L", "repetition",
     "S002: five more air carriers", "high", None,
     "lặp 'carriers' sau 5 câu ('air cargo carriers' = hãng chở hàng)", 1,
     None, None, "LC", None),
    ("S008", "cargo", "L", "repetition", "S007: air cargo carriers", "high",
     None, "rút gọn (air cargo → cargo), câu kề", 1, None, None, "LC", None),
    ("S008", "carried", "L", "repetition", "S007: air cargo carriers", "med",
     None,
     "biến thể hình thái (carriers → carried, cùng gốc carry); xuất hiện 2 "
     "lần trong câu — 1 mark (occ 2)", 2, None, None, "LC", None),
    ("S008", "air passenger", "L", "repetition",
     "S007: the air passenger industry", "high", None,
     "tái lập tổ hợp 'air passenger' (industry → planes), câu kề", 1, None,
     None, "LC", None),
    ("S010", "said", "L", "general word", "S006: explains", "med", None,
     "chuỗi động từ attribution (§8.1 v): 'said' tổng quát hóa 'explains' "
     "sau 4 câu", 1, None, None, "LC", None),
    ("S010", "our case", "L", "repetition", "S006: the case", "high", None,
     "cùng referent (vụ kiện chính) — khác 'that case' (vụ hàng hóa, hàng "
     "R); lặp 'case' sau 4 câu", 1, None, None, "LC", None),
    ("S010", "defendants", "L", "synonym",
     "S002: accused of the same thing", "med", None,
     "đồng nghĩa (bị buộc tội ↔ bị cáo): 'defendants in our case' = nhóm 5 "
     "hãng ở S002; 2 lần trong câu — mark occ 2", 2, None, None, "LC", None),
    ("S011", "Zapala", "L", "repetition", "S010: said Zapala", "high", None,
     "lặp tên người nói trong attribution, câu kề (§8.1 iv — v2 đánh dấu cả "
     "câu kề)", 1, None, None, "LC", None),
    ("S011", "said", "L", "repetition", "S010: said Zapala", "high", None,
     "chuỗi attribution (§8.1 v): lặp 'said' ở câu kề", 1, None, None, "LC",
     None),
    ("S012", "paid", "L", "synonym",
     "S005: have agreed to refund nearly $40 million", "med", None,
     "refund ↔ paid out — cùng sự kiện chi trả 40 triệu (đối chiếu 'can "
     "get' S011)", 1, None, None, "LC", None),
    ("S013", "exaplined", "L", "repetition", "S006: explains", "high", None,
     "chuỗi attribution: 'exaplined' (lỗi chính tả của 'explained' trong "
     "nguồn) cùng gốc explain với S006", 1, None, None, "LC", None),
    ("S014", "said", "L", "repetition", "S011: Zapala said", "high", None,
     "chuỗi attribution: lặp 'said' (dạng gần nhất) sau 3 câu", 1, None,
     None, "LC", None),
    ("S014", "money", "L", "repetition", "S011: how much money", "high",
     None, "lặp 'money' sau 3 câu (khoản tiền bồi thường)", 1, None, None,
     "LC", None),
    ("S014", "uncovering", "L", "synonym",
     "S006: U.S. government investigations into price-fixing", "med", None,
     "đồng nghĩa (điều tra ↔ phát hiện, bóc trần): cùng hành vi bộc lộ vụ "
     "lũng đoạn giá", 1, None, None, "LC", None),
    ("S014", "businesses", "L", "general word",
     "S007: the same players (S001: eight airlines)", "low", None,
     "tổng quát hóa: các hãng (players/airlines) là doanh nghiệp — câu phát "
     "biểu tổng quát về răn đe", 1, None, None, "LC", None),
    ("S015", "claims", "L", "synonym", "S014: The attorney said", "med",
     None,
     "chuỗi attribution (§8.1 v): 'claims' (vụ kiện khẳng định) tiếp nối "
     "said/explains ở câu kề", 1, None, None, "LC", None),
    ("S015", "trans-Pacific", "L", "repetition",
     "S001: flew on eight airlines across the Pacific", "high", None,
     "lặp 'Pacific' sau 14 câu (across the Pacific → trans-Pacific)", 1,
     None, None, "LC", None),
    ("S015", "travel", "L", "repetition", "S001: Travelers", "med", None,
     "biến thể hình thái (Travelers → travel, cùng gốc travel)", 1, None,
     None, "LC", None),
    ("S016", "Pacific", "L", "repetition", "S015: trans-Pacific travel",
     "high", None, "lặp 'Pacific' ở câu kề ('Pacific islands')", 1, None,
     None, "LC", None),
    ("S016", "involved", "L", "repetition", "S003: The case involves", "med",
     None,
     "biến thể hình thái (involves → involved) của chuỗi 'involve' (S001, "
     "S003)", 1, None, None, "LC", None),
    ("S018", "deny", "L", "repetition", "S017: deny the allegation", "high",
     None,
     "lặp động từ 'deny' ở câu kề — hai nhóm hãng cùng bác bỏ", 1, None,
     None, "LC", None),
    ("S018", "liability", "L", "repetition", "S017: any liability", "high",
     None, "lặp 'liability' ở câu kề", 1, None, None, "LC", None),
    ("S019", "ANA", "L", "repetition", "S018: All Nippon Airways (ANA)",
     "high", None,
     "tên riêng: lặp dạng viết tắt đã được giới thiệu ở câu kề", 1, None,
     None, "LC", None),
    ("S020", "file", "L", "repetition", "S013: file claims", "high", None,
     "chuỗi động từ 'file' (S011 file applications → S013 file claims → "
     "S020 file)", 1, None, None, "LC", None),
    ("S021", "obtained", "L", "synonym",
     "S011: how much money passengers potentially can get", "low", None,
     "đồng nghĩa (get ↔ obtain) sau 10 câu — 'nhận được' khép khung lede ↔ "
     "hướng dẫn", 1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 6 hàng, §4.2 ----------
    ("S002", "khác", "R", "comparative", "S001: 8 hãng hàng không", "med",
     None,
     "so sánh khác biệt: '5 hãng máy bay khác' = khác 8 hãng ở S001; EN đối "
     "ứng 'more' (S002); S005 VI mới dùng 'thêm… nữa' (trong câu — [TC])", 1,
     None, None, "LC", "A"),
    ("S007", "vụ kiện này", "R", "demonstrative",
     "S004: Vụ kiện (S001: một vụ kiện tập thể)", "high", None,
     "chỉ từ 'này' + lặp danh từ; đối ứng EN 'the case' (S006, L + alt "
     "R:the) — EN mạo từ → VI chỉ từ", 1, None, None, "LC", "A"),
    ("S011", "vụ này", "R", "demonstrative",
     "S010: một vụ kiện tập thể lớn đang được thụ lý ở quận đông của New "
     "York", "high", None,
     "chỉ từ trỏ vụ kiện hàng hóa; đối ứng EN 'that case' (S010)", 1, None,
     None, "LC", "A"),
    ("S013", "thời gian đó", "R", "demonstrative",
     "S001: trong khoảng thời gian từ năm 2000 đến nay", "high", None,
     "chỉ từ 'đó'; đối ứng EN 'the period of time' (S012) — EN 'the' → VI "
     "'đó'", 1, None, None, "LC", "A"),
    ("S017", "vụ kiện này", "R", "demonstrative",
     "S014: trong vụ kiện tập thể", "med", None,
     "xác định lại vụ kiện chính (khác 'những vụ kiện như vậy' S015); EN "
     "S016 'The routes involved' không có quy chiếu đối ứng — VI tự sinh quy "
     "chiếu", 1, None, None, "LC", "A"),
    ("S022", "việc này", "R", "demonstrative",
     "S021: nộp hồ sơ đòi bồi thường trên mạng hoặc gởi qua bưu điện",
     "high", None,
     "danh từ tổng quát 'việc' + chỉ từ 'này' trỏ hành động; đối ứng EN "
     "'that' (S021)", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 0 hàng, §2 ----------
    # VI không có zero khả hồi: EN "five more ∅" (S004) được lấp đầy
    # "thêm 5 hãng máy bay nữa" (S005); các câu bị động S013/S014/S022 phi nhân.

    # ---------- C (conjunction) — 5 hàng [LC], §5 ----------
    ("S009", "Trong thực tế", "C", "additive",
     "S008: Nhiều dịch vụ hàng không trong ngành vận tải hành khách lại làm "
     "luôn cả vận tải hàng hóa", "med", None,
     "tăng cường lập luận; đối ứng EN 'In fact' (S008)", 1, None, None, "LC",
     None),
    ("S010", "Và", "C", "additive",
     "S009: có một lượng hàng hóa lớn được chuyên chở hàng ngày… trong "
     "khoang hàng của các chiếc máy bay hành khách", "med", None,
     "thêm bước lập luận trong trích dẫn; đối ứng EN 'And' (S009)", 1, None,
     None, "LC", None),
    ("S011", "Và", "C", "additive",
     "S010: có một vụ kiện tập thể lớn đang được thụ lý… gắn liền với vụ "
     "thay đổi giá cước vận chuyển hàng hóa", "med", None,
     "đối ứng EN 'And' (S010); 'lại cũng chính là' cùng câu cùng quan hệ "
     "cộng thêm — 1 mark", 1, None, None, "LC", None),
    ("S019", "cũng", "C", "additive",
     "S018: Các hãng hàng không đồng ý giải quyết đã bác bỏ cáo buộc và phủ "
     "nhận trách nhiệm", "high", None,
     "cộng thêm giữa hai nhóm hãng; đối ứng EN 'also' (S018)", 1, None,
     None, "LC", None),
    ("S020", "Riêng", "C", "adversative",
     "S019: Những hãng vẫn đang bị kiện cũng phủ nhận trách nhiệm", "med",
     None,
     "đối ứng EN 'However' (S019) nhưng đổi dạng thức: đánh dấu ngoại lệ "
     "(ANA) thay vì đối kháng trực tiếp; quan hệ tương phản vẫn đọc được", 1,
     None, None, "LC", None),

    # ---------- L (lexical cohesion) — 30 hàng [LC], §6.3 ----------
    ("S002", "hành vi tương tự", "L", "general word",
     "S001: lũng đoạn giá vé", "med", "R: tương tự (so sánh đồng loại)",
     "'hành vi' — danh từ tổng quát cho hành vi lũng đoạn giá; 'tương tự' hạ "
     "đồng nhất (EN 'the same thing') → EN R → VI L", 1, None, None, "LC",
     None),
    ("S003", "Hành khách", "L", "repetition", "S001: Hành khách", "high",
     None,
     "tái lập sau 2 câu trong câu VI tự sinh (§8c) — lập lại chủ đề lede", 1,
     None, None, "LC", None),
    ("S003", "khoảng thời gian từ năm 2000", "L", "repetition",
     "S001: trong khoảng thời gian từ năm 2000 đến nay", "high", None,
     "tái lập gần nguyên văn (thêm 'cho') sau 2 câu, trong câu VI tự sinh",
     1, None, None, "LC", None),
    ("S005", "8 hãng hàng không", "L", "repetition",
     "S001: 8 hãng hàng không", "med", None,
     "tái lập nhóm 8 hãng sau 4 câu (S004 nêu tổng 26 hãng — kề trước); đối "
     "ứng EN 'eight airlines' (S004)", 1, None, None, "LC", None),
    ("S007", "lũng đoạn giá cả", "L", "repetition",
     "S001: lũng đoạn giá vé", "high", None,
     "biến thể ('giá vé' → 'giá cả'); đối ứng EN 'price-fixing' (S006)", 1,
     None, None, "LC", None),
    ("S008", "Ông Zapala", "L", "repetition",
     "S007: Luật sư Adam Zapala", "high", None,
     "biến thể rút gọn danh xưng ('Luật sư Adam' → 'Ông'); mở trích dẫn — "
     "lượt lời mới (§8.1 iii attribution)", 1, None, None, "LC", None),
    ("S008", "dịch vụ hàng không", "L", "synonym",
     "S001: 8 hãng hàng không", "med", None,
     "phép thế đẳng nghĩa ('dịch vụ hàng không' ↔ 'hãng hàng không'); đối "
     "ứng EN 'the same players' (S007, R comparative) — R→L", 1, None, None,
     "LC", None),
    ("S010", "vụ kiện tập thể", "L", "repetition",
     "S001: một vụ kiện tập thể", "med", None,
     "tái lập thuật ngữ sau 9 câu; referent khác — vụ kiện hàng hóa; đối ứng "
     "EN 'class action' (S009)", 1, None, None, "LC", None),
    ("S012", "Luật sư Zapala", "L", "repetition", "S008: Ông Zapala", "high",
     None,
     "biến thể danh xưng ('Ông' → 'Luật sư'), sau khối trích dẫn; EN 'Zapala "
     "said' (S011) lặp kề S010 nên chỉ inventory", 1, None, None, "LC", None),
    ("S012", "hành khách", "L", "repetition", "S003: Hành khách", "high",
     None, "tái lập sau 9 câu; đối ứng EN 'passengers' (S011, đồng nghĩa)", 1,
     None, None, "LC", None),
    ("S012", "số tiền", "L", "general word",
     "S006: gần 40 triệu đôla (S001: tiền thắng kiện)", "med", None,
     "danh từ tổng quát cho khoản tiền thắng kiện; đối ứng EN 'money' (S011)",
     1, None, None, "LC", None),
    ("S013", "Ông Zapala", "L", "repetition", "S012: Luật sư Zapala", "high",
     None,
     "biến thể danh xưng ('Luật sư' → 'Ông'), mở trích dẫn (lượt lời mới); "
     "đối ứng EN 'he exaplined' (S013, R — đại từ attribution, R→L)", 1,
     None, None, "LC", None),
    ("S013", "chuyến bay", "L", "repetition",
     "S003: các chuyến bay xuyên Thái Bình Dương", "med", None,
     "tái lập sau 10 câu; tiền trạm ở câu VI tự sinh; đối ứng EN 'flights' "
     "(S012)", 1, None, None, "LC", None),
    ("S014", "vụ kiện tập thể", "L", "repetition",
     "S001: một vụ kiện tập thể", "med", None,
     "tái lập sau 13 câu (S010 dùng lại thuật ngữ cho vụ hàng hóa); đối ứng "
     "EN 'the class' (S013)", 1, None, None, "LC", None),
    ("S014", "nộp hồ sơ đòi đền bù", "L", "repetition",
     "S012: nộp hồ sơ đòi bồi thường", "high", None,
     "biến thể ('bồi thường' → 'đền bù'); đối ứng EN 'file claims' (S013)",
     1, None, None, "LC", None),
    ("S014", "40 triệu đôla", "L", "repetition", "S006: gần 40 triệu đôla",
     "high", None,
     "tái lập sau 8 câu; đối ứng EN '$40 million' (S013)", 1, None, None,
     "LC", None),
    ("S015", "Luật sư Zapala", "L", "repetition", "S013: Ông Zapala", "high",
     None,
     "biến thể danh xưng ('Ông' → 'Luật sư'), khoảng cách 2 câu; đối ứng EN "
     "'The attorney' (S014)", 1, None, None, "LC", None),
    ("S015", "lũng đoạn giá vé", "L", "repetition",
     "S007: lũng đoạn giá cả", "high", None,
     "trở lại dạng 'giá vé' như S001, khoảng cách 8 câu; đối ứng EN "
     "'price-fixing' (S014)", 1, None, None, "LC", None),
    ("S015", "những vụ kiện như vậy", "L", "repetition",
     "S014: trong vụ kiện tập thể", "med", "R: như vậy",
     "lặp 'vụ kiện' + so sánh 'như vậy'; đối ứng EN 'such legal actions' "
     "(S014, L + alt R: such)", 1, None, None, "LC", None),
    ("S016", "Các hãng hàng không bị kiện", "L", "repetition",
     "S005: 8 hãng hàng không", "high", None,
     "tái lập sau 10 câu, sau khối trích dẫn; thêm 'bị kiện'; đối ứng EN "
     "'airlines' (S015)", 1, None, None, "LC", None),
    ("S016", "định giá vé", "L", "repetition", "S001: lũng đoạn giá vé",
     "med", None,
     "biến thể động từ ('lũng đoạn' → 'định giá'), giữ 'giá vé'; đối ứng EN "
     "'fix prices' (S015)", 1, None, None, "LC", None),
    ("S016", "hành khách", "L", "repetition", "S013: hành khách", "high",
     None, "tái lập sau 3 câu; đối ứng EN 'passengers' (S015)", 1, None,
     None, "LC", None),
    ("S018", "Các hãng hàng không", "L", "repetition",
     "S005: 8 hãng hàng không", "high", None,
     "tái lập sau 13 câu, mở đoạn; định ngữ 'đồng ý giải quyết' xác định lại "
     "nhóm 8 hãng; đối ứng EN 'The eight airlines' (S017)", 1, None, None,
     "LC", None),
    ("S018", "đồng ý giải quyết", "L", "repetition",
     "S005: thỏa thuận giải quyết", "high", None,
     "biến thể ('thỏa thuận' → 'đồng ý'), giữ 'giải quyết'; tái lập sau 13 "
     "câu; đối ứng EN 'which settled' (S017)", 1, None, None, "LC", None),
    ("S019", "Những hãng", "L", "repetition",
     "S018: Các hãng hàng không", "high", None,
     "biến thể rút gọn ('hãng hàng không' → 'hãng'); đối ứng EN 'Those still "
     "being sued' (S018, R demonstrative) — R→L", 1, None, None, "LC", None),
    ("S020", "lũng đoạn giá cả", "L", "repetition",
     "S015: lũng đoạn giá vé", "high", None,
     "khoảng cách 5 câu; đối ứng EN 'fixing the prices' (S019)", 1, None,
     None, "LC", None),
    ("S020", "vé giảm giá", "L", "repetition", "S004: vé máy bay", "high",
     None,
     "thêm định ngữ 'giảm giá', tái lập sau 16 câu; đối ứng EN 'discounted "
     "tickets' (S019)", 1, None, None, "LC", None),
    ("S021", "Những hành khách nào", "L", "repetition", "S001: Hành khách",
     "high", None,
     "tái lập sau 20 câu — khung mở (lede) ↔ đóng (hướng dẫn nộp hồ sơ); đối "
     "ứng EN 'Those' (S020, R) — R→L", 1, None, None, "LC", None),
    ("S021", "nhận bồi thường", "L", "repetition",
     "S013: Tiền bồi thường", "med", None,
     "tái lập sau 8 câu; đối ứng EN 'eligible for benefits' (S020) — VI đổi "
     "dạng vì S001 dùng 'tiền thắng kiện'", 1, None, None, "LC", None),
    ("S021", "nộp hồ sơ đòi bồi thường", "L", "repetition",
     "S012: nộp hồ sơ đòi bồi thường", "high", None,
     "tái lập nguyên cụm sau 9 câu — khung mở–đóng; đối ứng EN 'claim form' "
     "(S020)", 1, None, None, "LC", None),
]
