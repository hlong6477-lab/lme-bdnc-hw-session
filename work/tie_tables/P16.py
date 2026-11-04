# P16 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P16_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# occ note (CONVENTIONS §8.3): EN S013 "it" — substring "it" occurs 3x in the
# sentence ("wITh", "quITe", "about it"); the pronoun is occurrence 3.

ST = [
    # ---------- R (reference) — 9 hàng, §4.1 ----------
    ("S002", "the ruble", "R", "demonstrative",
     "S001: Russia's plunging currency", "med",
     "L: 'ruble' ~ 'currency' (đẳng nghĩa/thuộc)",
     "'the' + danh từ mới; sự xác định là liên kết chính tại vị trí; VI đối "
     "ứng 'đồng rúp' → L (dịch chuyển R→L, §7)", 1, None, None, "LC", "A"),
    ("S003", "That cutback", "R", "demonstrative",
     "S002: cutting back on spending", "high",
     "L: 'cutback' ← 'cutting back' (gia đình hình thái)",
     "chỉ từ 'That' + danh từ mới; quy chiếu mở rộng tới sự kiện S002; VI "
     "'Sự cắt giảm đó' (R)", 1, None, None, "LC", "A"),
    ("S006", "it", "R", "personal", "S005: the Russians", "med", None,
     "'it' = thị trường Nga (người Nga với tư cách thị trường) — quy chiếu mở "
     "rộng; mở lời trích dẫn Suladda; VI 'đó'", 1, None, None, "LC", "A"),
    ("S012", "We", "R", "personal",
     "S011: Suladda (attribution 'Suladda said')", "med", None,
     "ngôi 1 trong trích dẫn, attribution ở câu trước → đủ điều kiện [LC] "
     "(CONVENTIONS §1); 'we' inclusive (ngành du lịch); VI 'Chúng ta'",
     1, None, None, "LC", "A"),
    ("S012", "it", "R", "personal", "S011: things (to stay bad)", "med", None,
     "quy chiếu mở rộng tới tình hình khủng hoảng; 'things' S011 quá tổng "
     "quát, không đánh dấu riêng; VI 'tình trạng này'", 1, None, None, "LC",
     "A"),
    ("S013", "it", "R", "personal", "S012: it ('s going to end)", "high", None,
     "lặp quy chiếu 'it' trong cùng lời trích dẫn; VI đối ứng là ∅ bổ ngữ "
     "(E) — dịch chuyển R→E; occ 3 vì 'it' ⊂ 'with', 'quite'",
     3, None, None, "LC", "A"),
    ("S014", "other markets", "R", "comparative", "S013: the Russian market",
     "med", "L: 'markets' lặp kề 'market' S013",
     "'other' đối lập với 'the Russian market' vừa nêu — quy chiếu so sánh "
     "(H&H); VI 'các thị trường khác'", 1, None, None, "LC", "A"),
    ("S017", "those", "R", "demonstrative", "S015: the Russians", "med",
     "S: 'those' (đọc thế danh từ)",
     "'those still yearning…' — tập con của chuỗi du khách Nga; 'they' cùng "
     "câu [TC] không đánh dấu; VI hiện thực hóa 'những người…'",
     1, None, None, "LC", "A"),
    ("S018", "the \"unfavorable situation\"", "R", "demonstrative",
     "S012: it ('s going to end)", "med",
     "L: danh ngữ tự neo qua 'depreciating the ruble'",
     "quy chiếu mở rộng tới khủng hoảng; danh từ chung mới + mạo từ, trong "
     "lời Putin; VI 'tình hình' → L (R→L)", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 0 hàng: EN không có khe ∅ (analysis §2) ----------

    # ---------- C (conjunction) — 2 hàng [LC], §5 ----------
    ("S010", "But", "C", "adversative",
     "S009: The number of Russian visitors … totaled 1.4 million", "high",
     None, "tương phản: 11 tháng khá ổn (1,4 triệu) ↔ tháng 12 'a disaster'",
     1, None, None, "LC", None),
    ("S014", "But", "C", "adversative",
     "S013: they are quite worried about it", "high", None,
     "tương phản: lo ngại ↔ 'trying to shift to other markets'",
     1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 19 hàng [LC], §6.3 ----------
    ("S004", "the Russians", "L", "repetition", "S002: Russians", "high",
     "R: the",
     "tái lập chuỗi sau 2 câu; đầu ngữ lặp từ vựng tiền trạm nên L là liên "
     "kết chính (CONVENTIONS §1)", 1, None, None, "LC", None),
    ("S004", "big spenders", "L", "repetition", "S002: spending", "high",
     None, "gia đình hình thái 'spend-' ('spending' → 'spenders'); VI 'chịu "
     "chi' ~ 'chi tiêu'", 1, None, None, "LC", None),
    ("S005", "the beach resort", "L", "repetition",
     "S003: the beach resort city of Pattaya", "high", "R: the",
     "biến thể rút gọn (bỏ 'city of Pattaya'); khoảng cách 2 câu",
     1, None, None, "LC", None),
    ("S007", "Russian tourists", "L", "repetition", "S005: the Russians",
     "high", None,
     "biến thể mới vào chuỗi (tính từ hóa + 'tourists'); mở lời trích dẫn — "
     "điểm nối diễn ngôn (§8.1)", 1, None, None, "LC", None),
    ("S008", "Suladda", "L", "repetition", "S005: Suladda Sarutilavan",
     "high", None,
     "lặp tên người nói trong attribution 'said Suladda' sau 3 câu — "
     "§8.1(iii); VI lược attribution (§8)", 1, None, None, "LC", None),
    ("S009", "all of Thailand", "L", "repetition",
     "S001: Thailand's (multi-billion dollar tourism industry)", "high", None,
     "tái lập chuỗi sau 8 câu bằng biến thể 'all of' — trở lại phạm vi quốc "
     "gia; S003–S005 chỉ là định ngữ trong tên thực thể khác",
     1, None, None, "LC", None),
    ("S010", "a drop of 50 percent", "L", "repetition",
     "S004: a 70 percent drop", "high", None,
     "lặp 'drop' sau 6 câu; hai chỉ số khác nhau (đặt phòng ↔ tổng khách) — "
     "liên kết từ vựng, không quy chiếu", 1, None, None, "LC", None),
    ("S010", "the national hotel operators' association", "L", "synonym",
     "S004: the Thai Hotel Association", "low", "R: the",
     "bridging: có thể cùng một hiệp hội (mô tả lại) hoặc tổ chức khác — conf "
     "low, nêu cả hai phương án (CONVENTIONS §4)", 1, None, None, "LC", None),
    ("S011", "Suladda", "L", "repetition", "S008: said Suladda", "high", None,
     "attribution 'Suladda said' tái lập sau 3 câu — §8.1(iii)",
     1, None, None, "LC", None),
    ("S011", "popular destinations", "L", "superordinate",
     "S005: the beach resort", "high", None,
     "general word 'destinations' quy về chuỗi điểm nghỉ mát; khoảng cách 6 "
     "câu, mở đoạn + attribution mới", 1, None, None, "LC", None),
    ("S011", "visitors", "L", "superordinate", "S010: Russian tourists",
     "med", None,
     "general word ('tourists' ⊂ 'visitors'); khoảng cách 1 câu nhưng tại "
     "mở đoạn + attribution mới (§8.1(ii))", 1, None, None, "LC", None),
    ("S011", "Russian rubles", "L", "repetition", "S002: the ruble", "high",
     None,
     "tái lập chuỗi đồng rúp sau 9 câu bằng biến thể thêm 'Russian'; trong "
     "bổ ngữ 'converting … into Thai baht'", 1, None, None, "LC", None),
    ("S013", "the Russian market", "L", "repetition",
     "S006: a major or main market", "high", "R: the",
     "tái lập chuỗi 'market' sau 7 câu, xác định hóa + bổ nghĩa 'Russian'; "
     "trong lời trích dẫn Suladda", 1, None, None, "LC", None),
    ("S014", "Russian incoming tourists", "L", "repetition",
     "S010: Russian tourists", "high", None,
     "biến thể thêm 'incoming'; tái lập sau 4 câu trong lời trích dẫn",
     1, None, None, "LC", None),
    ("S014", "Suladda", "L", "repetition", "S011: Suladda said", "high", None,
     "attribution 'said Suladda' tái lập sau 3 câu — §8.1(iii); VI lược "
     "attribution (§8)", 1, None, None, "LC", None),
    ("S015", "resort cities", "L", "superordinate",
     "S011: popular destinations", "high", None,
     "từ tổng quát trở lại cụ thể, mở đoạn trả lời của ngành; chuỗi gốc "
     "'beach resort city' S003; 'islands' là thành viên mới (Phuket, Samui "
     "là đảo)", 1, None, None, "LC", None),
    ("S015", "the shortfall", "L", "synonym",
     "S014: the decreasing number of Russian incoming tourists", "high",
     "R: the",
     "'shortfall' đồng nghĩa 'drop/loss/decreasing' (chuỗi S004, S010); mở "
     "đoạn", 1, None, None, "LC", None),
    ("S016", "the Russian market", "L", "repetition",
     "S013: the Russian market", "high", "R: the",
     "tái lập cùng dạng sau 3 câu (qua 'other markets' S014); mạch nền 'In "
     "recent years'", 1, None, None, "LC", None),
    ("S018", "the ruble", "L", "repetition", "S011: Russian rubles", "high",
     "R: the",
     "tái lập chuỗi sau 7 câu tại attribution Putin ('depreciating the "
     "ruble')", 1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 6 hàng, §4.2 ----------
    ("S003", "Sự cắt giảm đó", "R", "demonstrative",
     "S002: (người Nga) đang cắt giảm chi tiêu", "high",
     "L: 'cắt giảm' lặp từ vựng",
     "chỉ từ 'đó' + danh từ lặp từ trở; quy chiếu mở rộng tới sự việc S002; "
     "đối ứng EN 'That cutback' (R)", 1, None, None, "LC", "A"),
    ("S006", "đó", "R", "demonstrative", "S005: người Nga", "med", None,
     "'đó' = thị trường (người Nga) — quy chiếu mở rộng; mở lời trích dẫn; "
     "đối ứng EN 'it'", 1, None, None, "LC", "A"),
    ("S011", "hiệp hội này", "R", "demonstrative",
     "S005: Hiệp hội Du lịch Thái Lan", "high", None,
     "VI tự sinh 'thuộc hiệp hội này' (EN không có đối ứng — §8); chỉ từ "
     "'này' xác định hiệp hội nơi bà Suladda làm giám đốc",
     1, None, None, "LC", "A"),
    ("S012", "Chúng ta", "R", "personal",
     "S011: Bà Suladda (attribution 'nói')", "med", None,
     "ngôi 1 inclusive trong trích dẫn; attribution ở câu trước → đủ điều "
     "kiện [LC] (CONVENTIONS §1); đối ứng EN 'We'", 1, None, None, "LC", "A"),
    ("S012", "tình trạng này", "R", "demonstrative",
     "S011: mọi chuyện (sẽ tiếp tục xấu đi)", "med", None,
     "chỉ từ 'này' + danh từ chung mới; quy chiếu mở rộng; 'mọi chuyện' S011 "
     "không đánh dấu riêng; đối ứng EN 'it'", 1, None, None, "LC", "A"),
    ("S014", "các thị trường khác", "R", "comparative",
     "S013: thị trường Nga", "med", "L: 'thị trường' lặp kề",
     "'khác' đối lập với 'thị trường Nga' vừa nêu — quy chiếu so sánh, giữ "
     "chức năng 'other' (mapping §3.12); đối ứng EN 'other markets'",
     1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 2 hàng, §2 ----------
    ("S011", None, "E", "nominal", "S011: tất cả (trong câu)", "high", None,
     "[TC] lược chủ ngữ vế tọa hợp sau '–' (zero kéo dài sang 'đang dự "
     "kiến'); hồi phục {tất cả}; đọc thêm thế đại từ khiếm diện theo dõi "
     "nhân vật; EN đối ứng dùng chủ ngữ dùng chung",
     1, "– ", "{tất cả}", "TC", None),
    ("S013", None, "E", "nominal", "S012: tình trạng này", "high", None,
     "[LC] lược bổ ngữ của 'lo ngại'; hồi phục {về tình trạng này}; EN đối "
     "ứng 'about it' (R) — dịch chuyển R→E; đọc thêm thế đại từ khiếm diện "
     "theo dõi 'tình trạng này'", 1, "lo ngại", "{về tình trạng này}",
     "LC", None),

    # ---------- C (conjunction) — 2 hàng [LC], §5 ----------
    ("S010", "Nhưng", "C", "adversative",
     "S009: Con số du khách Nga … khoảng 1,4 triệu", "high", None,
     "tương phản: 11 tháng ↔ tháng 12 'coi như là tai hại'; đối ứng EN "
     "'But' S010", 1, None, None, "LC", None),
    ("S014", "Nhưng", "C", "adversative", "S013: họ rất lấy làm lo ngại",
     "high", None,
     "tương phản: lo ngại ↔ 'tìm cách chuyển qua các thị trường khác'; đối "
     "ứng EN 'But' S014", 1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 19 hàng [LC], §6.3 ----------
    ("S002", "đồng rúp", "L", "synonym", "S001: Chỉ tệ Nga", "high", None,
     "phép thế đẳng nghĩa ('chỉ tệ Nga' = 'đồng rúp'); EN đối ứng 'the "
     "ruble' là R — dịch chuyển R→L (§7)", 1, None, None, "LC", None),
    ("S004", "du khách Nga", "L", "repetition", "S002: người Nga", "high",
     None,
     "biến thể mới vào chuỗi ('người Nga' → 'du khách Nga'); tại attribution "
     "'Theo Hiệp hội…' — điểm nối diễn ngôn", 1, None, None, "LC", None),
    ("S004", "chịu chi", "L", "repetition", "S002: chi tiêu", "high", None,
     "gia đình hình thái 'chi' ('chi tiêu' → 'chịu chi'); đối ứng EN 'big "
     "spenders' ~ 'spending'", 1, None, None, "LC", None),
    ("S005", "bờ biển nghỉ mát", "L", "repetition",
     "S003: thành phố biển nghỉ mát Pattaya", "high", None,
     "biến thể ('thành phố biển' → 'bờ biển'), giữ 'nghỉ mát'; khoảng cách 2 "
     "câu", 1, None, None, "LC", None),
    ("S007", "Du khách Nga", "L", "repetition", "S004: du khách Nga", "high",
     None,
     "tái lập cùng dạng sau 3 câu, mở lời trích dẫn (lượt lời mới); đối ứng "
     "EN 'Russian tourists'", 1, None, None, "LC", None),
    ("S009", "toàn bộ Thái Lan", "L", "repetition",
     "S001: Thái Lan (công nghiệp du lịch…)", "high", None,
     "tái lập chuỗi sau 8 câu bằng biến thể 'toàn bộ'; đối ứng EN 'all of "
     "Thailand'", 1, None, None, "LC", None),
    ("S010", "hiệp hội điều hành khách sạn quốc gia", "L", "synonym",
     "S004: Hiệp hội Khách sạn Thái", "low", None,
     "bridging: có thể cùng tổ chức (mô tả lại) hoặc khác — conf low, nêu cả "
     "hai phương án; đối ứng EN S010", 1, None, None, "LC", None),
    ("S010", "sụt giảm", "L", "repetition", "S004: sụt giảm (tới 70%)",
     "high", None,
     "lặp 'sụt giảm' sau 6 câu; hai chỉ số khác nhau — liên kết từ vựng; đối "
     "ứng EN 'a drop of 50 percent'", 1, None, None, "LC", None),
    ("S011", "Bà Suladda", "L", "repetition",
     "S005: Bà Suladda Sarutilavan", "high", None,
     "attribution tái lập sau 6 câu (VI bỏ attribution ở S008 — §8); danh "
     "xưng 'Bà' giữ nguyên", 1, None, None, "LC", None),
    ("S011", "những điểm đến", "L", "superordinate",
     "S005: bờ biển nghỉ mát", "high", None,
     "general word; khoảng cách 6 câu, mở đoạn + attribution mới; đối ứng EN "
     "'popular destinations'", 1, None, None, "LC", None),
    ("S011", "du khách", "L", "repetition", "S010: du khách Nga", "med", None,
     "rút gọn ('Nga' chuyển sang 'đồng rúp Nga' cùng vế); khoảng cách 1 câu "
     "nhưng tại mở đoạn + attribution mới (§8.1(ii)); đối ứng EN 'visitors'",
     1, None, None, "LC", None),
    ("S011", "đồng rúp Nga", "L", "repetition", "S002: đồng rúp", "high",
     None,
     "tái lập chuỗi sau 9 câu, biến thể thêm 'Nga'; đối ứng EN 'Russian "
     "rubles'", 1, None, None, "LC", None),
    ("S013", "thị trường Nga", "L", "repetition",
     "S006: (một) thị trường lớn và chủ yếu", "high", None,
     "tái lập chuỗi 'thị trường' sau 7 câu, biến thể thêm 'Nga'; trong lời "
     "trích dẫn; đối ứng EN 'the Russian market'", 1, None, None, "LC", None),
    ("S014", "du khách Nga", "L", "repetition", "S010: du khách Nga", "high",
     None,
     "tái lập cùng dạng sau 4 câu trong lời trích dẫn; đối ứng EN 'Russian "
     "incoming tourists'", 1, None, None, "LC", None),
    ("S015", "thành phố nghỉ mát", "L", "superordinate",
     "S011: những điểm đến", "high", None,
     "từ tổng quát trở lại cụ thể, mở đoạn; 'các đảo' là thành viên mới; đối "
     "ứng EN 'resort cities'", 1, None, None, "LC", None),
    ("S015", "khoản thất thu", "L", "synonym",
     "S014: (số du khách Nga) sụt giảm", "high", None,
     "'thất thu' đồng nghĩa 'sụt giảm' (chuỗi S004, S010); mở đoạn; đối ứng "
     "EN 'the shortfall'", 1, None, None, "LC", None),
    ("S016", "thị trường Nga", "L", "repetition", "S013: thị trường Nga",
     "high", None,
     "tái lập cùng dạng sau 3 câu (qua 'các thị trường khác' S014); mạch nền "
     "'Trong những năm gần đây'", 1, None, None, "LC", None),
    ("S018", "tình hình", "L", "synonym", "S012: tình trạng (này)", "med",
     None,
     "gần đồng nghĩa ('tình trạng' → 'tình hình'), tái lập sau 6 câu tại "
     "attribution Putin; EN đối ứng 'the \"unfavorable situation\"' là R — "
     "dịch chuyển R→L", 1, None, None, "LC", None),
    ("S018", "đồng rúp", "L", "repetition", "S011: đồng rúp Nga", "high",
     None,
     "tái lập chuỗi sau 7 câu tại attribution Putin ('làm hạ giá đồng "
     "rúp'); đối ứng EN 'the ruble'", 1, None, None, "LC", None),
]
