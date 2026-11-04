# SESSION.md — nhật ký phiên làm việc

- **Nhiệm vụ:** phân tích lại từ đầu (from scratch) 20 cặp bài báo EN–VI theo
  skill cohesion-en-vi (Halliday & Hasan 1976 · Trần Ngọc Thêm 1985/2006 ·
  Nguyễn Thanh Tùng 2020). KHÔNG copy kết quả benchmark.
- **Input:** `(Long's) Appendix 1 - 20 pairs.md`
  (md5 `8eb83d2e8b6a89f2f7ee0347c5a0ca66`, trùng bản benchmark trong repo
  skill — xác nhận bằng diff/md5; bản gốc giữ nguyên tại `input/`).

## Nhật ký

### Bước 0 — Khảo sát & bootstrap (hoàn tất)
- Clone repo skill về máy (ngoài repo này) để đọc phương pháp; smoke-test
  pipeline trên `examples/mini/` PASS (ingest → segment → annotate → render →
  build → validate 1/1 OK).
- Khởi tạo repo session: copy **chỉ file phương pháp** (SKILL.md, AGENTS.md,
  pipeline/, references/, templates/, prompts/, examples/mini/, requirements.txt).
  Không đưa `out/`, `download/BDNC/`, `scripts/tie_tables|align_tables/`,
  `REPLICATION_GUIDE.md` vào repo → bảo đảm không thể copy kết quả benchmark.
- **Phát hiện lỗi bóc tách của ingest mặc định** với file gốc: tiêu đề nằm ở
  nhiều dạng (hàng link trong bảng bị nuốt thành URL row; dòng standalone
  `SL:/TL:`; heading `# [title](url)`; hàng plain không định dạng) khiến nhiều
  cặp (P01–P06, P08, P10, P12–P15, P20) **mất lede** (đoạn đầu bị pop thành
  "title") và mất tiêu đề thật.
- Viết `scripts/normalize_input.py`: chuẩn hóa **bố cục** (heading Pair NN +
  1 hàng URL + 1 hàng tiêu đề bold + body nguyên văn byte-for-byte), giải
  quyết 5 kiểu tiêu đề bằng luật ưu tiên có audit trail
  (`input/normalize_report.json`): in-table linked → in-table ~ standalone EN
  (similarity chặt: identical/containment/ratio≥0.75; VI-trùng một mình
  KHÔNG đủ — bẫy P08/P10 subhead VI trùng headline) → in-table bold →
  standalone (lược đuôi site `| SBS…`/`| Reuters`/`| AP News`) → last-resort
  (P20: plain ngắn, không còn nguồn nào khác).
- Kết quả sau chuẩn hóa: 20/20 cặp đúng tiêu đề, lede đầy đủ trong body.
  Cảnh báo nguồn còn lại: **P20 không có URL trong file gốc** (ghi nhận là
  bất thường dữ liệu nguồn, không bịa URL).
- Chạy ingest + segment trên bản chuẩn hóa: 20 cặp,
  EN ~756 câu / VI ~637 câu (chi tiết trong `work/pairs/`).

### Kế hoạch (cập nhật liên tục)
- [x] Bước 0: bootstrap + chuẩn hóa input + ingest/segment + push
- [ ] Bước 1: pilot P01 (1 agent) — hiệu chỉnh quy ước nếu cần
- [ ] Bước 2: batch A P02–P06
- [ ] Bước 3: batch B P07–P11
- [ ] Bước 4: batch C P12–P16
- [ ] Bước 5: batch D P17–P20
- [ ] Bước 6: build Appendix 1 + export DOCX/PDF + validate
- [ ] Bước 7: Appendix 2 — thống kê + báo cáo phân tích tổng hợp
- [ ] Bước 8: kiểm tra trực quan + giao deliverable

### Ghi chú nguồn từng cặp (từ bước chuẩn hóa, chuyển cho agent tương ứng)
- P01: có các hàng subhead bold hai bên ('We're at a tipping point', Public
  support 'really important factor', 'By no means new to the world') lệch vị
  trí giữa EN–VI; một số hàng VI=none; một hàng EN có VI=none hẳn.
- P02: VI có câu tự sinh (dòng Wiradjuri, ô EN=none); nhiều ô none một bên.
- P03: tiêu đề lấy từ dòng standalone; bảng không có hàng tiêu đề.
- P04: nhiều hàng VI=none (khối cắt VI).
- P05: nhiều hàng VI=none + các hàng subhead VI-only (Hình phạt…, ADF mở cửa…).
- P06: nhiều hàng VI=none (khối cắt VI lớn).
- P08: hàng đầu body là subhead EN "State-by-state: …" ghép với headline VI.
- P10: đoạn EN "Beyond making overseas travel more expensive…" lặp 2 lần với
  2 bản dịch VI khác nhau; hàng đầu là deck (EN) + headline VI.
- P12: cặp micro (1 hàng body, 3 câu mỗi bên).
- P13: lede EN typo "outh Korea's" (mất chữ S); tiêu đề từ SL:/TL:.
- P14: tiêu đề VI "tự động trục xuất" so với EN 'self-deportation' (thêm sau);
  nhiều hàng VI=none (khối 2018).
- P15: một câu EN bị ngắt giữa chừng qua 2 hàng ("…this past December," /
  "was inside his university-owned apartment…"); có hàng "(1)" và hàng EN
  không có đối ứng VI; tiêu đề EN bold, VI plain.
- P16–P19: tiêu đề trùng standalone + in-table.
- P20: không có URL nguồn; có hàng lede VI tự sinh (ô EN=none); subhead EN
  "EU Aims for Public Shaming…" (VI=none); nhiều khối cắt một bên.
