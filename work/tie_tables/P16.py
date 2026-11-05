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

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn nội dung, lặp cùng dạng kể cả
    # câu kề, biến thể hình thái/đồng nghĩa, chuỗi động từ attribution;
    # 1 mark/câu/chuỗi; occ đếm tay. Không dùng regex/danh sách từ.
    ("S002", "crashing", "L", "synonym",
     "S001: plunging (currency)", "high", None,
     "đồng nghĩa ('crashing' ~ 'plunging': lao dốc) — chuỗi động từ mất giá",
     1, None, None, "LC", None),
    ("S002", "overseas travel", "L", "synonym",
     "S001: tourism industry", "med", None,
     "'travel' ~ 'tourism' (du lịch); người Nga cắt giảm du lịch nước ngoài",
     1, None, None, "LC", None),
    ("S005", "the Russians", "L", "repetition",
     "S004: the Russians", "high", "R: the",
     "lặp cùng dạng ở câu kề (§8.1(i)); sau attribution 'told VOA News'",
     1, None, None, "LC", None),
    ("S006", "Pattaya", "L", "repetition",
     "S003: the beach resort city of Pattaya", "high", None,
     "tái lập tên riêng trong trích dẫn; 'Pattaya office' S005 chỉ là định "
     "ngữ trong tên cơ quan nên không tính",
     1, None, None, "LC", None),
    ("S007", "number one", "L", "synonym",
     "S005: second to none", "med", None,
     "diễn giải lại trong trích dẫn ('number one' ~ 'second to none': đứng "
     "đầu)",
     1, None, None, "LC", None),
    ("S008", "said", "L", "synonym",
     "S005: told (VOA News)", "high", None,
     "chuỗi động từ attribution (§8.1(v)); 'said' ~ 'told'",
     1, None, None, "LC", None),
    ("S008", "Russian tourists", "L", "repetition",
     "S007: Russian tourists", "high", None,
     "lặp cùng dạng ở câu kề, trong cùng trích dẫn (§8.1(i))",
     1, None, None, "LC", None),
    ("S009", "Russian visitors", "L", "superordinate",
     "S008: Russian tourists", "high", None,
     "general word 'visitors' ('tourists' ⊂ 'visitors') — cùng quan hệ với "
     "hàng S011 hiện có",
     1, None, None, "LC", None),
    ("S010", "Russian tourists", "L", "repetition",
     "S008: Russian tourists", "high", None,
     "trở lại dạng 'tourists' qua biến thể 'Russian visitors' S009",
     1, None, None, "LC", None),
    ("S010", "December", "L", "repetition",
     "S004: December 28", "med", None,
     "lặp 'December' (mùa cao điểm 28/12–15/1 ↔ tháng 12); conf med vì S004 "
     "là ngày cụ thể",
     1, None, None, "LC", None),
    ("S010", "last year", "L", "repetition",
     "S008: Last year", "high", None,
     "lặp 'last year' (cùng chỉ năm 2013); 'compared to last year'",
     1, None, None, "LC", None),
    ("S010", "total", "L", "repetition",
     "S009: totaled (1.4 million)", "med", None,
     "gia đình hình thái 'total-' ('totaled' → 'the total number')",
     1, None, None, "LC", None),
    ("S010", "a disaster", "L", "collocation",
     "S001: suffering (tourism industry)", "low", None,
     "cùng trường nghĩa 'tình huống xấu' (S001 suffering → S010 disaster → "
     "S011 bad); liên tưởng trường nghĩa, conf low",
     1, None, None, "LC", None),
    ("S011", "expecting", "L", "repetition",
     "S010: expects (a drop of 50 percent)", "high", None,
     "lặp 'expect-' ở câu kề; dự báo của hiệp hội → nhận định của Suladda",
     1, None, None, "LC", None),
    ("S011", "bad", "L", "general word",
     "S010: a disaster", "med", None,
     "'stay bad' tổng quát hóa 'a disaster' (thảm họa → xấu)",
     1, None, None, "LC", None),
    ("S011", "Pattaya", "L", "repetition",
     "S006: Pattaya", "high", None,
     "tái lập tên riêng trong danh sách 'Pattaya, Phuket and Samui'",
     1, None, None, "LC", None),
    ("S011", "said", "L", "repetition",
     "S008: said (Suladda)", "high", None,
     "chuỗi động từ attribution (§8.1(v)); khác chuỗi tên riêng 'Suladda' "
     "cùng câu",
     1, None, None, "LC", None),
    ("S013", "worried", "L", "synonym",
     "S001: serious concerns", "high", None,
     "'worried' ~ 'concerns' (lo lắng); khoảng cách 12 câu, trong trích dẫn",
     1, None, None, "LC", None),
    ("S013", "hoteliers", "L", "synonym",
     "S010: the national hotel operators' association", "med", None,
     "'hoteliers' ~ 'hotel operators' (gia đình 'hotel-'); người ↔ tổ chức",
     1, None, None, "LC", None),
    ("S014", "decreasing", "L", "synonym",
     "S010: a drop of 50 percent", "high", None,
     "'decreasing' ~ 'drop' — chuỗi sụt giảm (S004 loss/drop → S010 → S015 "
     "shortfall)",
     1, None, None, "LC", None),
    ("S014", "said", "L", "repetition",
     "S011: (Suladda) said", "high", None,
     "chuỗi động từ attribution; cuối lời trích dẫn (§8.1(v))",
     1, None, None, "LC", None),
    ("S014", "Pattaya", "L", "repetition",
     "S011: Pattaya", "high", None,
     "tái lập tên riêng cuối lời trích dẫn ('to Pattaya')",
     1, None, None, "LC", None),
    ("S015", "the Russians", "L", "repetition",
     "S014: Russian incoming tourists", "high", "R: the",
     "tái lập chuỗi du khách Nga, mở đoạn; 'short-haul visitors' cùng câu "
     "trỏ thực thể khác (Trung Quốc/ASEAN) nên không đánh dấu",
     1, None, None, "LC", None),
    ("S015", "Thai", "L", "repetition",
     "S009: all of Thailand", "med", None,
     "gia đình hình thái 'Thai-/Thailand'; tính từ quốc tịch trong 'The Thai "
     "resort cities'",
     1, None, None, "LC", None),
    ("S015", "dependent", "L", "synonym",
     "S011: heavily reliant", "high", None,
     "'dependent' ~ 'reliant' (phụ thuộc); cùng khung 'X reliant/dependent "
     "on Y'",
     1, None, None, "LC", None),
    ("S015", "make up for", "L", "synonym",
     "S014: compensate", "high", None,
     "'make up for' ~ 'compensate' (bù đắp); câu kề",
     1, None, None, "LC", None),
    ("S015", "marketing initiatives", "L", "repetition",
     "S014: other markets", "low", None,
     "cùng gốc 'market-'; khác nghĩa (khuyến mãi ↔ thị trường) — liên kết "
     "hình thái, conf low",
     1, None, None, "LC", None),
    ("S016", "tourists", "L", "repetition",
     "S014: Russian incoming tourists", "med", None,
     "lặp 'tourists' với phạm vi mở rộng (mọi du khách, không chỉ Nga) — "
     "liên kết từ vựng, không quy chiếu",
     1, None, None, "LC", None),
    ("S016", "Thailand", "L", "repetition",
     "S009: all of Thailand", "high", None,
     "tái lập chuỗi 'Thailand' sau 7 câu",
     1, None, None, "LC", None),
    ("S017", "shifting", "L", "repetition",
     "S014: shift (to other markets)", "med", None,
     "lặp 'shift-'; chủ thể khác (ngành ↔ du khách) nhưng cùng trường chuyển "
     "hướng",
     1, None, None, "LC", None),
    ("S017", "said", "L", "repetition",
     "S014: said (Suladda)", "med", None,
     "attribution bị động ('are said to be', không nêu nguồn) — chuỗi động "
     "từ trích dẫn",
     1, None, None, "LC", None),
    ("S017", "vacation plans", "L", "synonym",
     "S002: overseas travel", "med", None,
     "'vacation' ~ 'travel' (du lịch); khoảng cách lớn nhưng chuỗi được duy "
     "trì qua các lần lặp 'tourists'",
     1, None, None, "LC", None),
    ("S018", "told", "L", "repetition",
     "S005: told (VOA News)", "med", None,
     "tái lập 'told' tại attribution Putin; chuỗi attribution xuyên văn bản "
     "(qua 'said' S008/S011/S014)",
     1, None, None, "LC", None),
    ("S018", "depreciating", "L", "synonym",
     "S002: crashing (the ruble)", "high", None,
     "'depreciating' ~ 'plunging/crashing' — chuỗi động từ mất giá; lời "
     "Putin",
     1, None, None, "LC", None),
    ("S018", "last", "L", "antonym",
     "S012: (going to) end", "med", None,
     "'last' (kéo dài) ↔ 'end' (kết thúc) — phản nghĩa về thời lượng",
     1, None, None, "LC", None),
    ("S018", "improve", "L", "antonym",
     "S011: (things to) stay bad", "med", None,
     "'improve' ↔ 'stay bad' — phản nghĩa về diễn biến tình hình",
     1, None, None, "LC", None),
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

    # ---------- L v2 bổ sung ----------
    # Theo CHÍNH SÁCH L v2 (CONVENTIONS §8.1): từ đơn nội dung, lặp cùng dạng
    # kể cả câu kề, biến thể hình thái/đồng nghĩa, tên riêng = 1 chuỗi, động
    # từ attribution = chuỗi riêng; 1 mark/câu/chuỗi; occ đếm tay. Quyết định
    # đọc hiểu theo văn bản VI (khác EN ở vài điểm: VI có 'Pattaya' định ngữ
    # vị trí S005, 'tua du lịch' S013; VI không có attribution S008/S014).
    # 39 hàng mới, đọc trực tiếp từ TT.txt / TT_sentmap.txt — L(TT) 19 → 58.
    ("S002", "sụt xuống", "L", "synonym", "S001: tuột giá", "high", None,
     "'sụt xuống' ~ 'tuột giá' — chuỗi động từ mất giá (S001→S002→'hạ giá' "
     "S018); đối ứng EN 'crashing' → 'plunging'",
     1, None, None, "LC", None),
    ("S002", "đi du lịch nước ngoài", "L", "repetition",
     "S001: du lịch (công nghiệp du lịch)", "high", None,
     "lặp từ 'du lịch' (ngành ↔ hoạt động) — liên kết từ vựng, không quy "
     "chiếu; EN đối ứng 'overseas travel' ~ 'tourism' (synonym vì EN khác "
     "từ)",
     1, None, None, "LC", None),
    ("S004", "mất đi", "L", "synonym", "S001: (đã bị) thiệt hại", "med",
     None,
     "'mất đi (du khách)' ~ 'thiệt hại' — trường nghĩa mất mát; 'sụt giảm' "
     "cùng câu thuộc chuỗi khác; EN 'the loss of' không đánh dấu riêng",
     1, None, None, "LC", None),
    ("S005", "Pattaya", "L", "repetition",
     "S003: (thành phố biển nghỉ mát) Pattaya", "high", None,
     "tái lập tên riêng trong chức danh 'văn phòng ở Pattaya' — định ngữ vị "
     "trí nhưng trỏ đúng thành phố (khác EN 'Pattaya office' không tính)",
     1, None, None, "LC", None),
    ("S005", "người Nga", "L", "repetition", "S004: du khách Nga", "high",
     None,
     "biến thể rút gọn ('du khách Nga' → 'người Nga'); sau attribution 'cho "
     "đài VOA biết'; đối ứng EN 'the Russians' S005",
     1, None, None, "LC", None),
    ("S006", "Pattaya", "L", "repetition", "S005: (văn phòng ở) Pattaya",
     "high", None,
     "lặp tên riêng ở câu kề, trong trích dẫn ('cho Pattaya'); đối ứng EN "
     "S006 (EN tính từ S003)",
     1, None, None, "LC", None),
    ("S007", "số một", "L", "synonym", "S005: không thua kém ai", "med",
     None,
     "diễn giải lại trong trích dẫn ('số một' ~ 'không thua kém ai': đứng "
     "đầu); đối ứng EN 'number one' S007",
     1, None, None, "LC", None),
    ("S008", "du khách Nga", "L", "repetition", "S007: Du khách Nga",
     "high", None,
     "lặp cùng dạng ở câu kề trong cùng trích dẫn (§8.1 i); đối ứng EN "
     "'Russian tourists' S008",
     1, None, None, "LC", None),
    ("S008", "Pattaya", "L", "repetition", "S006: Pattaya", "high", None,
     "tái lập tên riêng trong trích dẫn ('đến Pattaya'); EN không đánh dấu "
     "S008 nhưng VI theo §8.1(i) đánh dấu cả câu kề",
     1, None, None, "LC", None),
    ("S009", "du khách Nga", "L", "repetition", "S008: du khách Nga",
     "high", None,
     "lặp cùng dạng ở câu kề (§8.1 i); đối ứng EN 'Russian visitors' (EN "
     "khác từ nên superordinate)",
     1, None, None, "LC", None),
    ("S010", "tháng 12", "L", "repetition", "S004: (từ 28) tháng 12",
     "med", None,
     "lặp 'tháng 12' (mùa cao điểm 28/12–15/1 ↔ tháng 12); conf med vì S004 "
     "là ngày cụ thể; đối ứng EN 'December' S010",
     1, None, None, "LC", None),
    ("S010", "tai hại", "L", "repetition", "S001: thiệt hại", "low", None,
     "cùng gốc 'hại' ('thiệt hại' → 'tai hại'), khác từ loại (danh ↔ tính); "
     "khoảng cách 9 câu; đối ứng EN 'a disaster' → 'suffering' (collocation, "
     "low)",
     1, None, None, "LC", None),
    ("S010", "tổng số", "L", "repetition", "S009: tổng cộng", "med", None,
     "gia đình hình thái 'tổng-' ('tổng cộng' → 'tổng số'); đối ứng EN "
     "'total' S010",
     1, None, None, "LC", None),
    ("S010", "du khách Nga", "L", "repetition", "S009: du khách Nga",
     "high", None,
     "lặp cùng dạng ở câu kề (§8.1 i); đối ứng EN 'Russian tourists' S010",
     1, None, None, "LC", None),
    ("S010", "năm ngoái", "L", "repetition", "S008: Năm ngoái", "high",
     None,
     "lặp 'năm ngoái' (cùng chỉ năm 2013) trong 'so với năm ngoái'; đối ứng "
     "EN 'last year' S010",
     1, None, None, "LC", None),
    ("S011", "nói", "L", "synonym", "S005: cho (đài VOA) biết", "high",
     None,
     "chuỗi động từ attribution (§8.1 v); 'nói' ~ 'cho biết'; đối ứng EN "
     "'said' S011 (EN tính từ 'said' S008)",
     1, None, None, "LC", None),
    ("S011", "Pattaya", "L", "repetition", "S008: Pattaya", "high", None,
     "tái lập tên riêng trong danh sách 'Pattaya, Phuket và Samui'; đối ứng "
     "EN S011",
     1, None, None, "LC", None),
    ("S011", "Thái", "L", "repetition", "S009: (toàn bộ) Thái Lan", "med",
     None,
     "dạng rút gọn 'Thái' trong 'đồng baht của Thái' — gia đình hình thái "
     "'Thái-/Thái Lan'; đối ứng EN 'Thai' S015",
     1, None, None, "LC", None),
    ("S011", "dự kiến", "L", "repetition",
     "S010: dự kiến (mức sụt giảm là 50%)", "high", None,
     "lặp 'dự kiến' ở câu kề; dự báo hiệp hội → nhận định Suladda; đối ứng "
     "EN 'expecting' S011",
     1, None, None, "LC", None),
    ("S011", "xấu đi", "L", "general word", "S010: (coi như là) tai hại",
     "med", None,
     "'xấu đi' tổng quát hóa 'tai hại' (thảm họa → xấu); chuỗi tình huống "
     "xấu S001→S010→S011; đối ứng EN 'bad' S011",
     1, None, None, "LC", None),
    ("S013", "tua du lịch", "L", "repetition",
     "S002: đi du lịch (nước ngoài)", "med", None,
     "lặp 'du lịch' sau 11 câu ('Du lịch' trong tên hiệp hội S005 là thành "
     "phần tên riêng, không tính); chuỗi duy trì qua 'du khách'; EN 'tour' "
     "không đánh dấu",
     1, None, None, "LC", None),
    ("S013", "các khách sạn", "L", "repetition",
     "S010: (hiệp hội điều hành) khách sạn (quốc gia)", "high", None,
     "lặp 'khách sạn' trong trích dẫn (khách sạn trực tiếp ↔ hiệp hội — "
     "liên kết từ vựng, không quy chiếu); đối ứng EN 'hoteliers' S013",
     1, None, None, "LC", None),
    ("S013", "lo ngại", "L", "synonym", "S001: quan ngại (nghiêm trọng)",
     "high", None,
     "'lo ngại' ~ 'quan ngại' (cùng gốc 'ngại'); khoảng cách 12 câu, trong "
     "trích dẫn; đối ứng EN 'worried' S013",
     1, None, None, "LC", None),
    ("S014", "sụt giảm", "L", "repetition", "S010: (mức) sụt giảm (là 50%)",
     "high", None,
     "lặp 'sụt giảm' sau 4 câu trong trích dẫn; chuỗi S004→S010→S014→'thất "
     "thu' S015; đối ứng EN 'decreasing' S014",
     1, None, None, "LC", None),
    ("S014", "Pattaya", "L", "repetition", "S011: Pattaya", "high", None,
     "tái lập tên riêng cuối trích dẫn ('đến Pattaya'); đối ứng EN S014",
     1, None, None, "LC", None),
    ("S015", "Thái Lan", "L", "repetition", "S011: (đồng baht của) Thái",
     "high", None,
     "trở lại dạng đầy đủ 'Thái Lan' sau dạng rút gọn 'Thái' S011 ('các đảo "
     "của Thái Lan'); đối ứng EN 'Thai' S015",
     1, None, None, "LC", None),
    ("S015", "lệ thuộc", "L", "repetition", "S011: lệ thuộc (nặng vào)",
     "high", None,
     "lặp 'lệ thuộc' sau 4 câu, mở đoạn; EN đối ứng 'dependent' ~ 'reliant' "
     "(synonym vì EN khác từ)",
     1, None, None, "LC", None),
    ("S015", "người Nga", "L", "repetition", "S014: du khách Nga", "high",
     None,
     "biến thể rút gọn, câu kề, mở đoạn; 'khách thăm' cùng câu trỏ thực thể "
     "khác (TQ/ASEAN) nên không đánh dấu; đối ứng EN 'the Russians' S015",
     1, None, None, "LC", None),
    ("S015", "tiếp thị", "L", "repetition", "S014: (các) thị trường",
     "low", None,
     "cùng yếu tố Hán Việt 'thị' (chợ); khác nghĩa (tiếp thị = quảng bá ↔ "
     "thị trường) — liên kết hình thái, conf low; đối ứng EN 'marketing' ~ "
     "'market' S015",
     1, None, None, "LC", None),
    ("S015", "bù vào", "L", "repetition", "S014: bù đắp (lại)", "high",
     None,
     "gia đình hình thái 'bù' ('bù đắp' → 'bù vào'); câu kề; đối ứng EN "
     "'make up for' ~ 'compensate' S015",
     1, None, None, "LC", None),
    ("S016", "du khách", "L", "repetition", "S014: du khách Nga", "med",
     None,
     "lặp 'du khách' (qua 'người Nga' S015); phạm vi mở rộng — nguồn du "
     "khách nói chung; liên kết từ vựng, không quy chiếu; đối ứng EN "
     "'tourists' S016",
     1, None, None, "LC", None),
    ("S016", "Thái Lan", "L", "repetition", "S015: (các đảo của) Thái Lan",
     "high", None,
     "lặp 'Thái Lan' ở câu kề ('ở Thái Lan'); đối ứng EN 'Thailand' S016 "
     "(EN cách 7 câu)",
     1, None, None, "LC", None),
    ("S017", "nghe nói", "L", "repetition", "S011: (Bà Suladda) nói",
     "med", None,
     "attribution không nêu nguồn ('nghe nói'); chuỗi động từ attribution "
     "(cho biết S005 → nói S011 → nghe nói); đối ứng EN 'are said to be' "
     "S017",
     1, None, None, "LC", None),
    ("S017", "chuyển", "L", "repetition",
     "S014: chuyển (qua các thị trường khác)", "med", None,
     "lặp 'chuyển'; chủ thể khác (ngành ↔ du khách) nhưng cùng trường "
     "chuyển hướng; đối ứng EN 'shifting' S017",
     1, None, None, "LC", None),
    ("S017", "đi nghỉ", "L", "synonym", "S002: đi du lịch (nước ngoài)",
     "med", None,
     "'đi nghỉ' ~ 'đi du lịch' (nghỉ dưỡng); cùng gốc 'nghỉ' với chuỗi "
     "'nghỉ mát' S003–S015; đối ứng EN 'vacation plans' → 'overseas "
     "travel'",
     1, None, None, "LC", None),
    ("S018", "nói", "L", "repetition", "S017: nghe nói", "med", None,
     "chuỗi động từ attribution; 'nói với các phóng viên' — lượt lời Putin "
     "(qua 'cho biết' S005, 'nói' S011); đối ứng EN 'told' S018",
     1, None, None, "LC", None),
    ("S018", "hạ giá", "L", "synonym",
     "S002: sụt xuống (các mức thấp kỷ lục)", "high", None,
     "'hạ giá' ~ 'tuột giá'/'sụt xuống' — chuỗi động từ mất giá "
     "(S001→S002→S018); lời Putin; đối ứng EN 'depreciating' S018",
     1, None, None, "LC", None),
    ("S018", "cải thiện", "L", "antonym", "S011: (tiếp tục) xấu đi",
     "med", None,
     "'cải thiện' ↔ 'xấu đi' — phản nghĩa về diễn biến tình hình; đối ứng "
     "EN 'improve' ↔ 'stay bad'",
     1, None, None, "LC", None),
    ("S018", "kéo dài", "L", "antonym", "S012: chấm dứt", "med", None,
     "'kéo dài (tới khoảng hai năm)' ↔ 'chấm dứt' — phản nghĩa về thời "
     "lượng; đối ứng EN 'last' ↔ 'end'",
     1, None, None, "LC", None),
]
