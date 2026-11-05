# P12 tie table — WRITTEN BY HAND FROM THE MANUAL ANALYSIS.
# Source: work/analysis/P12_semantic.md (§2–§6). Do not add a row that is not
# in the analysis. No regex / word lists / counting loops were used.
#
# Row: (sent, text, cat, sub, ante, conf, alt, note, occ,
#       gap_after, recovered, level, ref)
#
# Cặp micro (3 đơn vị câu mỗi bên). Lưu ý §8a của analysis: ST S001+S002 (EN)
# và TT S002+S003 (VI) mỗi cặp là MỘT câu thật bị chia tại "Jr." — KHÔNG đánh
# dấu tie băng ranh giới giả ("his" trong câu thật; "chủ ngữ thiếu" không phải
# zero) nên không có hàng E/S/C ở hai phía.

ST = [
    # ---------- R (reference) — 1 hàng, §4.1 ----------
    ("S003", "the two politicians", "R", "demonstrative",
     "S001: Robert F. Kennedy Jr. + S002: Donald Trump", "high",
     "L: superordinate",
     "mạo từ + số từ 'two' truy hồi đúng 2 nhân vật đã nêu; 'politicians' là "
     "danh từ thượng vị mô tả; câu S003 thuộc khối VI cắt (§8b)",
     1, None, None, "LC", "A"),

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn có nội dung, thuật ngữ đa từ,
    # tên riêng, động từ attribution; đánh dấu cả lặp ở câu kề; 1 mark/câu/chuỗi.
    # Bổ sung 2 hàng (L 0 -> 2). Ranh giới câu thật duy nhất của EN là S002|S003
    # (S001+S002 là MỘT câu thật bị chẻ tại "Jr." — §8a), nên chỉ hạng mục ở
    # S003 mới có thể có tiền trạm liên câu thật. Các trường hợp bỏ: 'the two
    # politicians' (đã có hàng R — một dạng một hàng; đọc phụ superordinate với
    # President/presidential đã ghi trong alt); 'VOA', 'Carolyn Presutti',
    # 'Glendale', 'Arizona' lần đầu (prerequisite); 'first time' không thuộc
    # trường bầu cử; chuỗi President/presidential có cả hai thành viên trong
    # cùng câu thật S002 → không liên câu.
    ("S003", "reports", "L", "repetition",
     "S002: announced his endorsement", "med", None,
     "động từ attribution (v2 §8.1-v), chuỗi khung báo chí: 'announced' (lượt "
     "tuyên bố của Kennedy) → 'reports' (dòng nguồn VOA; §7: EN mở bằng lời "
     "tuyên bố rồi attribution); hai mục từ khác nhau — tái lập chuỗi khung "
     "chứ không lặp từ; câu thuộc khối VI cắt (§8b)",
     1, None, None, "LC", None),

    ("S003", "campaigned", "L", "collocation",
     "S002: the Republican presidential nominee", "med", None,
     "trường bầu cử (kho E §6.2): 'campaigned' liên tưởng cùng trường với "
     "'presidential nominee' (S002) — hai câu thật của EN chỉ chia sẻ trường "
     "nghĩa, không chia sẻ hình thức từ (§6.4); v2 cho phép collocation; câu "
     "thuộc khối VI cắt (§8b)",
     1, None, None, "LC", None),
]

TT = [
    # ---------- L (lexical cohesion) — 2 hàng, §6.3 ----------
    ("S003", "Trump", "L", "repetition", "S001: Donald Trump", "high", None,
     "biến thể rút gọn (họ) ← tên đầy đủ 'Donald Trump' (S001); chuỗi tên do "
     "câu dẫn tự sinh của VI lập nên",
     1, None, None, "LC", None),

    ("S003", "ứng cử viên tổng thống", "L", "repetition",
     "S001: một ứng viên khác", "med", None,
     "gia đình hình thái 'ứng viên/ứng cử viên'; hai thành viên khác thực thể "
     "(Kennedy vs Trump) — liên kết từ vựng thuần túy",
     1, None, None, "LC", None),

    # ---------- L v2 bổ sung ----------
    # Chính sách L v2 (CONVENTIONS §8.1): từ đơn có nội dung, thuật ngữ đa từ,
    # tên riêng, động từ attribution; đánh dấu cả lặp ở câu kề; 1 mark/câu/chuỗi.
    # Bổ sung 1 hàng (L 2 -> 3). Ranh giới câu thật duy nhất của VI là
    # S001|(S002+S003) (S002+S003 là MỘT câu thật bị chẻ tại "Jr." — §8a).
    # Các trường hợp bỏ: 'tổng thống' (S003, chuỗi C kho §6.2) — nằm gọn trong
    # span đã mã của hàng 'ứng cử viên tổng thống' (một dạng một hàng; hàng
    # riêng sẽ chồng marker → lỗi QC-b); 'tuyên bố' (S003) không có động từ
    # attribution trước đó trong VI; 'mới đây' từ chỉ thời gian, không tiền
    # trạm; 'Robert F. Kennedy Jr.' (S002), 'Đảng Cộng hòa' (S003) lần đầu nêu
    # tên (prerequisite).
    ("S003", "ủng hộ", "L", "repetition",
     "S001: ủng hộ (nhóm cử tri ủng hộ một ứng viên khác)", "high", None,
     "chuỗi 'ủng hộ' (kho D §6.2): lặp cùng dạng qua 2 câu thật kề nhau — v2 "
     "§8.1(i) bỏ ngoại lệ 'câu kề' của pilot; hai cặp chủ thể–bổ ngữ khác nhau "
     "(nhóm cử tri ↔ Kennedy) — lặp mục từ thuần túy, không quy chiếu; EN "
     "'endorsement' chỉ xuất hiện 1 lần (bất đối xứng)",
     1, None, None, "LC", None),
]
