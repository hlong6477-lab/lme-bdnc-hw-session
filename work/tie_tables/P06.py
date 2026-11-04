# P06 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# - text tie: gap_after=None, recovered=None
# - ellipsis: text=None, gap_after="exact substring ending before ∅",
#             recovered="{meaning}", gap_after="" only for sentence-initial ∅
# - level: "LC" intersentential / "TC" intra-sentential / "TD" title
# - ref:  R only, one of "A"/"C"/"E"; must be a manual decision, never defaulted
# - occ:  explicit when the same text/gap_after repeats in the sentence
#
# Categories: R reference | S substitution | E ellipsis | C conjunction | L lexical
# Do not add a row that is not in the analysis.  Do not use regex/word lists.
# Nguồn quyết định: work/analysis/P06_semantic.md (§2–§6). Cặp P06: EN 38 câu,
# VI 24 câu (VI tách EN S003 -> S003+S004; cắt trọn EN S024–S038).

ST = [
    # ---------- R (8) — analysis §4.1 ----------
    # R-EN1: đại từ ngôi 2 hướng độc giả — quy chiếu ngoại văn bản (ref=E);
    # "you're" cùng câu theo dõi cùng chuỗi, 1 mark, chọn occ 2 (đại từ độc lập)
    ("S001", "you", "R", "personal", "ngoài văn bản (độc giả bài viết)",
     "high", None,
     "quy chiếu ngoại: nhà báo gọi độc giả; VI đối ứng 'bạn' (R-VI1); "
     "dạng 'you're' cùng câu cùng chuỗi — 1 mark",
     2, None, None, "LC", "E"),

    # R-EN2: đại từ [−người] hồi quy trỏ quy trình ETIAS của câu trước
    ("S009", "It", "R", "personal", "S008: The ETIAS process",
     "high", None, "đại từ hồi quy; VI đối ứng 'Đây' (R-VI2, đổi dạng)",
     1, None, None, "LC", "A"),

    # R-EN3: quy chiếu mở rộng — It = "the driving force" (S030)
    ("S031", "It's", "R", "personal", "S030: the driving force",
     "med", None, "quy chiếu mở rộng tới 'the driving force' của câu trước",
     1, None, None, "LC", "A"),

    # R-EN4: sở hữu cách [+người, số nhiều] = content creators (S030);
    # "their trust" cùng câu cùng chuỗi — 1 mark, occ 1
    ("S031", "their", "R", "personal", "S030: Content creators",
     "high", None,
     "sở hữu cách = content creators; 'their trust' cùng câu cùng chuỗi "
     "(1 mark, occ 1)",
     1, None, None, "LC", "A"),

    # R-EN5: đại từ attribution (dạng "she said" tránh bẫy substring);
    # nằm trong khối bị VI cắt
    ("S031", "she said", "R", "personal", "S029: Richards said",
     "high", None, "đại từ attribution; khối EN-only (VI cắt)",
     1, None, None, "LC", "A"),

    # R-EN6: demonstrative quy chiếu mở rộng tới toàn bộ nhận định S032
    ("S033", "That's", "R", "demonstrative",
     "S032: Community-driven travel will be a big part of the change",
     "med", None, "quy chiếu mở rộng tới nhận định câu trước",
     1, None, None, "LC", "A"),

    # R-EN7: "respond to that" — trỏ nhu cầu lựa chọn xanh (S034)
    ("S035", "that", "R", "demonstrative",
     "S034: Travellers are actually going to be demanding eco-conscious options",
     "med", None, "chỉ từ hồi quy trỏ sự kiện câu trước",
     1, None, None, "LC", "A"),

    # R-EN8: đại từ attribution; khối EN-only
    ("S037", "he said", "R", "personal",
     "S036: Hugh Aitken, vice president of strategic relations and development at Skyscanner",
     "high", None, "đại từ attribution; khối EN-only (VI cắt)",
     1, None, None, "LC", "A"),

    # ---------- S (0) — analysis §3: không có phép thế ----------

    # ---------- E (0) — analysis §2: không có khe tỉnh lược ----------

    # ---------- C (5) — analysis §5 ----------
    # C-EN1: temporal, có màu sắc additive (chuyển sang hãng khác cùng chủ đề)
    ("S012", "Meanwhile", "C", "temporal",
     "S011: The airline will stop flying between Sydney and Seoul",
     "high", None, "chuyển mục sang hãng khác trong chủ đề thay đổi tuyến",
     1, None, None, "LC", None),

    # C-EN2: trạng từ cộng thêm — Virgin Australia gia nhập loạt hãng cắt giảm
    ("S013", "also", "C", "additive",
     "S012: Emirates will axe its Singapore to Melbourne route",
     "high", None, "trạng từ additive; VI đối ứng 'cũng' (C-VI3)",
     1, None, None, "LC", None),

    # C-EN3: đối lập "khó suy đoán" (S019) ↔ "ACCC ghi nhận tác động"
    ("S020", "However", "C", "adversative",
     "S019: making it difficult to speculate over factors that may impact airfares in the future",
     "high", None, "đối lập trong lượt trích dẫn ACCC; VI đối ứng 'Tuy nhiên' (C-VI4)",
     1, None, None, "LC", None),

    # C-EN4: đối lập "chiếm 15–25% chi phí" (S022) ↔ "mức thấp nhất từ 2021"
    ("S023", "However", "C", "adversative",
     "S022: the price of jet fuel, which will typically account for between 15 per cent and 25 per cent of an airline's operating costs",
     "high", None, "đối lập trong lượt trích dẫn ACCC; VI đối ứng 'Tuy nhiên' (C-VI5)",
     1, None, None, "LC", None),

    # C-EN5: đồng thời-đối trọng trong trích dẫn Aitken; đọc additive cũng được
    ("S038", "At the same time", "C", "temporal",
     "S037: Many airlines are adopting new technologies at pace",
     "med", None, "đồng thời-đối trọng; khối EN-only (VI cắt)",
     1, None, None, "LC", None),

    # ---------- L (17) — analysis §6.3 ----------
    # L-EN1: tái lập tên đầy đủ chương trình sau 2 câu (S003 chỉ dùng "the program")
    ("S004", "Global Entry program", "L", "repetition",
     "S002: the US Global Entry program",
     "high", None, "tái lập tên đầy đủ sau 2 câu",
     1, None, None, "LC", None),

    # L-EN2: danh từ thượng vị mô tả lại Qantas
    ("S011", "The airline", "L", "superordinate", "S010: Qantas",
     "high", "R: The", "thượng vị mới vào chuỗi hãng bay (Qantas)",
     1, None, None, "LC", None),

    # L-EN3: service -> route: đồng nghĩa mới vào chuỗi dịch vụ Cairns–Tokyo
    ("S014", "the route", "L", "synonym",
     "S013: its daily Cairns to Tokyo service",
     "high", "R: the", "đồng nghĩa service -> route",
     1, None, None, "LC", None),

    # L-EN4: biến thể số nhiều, tái lập tại mở đầu lượt trích dẫn (gap 2);
    # "the route" cùng câu cùng chuỗi — 1 mark
    ("S015", "the services", "L", "repetition",
     "S013: its daily Cairns to Tokyo service",
     "med", "R: the",
     "biến thể số nhiều tại mở đầu lượt trích dẫn; 'the route' cùng câu "
     "cùng chuỗi (1 mark)",
     1, None, None, "LC", None),

    # L-EN5: đồng nghĩa mới vào chuỗi giá vé
    ("S017", "ticket prices", "L", "synonym", "S016: airfares",
     "high", None, "đồng nghĩa airfares -> ticket prices; VI giữ 'giá vé' (không mark)",
     1, None, None, "LC", None),

    # L-EN6: tái lập "competition" sau 2 câu trong lượt trích dẫn mới
    ("S020", "greater competition", "L", "repetition",
     "S018: a significant reduction in competition",
     "high", None, "tái lập sau 2 câu, lượt trích dẫn mới của ACCC",
     1, None, None, "LC", None),

    # L-EN7: khung mở–đóng của trích dẫn ACCC (S019 -> S022), gap 3
    ("S022", "factors", "L", "repetition",
     "S019: factors that may impact airfares",
     "med", "R: the",
     "khung trích dẫn: 'khó suy đoán về factors' -> 'một trong những "
     "factors quan trọng hơn'; VI đối ứng 'yếu tố' (L-VI6)",
     1, None, None, "LC", None),

    # L-EN8: biến thể thay định ngữ online -> Internet, gap 2
    ("S027", "Internet search traffic", "L", "repetition",
     "S025: online search traffic",
     "high", None, "biến thể thay định ngữ, khoảng cách 2 câu; khối EN-only",
     1, None, None, "LC", None),

    # L-EN9: danh từ tổng quát mô tả lại Siem Reap
    ("S027", "the tourist hot spot", "L", "general word",
     "S026: Siem Reap in Cambodia",
     "med", "R: the", "general word cho Siem Reap; khối EN-only",
     1, None, None, "LC", None),

    # L-EN10: lặp tên người nói (rút gọn còn họ) trong attribution
    ("S029", "Richards", "L", "repetition", "S028: Vanessa Richards",
     "high", None, "rút gọn tên trong attribution; khối EN-only",
     1, None, None, "LC", None),

    # L-EN11: tái lập nguyên dạng sau 5 câu
    ("S029", "the world of travel", "L", "repetition",
     "S024: the world of travel",
     "high", None, "tái lập nguyên dạng sau 5 câu; khối EN-only",
     1, None, None, "LC", None),

    # L-EN12: danh hóa redefine -> the change
    ("S032", "the change", "L", "synonym",
     "S029: redefine the world of travel in 2025",
     "med", "R: the", "danh hóa: redefine -> the change; khối EN-only",
     1, None, None, "LC", None),

    # L-EN13: tái lập tổ hợp sau 5 câu, mở block trích dẫn mới
    ("S034", "eco-conscious", "L", "repetition",
     "S029: eco-conscious travel",
     "high", None, "tái lập tổ hợp sau 5 câu, mở block trích dẫn mới; EN-only",
     1, None, None, "LC", None),

    # L-EN14: tái lập chuỗi destinations sau 10 câu, khép trích dẫn Richards
    ("S035", "Destinations", "L", "repetition",
     "S025: certain destinations",
     "med", None, "tái lập sau 10 câu, khép trích dẫn Richards; EN-only",
     1, None, None, "LC", None),

    # L-EN15: tái lập tên công ty sau 11 câu tại attribution người nói mới
    ("S036", "Skyscanner", "L", "repetition",
     "S025: Travel comparison website Skyscanner's",
     "high", None, "lặp tên sau 11 câu tại attribution mới; EN-only",
     1, None, None, "LC", None),

    # L-EN16: tái lập dạng viết tắt sau 7 câu
    ("S036", "AI", "L", "repetition",
     "S029: artificial intelligence (AI) personalisation",
     "high", None, "tái lập dạng viết tắt sau 7 câu; EN-only",
     1, None, None, "LC", None),

    # L-EN17: biến thể thêm "macro-", gap 2, cùng lượt lời Aitken
    ("S038", "global macro-economic pressures", "L", "repetition",
     "S036: global economic pressures",
     "high", None, "biến thể thêm 'macro-', cùng lượt lời Aitken; EN-only",
     1, None, None, "LC", None),

    # ---------- L v2 bổ sung ----------
    # Theo CONVENTIONS §8.1 (v2): chuỗi gồm cả từ đơn nội dung (danh/động/
    # tính/trạng), thuật ngữ đa từ = 1 chuỗi, tên riêng = 1 chuỗi, động từ
    # attribution = chuỗi riêng; đánh dấu cả lặp cùng dạng ở câu kề; 1
    # mark/câu/chuỗi; "The + danh từ lặp" → L với alt='R: The'. Mỗi hàng là
    # một quyết định đọc hiểu tay theo ST_sentmap (khác referent thì bỏ:
    # "service" S013, "routes" S012/S018, "report" S023, "borders" S009).
    # 29 hàng mới (L: 17 → 46).
    ("S002", "the US", "L", "repetition",
     "S001: the United States", "high", None,
     "tên nước viết tắt (United States → US), câu kề; occ 2 — lần 'into "
     "the US', ngoài tên chương trình",
     2, None, None, "LC", None),
    ("S002", "eligible", "L", "repetition",
     "S001: you may be eligible", "high", None,
     "tính từ đơn lặp, câu kề; cùng chủ đề đủ điều kiện Global Entry",
     1, None, None, "LC", None),
    ("S003", "The program", "L", "repetition",
     "S002: the US Global Entry program", "high", "R: The",
     "rút gọn còn 'program', câu kề; 'the program' lần 2 cùng câu cùng "
     "chuỗi (1 mark)",
     1, None, None, "LC", None),
    ("S003", "Australians", "L", "repetition",
     "S002: eligible Australian travellers", "high", None,
     "tên riêng Úc (Australian → Australians), câu kề; ×2 trong câu "
     "(1 mark, occ 1)",
     1, None, None, "LC", None),
    ("S005", "next year", "L", "repetition",
     "S001: next year", "high", None,
     "tái lập khung thời gian 2025 sau 4 câu",
     1, None, None, "LC", None),
    ("S006", "the UK", "L", "repetition",
     "S005: the United Kingdom", "high", None,
     "tên nước viết tắt (United Kingdom → UK), câu kề",
     1, None, None, "LC", None),
    ("S008", "ETIAS", "L", "repetition",
     "S007: an ETIAS (European Travel Information and Authorisation System) "
     "visa waiver", "high", None,
     "tái lập tên hệ thống, câu kề",
     1, None, None, "LC", None),
    ("S009", "the new process", "L", "repetition",
     "S008: The ETIAS process", "high", "R: the",
     "thêm định ngữ 'new', câu kề; chuỗi 'process' mở từ S004 'screening "
     "process'",
     1, None, None, "LC", None),
    ("S009", "tourists", "L", "synonym",
     "S008: requiring travellers to complete", "high", None,
     "biến thể mới vào chuỗi du khách (travellers → tourists), câu kề",
     1, None, None, "LC", None),
    ("S011", "flights", "L", "repetition",
     "S004: US domestic flights", "high", None,
     "tái lập 'flights' sau 7 câu, cùng trường hàng không; 'flying' cùng "
     "câu cùng họ từ (1 mark)",
     1, None, None, "LC", None),
    ("S013", "cutting", "L", "synonym",
     "S012: Emirates will axe its Singapore to Melbourne route", "high",
     None,
     "động từ đồng nghĩa axe → cutting (cắt giảm tuyến), câu kề; hàng C "
     "'also' nối hai phát biểu",
     1, None, None, "LC", None),
    ("S015", "the airline", "L", "repetition",
     "S014: The airline", "high", "R: the",
     "lặp kề tại attribution, chuỗi hãng bay; VI đổi thành R 'hãng hàng "
     "không này'",
     1, None, None, "LC", None),
    ("S015", "visitors", "L", "synonym",
     "S009: simplify entry for tourists", "high", None,
     "biến thể mới vào chuỗi du khách (tourists → visitors), sau 6 câu",
     1, None, None, "LC", None),
    ("S017", "The report", "L", "repetition",
     "S016: the annual Amex Air Monitor report", "high", "R: The",
     "rút gọn tên báo cáo, câu kề",
     1, None, None, "LC", None),
    ("S017", "jump", "L", "synonym",
     "S016: airfares within and from Australia will surge", "high", None,
     "động từ đồng nghĩa surge → jump (cùng sự tăng giá vé 2025), câu kề",
     1, None, None, "LC", None),
    ("S019", "ACCC", "L", "repetition",
     "S018: the Australian Competition and Consumer Commission (ACCC)",
     "high", None,
     "tái lập viết tắt đã giới thiệu ở câu trước, tại attribution, câu kề",
     1, None, None, "LC", None),
    ("S019", "told", "L", "synonym",
     "S015: a statement from the airline said", "high", None,
     "chuỗi động từ attribution (§8.1): said → told, sau 4 câu",
     1, None, None, "LC", None),
    ("S021", "reduce", "L", "repetition",
     "S018: a significant reduction in competition", "high", None,
     "gia đình hình thái (reduction → reduce), sau 3 câu",
     1, None, None, "LC", None),
    ("S022", "significant", "L", "repetition",
     "S018: a significant reduction in competition", "high", None,
     "tính từ lặp sau 4 câu; chuỗi mở từ S005 'most significant changes'",
     1, None, None, "LC", None),
    ("S023", "the price of jet fuel", "L", "repetition",
     "S022: the price of jet fuel", "high", "R: the",
     "tái lập nguyên văn cụm, câu kề",
     1, None, None, "LC", None),
    ("S025", "destinations", "L", "repetition",
     "S024: the actual destinations", "high", None,
     "câu kề; cùng chuỗi với S035 (L-EN14)",
     1, None, None, "LC", None),
    ("S029", "predicts", "L", "repetition",
     "S017: The report predicts", "high", None,
     "tái lập động từ dự báo sau 12 câu (Richards ↔ báo cáo Amex)",
     1, None, None, "LC", None),
    ("S029", "trends", "L", "repetition",
     "S024: myriad trends", "high", None,
     "từ khoá chủ đề lặp sau 5 câu; S025 'Travel Trends 2025' cùng chuỗi "
     "(trong tên báo cáo)",
     1, None, None, "LC", None),
    ("S030", "Content creators", "L", "repetition",
     "S029: content creators", "high", None,
     "lặp kề tại mở đầu trích dẫn; VI cắt khối này",
     1, None, None, "LC", None),
    ("S031", "connect", "L", "synonym",
     "S028: designed to link content creators with consumers", "high", None,
     "đồng nghĩa link → connect (cùng khung nối người sáng tạo với người "
     "dùng), sau 3 câu",
     1, None, None, "LC", None),
    ("S032", "travellers", "L", "repetition",
     "S015: visitors travelling from Japan to Australia", "high", None,
     "tái lập chuỗi du khách (travellers/tourists/visitors) sau 17 câu",
     1, None, None, "LC", None),
    ("S035", "communities", "L", "repetition",
     "S032: Community-driven travel", "high", None,
     "gia đình hình thái (community → communities), sau 3 câu",
     1, None, None, "LC", None),
    ("S037", "AI-driven", "L", "repetition",
     "S036: the use of AI", "high", None,
     "tái lập chuỗi AI dưới dạng tính từ hóa, câu kề; khối EN-only",
     1, None, None, "LC", None),
    ("S038", "airlines", "L", "repetition",
     "S037: Many airlines", "high", None,
     "lặp kề trong lượt lời Aitken; chuỗi 'airline' xuyên văn bản (S011 "
     "The airline, S019 airline industry)",
     1, None, None, "LC", None),
]

TT = [
    # ---------- R (4) — analysis §4.2 ----------
    # R-VI1: đại từ ngôi 2 hướng độc giả — quy chiếu ngoại văn bản (ref=E),
    # đối xứng với EN "you"; "bạn" xuất hiện 2 lần cùng chuỗi — 1 mark, occ 1
    ("S001", "bạn", "R", "personal", "ngoài văn bản (độc giả bài viết)",
     "high", None,
     "quy chiếu ngoại: nhà báo gọi độc giả; EN đối ứng 'you' (R-EN1); "
     "'bạn' thứ hai cùng câu cùng chuỗi — 1 mark (occ 1)",
     1, None, None, "LC", "E"),

    # R-VI2: chỉ từ hồi quy trỏ quy trình ETIAS; EN đối ứng "It's" (R-EN2)
    ("S010", "Đây", "R", "demonstrative", "S009: Quy trình ETIAS",
     "high", None, "chỉ từ hồi quy (quy chiếu mở rộng); EN dùng đại từ 'It'",
     1, None, None, "LC", "A"),

    # R-VI3: chỉ từ "này" + danh từ tổng quát trỏ Virgin Australia;
    # EN đối ứng "The airline" là L — dịch chuyển EN the -> VI này
    ("S015", "Hãng hàng không này", "R", "demonstrative",
     "S014: Virgin Australia",
     "high", None,
     "chỉ từ 'này' + general word 'hãng hàng không'; EN đối ứng 'The "
     "airline' (L-EN3) — dịch chuyển the -> này",
     1, None, None, "LC", "A"),

    # R-VI4: chỉ từ "này" + danh từ mới "tuyến bay" trỏ dịch vụ Cairns–Tokyo;
    # EN đối ứng "the route" là L
    ("S016", "tuyến bay này", "R", "demonstrative",
     "S015: dịch vụ từ Cairns đến Tokyo",
     "high", None,
     "chỉ từ 'này' + danh từ mới 'tuyến bay' (đồng nghĩa 'dịch vụ'); EN "
     "đối ứng 'the route' (L-EN4) — dịch chuyển the -> này",
     1, None, None, "LC", "A"),

    # ---------- S (0) — analysis §3: không có phép thế ----------

    # ---------- E (0) — analysis §2: không có zero chủ ngữ liên câu ----------

    # ---------- C (5) — analysis §5 ----------
    # C-VI1: TỰ SINH khi VI tách EN S003 thành 2 câu; EN gốc là cụm cộng thêm
    # "with work underway" — không có đối lập (dịch chuyển, §7)
    ("S004", "Tuy nhiên", "C", "adversative",
     "S003: Chương trình sẽ được bắt đầu từ tháng này nhưng chỉ dành cho một số lượng hạn chế người Úc",
     "high", None,
     "tự sinh khi tách EN S003 thành 2 câu; EN diễn đạt additive bằng "
     "'with work underway' — không có hàng C đối ứng phía EN",
     1, None, None, "LC", None),

    # C-VI2: đối ứng "Meanwhile" (C-EN1) 1–1
    ("S013", "Trong khi đó", "C", "temporal",
     "S012: Hãng hàng không sẽ ngừng bay giữa Sydney và Seoul",
     "high", None, "đối ứng 'Meanwhile' 1–1",
     1, None, None, "LC", None),

    # C-VI3: đối ứng "also" (C-EN2) 1–1
    ("S014", "cũng", "C", "additive",
     "S013: Emirates sẽ cắt giảm các chuyến bay giữa Singapore và Melbourne",
     "high", None, "đối ứng 'also' 1–1",
     1, None, None, "LC", None),

    # C-VI4: đối ứng "However" (C-EN3) 1–1
    ("S021", "Tuy nhiên", "C", "adversative",
     "S020: khiến việc suy đoán về các yếu tố có thể tác động đến giá vé máy bay trong tương lai trở nên khó khăn",
     "high", None, "đối ứng 'However' (S020) 1–1",
     1, None, None, "LC", None),

    # C-VI5: đối ứng "However" (C-EN4) 1–1
    ("S024", "Tuy nhiên", "C", "adversative",
     "S023: giá nhiên liệu máy bay, thường chiếm từ 15 đến 25 phần trăm chi phí hoạt động",
     "high", None, "đối ứng 'However' (S023) 1–1",
     1, None, None, "LC", None),

    # ---------- L (6) — analysis §6.3 ----------
    # L-VI1: đồng nghĩa mới vào chuỗi "chương trình"; EN đối ứng "work underway"
    ("S004", "kế hoạch", "L", "synonym",
     "S003: Chương trình",
     "med", None,
     "VI đổi từ gọi: chương trình -> kế hoạch; EN đối ứng là danh từ "
     "chung 'work underway' (S003)",
     1, None, None, "LC", None),

    # L-VI2: tái lập tên đầy đủ sau 3 câu (S003–S004 chỉ dùng dạng rút)
    ("S005", "chương trình Global Entry", "L", "repetition",
     "S002: chương trình Nhập cảnh Toàn cầu ưu tiên - Global Entry",
     "high", None, "tái lập tên đầy đủ sau 3 câu; EN đối ứng S004 (L-EN1)",
     1, None, None, "LC", None),

    # L-VI3: danh từ thượng vị mô tả lại Qantas; EN đối ứng "The airline" (S011)
    ("S012", "Hãng hàng không", "L", "superordinate", "S011: Qantas",
     "high", None, "thượng vị mới vào chuỗi hãng bay; EN đối ứng 'The airline' (L-EN2)",
     1, None, None, "LC", None),

    # L-VI4: biến thể số nhiều, tái lập tại mở đầu lượt trích dẫn
    ("S016", "các dịch vụ", "L", "repetition",
     "S015: dịch vụ từ Cairns đến Tokyo",
     "med", None, "biến thể số nhiều tại mở đầu lượt trích dẫn (Virgin)",
     1, None, None, "LC", None),

    # L-VI5: biến thể hình thái cạnh tranh -> đối thủ cạnh tranh, gap 2
    ("S021", "đối thủ cạnh tranh", "L", "repetition",
     "S019: sự cạnh tranh",
     "high", None, "biến thể hình thái, khoảng cách 2 câu; EN đối ứng "
     "'greater competition' (L-EN6)",
     1, None, None, "LC", None),

    # L-VI6: khung mở–đóng của trích dẫn ACCC (S020 -> S023), gap 3
    ("S023", "yếu tố", "L", "repetition",
     "S020: các yếu tố",
     "med", None, "khung trích dẫn ACCC; EN đối ứng 'factors' (L-EN7)",
     1, None, None, "LC", None),
]
