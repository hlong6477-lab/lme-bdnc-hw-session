# P02 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P02_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)

ST = [
    # ---------- R (reference) — 22 hàng, §4.1 ----------
    # R-EN1
    ("S003", "She", "R", "personal", "S002: Tyrah Chan-Hampton", "high",
     None, "chủ ngữ đại từ sau tên đầy đủ; chuỗi Tyrah; đối ứng VI 'Cô'",
     1, None, None, "LC", "A"),
    # R-EN2
    ("S004", "They", "R", "personal",
     "S003: She … kinship care with her aunt", "high", None,
     "[+người, số nhiều ghép]: she + dì (chuỗi đôi); đối ứng VI 'Cả hai'",
     1, None, None, "LC", "A"),
    # R-EN3
    ("S006", "it", "R", "personal", "S002: the word 'homeless'", "high",
     None,
     "'to say it' — 'it' = từ 'homeless' (đề cập từ ngữ, khoảng cách 4 câu); "
     "'it' chủ ngữ hình thức và 'it' ⊂ 'with' không đánh dấu — occ 3; VI đối "
     "ứng tân ngữ zero (E-VI1)", 3, None, None, "LC", "A"),
    # R-EN4
    ("S008", "we", "R", "personal", "S007: she said (attribution)", "high",
     None,
     "đại từ ngôi 1 trong trích dẫn, attribution ở câu trước (CONVENTIONS "
     "§1); we = Tyrah + gia đình; 'my mum/me/my siblings/us' cùng chuỗi nói "
     "— 1 mark", 1, None, None, "LC", "A"),
    # R-EN5
    ("S013", "the list", "R", "demonstrative", "S012: the 20 hotspots",
     "med", None,
     "mạo từ + đầu danh từ mới 'list' — sự xác định là liên kết duy nhất; "
     "bridging (S012 không dùng từ 'list'); tiền lệ P01 'the project'",
     1, None, None, "LC", "A"),
    # R-EN6
    ("S017", "she said", "R", "personal", "S016: Corin Moffatt", "high",
     None,
     "đại từ attribution cuối trích dẫn (dùng văn bản 'she said' tránh bẫy "
     "substring); VI 'bà nói'", 1, None, None, "LC", "A"),
    # R-EN7
    ("S017", "that list", "R", "demonstrative", "S013: the list", "high",
     None, "demonstrative; VI 'danh sách này'", 1, None, None, "LC", "A"),
    # R-EN8
    ("S017", "that combination of challenges", "R", "demonstrative",
     "S016: the number of young people experiencing homelessness, rates of "
     "youth unemployment, and rates of finishing high school", "high", None,
     "demonstrative + danh từ tổng quát truy hồi bộ ba yếu tố; khoảng cách 1",
     1, None, None, "LC", "A"),
    # R-EN9
    ("S018", "We", "R", "personal", "S017: she said (attribution)", "med",
     None,
     "lời trích tiếp tục (không attribution trong câu); We = Moffatt/Foyer — "
     "quy chiếu mở rộng; VI dịch 'chúng ta' (bao trùm) — dịch chuyển hệ ngôi",
     1, None, None, "LC", "A"),
    # R-EN10
    ("S018", "the problem", "R", "demonstrative",
     "S016: young people experiencing homelessness", "med",
     "L: general word ← chuỗi homelessness",
     "mạo từ + danh từ tổng quát 'problem' (quá tản mát để làm L) — sự xác "
     "định là liên kết duy nhất", 1, None, None, "LC", "A"),
    # R-EN11
    ("S021", "she said", "R", "personal", "S020: Moffat said", "high", None,
     "attribution; tiền trạm gần nhất là tên (biến thể chính tả Moffat, §8c)",
     1, None, None, "LC", "A"),
    # R-EN12
    ("S022", "you", "R", "personal",
     "(ngoại văn bản: ngôi 2 generic trong lời Moffatt)", "high", None,
     "ref=E; attribution 'she said' ở câu trước (S021) → đủ điều kiện; ×4 "
     "trong câu, 1 mark (occ 2 = 'if you don't have that'; occ 1/6 ⊂ "
     "'young'); VI đối ứng 'họ' (ref=A) — đổi ngôi + đổi hướng (§7)",
     2, None, None, "LC", "E"),
    # R-EN13
    ("S026", "she said", "R", "personal", "S025: Moffat said", "high", None,
     "attribution", 1, None, None, "LC", "A"),
    # R-EN14
    ("S027", "we", "R", "personal", "S026: she said (attribution)", "med",
     None,
     "'And so what we see too often' — lời trích tiếp tục; we = Foyer/các "
     "nhà quan sát — quy chiếu mở rộng", 1, None, None, "LC", "A"),
    # R-EN15
    ("S029", "He believes", "R", "personal", "S028: David MacKenzie",
     "high", None,
     "chủ ngữ đại từ sau tên đầy đủ; VI 'Ông nhấn mạnh' (S033 — lệch ranh "
     "giới do gộp–tái phân bổ)", 1, None, None, "LC", "A"),
    # R-EN16
    ("S031", "we", "R", "personal", "S030: he said (attribution)", "med",
     None,
     "'If we don't act to prevent it' — we = người nói + xã hội, đọc bao "
     "trùm; VI 'chúng ta' 1–1", 1, None, None, "LC", "A"),
    # R-EN17
    ("S031", "it", "R", "personal", "S028: youth homelessness", "med", None,
     "'to prevent it' — hồi quy về vấn đề (khoảng cách 3); phương án 2: trội "
     "quy chiếu với 'the flow … into homelessness' cùng câu ([TC], không "
     "đánh dấu) — ghi cả hai", 1, None, None, "LC", "A"),
    # R-EN18
    ("S033", "he said", "R", "personal", "S032: MacKenzie said", "high",
     None, "attribution", 1, None, None, "LC", "A"),
    # R-EN19
    ("S036", "She said", "R", "personal", "S035: Chan-Hampton", "high",
     None, "mở khối Tyrah sau subhead S034; VI 'Cô cho biết'",
     1, None, None, "LC", "A"),
    # R-EN20
    ("S043", "this", "R", "demonstrative",
     "S042: an ambitious housing and homelessness reform agenda", "high",
     None,
     "'As part of this' — demonstrative; nằm trong khối VI thay (§8e) → "
     "EN-only", 1, None, None, "LC", "A"),
    # R-EN21
    ("S044", "This", "R", "demonstrative", "S043: significant investments",
     "high", None,
     "'This includes young people…' — demonstrative truy hồi khoản đầu tư; "
     "khối VI thay (§8e) → EN-only", 1, None, None, "LC", "A"),
    # R-EN22
    ("S046", "They said", "R", "personal", "S045: The spokesperson said",
     "high", None,
     "[+người] = phát ngôn viên; VI đối ứng là gạch đầu dòng bỏ attribution "
     "→ EN-only", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 1 hàng [TC], §2 ----------
    # E-EN1
    ("S004", None, "E", "verbal",
     "S004: lived in a refuge (trong câu)", "high", None,
     "[TC] gapping động từ ở vế phối hợp thứ ba ('and then ∅ with extended "
     "family'); hồi phục {lived} ← cùng câu; VI đối ứng lấp đầy bằng động từ "
     "'ở nhờ' — chỉ EN có E", 1, "and then ", "{lived}", "TC", None),

    # ---------- C (conjunction) — 5 hàng [LC], §5.1 ----------
    # C-EN1
    ("S011", "And", "C", "additive",
     "S010: More than 122,000 people experience homelessness…", "high",
     None,
     "'And according to…' — nối thêm nguồn số liệu thứ hai (AIHW) sau ABS; "
     "đọc continuative cũng được, chọn additive; VI đối ứng 'cũng' (S012) "
     "đổi loại từ + vị trí (§8g)", 1, None, None, "LC", None),
    # C-EN2
    ("S026", "also", "C", "additive",
     "S025: many young people access crisis centres or emergency support "
     "services", "high", None,
     "'young people also need…' — cộng thêm nhu cầu vào chuỗi nội dung S025; "
     "VI 'cũng' (S030) giữ 1–1", 1, None, None, "LC", None),
    # C-EN3
    ("S027", "And so", "C", "causal",
     "S026: there are not enough services there", "high", None,
     "'And so what we see too often…' — hệ quả từ 'không đủ dịch vụ'; VI "
     "'Vì vậy' (S031) 1–1", 1, None, None, "LC", None),
    # C-EN4
    ("S029", "also", "C", "additive",
     "S023–S027: các biện pháp tài trợ foyer / nhà ở trung hạn", "med",
     None,
     "'there should also be more focus on prevention' — cộng phòng ngừa vào "
     "các giải pháp đã nêu; tiền trạm gần nhất S027; VI lược 'cũng' khi gộp "
     "vế vào S032 → EN-only", 1, None, None, "LC", None),
    # C-EN5
    ("S046", "also", "C", "additive", "S045: was providing $9.3 billion…",
     "high", None,
     "khoản đầu tư thứ hai ($91.7 million); VI là gạch đầu dòng bỏ 'also' "
     "→ EN-only", 1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 39 hàng [LC], §6.3 ----------
    ("S004", "extended family", "L", "collocation",
     "S003: kinship care with her aunt", "med", None,
     "liên tưởng trường nghĩa họ hàng (kinship↔family), kề", 1, None, None,
     "LC", None),
    ("S005", "housing insecurity", "L", "repetition",
     "S002: housing insecurity throughout her youth", "high", None,
     "tái lập tổ hợp sau 3 câu", 1, None, None, "LC", None),
    ("S006", "shame", "L", "synonym", "S005: felt embarrassed", "high",
     None, "biến thể mới vào chuỗi cảm xúc (embarrassed→shame), kề",
     1, None, None, "LC", None),
    ("S007", "cousins", "L", "repetition", "S004: her sister and cousin",
     "high", None,
     "tái lập sau 3 câu (trong trích dẫn); 'family members' ← 'extended "
     "family' (S004) cùng câu — nêu note/inventory, 1 mark/câu/chuỗi",
     1, None, None, "LC", None),
    ("S008", "stigma", "L", "repetition",
     "S005: the stigma attached to homelessness", "high", None,
     "tái lập sau 3 câu (trích dẫn mới)", 1, None, None, "LC", None),
    ("S008", "shame", "L", "repetition", "S006: struggled a lot with shame",
     "high", None, "tái lập sau 2 câu (trích dẫn mới)", 1, None, None,
     "LC", None),
    ("S012", "the 20 hotspots", "L", "repetition",
     "S001: the top 20 'hotspots'", "high", None,
     "tái lập sau 11 câu", 1, None, None, "LC", None),
    ("S012", "without a home", "L", "synonym",
     "S010: experience homelessness", "high", None,
     "biến thể mới vào chuỗi homelessness (diễn đạt thay thế), sau 2 câu",
     1, None, None, "LC", None),
    ("S012", "struggling to find a place to live", "L", "repetition",
     "S001: struggling to find a place to live", "high", None,
     "tái lập nguyên dạng cụm sau 11 câu", 1, None, None, "LC", None),
    ("S015", "the top 20", "L", "repetition", "S012: the 20 hotspots",
     "med", "R: the",
     "tái lập tổ hợp sau 3 câu (chuỗi bắt đầu S001 'top 20')", 1, None,
     None, "LC", None),
    ("S016", "the Foyer Foundation", "L", "repetition",
     "S012: the Foyer Foundation", "high", "R: the",
     "tái lập tên tổ chức sau 4 câu, tại attribution", 1, None, None,
     "LC", None),
    ("S016", "the analysis", "L", "repetition",
     "S012: New analysis by the Foyer Foundation", "high", "R: the",
     "tái lập sau 4 câu; VI đối ứng 'phân tích này' là R — bất đối xứng có "
     "chủ đích (§7)", 1, None, None, "LC", None),
    ("S020", "Moffat", "L", "repetition", "S016: Corin Moffatt", "high",
     None,
     "lặp tên người nói trong attribution sau 4 câu; biến thể chính tả "
     "Moffatt→Moffat (§8c)", 1, None, None, "LC", None),
    ("S020", "domestic violence", "L", "repetition",
     "S008: my mum struggled with domestic violence", "high", None,
     "tái lập sau 12 câu", 1, None, None, "LC", None),
    ("S021", "afford housing", "L", "repetition",
     "S020: lack of affordable housing", "high", None,
     "gia đình hình thái (affordable→afford), kề", 1, None, None, "LC",
     None),
    ("S022", "safe and secure accommodation", "L", "synonym",
     "S021: struggling to afford housing", "high", None,
     "biến thể mới (housing→accommodation), kề", 1, None, None, "LC", None),
    ("S023", "Foyer", "L", "repetition", "S016: the Foyer Foundation",
     "high", None,
     "rút gọn tên (dạng ngắn), sau 7 câu; VI giữ nguyên 'Foyer Foundation'",
     1, None, None, "LC", None),
    ("S024", "stable accommodation", "L", "repetition",
     "S022: safe and secure accommodation", "high", None,
     "tái lập accommodation sau 2 câu, đổi định ngữ (safe and "
     "secure→stable)", 1, None, None, "LC", None),
    ("S024", "transitional housing", "L", "synonym",
     "S023: medium-term housing", "med", None,
     "biến thể mới ← medium-term housing, kề", 1, None, None, "LC", None),
    ("S024", "people aged 16 to 25", "L", "repetition",
     "S012: people aged 16 to 24", "med", None,
     "tái lập tổ hợp 'people aged 16 to N' đổi số (16-24→16-25), sau 12 câu",
     1, None, None, "LC", None),
    ("S025", "Moffat", "L", "repetition", "S020: Moffat said", "high", None,
     "lặp tên người nói trong attribution sau 5 câu", 1, None, None, "LC",
     None),
    ("S026", "crisis services", "L", "repetition", "S025: crisis centres",
     "med", None, "đổi hạt nhân (centres→services), sau 2 câu", 1, None,
     None, "LC", None),
    ("S026", "medium and longer-term housing options", "L", "repetition",
     "S023: medium-term housing", "high", None,
     "tái lập + biến thể (medium-term→medium and longer-term), sau 3 câu",
     1, None, None, "LC", None),
    ("S027", "pathway", "L", "repetition",
     "S023: provide a pathway out of homelessness", "high", None,
     "tái lập 'pathway…out of' sau 4 câu", 1, None, None, "LC", None),
    ("S028", "youth homelessness", "L", "repetition",
     "S020: youth homelessness in Australia", "high", None,
     "tái lập tổ hợp chủ đề sau 8 câu, mở khối MacKenzie", 1, None, None,
     "LC", None),
    ("S031", "the problem", "L", "repetition",
     "S018: the problem is very widespread", "high", "R: the",
     "tái lập sau 13 câu; VI đối ứng 'vấn đề này' là R — bất đối xứng có "
     "chủ đích (§7)", 1, None, None, "LC", None),
    ("S032", "MacKenzie", "L", "repetition", "S028: David MacKenzie",
     "high", None,
     "lặp tên người nói trong attribution sau 4 câu (rút gọn họ)",
     1, None, None, "LC", None),
    ("S035", "Chan-Hampton", "L", "repetition", "S002: Tyrah Chan-Hampton",
     "high", None,
     "tái lập tên nhân vật sau 33 câu (dạng rút gọn), sau subhead S034; VI "
     "dùng tên đầy đủ", 1, None, None, "LC", None),
    ("S036", "a youth foyer", "L", "repetition",
     "S024: Youth foyers offer transitional housing", "high", None,
     "tái lập sau 12 câu (số ít)", 1, None, None, "LC", None),
    ("S037", "unsafe", "L", "antonym",
     "S022: safe and secure accommodation", "med", None,
     "trái nghĩa ← safe, sau 15 câu; 'unstable' ← 'stable' (S024) cùng hàng",
     1, None, None, "LC", None),
    ("S037", "secure housing", "L", "repetition",
     "S022: safe and secure accommodation", "high", None,
     "tái lập 'secure' + housing sau 15 câu", 1, None, None, "LC", None),
    ("S039", "crisis accommodation", "L", "repetition",
     "S026: crisis services", "high", None,
     "tái lập 'crisis + N' sau 13 câu, đổi hạt nhân (services→"
     "accommodation); chuỗi bắt đầu S025 'crisis centres'", 1, None, None,
     "LC", None),
    ("S045", "The spokesperson", "L", "repetition",
     "S042: the spokesperson said", "high", None,
     "tái lập sau 3 câu", 1, None, None, "LC", None),
    ("S045", "homelessness services sectors", "L", "repetition",
     "S011: homelessness services report", "high", None,
     "tái lập tổ hợp 'homelessness services' sau 34 câu", 1, None, None,
     "LC", None),
    ("S045", "National Agreement on Social Housing and Homelessness", "L",
     "repetition", "S042: housing and homelessness reform agenda", "med",
     None,
     "tái lập tổ hợp 'housing and homelessness' sau 3 câu", 1, None, None,
     "LC", None),
    ("S046", "investing", "L", "repetition", "S043: significant investments",
     "high", None,
     "gia đình hình thái (investments→investing), sau 3 câu; tiền trạm ở "
     "khối VI thay (§8e)", 1, None, None, "LC", None),
    ("S046", "prevention", "L", "repetition",
     "S030: prevention, that's better…", "high", None,
     "tái lập sau 16 câu trong tổ hợp mới; ×2 trong câu (prevention "
     "services / prevention program, occ 1) — 1 mark", 1, None, None,
     "LC", None),
    ("S047", "transitional accommodation", "L", "repetition",
     "S024: transitional housing", "high", None,
     "tái lập sau 23 câu, đổi hạt nhân (housing→accommodation)", 1, None,
     None, "LC", None),
    ("S047", "domestic violence", "L", "repetition",
     "S020: high rates of domestic violence", "high", None,
     "tái lập sau 27 câu", 1, None, None, "LC", None),
]

TT = [
    # ---------- R (reference) — 22 hàng, §4.2 ----------
    # R-VI1
    ("S003", "Cô", "R", "personal", "S002: Tyrah Chan-Hampton", "high",
     None, "đối ứng R-EN1 ('She')", 1, None, None, "LC", "A"),
    # R-VI2
    ("S004", "Cả hai", "R", "personal", "S003: cô … sống cùng dì", "high",
     None,
     "lượng từ + số từ pronominal ('cả hai' = both) truy hồi cặp cô + dì; "
     "đối ứng R-EN2 ('They')", 1, None, None, "LC", "A"),
    # R-VI3
    ("S006", "cô bộc bạch", "R", "personal", "S005: Tyrah chia sẻ", "high",
     None,
     "attribution; tiền trạm gần nhất là tên 'Tyrah' (S005 VI dùng tên, EN "
     "dùng 'She') → phát sinh hàng VI mà EN không có (§7)",
     1, None, None, "LC", "A"),
    # R-VI4
    ("S008", "cô chia sẻ", "R", "personal", "S007: Chan-Hampton", "high",
     None,
     "attribution; tiền trạm nằm ở câu VI tự sinh (Wiradjuri) — tie VI đứng "
     "độc lập (CONVENTIONS §1)", 1, None, None, "LC", "A"),
    # R-VI5
    ("S009", "chúng tôi", "R", "personal", "S008: cô chia sẻ (attribution)",
     "high", None,
     "đại từ ngôi 1 trong trích dẫn, attribution ở câu trước; chúng tôi = "
     "Tyrah + mẹ + anh chị em; 'mẹ tôi/tôi/các anh chị em' cùng chuỗi nói — "
     "1 mark (occ 1; ×2 trong câu); đối ứng R-EN4",
     1, None, None, "LC", "A"),
    # R-VI6
    ("S014", "danh sách", "R", "demonstrative", "S013: 20 “điểm nóng”",
     "med", None,
     "danh từ tổng quát 'danh sách' xuất hiện lần đầu, không có chỉ từ — "
     "tính xác định (đứng đầu danh sách) là liên kết duy nhất; bridging như "
     "R-EN5; câu có lặp đôi 'đứng đầu danh sách' (§8a — occ 1 theo substring "
     "thật)", 1, None, None, "LC", "A"),
    # R-VI7
    ("S017", "phân tích này", "R", "demonstrative",
     "S013: Phân tích mới của Foyer Foundation", "med",
     "L: tái lập 'phân tích' sau 4 câu",
     "chỉ từ 'này' + hạt nhân lặp 'phân tích'; tiền lệ P05 ('Khoản thuế "
     "này'); EN đối ứng 'the analysis' là L — bất đối xứng có chủ đích (§7)",
     1, None, None, "LC", "A"),
    # R-VI8
    ("S018", "bà nói", "R", "personal", "S017: Corin Moffatt", "high", None,
     "attribution honorific 'bà'; đối ứng R-EN6", 1, None, None, "LC", "A"),
    # R-VI9
    ("S018", "danh sách này", "R", "demonstrative",
     "S016: Danh sách 20 điểm nóng về vô gia cư thanh niên", "high", None,
     "chỉ từ + danh từ; đối ứng R-EN7 ('that list')", 1, None, None,
     "LC", "A"),
    # R-VI10
    ("S018", "những thách thức này", "R", "demonstrative",
     "S017: số lượng thanh niên vô gia cư, tỷ lệ thất nghiệp…, tỷ lệ hoàn "
     "thành trung học phổ thông", "high", None,
     "chỉ từ + danh từ tổng quát; đối ứng R-EN8", 1, None, None, "LC", "A"),
    # R-VI11
    ("S022", "bà nói", "R", "personal", "S021: Theo Corin Moffatt", "high",
     None, "attribution; đối ứng R-EN11", 1, None, None, "LC", "A"),
    # R-VI12
    ("S024", "điều đó", "R", "demonstrative",
     "S023: chỗ ở an toàn và ổn định", "high", None,
     "danh từ tổng quát 'điều' + chỉ từ 'đó'; do VI tách câu EN S022 thành "
     "đôi → tie [LC], EN 'that' nằm cùng câu ([TC], không đánh dấu) — §7",
     1, None, None, "LC", "A"),
    # R-VI13
    ("S024", "họ", "R", "personal", "S023: nhiều thanh niên", "high", None,
     "[+người, số nhiều]; đối ứng vị trí EN 'you' generic (ref=E) — đổi ngôi "
     "+ đổi hướng (§7); occ 1 ('họ' ⊂ 'học' ×2 — đếm substring thật)",
     1, None, None, "LC", "A"),
    # R-VI14
    ("S028", "Những trung tâm này", "R", "demonstrative",
     "S027: Youth foyers là các trung tâm…", "high", None,
     "chỉ từ 'này' + danh từ tổng quát; EN đối ứng 'them' nằm cùng câu S024 "
     "([TC]) — VI tách câu làm tie thành [LC] (§7)",
     1, None, None, "LC", "A"),
    # R-VI15
    ("S030", "bà nói", "R", "personal", "S029: Theo Corin Moffatt", "high",
     None, "attribution; đối ứng R-EN13", 1, None, None, "LC", "A"),
    # R-VI16
    ("S033", "Ông nhấn mạnh", "R", "personal", "S032: David MacKenzie",
     "high", None,
     "attribution honorific 'ông' + động từ tường thuật; đối ứng R-EN15 "
     "('He believes') — lệch ranh giới câu do gộp–tái phân bổ",
     1, None, None, "LC", "A"),
    # R-VI17
    ("S035", "chúng ta", "R", "personal", "S034: ông nói (attribution)",
     "med", None,
     "đại từ ngôi 1 trong trích dẫn, attribution ở câu trước; chúng ta bao "
     "trùm (người nói + xã hội); đối ứng R-EN16",
     1, None, None, "LC", "A"),
    # R-VI18
    ("S035", "vấn đề này", "R", "demonstrative",
     "S019: vấn đề vô gia cư ở thanh niên", "med",
     "L: tái lập 'vấn đề' sau 16 câu",
     "chỉ từ 'này' + hạt nhân lặp 'vấn đề'; EN đối ứng 'the problem' (S031) "
     "là L — bất đối xứng có chủ đích (§7)", 1, None, None, "LC", "A"),
    # R-VI19
    ("S037", "ông chia sẻ", "R", "personal", "S036: MacKenzie cảnh báo",
     "high", None, "attribution; đối ứng R-EN18 ('he said')",
     1, None, None, "LC", "A"),
    # R-VI20
    ("S040", "Cô cho biết", "R", "personal", "S039: Tyrah Chan-Hampton",
     "high", None, "attribution; đối ứng R-EN19", 1, None, None, "LC", "A"),
    # R-VI21
    ("S042", "cô nói", "R", "personal", "S041: Tyrah Chan-Hampton", "high",
     None,
     "attribution; EN đối ứng 'she said' (S038) bị bỏ vì chuỗi đại từ kề "
     "(S037 'she believes' ← S036 'She said') — VI neo lại bằng tên nên có "
     "hàng (§7)", 1, None, None, "LC", "A"),
    # R-VI22
    ("S048", "Những khoản đầu tư này", "R", "demonstrative",
     "S047: Các khoản đầu tư chính của chính phủ", "high", None,
     "câu VI tự sinh (thay khối S043–S044) — tie VI đứng độc lập, tiền trạm "
     "trong văn bản VI; đối ứng chức năng với R-EN21 nhưng không phải cặp "
     "dịch", 1, None, None, "LC", "A"),

    # ---------- E (ellipsis) — 1 hàng [LC], §2 ----------
    # E-VI1
    ("S006", None, "E", "nominal", "S002: thuộc diện \"vô gia cư\"", "med",
     None,
     "[LC] tân ngữ zero của 'nói' ('chỉ cần nói ∅ ra thôi'); EN đối ứng đại "
     "từ tường minh 'to say it' (R-EN3) — R↔E; phương án đọc ngược: 'nói "
     "ra' là động từ trọn vẹn (speak out) — ghi cả hai, chọn đánh dấu",
     1, "chỉ cần nói", "{từ \"vô gia cư\"}", "LC", None),

    # ---------- C (conjunction) — 3 hàng [LC], §5.2 ----------
    # C-VI1
    ("S012", "cũng", "C", "additive",
     "S011: hơn 122.000 người… rơi vào cảnh vô gia cư", "high", None,
     "'Báo cáo… cũng cho thấy' — đối ứng C-EN1 ('And'); VI hiện thực hóa nối "
     "bằng trạng từ giữa câu thay liên từ đầu câu", 1, None, None, "LC",
     None),
    # C-VI2
    ("S030", "cũng", "C", "additive",
     "S029: nhiều thanh niên tìm đến các trung tâm khủng hoảng…", "high",
     None, "'thanh niên cũng cần…' — đối ứng C-EN2, giữ 1–1",
     1, None, None, "LC", None),
    # C-VI3
    ("S031", "Vì vậy", "C", "causal",
     "S030: hiện nay không có đủ dịch vụ để đáp ứng nhu cầu đó", "high",
     None, "đối ứng C-EN3 ('And so'), giữ 1–1", 1, None, None, "LC", None),

    # ---------- L (lexical cohesion) — 41 hàng [LC], §6.3 ----------
    ("S004", "nhà người thân", "L", "synonym",
     "S003: chương trình chăm sóc họ hàng", "med", None,
     "biến thể (họ hàng↔người thân), kề; đối ứng EN 'extended family' "
     "(collocation)", 1, None, None, "LC", None),
    ("S005", "Tyrah", "L", "repetition", "S002: Tyrah Chan-Hampton", "high",
     None,
     "rút gọn tên (dạng gọi), sau 3 câu; EN đối ứng là đại từ 'She' (S005)",
     1, None, None, "LC", None),
    ("S005", "bất ổn về nhà ở", "L", "repetition",
     "S002: tình trạng bất ổn về nhà ở", "high", None,
     "tái lập tổ hợp sau 3 câu", 1, None, None, "LC", None),
    ("S007", "Chan-Hampton", "L", "repetition", "S002: Tyrah Chan-Hampton",
     "high", None,
     "tái lập tên (dạng họ) sau 5 câu, trong câu VI tự sinh; S005 dùng dạng "
     "'Tyrah'", 1, None, None, "LC", None),
    ("S008", "anh chị em họ", "L", "repetition", "S004: chị gái và em họ",
     "high", None,
     "tái lập 'họ' sau 4 câu (trong trích dẫn); 'người thân' ← 'nhà người "
     "thân' (S004) cùng câu — nêu note/inventory, 1 mark/câu/chuỗi",
     1, None, None, "LC", None),
    ("S009", "từ ‘vô gia cư’", "L", "repetition",
     "S002: thuộc diện \"vô gia cư\"", "high", None,
     "tái lập đề cập từ ngữ sau 7 câu (metalinguistic); giữ nguyên ngoặc "
     "đơn cong (§8i)", 1, None, None, "LC", None),
    ("S013", "20 “điểm nóng”", "L", "repetition",
     "S001: 20 \"điểm nóng\" trên khắp cả nước", "high", None,
     "tái lập sau 12 câu; S013 dùng ngoặc kép cong (§8i)", 1, None, None,
     "LC", None),
    ("S013", "không có nơi ở", "L", "synonym",
     "S011: rơi vào cảnh vô gia cư", "high", None,
     "biến thể mới vào chuỗi vô gia cư, sau 2 câu", 1, None, None, "LC",
     None),
    ("S013", "đang chật vật tìm kiếm chỗ ở ổn định", "L", "repetition",
     "S001: chật vật tìm kiếm một nơi ở", "high", None,
     "tái lập biến thể cụm sau 12 câu (một nơi ở→chỗ ở ổn định)",
     1, None, None, "LC", None),
    ("S016", "Danh sách 20 điểm nóng về vô gia cư thanh niên", "L",
     "repetition", "S013: 20 “điểm nóng”; S014: đứng đầu danh sách", "high",
     None,
     "tái lập tổ hợp sau 2 câu, đổi định ngữ (VI đổi chủ ngữ câu)",
     1, None, None, "LC", None),
    ("S017", "Foyer Foundation", "L", "repetition",
     "S013: Foyer Foundation", "high", None,
     "tái lập tên tổ chức sau 4 câu, tại attribution", 1, None, None,
     "LC", None),
    ("S021", "Corin Moffatt", "L", "repetition", "S017: Corin Moffatt",
     "high", None, "tái lập tên đầy đủ sau 4 câu ('Theo + tên')",
     1, None, None, "LC", None),
    ("S021", "bạo lực gia đình", "L", "repetition", "S009: vì bạo lực gia đình",
     "high", None, "tái lập sau 12 câu", 1, None, None, "LC", None),
    ("S023", "chỗ ở an toàn và ổn định", "L", "synonym",
     "S022: trang trải chi phí nhà ở", "high", None,
     "biến thể mới (nhà ở→chỗ ở), kề", 1, None, None, "LC", None),
    ("S025", "Foyer Foundation", "L", "repetition",
     "S017: Foyer Foundation", "high", None,
     "tái lập tên tổ chức sau 8 câu", 1, None, None, "LC", None),
    ("S025", "nơi ở ổn định", "L", "synonym",
     "S023: chỗ ở an toàn và ổn định", "high", None,
     "biến thể (chỗ ở→nơi ở), sau 2 câu", 1, None, None, "LC", None),
    ("S027", "thanh niên từ 16 đến 25 tuổi", "L", "repetition",
     "S013: thanh niên trong độ tuổi 16-24", "med", None,
     "tái lập tổ hợp 'thanh niên… tuổi' đổi số (16-24→16 đến 25), sau 14 câu",
     1, None, None, "LC", None),
    ("S028", "chỗ ở ổn định", "L", "repetition", "S025: nơi ở ổn định",
     "high", None,
     "tái lập sau 3 câu (dao động về 'chỗ ở')", 1, None, None, "LC", None),
    ("S029", "Corin Moffatt", "L", "repetition", "S021: Theo Corin Moffatt",
     "high", None, "tái lập tên đầy đủ sau 8 câu ('Theo + tên')",
     1, None, None, "LC", None),
    ("S030", "nhà ở trung hạn và dài hạn", "L", "repetition",
     "S025: nhà ở trung hạn", "high", None,
     "tái lập 'nhà ở trung hạn' sau 5 câu + mở rộng (thêm 'dài hạn')",
     1, None, None, "LC", None),
    ("S031", "hệ thống hỗ trợ khẩn cấp", "L", "repetition",
     "S030: dịch vụ khẩn cấp", "med", None,
     "đổi hạt nhân (dịch vụ→hệ thống), kề; EN đối ứng 'the system' nằm cùng "
     "câu S027 ([TC], không đánh dấu)", 1, None, None, "LC", None),
    ("S031", "lối thoát", "L", "repetition",
     "S025: tạo cơ hội thoát khỏi cảnh vô gia cư", "med", None,
     "biến thể ← 'thoát khỏi' (pathway), sau 6 câu", 1, None, None, "LC",
     None),
    ("S032", "vấn đề vô gia cư ở thanh niên", "L", "repetition",
     "S020: (subhead) cuộc khủng hoảng vô gia cư ở thanh niên", "med", None,
     "biến thể ← subhead (cuộc khủng hoảng→vấn đề), sau 12 câu",
     1, None, None, "LC", None),
    ("S034", "công tác phòng ngừa", "L", "repetition",
     "S032: công tác phòng ngừa", "high", None,
     "tái lập sau 2 câu (trong trích dẫn)", 1, None, None, "LC", None),
    ("S036", "MacKenzie", "L", "repetition", "S032: David MacKenzie",
     "high", None, "lặp tên người nói sau 4 câu (rút gọn họ)",
     1, None, None, "LC", None),
    ("S037", "bế tắc", "L", "repetition", "S024: rơi vào tình cảnh bế tắc",
     "high", None,
     "tái lập sau 13 câu; EN hai đầu dùng diễn đạt khác (very hard / things "
     "go wrong) — VI hội tụ (§6.4)", 1, None, None, "LC", None),
    ("S039", "Tyrah Chan-Hampton", "L", "repetition", "S007: Chan-Hampton",
     "high", None,
     "tái lập tên đầy đủ sau 32 câu, sau subhead S038", 1, None, None,
     "LC", None),
    ("S040", "youth foyer", "L", "repetition",
     "S027: Youth foyers là các trung tâm…", "high", None,
     "tái lập sau 13 câu (số ít, giữ nguyên tiếng Anh)", 1, None, None,
     "LC", None),
    ("S041", "Tyrah Chan-Hampton", "L", "repetition",
     "S039: Tyrah Chan-Hampton", "high", None,
     "tái lập tên sau 2 câu ('Theo + tên'; EN đối ứng là đại từ 'she')",
     1, None, None, "LC", None),
    ("S041", "bất ổn hoặc nguy hiểm", "L", "antonym",
     "S023: chỗ ở an toàn và ổn định", "med", None,
     "trái nghĩa ← 'an toàn và ổn định', sau 18 câu ('bất ổn'↔'ổn định', "
     "'nguy hiểm'↔'an toàn') — một hàng cho cả hai cặp (analysis §6.3: "
     "'bất ổn… nguy hiểm')", 1, None, None, "LC", None),
    ("S041", "chỗ ở an toàn", "L", "repetition",
     "S023: chỗ ở an toàn và ổn định", "high", None,
     "tái lập 'chỗ ở an toàn' sau 18 câu", 1, None, None, "LC", None),
    ("S042", "không an toàn", "L", "synonym",
     "S041: môi trường bất ổn hoặc nguy hiểm", "med", None,
     "đồng nghĩa ← 'nguy hiểm', kề", 1, None, None, "LC", None),
    ("S043", "các trung tâm tạm trú", "L", "repetition",
     "S004: sống trong nhà tạm trú", "high", None,
     "tái lập 'tạm trú' sau 39 câu, đổi hạt nhân (nhà→trung tâm); hội tụ với "
     "'refuge' (S004) — EN dùng 'crisis accommodation'", 1, None, None,
     "LC", None),
    ("S046", "người phát ngôn", "L", "repetition",
     "S045: một phát ngôn viên của Bộ Dịch vụ Xã hội", "high", None,
     "biến thể từ trở (phát ngôn viên→người phát ngôn), kề",
     1, None, None, "LC", None),
    ("S048", "vòng xoáy vô gia cư", "L", "synonym",
     "S046: giải quyết tình trạng vô gia cư", "med", None,
     "biến thể mới vào chuỗi vô gia cư (ẩn dụ 'vòng xoáy'), sau 2 câu; câu "
     "VI tự sinh", 1, None, None, "LC", None),
    ("S049", "Thỏa thuận Quốc gia về Nhà ở Xã hội và Vô gia cư", "L",
     "repetition", "S046: nhà ở và giải quyết tình trạng vô gia cư", "med",
     None, "tái lập tổ hợp 'Nhà ở… Vô gia cư' sau 3 câu", 1, None, None,
     "LC", None),
    ("S049", "dịch vụ hỗ trợ vô gia cư", "L", "repetition",
     "S012: các dịch vụ hỗ trợ vô gia cư", "high", None,
     "tái lập tổ hợp sau 37 câu", 1, None, None, "LC", None),
    ("S050", "đầu tư", "L", "repetition",
     "S047: Các khoản đầu tư chính của chính phủ", "high", None,
     "gia đình hình thái (khoản đầu tư→đầu tư), sau 3 câu", 1, None, None,
     "LC", None),
    ("S050", "phòng ngừa", "L", "repetition", "S034: công tác phòng ngừa",
     "high", None, "tái lập sau 16 câu trong tổ hợp mới", 1, None, None,
     "LC", None),
    ("S051", "nhà ở chuyển tiếp", "L", "repetition",
     "S027: cung cấp nhà ở chuyển tiếp", "high", None,
     "tái lập sau 24 câu (tiền trạm gieo bởi subhead tự sinh S026)",
     1, None, None, "LC", None),
    ("S051", "bạo lực gia đình", "L", "repetition",
     "S021: bạo lực gia đình ở mức đáng báo động", "high", None,
     "tái lập sau 30 câu", 1, None, None, "LC", None),
]
