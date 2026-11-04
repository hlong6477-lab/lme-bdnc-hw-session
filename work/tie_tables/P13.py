# P13 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P13_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)

ST = [
    # ---------- R (reference) — 4 hàng, §4.1 ----------
    ("S002", "the reclusive state", "R", "demonstrative", "S001: North Korea",
     "high", None,
     "danh ngữ mô tả mới; 'the' là liên kết duy nhất; VI lặp tên 'Triều Tiên' "
     "(R→L, lặp kề — không đánh dấu VI)", 1, None, None, "LC", "A"),
    ("S003", "its", "R", "personal",
     "S002: the reclusive state (North Korea)", "high", None,
     "its citizens = công dân Triều Tiên; VI hiện thực hóa 'công dân Triều Tiên'",
     1, None, None, "LC", "A"),
    ("S004", "the announcement", "R", "demonstrative",
     "S001: nội dung phát biểu ('has said')", "med", "L: 'announcement' ~ 'said'",
     "quy chiếu mở rộng; 'the' là liên kết duy nhất (danh từ mới); VI 'thông "
     "báo này'", 1, None, None, "LC", "A"),
    ("S013", "They", "R", "personal", "S011: Vatican officials", "high", None,
     "[+người, số nhiều]; câu thuộc khối VI cắt (§8b)", 1, None, None, "LC",
     "A"),

    # ---------- E (ellipsis) — 1 hàng [TC], §2 ----------
    ("S002", None, "E", "nominal", "S002: Any visit (trong câu)", "med",
     "L: 'the first' danh từ hóa",
     "[TC] tỉnh lược danh từ sau ordinal; hồi phục {visit} ← 'Any visit' cùng "
     "câu; VI lấp 'lần đầu tiên'", 1, "the first", "{visit}", "TC", None),

    # ---------- C (conjunction) — 3 hàng [LC], §5 ----------
    ("S010", "a month earlier", "C", "temporal",
     "S009: Moon Jae-in verbally relayed an invitation", "high", None,
     "quá khứ hoàn thành neo cuộc gặp Kim–Moon trước sự kiện chuyển thư mời 2018",
     1, None, None, "LC", None),
    ("S011", "afterwards", "C", "temporal",
     "S010: Kim and Moon had met a month earlier", "med", None,
     "vị trí giữa câu nhưng neo liên câu về chuỗi sự kiện 2018; khối VI cắt (§8b)",
     1, None, None, "LC", None),
    ("S012", "since then", "C", "temporal",
     "S009: In 2018 (thời điểm chuyển thư mời)", "high", None,
     "'then' hồi quy thời điểm 2018; khối VI cắt (§8b)", 1, None, None, "LC",
     None),

    # ---------- L (lexical cohesion) — 12 hàng [LC], §6.3 ----------
    ("S004", "the official agency", "L", "repetition",
     "S001: a Catholic news agency", "high", "R: the",
     "biến thể tổ hợp ('news agency' → 'official agency'); Fides đồng quy "
     "chiếu với hãng tin S001", 1, None, None, "LC", None),
    ("S005", "a possible papal visit", "L", "repetition",
     "S001: a possible visit by Pope Francis", "high", None,
     "biến thể thêm 'papal' (đồng thời tái lập chuỗi pope); tái lập sau 4 câu",
     1, None, None, "LC", None),
    ("S005", "Pyongyang", "L", "collocation", "S001: North Korea", "high",
     None, "liên tưởng thủ đô ↔ quốc gia (phép liên tưởng)", 1, None, None,
     "LC", None),
    ("S006", "director of the National Intelligence Service", "L", "synonym",
     "S001: outh Korea's intelligence chief", "high", None,
     "câu định danh Park: 'director' ↔ 'chief' (đồng nghĩa) + 'Intelligence' "
     "gia đình hình thái; nguyên văn typo 'outh' (§8a)", 1, None, None, "LC",
     None),
    ("S008", "The intelligence agency", "L", "repetition",
     "S006: the National Intelligence Service", "high", "R: The",
     "biến thể ('Service' → 'agency'); khoảng cách 2 câu", 1, None, None,
     "LC", None),
    ("S008", "Seoul", "L", "collocation", "S005: South Korea", "high", None,
     "liên tưởng thủ đô ↔ quốc gia (phép liên tưởng)", 1, None, None, "LC",
     None),
    ("S009", "North Korean", "L", "repetition", "S001: North Korea", "high",
     None, "gia đình hình thái (tính từ hóa); mở đoạn nền 2018", 1, None,
     None, "LC", None),
    ("S009", "the pope", "L", "repetition", "S001: Pope Francis", "high",
     "R: the",
     "'Pope' lặp từ trở + mạo từ xác định; S002 'a pope' là generic — không "
     "tính; mở đoạn nền 2018", 1, None, None, "LC", None),
    ("S011", "an official written invitation", "L", "repetition",
     "S009: an invitation", "high", None,
     "biến thể thêm bổ nghĩa 'official written'", 1, None, None, "LC", None),
    ("S013", "the pope", "L", "repetition", "S009: the pope", "high", "R: the",
     "tái lập sau 4 câu trong lời Vatican officials", 1, None, None, "LC",
     None),
    ("S013", "the two Koreas", "L", "repetition",
     "S009: South Korean President Moon Jae-in và North Korean leader Kim Jong Un",
     "high", "R: the two",
     "gộp hai chuỗi Nam–Bắc Triều Tiên đã thiết lập (S001, S009)", 1, None,
     None, "LC", None),
    ("S013", "such a trip", "L", "synonym",
     "S005: a possible papal visit", "med", "R: such",
     "'trip' đồng nghĩa 'visit'; 'such' khả năng quy chiếu — chọn L vì từ vựng "
     "là liên kết chính", 1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 1 hàng, §4.2 ----------
    ("S004", "thông báo này", "R", "demonstrative",
     "S001: nội dung phát biểu của Giám đốc cơ quan tình báo", "high", None,
     "demonstrative 'này' + danh từ mới; quy chiếu mở rộng; đối ứng EN 'the "
     "announcement' (R-EN3)", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 1 hàng [TC], §2 ----------
    ("S007", None, "E", "nominal", "S007: một người (trong câu)", "high", None,
     "[TC] lược chủ ngữ vế tọa hợp sau 'và' (zero kéo dài đến vế 'nhưng không "
     "xác nhận'); hồi phục {một người}; đọc thêm thế đại từ khiếm diện theo "
     "dõi nhân vật; EN đối ứng dùng chủ ngữ dùng chung", 1, "và ",
     "{một người}", "TC", None),

    # ---------- L (lexical cohesion) — 6 hàng [LC], §6.3 ----------
    ("S004", "hãng tin chính thức", "L", "repetition",
     "S001: một hãng thông tấn Công giáo", "high", None,
     "biến thể rút gọn ('hãng thông tấn' → 'hãng tin'); Fides đồng quy chiếu "
     "với hãng tin S001", 1, None, None, "LC", None),
    ("S005", "Giáo hoàng Francis", "L", "repetition",
     "S001: Giáo hoàng Francis", "high", None,
     "tái lập chuỗi nhân vật sau 4 câu; EN đối ứng 'papal' (gộp trong hàng 'a "
     "possible papal visit')", 1, None, None, "LC", None),
    ("S005", "Bình Nhưỡng", "L", "collocation", "S001: Triều Tiên", "high",
     None, "liên tưởng thủ đô ↔ quốc gia (phép liên tưởng); đối ứng EN "
     "'Pyongyang'", 1, None, None, "LC", None),
    ("S006", "giám đốc của Cơ quan Tình báo Quốc gia", "L", "repetition",
     "S001: Giám đốc cơ quan tình báo Hàn Quốc", "high", None,
     "câu định danh Park; đảo tổ hợp với 'của'; tái lập sau 5 câu", 1, None,
     None, "LC", None),
    ("S008", "Cơ quan tình báo", "L", "repetition",
     "S006: Cơ quan Tình báo Quốc gia", "high", None,
     "biến thể ('Quốc gia' → 'ở Seoul'); theo §3.9 lặp danh từ VI = L; khoảng "
     "cách 2 câu", 1, None, None, "LC", None),
    ("S008", "Seoul", "L", "collocation", "S005: Hàn Quốc", "high", None,
     "liên tưởng thủ đô ↔ quốc gia; đối ứng EN 'Seoul' S008", 1, None, None,
     "LC", None),
]
