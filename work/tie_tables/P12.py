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
]
