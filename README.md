# lme-bdnc-hw-session — phiên phân tích lại từ đầu (from scratch)

Repo này là **môi trường làm việc** cho nhiệm vụ:

> **COHESION BEYOND THE SENTENCE LEVEL — A Comparison of Cohesive Devices in
> English and Vietnamese** — phân tích ngôn ngữ học theo Halliday & Hasan
> (1976) cho phía EN, Trần Ngọc Thêm (*Hệ thống liên kết văn bản tiếng Việt*,
> 1985/2006, dẫn theo Nguyễn Thanh Tùng 2020) cho phía VI, trên 20 cặp bài báo
> song song Anh–Việt (SBS / VOA / Reuters / AP).

## Nguyên tắc độc lập (yêu cầu của chủ nhiệm)

- Phương pháp lấy từ skill **cohesion-en-vi**
  (github.com/longme179/Cohesive-Devices-in-English-and-Vietnamese-Analyzing-SKILL):
  chỉ copy các file **phương pháp** — `SKILL.md`, `AGENTS.md`, `pipeline/`,
  `references/`, `templates/`, `prompts/`, `examples/mini/`.
- **KHÔNG copy bất kỳ kết quả nào** của bộ benchmark trong repo skill
  (`out/`, `download/BDNC/`, `scripts/tie_tables/`, `scripts/align_tables/`
  không được đưa vào repo này). Mỗi cặp được **đọc và phân tích lại từ đầu**;
  benchmark không có mặt trong môi trường làm việc để bảo đảm tính độc lập.
- Mọi tie do người/agent đọc ngữ cảnh rồi viết tay; script chỉ bóc tách,
  tách câu, định vị, kiểm chứng, render và đóng gói (nguyên tắc manual-first
  của SKILL.md).

## Cấu trúc

```
SKILL.md / AGENTS.md       hợp đồng vận hành của skill (nguyên văn)
CONVENTIONS.md             quy ước gán nhãn ràng buộc cho 20 cặp (phiên này)
pipeline/                  các giai đoạn cơ học: ingest → segment → annotate
                           → render → build_appendix → export_docx/pdf → validate
references/                4 digest lý thuyết + bảng quyết định EN–VI
templates/                 input / analysis / tie-table templates
examples/mini/             ví dụ mẫu 5 hàng (chạy được end-to-end)
input/
  Appendix1-20-pairs.md    bản gốc người dùng (không sửa, md5 đã ghi nhận)
  appendix1.normalized.md  bản chuẩn hóa bố cục (chỉ sắp xếp lại, không đổi chữ)
  normalize_report.json    audit trail việc chuẩn hóa từng cặp
scripts/normalize_input.py script chuẩn hóa (có docstring giải thích lý do)
work/                      cây làm việc: pairs/PXX/, analysis/, tie_tables/
out/appendix1/             Appendix 1 thành phẩm (md/html/docx/pdf + IR + stats)
report/                    Appendix 2 — thống kê + báo cáo phát hiện
deliverables/              bản giao cuối
SESSION.md                 nhật ký phiên làm việc (cập nhật theo từng push)
```

## Trạng thái

Xem `SESSION.md`.

## Cách chạy lại (từ gốc repo)

```bash
python3 scripts/normalize_input.py                                  # chỉ khi cần dựng lại input
python3 -m pipeline.ingest  --input input/appendix1.normalized.md --work work
python3 -m pipeline.segment --work work
# với từng cặp: viết work/analysis/PXX_semantic.md + work/tie_tables/PXX.py (TAY)
python3 -m pipeline.annotate --work work --pair PXX
python3 -m pipeline.render   --work work --pair PXX
python3 -m pipeline.build_appendix --work work --out out/appendix1
python3 -m pipeline.export_docx    --out out/appendix1
python3 -m pipeline.export_pdf     --out out/appendix1
python3 -m pipeline.validate       --work work --out out/appendix1
```
