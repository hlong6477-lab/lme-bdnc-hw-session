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

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn nội dung, tên riêng, thuật ngữ
    # đa từ, động từ attribution — 33 hàng mới; 12 hàng L cũ giữ nguyên.
    ("S002", "Any visit", "L", "repetition",
     "S001: a possible visit by Pope Francis", "high", None,
     "chuỗi chuyến thăm: 'visit' lặp câu kề; 'Any' là lượng từ",
     1, None, None, "LC", None),
    ("S002", "priests", "L", "collocation", "S001: a Catholic news agency",
     "med", None,
     "trường liên tưởng tôn giáo Công giáo (linh mục), câu kề",
     1, None, None, "LC", None),
    ("S003", "Catholic", "L", "repetition", "S001: a Catholic news agency",
     "high", None, "tính từ tái lập chuỗi Công giáo, gap 2",
     1, None, None, "LC", None),
    ("S004", "South Korea", "L", "repetition", "S001: outh Korea's", "high",
     None,
     "tên nước, gia đình hình thái 'Korea'; S001 lỗi nguồn thiếu 'S' (§8a), "
     "gap 3", 1, None, None, "LC", None),
    ("S004", "said", "L", "repetition", "S001: has said", "high", None,
     "động từ attribution, gap 3", 1, None, None, "LC", None),
    ("S004", "a Mass", "L", "collocation", "S003: Catholic", "med", None,
     "trường liên tưởng tôn giáo (thánh lễ ↔ Công giáo)",
     1, None, None, "LC", None),
    ("S004", "the Pontifical Mission Societies", "L", "synonym",
     "S001: Pope Francis", "med", None,
     "'Pontifical' = 'thuộc Giáo hoàng' ≈ papal; tên riêng = 1 chuỗi",
     1, None, None, "LC", None),
    ("S005", "Fides", "L", "repetition", "S004: Fides", "high", None,
     "tên riêng hãng tin, gap 1", 1, None, None, "LC", None),
    ("S005", "said", "L", "repetition", "S004: said", "high", None,
     "động từ attribution, gap 1", 1, None, None, "LC", None),
    ("S005", "Park", "L", "repetition", "S004: Park Jie-won", "high", None,
     "tên riêng rút gọn còn họ, gap 1", 1, None, None, "LC", None),
    ("S005", "the Mass", "L", "repetition", "S004: a Mass", "high", "R: the",
     "thánh lễ tái lập với mạo từ xác định, gap 1",
     1, None, None, "LC", None),
    ("S005", "the Vatican's", "L", "repetition", "S001: the Vatican", "high",
     "R: the", "tái lập sau 4 câu, sở hữu cách", 1, None, None, "LC", None),
    ("S005", "South Korea", "L", "repetition", "S004: South Korea", "high",
     None, "tên nước lặp câu kề", 1, None, None, "LC", None),
    ("S005", "Archbishop", "L", "collocation", "S004: a Mass", "med", None,
     "trường liên tưởng tôn giáo (tổng giám mục); 2 lần trong câu",
     2, None, None, "LC", None),
    ("S006", "Park", "L", "repetition", "S005: Park", "high", None,
     "tên riêng, gap 1", 1, None, None, "LC", None),
    ("S007", "Park", "L", "repetition", "S006: Park", "high", None,
     "tên riêng, gap 1", 1, None, None, "LC", None),
    ("S007", "the church", "L", "collocation", "S005: the Mass", "med", None,
     "liên tưởng nhà thờ ↔ thánh lễ (nơi Park phát biểu), gap 2",
     1, None, None, "LC", None),
    ("S007", "spoke", "L", "synonym", "S005: told", "high", None,
     "động từ attribution ('spoke' ≈ 'told' — phát biểu), gap 2",
     1, None, None, "LC", None),
    ("S007", "comments", "L", "synonym", "S004: the announcement", "med",
     None,
     "'comments' ≈ 'announcement' — cùng chỉ lời Park tại thánh lễ, gap 3",
     1, None, None, "LC", None),
    ("S007", "attendance", "L", "collocation", "S005: the Mass", "low", None,
     "cầu nối tham dự ↔ thánh lễ (Park dự thánh lễ); liên tưởng gián tiếp, "
     "gap 2", 1, None, None, "LC", None),
    ("S008", "Park's", "L", "repetition", "S007: Park", "high", None,
     "tên riêng sở hữu cách, gap 1", 1, None, None, "LC", None),
    ("S008", "confirmed", "L", "repetition", "S007: confirmed", "high", None,
     "động từ 'xác nhận' tái lập, gap 1", 1, None, None, "LC", None),
    ("S008", "comments", "L", "repetition", "S007: comments", "high", None,
     "danh từ 'phát biểu' tái lập, gap 1", 1, None, None, "LC", None),
    ("S009", "South Korean", "L", "repetition", "S005: South Korea", "high",
     None,
     "gia đình hình thái (tính từ hóa), gap 4; mở đoạn nền 2018",
     1, None, None, "LC", None),
    ("S009", "an invitation", "L", "collocation",
     "S005: a possible papal visit", "med", None,
     "liên tưởng thư mời ↔ chuyến thăm (nội dung thư mời), gap 4",
     1, None, None, "LC", None),
    ("S009", "relayed", "L", "synonym", "S005: told", "med", None,
     "động từ truyền đạt 'chuyển lời' — biến thể chuỗi attribution, gap 4",
     1, None, None, "LC", None),
    ("S010", "Kim and Moon", "L", "repetition",
     "S009: Kim Jong Un và Moon Jae-in", "high", None,
     "hai tên riêng rút gọn còn họ, gap 1", 1, None, None, "LC", None),
    ("S011", "Vatican officials", "L", "repetition",
     "S005: the Vatican's", "high", None,
     "'Vatican' tái lập trong tổ hợp mới, gap 6", 1, None, None, "LC", None),
    ("S011", "said", "L", "repetition", "S005: said", "high", None,
     "động từ attribution, gap 6", 1, None, None, "LC", None),
    ("S012", "any invitation", "L", "repetition",
     "S011: an official written invitation", "high", None,
     "chuỗi thư mời, biến thể rút gọn, gap 1", 1, None, None, "LC", None),
    ("S013", "said", "L", "repetition", "S011: said", "high", None,
     "động từ attribution, gap 2", 1, None, None, "LC", None),
    ("S013", "consider", "L", "repetition", "S011: considered", "high", None,
     "động từ 'xem xét' tái lập, gap 2", 1, None, None, "LC", None),
    ("S013", "made", "L", "repetition", "S004: made the announcement", "med",
     None,
     "động từ nhẹ 'make' tái lập ('made the announcement' ↔ 'made many "
     "appeals'), gap 9", 1, None, None, "LC", None),
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

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1, thay thế chính sách hẹp §6.1 analysis):
    # từ đơn nội dung, tên riêng, thuật ngữ đa từ, động từ attribution đều là 1
    # chuỗi; lặp cùng dạng ở câu kề CŨNG được đánh dấu. 30 hàng mới; 6 hàng L cũ
    # giữ nguyên. Quyết định độc lập theo văn bản VI (hàng EN chỉ để đối chiếu).
    ("S002", "chuyến thăm", "L", "repetition",
     "S001: chuyến thăm (trong 'thực hiện chuyến thăm tới Triều Tiên')",
     "high", None,
     "lặp danh từ ở câu kề (v2 bỏ hạn chế 'câu kề không đánh dấu'); EN đối "
     "ứng 'Any visit'", 1, None, None, "LC", None),
    ("S002", "Triều Tiên", "L", "repetition", "S001: Triều Tiên", "high",
     None,
     "lặp tên riêng ở câu kề (v2); EN dùng R 'the reclusive state' — VI "
     "thuần lặp tên nên theo TNT thuộc L", 1, None, None, "LC", None),
    ("S002", "linh mục", "L", "collocation",
     "S001: Công giáo (trong 'hãng thông tấn Công giáo')", "med", None,
     "trường liên tưởng tôn giáo (linh mục ↔ Công giáo), câu kề; EN đối ứng "
     "'priests'", 1, None, None, "LC", None),
    ("S003", "Triều Tiên", "L", "repetition", "S002: Triều Tiên", "high",
     None,
     "lặp tên riêng ở câu kề (v2); EN đối ứng 'its citizens' — VI hiện thực "
     "hóa 'công dân Triều Tiên'", 1, None, None, "LC", None),
    ("S003", "Công giáo", "L", "repetition",
     "S001: Công giáo (trong 'hãng thông tấn Công giáo')", "high", None,
     "tái lập chuỗi Công giáo, gap 2; EN đối ứng 'Catholic'",
     1, None, None, "LC", None),
    ("S003", "tín đồ", "L", "collocation", "S002: linh mục", "med", None,
     "trường liên tưởng tôn giáo (tín đồ ↔ linh mục — nhân vật tôn giáo), "
     "gap 1", 1, None, None, "LC", None),
    ("S003", "đức tin", "L", "collocation", "S001: Công giáo", "med", None,
     "trường liên tưởng tôn giáo (đức tin ↔ Công giáo), gap 2; EN v2 không "
     "đánh dấu 'faith' — quyết định riêng phía VI", 1, None, None, "LC",
     None),
    ("S004", "cho biết", "L", "repetition", "S001: cho biết", "high", None,
     "động từ attribution, gap 3 (S001 có 2 lần 'cho biết'); EN đối ứng "
     "'said'", 1, None, None, "LC", None),
    ("S004", "Hàn Quốc", "L", "repetition",
     "S001: Hàn Quốc (trong 'cơ quan tình báo Hàn Quốc')", "high", None,
     "tên nước, gap 3; EN đối ứng 'South Korea'", 1, None, None, "LC",
     None),
    ("S004", "thánh lễ", "L", "collocation", "S003: Công giáo", "med",
     None,
     "trường liên tưởng tôn giáo (thánh lễ ↔ Công giáo), gap 1; EN đối ứng "
     "'a Mass'", 1, None, None, "LC", None),
    ("S004", "Hiệp hội Truyền giáo Giáo hoàng", "L", "synonym",
     "S001: Giáo hoàng Francis", "med", None,
     "'Giáo hoàng' trong tên riêng tổ chức ≈ papal; v2: tên riêng = 1 "
     "chuỗi; EN đối ứng 'the Pontifical Mission Societies'",
     1, None, None, "LC", None),
    ("S004", "Mokpo", "L", "collocation", "S001: Hàn Quốc", "med", None,
     "liên tưởng thành phố ↔ quốc gia (Mokpo thuộc Hàn Quốc), gap 3; cùng "
     "kiểu liên tưởng Seoul/Bình Nhưỡng nhưng không phải thủ đô",
     1, None, None, "LC", None),
    ("S005", "Fides", "L", "repetition", "S004: Fides", "high", None,
     "tên riêng hãng tin, gap 1; EN đối ứng 'Fides'", 1, None, None, "LC",
     None),
    ("S005", "đưa tin", "L", "synonym", "S004: cho biết", "med", None,
     "động từ attribution biến thể ('đưa tin' ≈ 'cho biết'), gap 1; EN đối "
     "ứng 'said' (lặp nguyên dạng)", 1, None, None, "LC", None),
    ("S005", "Park", "L", "repetition", "S004: Park Jie-won", "high",
     None,
     "tên riêng rút gọn còn họ, gap 1; EN đối ứng 'Park'",
     1, None, None, "LC", None),
    ("S005", "Thánh lễ", "L", "repetition", "S004: thánh lễ", "high",
     None,
     "thánh lễ tái lập (dạng viết hoa 'Thánh lễ' giữ nguyên văn), "
     "gap 1; EN đối ứng 'the Mass'", 1, None, None, "LC", None),
    ("S005", "Tổng giám mục", "L", "collocation", "S004: thánh lễ", "med",
     None,
     "trường liên tưởng tôn giáo (tổng giám mục ↔ thánh lễ), gap 1; 2 lần "
     "trong câu — occ 2; EN đối ứng 'Archbishop'", 2, None, None, "LC",
     None),
    ("S005", "Vatican", "L", "repetition", "S001: Vatican", "high", None,
     "tái lập sau 4 câu trong tổ hợp 'đại sứ của Vatican'; EN đối ứng 'the "
     "Vatican's'", 1, None, None, "LC", None),
    ("S005", "Hàn Quốc", "L", "repetition", "S004: Hàn Quốc", "high",
     None,
     "tên nước lặp câu kề; EN đối ứng 'South Korea'", 1, None, None, "LC",
     None),
    ("S005", "khả năng", "L", "repetition",
     "S001: khả năng (trong 'làm việc về khả năng')", "high", None,
     "danh từ 'khả năng' tái lập sau 4 câu; EN gộp trong NP 'a possible "
     "papal visit' (hàng cũ)", 1, None, None, "LC", None),
    ("S005", "Gwangju", "L", "collocation", "S004: Hàn Quốc", "med", None,
     "liên tưởng thành phố ↔ quốc gia (Gwangju thuộc Hàn Quốc), gap 1; yếu "
     "hơn liên tưởng thủ đô Seoul/Bình Nhưỡng", 1, None, None, "LC", None),
    ("S006", "Park", "L", "repetition", "S005: Park", "high", None,
     "tên riêng, gap 1; EN đối ứng 'Park'", 1, None, None, "LC", None),
    ("S007", "Park", "L", "repetition", "S006: Park", "high", None,
     "tên riêng, gap 1; EN đối ứng 'Park'", 1, None, None, "LC", None),
    ("S007", "nhà thờ", "L", "collocation", "S005: Thánh lễ", "med", None,
     "liên tưởng nhà thờ ↔ thánh lễ (nơi Park phát biểu), gap 2; EN đối "
     "ứng 'the church'", 1, None, None, "LC", None),
    ("S007", "nói chuyện", "L", "repetition",
     "S005: nói (trong 'ông Park nói với những người tham dự')", "high",
     None,
     "động từ attribution, gia đình hình thái 'nói', gap 2; EN đối ứng "
     "'spoke' (synonym ← 'told')", 1, None, None, "LC", None),
    ("S007", "bình luận", "L", "synonym",
     "S004: thông báo (trong 'đưa ra thông báo này')", "med", None,
     "'bình luận' ≈ 'thông báo' — cùng chỉ lời Park tại thánh lễ, gap 3; "
     "EN đối ứng 'comments' ≈ 'the announcement'", 1, None, None, "LC",
     None),
    ("S007", "tham dự", "L", "repetition",
     "S005: tham dự (trong 'những người tham dự Thánh lễ')", "high", None,
     "lặp 'tham dự' (người tham dự → sự tham dự của ông), gap 2; EN đối "
     "ứng 'attendance' (chỉ collocation tới 'the Mass')",
     1, None, None, "LC", None),
    ("S008", "Park", "L", "repetition", "S007: Park", "high", None,
     "tên riêng, gap 1; EN đối ứng 'Park's'", 1, None, None, "LC", None),
    ("S008", "xác nhận", "L", "repetition", "S007: xác nhận", "high",
     None,
     "động từ 'xác nhận' tái lập (S007 có 2 lần), gap 1; EN đối ứng "
     "'confirmed'", 1, None, None, "LC", None),
    ("S008", "bình luận", "L", "repetition", "S007: bình luận", "high",
     None,
     "danh từ 'bình luận' tái lập, gap 1; EN đối ứng 'comments'",
     1, None, None, "LC", None),
]
