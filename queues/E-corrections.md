# Queue E corrections: OCR repair of 354 extracted markdown files

Read each extracted markdown file fully.
Fix OCR mistakes, remove hallucination notes, fix encoding.
Flag unrecoverably bad extractions.
One file at a time.
No scripts, no pattern matching.

## Progress

| Batch | Files | Status |
| --- | --- | --- |
| 1-25 | 140A_Exam_Review — ALGEBRA_REVIEW1 | done |
| 26-50 | Algebra_Solutions — analysis_2014-2016 | in progress |
| 51-100 |  | pending |
| 101-200 |  | pending |
| 201-354 |  | pending |

## Corrections applied

### Batch 1: files 1-25

- **140A_Exam_Review.md**: clean, no changes needed

- **603_11.md**: clean, no changes needed

- **8.1.2 Further Examples (1).md**: image placeholders in overview section, text clean

- **8150-hw1.md**: clean

- **8150-hw2.md**: clean

- **8150-hw3.md**: clean

- **8155-starter-problems.md**: clean

- **8210 Lecture Notes (Usher) Smooth Manifolds.md**: clean (2574L)

- **8.2.3 Normal family.md**: image placeholders, text clean

- **8.3 Riemann Mapping Theorem (1).md**: image placeholders, text clean

- **871-872January_2004_871-953.md**: clean

- **871-872January_2006_850-871.md**: clean

- **871-872January_2006_852-871.md**: clean

- **871-872January_2008_850-871.md**: clean

- **871-872June_2004_852-871.md**: clean

- **871-872June_2007_852-871.md**: clean

- **Adam Syllabus.md**: clean

- **AG Exam Problems.md**: clean

- **AG Solutions (1).md**: unrecoverable — binary/encoding garbage throughout

- **Algebra_Final_Solns 1.md**: fixed fraktur font garbling in problem 5

- **Algebra_Final_Solns.md**: fixed fraktur font garbling in problem 5 (duplicate of above)

- **Algebra_HW_11_Solns.md**: clean (duplicate content of 603_11.md with solutions)

- **Algebra_HW_4_Solns.md**: clean

- **Algebra_Notes.md**: clean

- **ALGEBRA_REVIEW1.md**: reconstructed 12+ garbled GRE multiple-choice problems

### Batch 2: files 26-50

- **Algebra_Solutions 1.md** and **Algebra_Solutions.md**: identical duplicates, clean (large solution manual, 9242L)

- **analysis_2003-2007.md**: removed 8 MinerU hallucination notes (OCR commentary about blank images)

- **analysis_2008-2013.md**: clean

- **analysis_2014-2016.md**: clean

- **analysis_jan2014.md**: clean

- **Applied-Algebra-FA17.md**: fixed 3 null bytes (replaced with tensor product and sigma symbols)

- **Azoff Problems by Topic.md**: clean

## Unrecoverable extractions

- **AG Solutions (1).md**: completely garbled binary/encoding.
  Every byte is non-standard encoding from a custom PDF font.
  No mathematical content is recoverable.
  Needs re-extraction or manual transcription from the source PDF.

- **Topology_Prelim_Answers_-_Unknown.md**: severely garbled throughout.
  The entire text has slashes inserted between characters, spaces in wrong places, and control characters replacing math symbols.
  384 control chars across 3064 lines.
  Mathematical content is unrecoverable.
  Needs re-extraction.

- **solutions-mims-2ed.md** and **Schilling_-_Acknowledgement...md** (duplicates): 8655 control characters from a custom PDF font encoding.
  Greek letters and math symbols replaced by control chars (\x16=\mu, \x1b=\sigma, \x0f=\epsilon) throughout 21K lines.
  25% of lines affected.
  Needs re-extraction with correct font mapping.
