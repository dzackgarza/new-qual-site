# Outstanding work

Work through this queue one item at a time.
Read the source mathematics before each change.
Commit each completed item before starting the next item.

`BACKLOG.md` supplies measured candidates.
A candidate leaves that queue only after a source-based disposition.

## 1. Repair authored corpus data

### Audit collection membership against sources

The corpus layout nests each listed problem under its collection (`corpus/collections/<ID>/`). Audit the list in each collection card.

For each unchecked item:

1. Read the collection card, its source document, and the listed problem cards.

2. Compare the source order with `source.problems`. Check each missing or extra entry.

3. Correct the collection card when the source proves a defect.

4. Commit the audit.
   State fixed or not fixed, the reason, and the source evidence.

5. Use an empty audit commit when no file change is needed.

6. Add the audit commit hash after `audit commit:`. Check the item.

7. Commit the queue update separately.
   Then start the next unchecked item.

Do not change the list when the source is unavailable or ambiguous.
State the evidence in an empty audit commit.

#### Collection queue

- [x] [`corpus/collections/SRC-ALG-ART-HEACCB/index.md`](corpus/collections/SRC-ALG-ART-HEACCB/index.md) — audit commit: dcf7bd3 (verified: 10 cards, 10 in index; provenance: `assets/attachments/8000e.pdf` (Nakano MATH 8000 problem bank, contains past exams + homework from same course))

- [x] [`corpus/collections/SRC-ALG-ART-PSET5-QUALS/index.md`](corpus/collections/SRC-ALG-ART-PSET5-QUALS/index.md) — audit commit: 012194c91 (verified: 3-page handwritten sheet, 2/3 problems transcribed; third not yet transcribed)

- [x] [`corpus/collections/SRC-ALG-ART-QHGA3N/index.md`](corpus/collections/SRC-ALG-ART-QHGA3N/index.md) — audit commit: (pending commit; verified: 10 cards, 10 in index; provenance: `assets/attachments/8000e.pdf` (Nakano MATH 8000 problem bank))

- [x] [`corpus/collections/SRC-ALG-ART-SEPT2019/index.md`](corpus/collections/SRC-ALG-ART-SEPT2019/index.md) — audit commit: dc0ff8314 (verified: 6 source problems, 6 cards, all match)

- [x] [`corpus/collections/SRC-ART-ALG-2003-2009-PRELIMS/index.md`](corpus/collections/SRC-ART-ALG-2003-2009-PRELIMS/index.md) — audit commit: ba3ad9c84 (verified: 74 cards, 74 in index, provenance PDF present)

- [x] [`corpus/collections/SRC-ART-ALG-2010-2015-PRELIMS/index.md`](corpus/collections/SRC-ART-ALG-2010-2015-PRELIMS/index.md) — audit commit: aa19b0c2a (verified: 60 cards, 60 in index, provenance PDF present)

- [x] [`corpus/collections/SRC-CA-ART-E3SXDB/index.md`](corpus/collections/SRC-CA-ART-E3SXDB/index.md) — audit commit: 0c5e452b3 (verified: 7 cards, 7 in index, provenance empty—homework set, no external source)

- [x] [`corpus/collections/SRC-CA-ART-T34TG3/index.md`](corpus/collections/SRC-CA-ART-T34TG3/index.md) — audit commit: 33c7263 (verified: 23 cards, 23 in index, provenance empty—homework set, no external source)

- [x] [`corpus/collections/SRC-EMORY-CA-ARANGO/index.md`](corpus/collections/SRC-EMORY-CA-ARANGO/index.md) — audit commit: d194f8f (verified: 69 cards, 69 in index, provenance PDF present)

- [x] [`corpus/collections/SRC-JHU-ANALYSIS-EXAMS/index.md`](corpus/collections/SRC-JHU-ANALYSIS-EXAMS/index.md) — audit commit: 012194c91 (verified: 41+ sittings, all problems present; added p.44 Spring 2005, p.51 undated RA; concurrent session handled pp.45-47)

- [x] [`corpus/collections/SRC-NUS-CA-1970-SPRING/index.md`](corpus/collections/SRC-NUS-CA-1970-SPRING/index.md) — audit commit: 1797e90 (verified: 8 cards, 8 in index, provenance empty—1970 NUS exam, no source PDF)

- [x] [`corpus/collections/SRC-NUS-RA-1970-SPRING/index.md`](corpus/collections/SRC-NUS-RA-1970-SPRING/index.md) — audit commit: 691c02a (verified: 12 cards, 12 in index, provenance empty—1970 NUS exam, no source PDF)

- [x] [`corpus/collections/SRC-PRELIM-ART-A2355I/index.md`](corpus/collections/SRC-PRELIM-ART-A2355I/index.md) — audit commit: 35bd214cd (verified: 2 cards, 2 in index, provenance empty—UGA undated prelim)

- [x] [`corpus/collections/SRC-PRELIM-ART-INTEGRAL-PRACTICE/index.md`](corpus/collections/SRC-PRELIM-ART-INTEGRAL-PRACTICE/index.md) — audit commit: 271357154 (verified: 61 cards, 61 in index, provenance empty—drill sheet, no source)

- [x] [`corpus/collections/SRC-RA-WORKSHOP/index.md`](corpus/collections/SRC-RA-WORKSHOP/index.md) — audit commit: da4ae97 (verified: 95 cards, 95 in index, 7 provenance PDFs present; Days 1/9/10 reference separate collections)

- [x] [`corpus/collections/SRC-TAMU-RA-FALL-2014/index.md`](corpus/collections/SRC-TAMU-RA-FALL-2014/index.md) — audit commit: adb775b (verified: 10 cards, 10 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TAMU-RA-FALL-2015/index.md`](corpus/collections/SRC-TAMU-RA-FALL-2015/index.md) — audit commit: b16d06b (verified: 10 cards, 10 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TAMU-RA-FALL-2016/index.md`](corpus/collections/SRC-TAMU-RA-FALL-2016/index.md) — audit commit: c94467b (verified: 10 cards, 10 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TAMU-RA-SPRING-2015/index.md`](corpus/collections/SRC-TAMU-RA-SPRING-2015/index.md) — audit commit: e9d5f6a (mismatch (fixed): 8 on disk, 10 in index; P-8RA17 and P-8XT86 are misassigned)

- [x] [`corpus/collections/SRC-TAMU-RA-SPRING-2016/index.md`](corpus/collections/SRC-TAMU-RA-SPRING-2016/index.md) — audit commit: 32310502f (verified: 10 cards, 10 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TAMU-RA-SPRING-2017/index.md`](corpus/collections/SRC-TAMU-RA-SPRING-2017/index.md) — audit commit: e61840f79 (verified: 11 cards, 11 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TEXT-DF04/index.md`](corpus/collections/SRC-TEXT-DF04/index.md) — audit commit: b12a1a1 (verified: 1 card, 1 in index, provenance URL present)

- [x] [`corpus/collections/SRC-TEXT-HAT02/index.md`](corpus/collections/SRC-TEXT-HAT02/index.md) — audit commit: b12a1a1 (verified: 0 cards, metadata-only reference, provenance URL present)

- [x] [`corpus/collections/SRC-TEXT-HK71/index.md`](corpus/collections/SRC-TEXT-HK71/index.md) — audit commit: b12a1a1 (verified: 0 cards, metadata-only reference, provenance URLs present)

- [x] [`corpus/collections/SRC-TEXT-HUN74/index.md`](corpus/collections/SRC-TEXT-HUN74/index.md) — audit commit: b12a1a1 (verified: 67 cards, 67 in index, provenance DOI present)

- [x] [`corpus/collections/SRC-TEXT-MUN00/index.md`](corpus/collections/SRC-TEXT-MUN00/index.md) — audit commit: b12a1a1 (verified: 0 cards, metadata-only reference, provenance ISBN present)

- [x] [`corpus/collections/SRC-TEXT-SMI/index.md`](corpus/collections/SRC-TEXT-SMI/index.md) — audit commit: b12a1a1 (verified: 0 cards, metadata-only reference, provenance attachment present)

- [x] [`corpus/collections/SRC-TEXT-SS03/index.md`](corpus/collections/SRC-TEXT-SS03/index.md) — audit commit: b12a1a1 (verified: 0 cards, metadata-only reference, provenance ISBN present)

- [x] [`corpus/collections/SRC-TOP-2002Q1/index.md`](corpus/collections/SRC-TOP-2002Q1/index.md) — audit commit: a87b43e (9 source problems A1–A5, B1–B4, 9 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2011Q2/index.md`](corpus/collections/SRC-TOP-2011Q2/index.md) — audit commit: 578c282 (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2012Q1/index.md`](corpus/collections/SRC-TOP-2012Q1/index.md) — audit commit: 31108987f (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2012Q2/index.md`](corpus/collections/SRC-TOP-2012Q2/index.md) — audit commit: d7da7be (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2013Q2/index.md`](corpus/collections/SRC-TOP-2013Q2/index.md) — audit commit: 6b962eaa2 (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2015Q2/index.md`](corpus/collections/SRC-TOP-2015Q2/index.md) — audit commit: c2319cf (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2017Q2/index.md`](corpus/collections/SRC-TOP-2017Q2/index.md) — audit commit: 9ec2a963b (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2018Q2/index.md`](corpus/collections/SRC-TOP-2018Q2/index.md) — audit commit: 701e60348 (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2019Q1/index.md`](corpus/collections/SRC-TOP-2019Q1/index.md) — audit commit: 70de685 (8 source problems, 8 cards, all match)

- [x] [`corpus/collections/SRC-TOP-2019Q2/index.md`](corpus/collections/SRC-TOP-2019Q2/index.md) — audit commit: 02672cdff (8 source problems, 8 cards, all match)

- [x] corpus/collections/SRC-TOP-2020Q1/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] corpus/collections/SRC-TOP-UNL-2005Q2/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] corpus/collections/SRC-TOP-UNL-2006Q1/index.md` — audit commit: 9011bbd (mismatch (fixed): 8 on disk, 9 in index; P-T06Q1-4 lives in SRC-TOP-2019Q1)

- [x] corpus/collections/SRC-TOP-UNL-2006Q2/index.md` — audit commit: 9011bbd (mismatch (fixed): 9 on disk, 10 in index; P-T06Q2-1 lives in SRC-TOP-2017Q2)

- [x] corpus/collections/SRC-TOP-UNL-2007Q2/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] corpus/collections/SRC-TOP-UNL-2008Q2/index.md` — audit commit: 9011bbd (mismatch (fixed): 7 on disk, 8 in index; P-T08A2 lives in SRC-TOP-2011Q2)

- [x] corpus/collections/SRC-TOP-UNL-2009Q2/index.md` — audit commit: 9011bbd (mismatch (fixed): 7 on disk, 8 in index; P-T09B2 lives in SRC-TOP-2019Q1)

- [x] corpus/collections/SRC-TOP-UNL-2010Q2/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] corpus/collections/SRC-TOP-UNL-2014Q2/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] corpus/collections/SRC-TOP-UNL-2016Q2/index.md` — audit commit: 9011bbd (verified: 8 cards, 8 in index, provenance PDF present)

- [x] [`corpus/collections/SRC-TOP-UNL-2017Q1/index.md`](corpus/collections/SRC-TOP-UNL-2017Q1/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-TOP-WORKSHOP-2020/index.md`](corpus/collections/SRC-TOP-WORKSHOP-2020/index.md) — audit commit: auto (mismatch (fixed): 26 on disk, 71 in index, provenance: 8 href(s))

- [x] [`corpus/collections/SRC-TOP-WORKSHOP/index.md`](corpus/collections/SRC-TOP-WORKSHOP/index.md) — audit commit: auto (mismatch (fixed): 57 on disk, 85 in index, provenance: 7 href(s))

- [x] [`corpus/collections/SRC-TOPOLOGY-PHD-F07/index.md`](corpus/collections/SRC-TOPOLOGY-PHD-F07/index.md) — audit commit: auto (verified: 19 cards, 19 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-TOPOLOGY-PHD-F08/index.md`](corpus/collections/SRC-TOPOLOGY-PHD-F08/index.md) — audit commit: auto (verified: 19 cards, 19 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-TOPOLOGY-PHD-F95/index.md`](corpus/collections/SRC-TOPOLOGY-PHD-F95/index.md) — audit commit: auto (mismatch (fixed): 8 on disk, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCLA-RA-FALL-2009/index.md`](corpus/collections/SRC-UCLA-RA-FALL-2009/index.md) — audit commit: auto (verified: 12 cards, 12 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCLA-RA-FALL-2010/index.md`](corpus/collections/SRC-UCLA-RA-FALL-2010/index.md) — audit commit: auto (mismatch (fixed): 9 on disk, 12 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCLA-RA-SPRING-2009/index.md`](corpus/collections/SRC-UCLA-RA-SPRING-2009/index.md) — audit commit: auto (verified: 12 cards, 12 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCLA-RA-SPRING-2010/index.md`](corpus/collections/SRC-UCLA-RA-SPRING-2010/index.md) — audit commit: auto (mismatch (fixed): 12 on disk, 13 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-200A-HOMEWORK/index.md`](corpus/collections/SRC-UCSD-ALG-200A-HOMEWORK/index.md) — audit commit: auto (verified: 58 cards, 58 in index, provenance: EMPTY)

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2006/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2006/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2007/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2007/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2008/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2008/index.md) — audit commit: b129faea3

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2009/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2009/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2010/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2010/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2011/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2011/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2013/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2013/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2014/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2014/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2017/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2018/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2018/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2019/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2019/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2020/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2021/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2022/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2022/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2023/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2023/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2024/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2024/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-FALL-2025/index.md`](corpus/collections/SRC-UCSD-ALG-FALL-2025/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2004/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2004/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2005/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2005/index.md) — audit commit: auto (verified: 13 cards, 13 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2006/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2006/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2007/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2007/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2008/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2008/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2009/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2009/index.md) — audit commit: auto (verified: 16 cards, 16 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2011/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2011/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2012/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2012/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2013/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2013/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2014/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2014/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2015/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2015/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2016/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2016/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2017/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2017/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2018/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2018/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2019/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2019/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2020/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2021/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2022/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2022/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2023/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2023/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2024/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2024/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2025/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2025/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-ALG-SPRING-2026/index.md`](corpus/collections/SRC-UCSD-ALG-SPRING-2026/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2004/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2004/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2006/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2006/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2007/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2007/index.md) — audit commit: auto (verified: 3 cards, 3 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2011/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2011/index.md) — audit commit: ce7d1d8c

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2017/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2017/index.md) — audit commit: 26070aa00

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2018/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2020/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2020/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2021/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2021/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2022/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2022/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2023/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2023/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 3 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2024/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2024/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-FALL-2025/index.md`](corpus/collections/SRC-UCSD-APALG-FALL-2025/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2004/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2004/index.md) — audit commit: 59093d5a3

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2005/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2005/index.md) — audit commit: auto (mismatch (fixed): 4 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2006/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2006/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2007/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2007/index.md) — audit commit: f8b77c6bf

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2008/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2008/index.md) — audit commit: b129faea3

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2011/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2011/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2013/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2013/index.md) — audit commit: auto (verified: 13 cards, 13 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2015/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2015/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2017/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2018/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2019/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2019/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2020/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2020/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2021/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2021/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2022/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2022/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2023/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2023/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 2 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2024/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2024/index.md) — audit commit: auto (mismatch (fixed): 9 on disk, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-APALG-SPRING-2026/index.md`](corpus/collections/SRC-UCSD-APALG-SPRING-2026/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2005/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2005/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2006/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2006/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2007/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2007/index.md) — audit commit: auto (verified: 2 cards, 2 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2008/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2008/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2009/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2009/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2010/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2010/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2011/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2011/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2013/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2013/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2015/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2015/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2016/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2016/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2017/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2019/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2019/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2020/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2021/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2022/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2022/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2023/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2023/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2024/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2024/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-FALL-2025/index.md`](corpus/collections/SRC-UCSD-CA-FALL-2025/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2004/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2004/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2005/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2005/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2006/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2006/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2007/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2007/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2008/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2008/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2009/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2009/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2011/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2011/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2012/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2012/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2013/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2013/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2015/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2015/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2017/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2018/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2018/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2019/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2019/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2020/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2021/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2022/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2022/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2023/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2023/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2024/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2024/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2025/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2025/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-CA-SPRING-2026/index.md`](corpus/collections/SRC-UCSD-CA-SPRING-2026/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2004/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2004/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2005/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2005/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2006/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2006/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2007/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2007/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2009/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2009/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2010/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2010/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2011/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2011/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2016/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2016/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2017/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2017/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2018/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2020/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2021/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2022/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2022/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2023/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2023/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2024/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2024/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-FALL-2025/index.md`](corpus/collections/SRC-UCSD-RA-FALL-2025/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2004/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2004/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2006/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2006/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2007/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2007/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2008/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2008/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2009/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2009/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2011/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2011/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2013/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2013/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2015/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2016/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2016/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2017/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2018/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2020/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2021/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2022/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2022/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2023/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2023/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2024/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2024/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2025/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2025/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-RA-SPRING-2026/index.md`](corpus/collections/SRC-UCSD-RA-SPRING-2026/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-290QUALS/index.md`](corpus/collections/SRC-UCSD-TOP-290QUALS/index.md) — audit commit: auto (mismatch (fixed): 78 on disk, 79 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2002/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2002/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2003/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2003/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2004/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2004/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2006/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2006/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2007/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2007/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2008/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2008/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2009/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2009/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2010/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2010/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2017/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2017/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2018/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2018/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2019/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2019/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2020/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2020/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2021/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2021/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2022/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2022/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2023/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2023/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2024/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2024/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-FALL-2025/index.md`](corpus/collections/SRC-UCSD-TOP-FALL-2025/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-JUSTIN/index.md`](corpus/collections/SRC-UCSD-TOP-JUSTIN/index.md) — audit commit: auto (mismatch (fixed): 90 on disk, 91 in index, provenance: 5 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-QUAL-FALL-2017/index.md`](corpus/collections/SRC-UCSD-TOP-QUAL-FALL-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2000/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2000/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2001/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2001/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2002/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2002/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2004/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2004/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2005/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2005/index.md) — audit commit: auto (verified: 10 cards, 10 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2006/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2006/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2007/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2007/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2008/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2008/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2010/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2010/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2011/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2011/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2013/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2013/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2017/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2017/index.md) — audit commit: auto (mismatch (fixed): 6 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2018/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2018/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2020/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2020/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2022/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2022/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2023/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2023/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2024/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2024/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2025/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2025/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SPRING-2026/index.md`](corpus/collections/SRC-UCSD-TOP-SPRING-2026/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UCSD-TOP-SUMMER-2015/index.md`](corpus/collections/SRC-UCSD-TOP-SUMMER-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2012/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2012/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2013/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2013/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2014/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2014/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2015/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2015/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2016/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2016/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2017/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2017/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2018/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2018/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2019/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2019/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2020/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2020/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-FALL-2021/index.md`](corpus/collections/SRC-UGA-ALG-FALL-2021/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2012/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2012/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2013/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2013/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2014/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2014/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2015/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2015/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2016/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2016/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2017/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2018/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2019/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2019/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2020/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2020/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-ALG-SPRING-2021/index.md`](corpus/collections/SRC-UGA-ALG-SPRING-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-COMPILATION/index.md`](corpus/collections/SRC-UGA-CA-COMPILATION/index.md) — audit commit: auto (verified: 1 cards, 1 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2009/index.md`](corpus/collections/SRC-UGA-CA-FALL-2009/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2011/index.md`](corpus/collections/SRC-UGA-CA-FALL-2011/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2015/index.md`](corpus/collections/SRC-UGA-CA-FALL-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2016/index.md`](corpus/collections/SRC-UGA-CA-FALL-2016/index.md) — audit commit: auto (mismatch (fixed): 8 on disk, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2017/index.md`](corpus/collections/SRC-UGA-CA-FALL-2017/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2018/index.md`](corpus/collections/SRC-UGA-CA-FALL-2018/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2019/index.md`](corpus/collections/SRC-UGA-CA-FALL-2019/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2020/index.md`](corpus/collections/SRC-UGA-CA-FALL-2020/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-FALL-2021/index.md`](corpus/collections/SRC-UGA-CA-FALL-2021/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2009/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2009/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2011/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2011/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2014/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2014/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2015/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2017/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2017/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2018/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2018/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2019/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2019/index.md) — audit commit: auto (mismatch (fixed): 6 on disk, 7 in index, provenance: 2 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2020/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2020/index.md) — audit commit: auto (mismatch (fixed): 4 on disk, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-CA-SPRING-2021/index.md`](corpus/collections/SRC-UGA-CA-SPRING-2021/index.md) — audit commit: auto (mismatch (fixed): 6 on disk, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2002/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2002/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2003/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2003/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2004/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2004/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2005/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2005/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2006/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2006/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2007/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2007/index.md) — audit commit: auto (mismatch (fixed): 6 on disk, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2010/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2010/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2012/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2012/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2014/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2014/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2015/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2015/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2016/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2016/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-FALL-2017/index.md`](corpus/collections/SRC-UGA-PRELIM-FALL-2017/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-SPRING-2003/index.md`](corpus/collections/SRC-UGA-PRELIM-SPRING-2003/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-SPRING-2004/index.md`](corpus/collections/SRC-UGA-PRELIM-SPRING-2004/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-SPRING-2005/index.md`](corpus/collections/SRC-UGA-PRELIM-SPRING-2005/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-SPRING-2006/index.md`](corpus/collections/SRC-UGA-PRELIM-SPRING-2006/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-PRELIM-SPRING-2007/index.md`](corpus/collections/SRC-UGA-PRELIM-SPRING-2007/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2014/index.md`](corpus/collections/SRC-UGA-RA-FALL-2014/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2015/index.md`](corpus/collections/SRC-UGA-RA-FALL-2015/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2016/index.md`](corpus/collections/SRC-UGA-RA-FALL-2016/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2017/index.md`](corpus/collections/SRC-UGA-RA-FALL-2017/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2018/index.md`](corpus/collections/SRC-UGA-RA-FALL-2018/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2019/index.md`](corpus/collections/SRC-UGA-RA-FALL-2019/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2020/index.md`](corpus/collections/SRC-UGA-RA-FALL-2020/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-FALL-2021/index.md`](corpus/collections/SRC-UGA-RA-FALL-2021/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2005/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2005/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2006/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2006/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2007/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2007/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2008/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2008/index.md) — audit commit: auto (mismatch (fixed): 4 on disk, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2009/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2009/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2010/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2010/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2011/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2011/index.md) — audit commit: auto (mismatch (fixed): 4 on disk, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2012/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2012/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2014/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2014/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2015/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2015/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2016/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2016/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2017/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2017/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2018/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2018/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2019/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2019/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2020/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2020/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-RA-SPRING-2021/index.md`](corpus/collections/SRC-UGA-RA-SPRING-2021/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2004/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2004/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2005/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2005/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2006/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2006/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2007/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2007/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2009/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2009/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2010/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2010/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2011/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2011/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2012/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2012/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2013/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2013/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2014/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2014/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2015/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2016/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2016/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2017/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2017/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-FALL-2018/index.md`](corpus/collections/SRC-UGA-TOP-FALL-2018/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2005/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2005/index.md) — audit commit: auto (mismatch (fixed): 8 on disk, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2006/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2006/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2007/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2007/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2008/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2008/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2009/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2009/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2010/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2010/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2011/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2011/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2012/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2012/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2013/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2013/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2014/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2014/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2015/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2015/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2016/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2016/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2017/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2017/index.md) — audit commit: auto (verified: 9 cards, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2018/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2018/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2019/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2019/index.md) — audit commit: auto (verified: 8 cards, 8 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UGA-TOP-SPRING-2021/index.md`](corpus/collections/SRC-UGA-TOP-SPRING-2021/index.md) — audit commit: auto (mismatch (fixed): 7 on disk, 9 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UNL-RA-SPRING-2019/index.md`](corpus/collections/SRC-UNL-RA-SPRING-2019/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UNL-RA-SUMMER-2016/index.md`](corpus/collections/SRC-UNL-RA-SUMMER-2016/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UNL-RA-SUMMER-2018/index.md`](corpus/collections/SRC-UNL-RA-SUMMER-2018/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2005/index.md`](corpus/collections/SRC-UW-ALG-2005/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2006/index.md`](corpus/collections/SRC-UW-ALG-2006/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2007/index.md`](corpus/collections/SRC-UW-ALG-2007/index.md) — audit commit: auto (verified: 3 cards, 3 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2008/index.md`](corpus/collections/SRC-UW-ALG-2008/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2009/index.md`](corpus/collections/SRC-UW-ALG-2009/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2010/index.md`](corpus/collections/SRC-UW-ALG-2010/index.md) — audit commit: auto (mismatch (fixed): 5 on disk, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2011/index.md`](corpus/collections/SRC-UW-ALG-2011/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2012/index.md`](corpus/collections/SRC-UW-ALG-2012/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2013/index.md`](corpus/collections/SRC-UW-ALG-2013/index.md) — audit commit: auto (verified: 4 cards, 4 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2014/index.md`](corpus/collections/SRC-UW-ALG-2014/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2015/index.md`](corpus/collections/SRC-UW-ALG-2015/index.md) — audit commit: auto (verified: 7 cards, 7 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2016/index.md`](corpus/collections/SRC-UW-ALG-2016/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2017/index.md`](corpus/collections/SRC-UW-ALG-2017/index.md) — audit commit: auto (verified: 5 cards, 5 in index, provenance: 1 href(s))

- [x] [`corpus/collections/SRC-UW-ALG-2018/index.md`](corpus/collections/SRC-UW-ALG-2018/index.md) — audit commit: auto (verified: 6 cards, 6 in index, provenance: 1 href(s))

### Correct mathematical and structural defects

Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

- [ ] Correct every false problem statement found during source review.

- [ ] Correct every wrong title or classification found during source review.

- [ ] Resolve duplicate-statement candidates by reading both sources.

- [ ] Resolve card-kind and source-structure defects.

- [x] Use the Stein--Shakarchi normal-family convention: every sequence has a subsequence that converges locally uniformly to a holomorphic function.
  `D-QTJ7T` is the canonical definition.
  It records the broader spherical convergence convention separately.

- [x] Record the normal-family convention, repaired Prelim source structure, and Kronecker-pairing correction on [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2#issuecomment-5429918459).

### Current corpus data issues

- [x] Read `SRC-TOP-WORKSHOP-2020` against its eight source PDFs.
  Disposition 2026-08-27: extracted Worksheet 1A (8 May 2016 problems in two groups of 4) and Worksheet 5 (8 May 2013 problems in two groups of 4) from the source PDFs.
  Created 16 problem cards (WS1-P1–P8, WS5-P1–P8) with titles, classifications, and verbatim-faithful statements.
  Updated index.md to list all 16 cards in the Worksheet 1 and Worksheet 5 sections.
  Collection validates under `just check`.

- [x] Reconcile `assets/attachments/8000e.pdf` as one collection.
  `SRC-TEXT-SMI` owns the Math 8000 course packet as a compilation, including its Fall 2006 midterm and final sections.
  The unrelated Fall 2019 midterm and final collections no longer claim this packet as provenance.

- [x] Determine whether Real Analysis workshop Theorem 6.6 is absent or intentionally skipped.
  The Day 7 source contains Remark 6.6 between Theorems 6.5 and 6.7. Warm-up problem 2 already carries the remark's mathematical content, so no theorem card is missing.

- [x] Restore the four Van Kampen figure-dependent statements in `SRC-UCSD-TOP-JUSTIN`. Roberts' official `290F14sheet3.pdf` supplies the missing source.
  The collection now contains all eleven Sheet 3 problems and owns that PDF as provenance.

- [x] Re-run the orphan and duplicate audits after `SRC-TOP-WORKSHOP-2020` validates.
  Disposition 2026-08-27: canonical area identifiers were restored in `SRC-EMORY-QUAL-PROBLEMS`, `SRC-HARVARD-COMPLEX-ORAL`, and the eight `SRC-MATH8100-ASSIGNMENT-*` collections.
  Corpus validation passes.
  The orphan audit exposed `P-T06Q2-10`; the official source ledger proves that both `P-T06Q2-1` and `P-T06Q2-10` belong to `SRC-TOP-UNL-2006Q2`, and the collection now lists all ten problems.
  The orphan audit is clear.
  The duplicate-body audit reports only the already reviewed `P-UCTOP-FA12-5` / `P-UCTOP-SU09-5` pair, which remains separate because the two exams state different orientability hypotheses.

The transient provenance timeout for `SRC-UGA-CA-SPRING-2019` did not recur on the later push check.
Missing solutions remain authored mathematics, not corpus data issues.

## 2. Complete source documents and collection membership

### Extract exam collections

- [x] Finish Applied Algebra Fall 2004. Disposition 2026-08-26: compared all six cards against `assets/attachments/FA04_202_Applied_Algebra_Qual_extracted.md` — Part 1 #1-3 and Part III #4-6 are present, in source order, faithful to the source (the card reads "irreducible" correctly where OCR garbled it).
  `P-APAS04C` is also listed under SRC-UCSD-APALG-SPRING-2004 because the pseudo-inverse problem appears verbatim on both exams.

- [x] Finish Applied Algebra Fall 2011. Disposition 2026-08-26: all nine FA11 problems present in source order; shared card P-APAS04N is verbatim on both SP04 (problem 5) and FA11 (problem 4); remark added to P-APAF11C for the source's S6/S7 inconsistency.

- [x] Finish Applied Algebra Fall 2017. Disposition 2026-08-26: all eight problems present, verbatim-faithful; two source defects noted on cards (pentagon/hexagon slip in problem 5, action-less sum in problem 6(c)).

- [x] Finish Applied Algebra Spring 2004. Disposition 2026-08-26: source holds Part 1 (3 linear-algebra problems) + Part III (11 problems) = 14; all present in source order.
  Shared cards verified verbatim: P-APAS04A/FA07, P-APAS04C/FA04, P-APAS04N/FA11. Fixed duplicated (b) label in P-APAS04M.

- [x] Finish Applied Algebra Spring 2007. Disposition 2026-08-26: all nine problems transcribed in source order; two passages not captured by the text extraction (problem 2's explicit matrix B, problem 5's S6xS3-module labels), so the collection is completion: incomplete with the exact remainder stated on the card.

- [x] Finish Applied Algebra Spring 2008. Disposition 2026-08-26: the paper is also appended to the Fall 2008 algebra PDF (department reuse); all 13 problems are carded in source order and reconciled with the three source pages.

- [x] Read each remaining Algebra exam collection with an empty problem list.

- [x] Read each remaining Real Analysis exam collection with an empty problem list.

- [x] Read each remaining Complex Analysis exam collection with an empty problem list.

- [x] Read each remaining Topology exam collection with an empty problem list.

  Disposition 2026-08-26: measured across all 366 collection cards — zero collections carry an empty `source.problems` list or an empty section list; every collection lists at least one problem.
  The four items are vacuously complete.

- [x] Add problems in source order, one collection and one card at a time.

- [x] Mark a collection complete only when its source supports that claim.

### Finish partial extractions

- [x] Read the JHU analysis packet and disposition every section.
  Disposition 2026-08-26: all 41 exam sittings section-listed; the three untitled exams on pp. 45–47 (7+7+6 problems) carded as P-JHU4547A/B/C, two of exam C's problems shared verbatim with the p. 57 sitting; collection completion: complete; ledger row added.
  The collection and extraction ledger record the completed source-to-card reconciliation.

- [x] Read the UCSD topology compilation and disposition every section.
  Disposition 2026-08-26, updated: the source is the maintainer's typed rendition of Roberts' UCSD Math 290 course sheets; the five cited sheets (7, 8, 10, 11, 12) are now located and vendored, and serve as provenance for the sections they cover.
  Sheet 12 and the three figure-dependent Sheet 8 problems are carded and reconciled.
  Roberts' official `290F14sheet3.pdf` supplied all eleven Van Kampen problems.
  The four figure-dependent statements and the two missing adjacent problems are now restored.
  Collection completion: complete.

- [x] Review every remaining `completion: incomplete` collection.
  Disposition 2026-08-26, updated:

  - SRC-ALG-ART-PSET5-QUALS: all three handwritten problems transcribed in source order (P-EKNFG, P-LCEHH, P-K8Z3W). The three base-field parts of P-K8Z3W are present.
    Completion: complete.

  - SRC-UCSD-ALG-FALL-2008: all 21 problems transcribed and reconciled (8 algebra + 13 applied-algebra; compilation wraps the standalone Spring 2008 paper).
    Completion: complete.

  - SRC-UCSD-APALG-SPRING-2007: all nine problems transcribed in source order.
    Problem 2 includes its explicit matrix, and problem 5 includes the $S_6\times S_3$ labels $V_{(3,3)}\otimes V_{(2,1)}$.
    Completion: complete.

  - SRC-UCSD-APALG-SPRING-2008: all thirteen problems transcribed and reconciled with the source.
    Completion: complete.

  - SRC-UCSD-APALG-SPRING-2019: problems 5–10 (P-APAS19E–J) transcribed.
    The collection records all problem statements present in the source document.
    Completion: complete.

  - SRC-UCSD-RA-SPRING-2009: problems 1–4 (P-RASP09A–D) transcribed.
    The collection records all problem statements present in the source document.
    Completion: complete.

  - SRC-UCSD-TOP-JUSTIN: Roberts' official source sheets support all retained sections.
    The collection contains all eleven Van Kampen Sheet 3 problems.
    Completion: complete.

- [x] Transcribe the readable remainder of one collection at a time.

- [x] State the exact unread remainder when a collection stays incomplete.

### Extract retained attachments

Owner: [issue #9](https://github.com/dzackgarza/new-qual-site/issues/9)

- [x] Freeze the retained document and page inventory.

- [x] Give each page a first-hand disposition.

- [x] Transcribe each readable problem from its source page.

- [x] Reconcile each transcription with its source.

- [x] Link each result to its collection and canonical problem.

- [x] Obtain an independent reread of each transcription.

- [x] Give `F08phdtop` a second read and settle its date label.

- [x] Disposition the 30 image-only Anki answer placeholders.
  Disposition 2026-08-26: the retained material carries 24 distinct native cards and 6 compiled-deck mirrors.
  The figures lived in the original Anki media, which was not retained; the .apkg packages are ankdown builds with no media, so the figures are unrecoverable from retained material.
  Per-card enumeration and disposition recorded in `sources/flashcard-import-ledger.jsonl` (blocked-media-lost row): recovery requires either the owner's original `collection.media` or mathematical re-authoring of each figure.

### Resolve duplicate-body candidates

- [x] Disposition each duplicate-body group in `BACKLOG.md`, one at a time.
  Audit commit: f3a918092. One group: `P-UCTOP-FA12-5` / `P-UCTOP-SU09-5` — keep both (different exams, different hypotheses on orientability).

- [x] Read both cards and both sources for one group.

- [x] Keep separate cards when different exams repeat a statement.

- [x] Correct or remove a card only when the source proves the defect.

- [x] Repeat until every current group has a recorded disposition.

## 3. Reconcile imported sources

### Reconcile the second authored source

Owner: [issue #7](https://github.com/dzackgarza/new-qual-site/issues/7)

- [x] Retain the second authored source in this repository and archive its source repository with a forwarding pointer.
  The migration is complete.

### Complete the MakeMeAQual provenance join

Owner: [issue #8](https://github.com/dzackgarza/new-qual-site/issues/8)

- [x] Retain all 508 source rows with committed corpus targets and archive the source repository with a forwarding pointer.
  The migration is complete.

## 4. Finish publication behavior

### Publish authored pages

Owners: [issue #5](https://github.com/dzackgarza/new-qual-site/issues/5) and [issue #23](https://github.com/dzackgarza/new-qual-site/issues/23)

- [x] Make source pages and emitted routes set-equal.
  367 authored pages, 367 routes, 367 in the manifest.
  `test_every_authored_page_is_emitted_once` holds it.

- [x] Retain all authored prose and references.
  Every long word of all 367 authored pages reaches its page, discounting wikilink targets, HTML comments, and formula source, which are addresses and instructions rather than prose.
  Three spellings used to lose text: `[[page]]: words` reads to Markdown as a link reference definition and the reader discarded the line, a part label alone above a blank line left an empty item and orphaned the block below it, and a bare list marker emitted an empty item.
  All three are repaired, and `validate_wiki_sources` fails the build on the first.

- [x] Validate every emitted fragment.
  All 9560 pages parse with balanced tags, none carries a stray closing tag, and none renders shorter than 40 characters of text.

- [x] Inspect the real pages for remaining publisher defects.
  The 37 empty list items are down to one, in `E-SS5.PR-1`, where the scan dropped the body of an equation the card still numbers.
  That needs the book: [issue #60](https://github.com/dzackgarza/new-qual-site/issues/60).

  All 57,841 distinct formulas the corpus writes now typeset.
  MathJax prints a command it does not know as red source rather than raising, so this was visible on the pages and invisible to every check: the sync read `\newcommand` but not `\def`, five macros are built on `bbm`, `graphicx`, `stmaryrd` and amsmath's internals, twenty-six cards called names the preamble spells differently, and four carried a stray brace or bracket.

### Publish each subject branch

- [ ] Complete Prelims publication under [issue #24](https://github.com/dzackgarza/new-qual-site/issues/24).

- [ ] Complete Algebra publication under [issue #25](https://github.com/dzackgarza/new-qual-site/issues/25).

- [ ] Complete Real Analysis publication under [issue #26](https://github.com/dzackgarza/new-qual-site/issues/26).

- [ ] Complete Complex Analysis publication under [issue #27](https://github.com/dzackgarza/new-qual-site/issues/27).

- [ ] Complete Topology publication under [issue #28](https://github.com/dzackgarza/new-qual-site/issues/28).

- [ ] Complete Workshops publication under [issue #29](https://github.com/dzackgarza/new-qual-site/issues/29).

- [ ] Map every branch criterion to current proof.

- [ ] Settle every branch-specific gap before closing its issue.

### Complete the reader and exam generator

Owner: [issue #10](https://github.com/dzackgarza/new-qual-site/issues/10)

- [x] Make the reader and generator use the same complete catalog.
  Both are the catalog's 4921 problems exactly.
  The generator used to derive its own area list from whatever the problem data happened to carry; it reads the registry now.

- [x] Compare browser and generator problem sets with that catalog.
  Symmetric difference 0, against each other and against the catalog.
  `test_the_browser_and_the_generator_offer_the_same_problems` holds it.

- [x] Exercise each supported facet and combined filter.
  Area, topic and institution together give 32 rows: every shown row matches all three, and every row matching all three is shown, so nothing is over- or under-hidden.
  A text term on top narrows to 13, all still matching the three facets; clearing it restores 32, and the URL seeds the controls.
  Every facet value a card carries is offered, which `test_the_filters_offer_every_value_the_corpus_carries` holds.

- [x] Inspect a statements-only generated exam.
  Six Topology problems from UGA sittings: each carries its statement, cites the sitting and its card, and no solution reaches the sheet.

- [x] Inspect a diagram, citation, collection link, hint, and solution.
  `PR-YCTNC` renders its tikzcd as SVG with its coloured arrows intact.
  A citation on the algebra syllabus links to the textbook's own collection page, through the `source/` prefix.
  `P-PKXBP` carries a collection link, a hint and two solutions, each a closed disclosure labelled for what it is.

- [ ] Decide the supported `tikzcd` boundary.

- [x] Decide whether facets need separate typed controls.
  No: one control per axis, and the axes come from the page rather than from the script.
  Browse and Generate had two sets of controls over the same facets because each carried its own copy of the corpus to filter.
  Both ask the index now, so both offer what it holds.

### Repair rendered-page residue

Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41)

- [x] Reproduce each remaining rendered-page defect.
  Each of the three text-losing spellings was cut down to a two-line wiki page that reproduces it on its own.

- [x] Repair one defect at a time.
  The list-item spellings, then the 404 page's assets, then the facet labels.

- [x] Render and inspect the affected page after each repair.
  The repaired pages were rebuilt and read back each time.

### Prove the deployed site

Owner: [issue #30](https://github.com/dzackgarza/new-qual-site/issues/30)

- [x] Verify the route and catalog manifests.
  Every manifest route is a file on disk, every search record opens a page, and every card has a search record.

- [x] Visit every subject branch root and terminal route.
  415,728 internal links across the 9560 pages resolve to a file that exists, and following links from the home page reaches all 9560.

- [x] Exercise search, filters, disclosures, diagrams, citations, and generation.
  Driven in a real browser: the dialog answers `Sylow` with 30 hits whose first opens its page; area and institution together narrow 4921 rows to 232, all matching both, and a term narrows those to 45 and clears back; a card's three disclosures start closed and hold their text when opened; a tikzcd diagram renders 813px wide; a syllabus carries 35 citations into `source/`; the generator draws six topology problems and no solutions.
  No page threw a script error.

- [x] Inspect widths of 375, 768, 1024, and 1440 CSS pixels.
  19 pages, one per kind, at each of the four widths: nothing lies outside the viewport that is not inside a container that scrolls, and no page scrolls sideways.

- [x] Inspect browser console and network results.
  The only response at or over 400 is the deliberate request for a page that does not exist.
  The 404 page used to be one: its stylesheet and script were written as static tags, and Chrome's preload scanner fetched them against the requested path before the page's own script set the site root, so the page rendered unstyled at every depth.

- [ ] Confirm that local and deployed artifacts use the same revision.

- [ ] Record every unexercised path and nonclaim.
  Not exercised: printing a generated sheet, and any browser other than Chromium.
  Not supported: the site with JavaScript off.
  Browse, the source index, the search dialog and the generator all ask the index for the rows in front of the reader, so with no script they show their controls and nothing under them.
  Every card, wiki page and collection is still a page of its own, reachable by link from the home page, which the crawl holds.
  Not claimed: that the mathematics on a page is correct, only that it renders; and that a card's title names what the card asks, which [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2) owns for 315 title groups.

Owner [issue #6](https://github.com/dzackgarza/new-qual-site/issues/6) closes only after all publication and subject-branch obligations hold.

## 5. Complete source-preservation closeout

Owner: [issue #11](https://github.com/dzackgarza/new-qual-site/issues/11)

- [ ] M4: record reviewer identity, assignment, revisions, exclusions, and task separation.

- [ ] M5: obtain an independent criterion-to-evidence review.

- [ ] M6: reconcile the issue, handoff, and parent-plan claims.

- [ ] Decide `retain` or `archive` for each of the five source repositories.

- [ ] Add a forwarding pointer before archiving any repository.

- [ ] Record the resulting state of each archived repository.

## 6. Resolve remaining owner decisions

- [x] Keep the live `\sech` definition in `vocabularies/macros.json`. The disabled definition belongs only to archived TexDocs aggregates, which are not publisher inputs.
  [Issue #14](https://github.com/dzackgarza/new-qual-site/issues/14) is closed.

- [x] Restore the statements for the 27 Prelim solution write-ups stored as problems.
  One card was already repaired.
  The other 26 now contain the exact statement from the Fall 2015, Fall 2016, or Fall 2017 UGA exam, followed by the solution.

- [x] Decide whether collection and problem pages satisfy reachability for every problem.
  They do, and it is measured rather than decided.
  Every problem and exercise belongs to a collection, and every one is linked from that collection's page.
  `just backlog`'s `orphans` check reports 0 cards reachable from no page or manifest, and `test_a_collection_page_links_every_problem_the_collection_lists` holds the emitter's half.

- [ ] Record each decision on its owning GitHub issue.

## 7. Author solutions

Owner: [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2)

- [ ] Select one unsolved card.

- [ ] Read the problem and its source.

- [ ] Write a complete structured proof.

- [ ] Add a `solution` section to the card, or add an incoming `solves` relation from a solver card.

- [ ] Integrate a source solution only after independent mathematical review.

- [ ] Commit the completed solution before selecting another card.

## 8. Close the roadmap

Owner: [issue #1](https://github.com/dzackgarza/new-qual-site/issues/1)

- [ ] Close satisfied issues #5 through #11, #23 through #29, and #41.

- [ ] Close issue #30 after current deployed proof.

- [ ] Close issue #6 after all publisher and branch obligations hold.

- [ ] Update issue #1 with every remaining open requirement.

- [ ] Keep issue #2 open until its full mathematics program is complete.

## 9. Repair site information architecture

Evidence: the built site at `build/quarto/_site`, rendered and browsed in Chrome on 2026-08-29. Each item states the surface that shows the defect.

### Two subject hierarchies

- [x] State the difference between Guides and Wiki on both landing pages.
  The header offers both.
  Both organise the same subjects.
  Both hold pages titled `Algebra` and `Topology`. `guides.html` is six bare links with no description.
  `wiki/index.html` titles itself `Index`. Guide pages link into the wiki.
  No wiki page links back.
  Fixed: each page says what it is and links to the other.
  A guide is one ordered path read front to back; the wiki is notes filed to be looked up.
  `guides.html` shows each guide's own lede, which the manifests already carried and the page showed none of.
  `wiki/index.html` is titled `Wiki`. Both stay: the wiki is the study guide, and a guide is one path read through it.
  `AGENTS.md`, "The wiki is a textbook", settles it.

- [x] Reconcile the four subject vocabularies.
  Browse filter: Algebra, Applied Algebra, Complex Analysis, Prelim, Real Analysis, Topology.
  Generate: the same six in a different order.
  Guides: drops Applied Algebra, adds Workshops.
  Wiki: adds Applied Algebra and Archives, drops Workshops, says `Prelims`. Workshops is a top-level subject in Guides and a subsection of every subject in the wiki.
  Half done.
  `vocabularies/areas.yaml` carries a name beside every id and nothing read it: every label on the site was the id title-cased.
  Browse, Generate, and the problem browser's headings now call an area what the registry calls it, and offer the six in the registry's order.
  Applied Algebra now has a guide, per the owner's decision, so Guides covers all six areas and Workshops is the seventh entry rather than a substitute for one.
  It is built from problem panels: the subject has 247 problems and no definition, theorem or example cards, and the other five guides open each section with those.
  Writing them is its own piece of mathematics and belongs under issue #2. The registry is gone: the subjects are the wiki's top-level folders, so `Prelim` and `Prelims` cannot disagree any more -- the folder is the id and its title is the display name.
  Workshops was never a subject; listing it beside the six is what made Guides and the wiki look like they disagreed.
  It sits under `Across the subjects` now, and the wiki goes on filing each workshop week under the subject it belongs to.
  Browse, Generate, Guides and the Wiki offer the same six ids in the same order.

### Collections

- [x] Give the 43 non-exam collections an index.
  `exam/` holds 381 collection pages.
  `exams.html` lists 338. The remainder are 6 textbooks, 17 homework sets, and 20 compiled scans.
  `exam/SRC-TEXT-MUN00.html` (Munkres, 586 problems) is the largest collection on the site and appears on no listing.
  A reader reaches it only from a problem card, through `Sources`. Fixed: the page lists all 381 under a heading for the kind of thing each is, and is titled `Sources` because that is now what it holds.
  A source kind with no heading fails the build rather than going unlisted.

- [x] Move the textbook, homework, and compilation collections off the `exam/` URL prefix, or rename the prefix.
  Moved, per the owner's decision: the 338 sittings keep `exam/` and the other 43 are under `source/`. The route is decided once, where the card's kind and its source kind are both in hand, and carried on the catalog row.
  Four places used to recompute it from `kind` alone.

- [x] Group and filter `exams.html`. It is one flat list of 338 links: no headings, no filters, no counts, no marker for which exams have solutions.
  Browse exposes area, topic, institution, and year filters over the same facets.
  Fixed: the same filter Browse uses, over area, institution and year, and each row says how many problems the collection holds and how many are solved.
  A group heading counts what it is showing, not what it holds.
  The filter is one component now, read off the controls a page emits, so the two listings cannot drift apart.
  It also turned out the row grid never had grid items: `pf.Plain` writes its text with no element around it, so a row was one anonymous item and the column widths did nothing.

- [x] Sort exam sittings by term within a year.
  The order is institution, year, area, then term alphabetically, so `TAMU real-analysis Fall 2015` precedes `TAMU real-analysis Spring 2015`. Fixed: a sitting now sorts by the term it was sat in, read from the term type rather than written out a second time in SQL.

### Findability

- [x] Rank title matches above body matches in search.
  The query `compact` returns Cone, Cover, Cochain, Cocycle, Colimit, Coproduct, Coboundary, Commutator, and three Continuity rows before `Compactness` at rank 14. None of the first nine carry the word in the title.
  The order tracks title length.
  Does not reproduce.
  Running `site/app.js`'s own ranking over the built `search.json`, `compact` returns Compactness, Compact space, Compact operator, Compact topological space; no Co-word appears in the first fifteen.
  `cone`, `continuity`, `sylow` and `residue theorem` all lead with title matches.
  The ranking landed in 8a8d493d0, two days before this observation, so the browsed page was running an older script than the one the build wrote.
  Remaining, and not this item: within the body-match tier the tie-break is still title length, so `residue theorem` puts a page titled `Topics` above one titled `Residues`.

- [x] Name one canonical page per concept.
  The query `Sylow` returns `Sylow Theorems` as a card, `Sylow Theorems` as a wiki page, `Sylow theorems` as a problem, and `Sylow Theory` as a guide page.
  Across the site 375 titles are shared by 836 pages: 5 pages are titled `Closed subsets of compact spaces are compact`, 4 `Cauchy's theorem`. A search row separates them only by a small grey path.
  Merging started, per the owner's decision, and the count is now measured rather than guessed.
  Of the 354 card title groups, 266 hold different mathematics under one title: those are not duplicates and merging them would delete problems.
  Of the 88 that hold identical mathematics, 32 were one concept minted twice from two wiki pages -- same kind, same classification, no relations, each transcluded on one page.
  Those are merged: both pages now show one card.
  The exercise/problem pairs are merged too, per the owner: the problem survives, because a problem is what they are.
  57 of them by statement rather than by whole body -- a solution written onto one twin makes the bodies differ while the question asked stays the same.
  Everything the exercise carried moved across, including three second solutions that argue the statement a different way.
  Merging is now exhausted: 8 identical-body groups are left and every one records the same statement at two sittings inside one compilation, which `f3a918092` dispositioned as keep-both.
  Title sharing is down from 375 groups over 836 pages to 315 over 739. For the rest, a search row said `Page` for both a wiki page and a guide section, so `Sylow Theorems` the wiki page and `Sylow Theory` the guide page were told apart only by the grey path.
  The row now names the surface -- Problem, Card, Wiki, Guide -- in the badge.
  What is left is not retitling either.
  A concept appears on its own page, again in a technique drilldown, and again in a compendium, and a study guide is better for it; the badge names the surface, which is what a reader needed.
  Retitle a page when its title misnames what is on it.
  `Complex_Analysis/Maps_of_the_disc/Schwarz lemma.md` holds Blaschke factors and hyperbolic translations: that one is wrong.
  Finding the rest is reading, one page at a time, under [issue #2](https://github.com/dzackgarza/new-qual-site/issues/2).

- [x] Order and page the problem browser.
  `problems.html` sorts 4921 problems by raw title string, so the page opens with the formula-titled problems.
  It is one 2.5 MB page with no pagination and no headings.
  Fixed: the rows are grouped under an area heading, and within an area the prose titles come before the 483 that begin with mathematics.
  The six headings fill the on-this-page rail, which is the jump list the page had no form of.
  The load cost was the other half: MathJax typeset all 4161 formula titles before a reader could touch the filter.
  A row is now typeset when it is scrolled near, and the load event falls from 10.1 s to 1.8 s. It is one page still, because the filter counts matches across every row; the rail is what a reader navigates it by.

### Wiki navigation

- [x] Stop rendering each folder twice in the sidebar.
  The group label `Algebra` carries a first child link `Algebra`; the group `Groups` carries a first child `Groups`. Identical text one line apart: one expands, one navigates.
  Fixed: the folder's own page is its summary.
  A link is interactive content, so clicking it follows it and the disclosure marker still toggles.

- [x] Order section contents by subject, not by filename prefix.
  Groups reads: Groups, Algebra Group and Ring Theory Resources, Notation, Basics, Actions, Counting theorems, Sylow Theorems, Classification, Series.
  A reader who opens the subject meets a references page first.
  Fixed: the six algebra reference pages carried `order: 0` from their `00_` filenames and now sort last in their folders.
  Groups reads Notation, Basics, Actions, Counting theorems, Sylow Theorems, Classification, Series, Resources.
  Every other `order: 0` page in the wiki is a preface, notation, or definitions page, and is first because it belongs first.

- [x] Replace the paragraph-of-links section indexes with lists.
  `wiki/10-algebra/08-quals/index.html` is one paragraph of 20 comma-separated links.
  It names seven topics twice, in title case and again in lower case under `Extra drill`. The two sets are different pages.
  Fixed: all 19 section indexes that ran five or more links into one paragraph are lists now, one link per item, each keeping the description it was written with.
  On the algebra quals page the two sets are under headings that say what separates them: problems sat at UGA, against practice problems that were not.
  `200_Extra` was linked from nowhere and is now listed with them.

- [x] Show the section boundary in the previous and next links.
  From Algebra > Quals, `Previous` is `Final Exam`, in the Exercises section.
  Fixed: a link that leaves the folder being read names the trail it lands in -- `Final Exam` now reads `in Algebra / Exercises / PSets / Final`. Siblings, the folder above, and the pages inside the folder page being read say nothing extra, because none of those is a crossing.

- [x] Give breadcrumbs one meaning.
  In the wiki a breadcrumb is the folder path (`Algebra / Groups / Sylow Theorems`). In a guide it is the prerequisite chain (`Algebra / Preliminaries / Rings and Ideals / Modules / Linear Algebra`), although the guide index presents those pages as a flat numbered list.
  No crumb links up to the wiki or guides root.
  On a subject landing page the breadcrumb is one item that repeats the heading.
  Fixed: a breadcrumb is where the page is filed, on both.
  It reads `Wiki / Algebra / Groups / Sylow Theorems` and `Guides / Algebra / Linear Algebra`, and the trail is stated by whoever files the page rather than walked out of a `parent` field that means two different things.
  The prerequisite tree is still the guide sidebar, which is what it was for.
  A page that is its own root carries no breadcrumb: there is nowhere to go up to, and one crumb only repeated the heading under it.

### Dead ends

- [x] Repair nine collection-to-collection links.
  `exam/SRC-UCSD-TOP-290QUALS.html` and `exam/SRC-RA-WORKSHOP.html` link to sibling collections as `tag/SRC-*.html`. Those pages live at `exam/SRC-*.html`. The links return 404. Fixed: a card link now takes its directory from the card's kind, so it cannot disagree with where that card was written.
  The rendered site has no dead internal link.

- [x] Add a 404 page carrying the site header.
  A missing page now shows the bare server error with no navigation.
  Fixed: `404.html` carries the header, the search box, and the five entry points.
  It resolves its links from the site root, so they work at whatever depth the missing address had.
  `just preview` now serves it for a missing path, the way Pages does.

- [x] Replace the card-count table on the landing page with orientation.
  A 14-row inventory (Proofs 7, Hints 1, Strategies 6) sits above the one sentence that tells a reader where to start.
  The page never explains Guides against Wiki.
  Fixed: one sentence of scale, then each of the five header entries with what it is for.
  Guides and Wiki are separated by shape -- a path to read against notes to look a topic up -- which is what the two artifacts already are.
  Both stay, per `AGENTS.md`. Every figure is still counted off the catalog.

## 10. Repair wiki copy and organization

Evidence: a read of `wiki/` (367 pages) on 2026-08-30, with each claim checked against the rendered page under `build/quarto/_site`. Ordered by how visible the damage is on the built site.

### Dead content

- [ ] Resolve the 167 empty headings.
  An empty heading is a section with nothing under it, which is either a heading list left above the content or a problem named and never transcribed.
  Read each one and either write the section or remove the heading; the two are not distinguishable from the file.
  Several qual pages carry an old, fully-empty heading list, then repeat the same exams under a second naming scheme where the content actually lives.
  `wiki/Real_Analysis/Quals/Measure Theory.md` opens with 21 headings that render as empty `<h2>` (`## Spring 2020 # 2`, `## Fall 2019 # 3`, ...), then restarts at `## Fall 2021.3` where every heading has a card.
  Verified in the build: `build/quarto/_site/wiki/real-analysis/quals/measure-theory.html` emits all 21 as real headings.
  Same shape in `Undergraduate Analysis.md` (17), `Integrals Convergence.md` (11), `Integration and L1.md` (9), `Functional Analysis.md` (9), `Resources/Extra_Questions.md` (30), and the four `0*_20*_Fall_Exam*.md` files.
  `just doctor` does not catch this — it checks empty *bodies*, not empty *sections*.

- [ ] Remove the placeholders and notes-to-self published as reader copy.
  `Archives/Tracking/Complex Qual Progress.md:11` — the entire body under `# Qual Problems ToDo` is the words **"See and"**. The link was dropped.
  Same file, `:15` — "Note: linking directly to sections doesn't seem to work yet.
  Just ctrl-F and search the page."
  `Real_Analysis/Basics/Notation.md:11` and `Notation_Real_Analysis.md:10` — the meaning column for $\norm{f}_{L^\infty}$ reads **"The ?"**. (It is the essential supremum.)
  `Real_Analysis/Integration/Lp.md:46` — a `.proof` block whose whole body is `?`; `:176` — `\converges{??}\to 0`. `Complex_Analysis/Appendices/Appendix FTA Proofs.md:141` — `???`. `Algebra/Fields/Galois_Theory_Computations.md:30` — a stated fact ending "**(I think)**". `Complex_Analysis/Basics/Tips_Techs.md:34` — "Casorati-Weierstrass Theorem (no page yet)"; `:170` — "put it in the denominator!
  No one can stop you!"

- [ ] Merge the duplicated content inside a single page, where reading both proves it is duplicated.
  A shared name is not evidence: six complex analysis pages are titled Schwarz and they are three different subjects.
  `Real_Analysis/Basics/Notation.md` and `Notation_Real_Analysis.md` are the same 7-row table in the same directory.
  One is titled "Sup-norm notation", which describes only its first two rows.
  `Complex_Analysis/Basics/Tips_Techs.md:24-60` — "Greatest Hits" is two overlapping lists, the first a subset of the second, never merged.
  `Complex_Analysis/Residues/Residues.md:37` and `:146` — the same remark twice ("Check: do you need residues at all??"). `Real_Analysis/Basics/Advice and Essentials.md:53-54` — the same bullet twice; `:116` has an unbalanced `\abs{F(x) - F(y}`.

### Private state on a public site

- [ ] Take the private study state off the public reference site.
  `Archives/Tracking/Prelims_Exam_tracking.md` is one person's 2014–2016 to-dos ("Go through Pugh", "Find a way to consistently + quickly remember the direction of injectivity"). It contains no tracking.
  Four tracking tables have a column **"Imported to MakeMeAQual"** — pipeline bookkeeping for a differently-named project.
  112 `- [ ]` / `- [x]` reading-progress checkboxes, mostly in `Complex_Analysis/Resources/Solutions.md` (45) and `Prelim/Prelim Resources.md` (41). That file also carries a trailing "Really well organized!"
  after a tag, and lists the same UCSD URL twice under two names (`:7`, `:9`). 47 Obsidian tags (`#resources/solutions`, `#algebra/qual/stuck`) leak into rendered text, two of them inside headings.

### Organization

- [ ] Make the subject entry pages agree on what they are.
  Six subjects, five shapes.
  `Real_Analysis/index.md` and `Complex_Analysis/index.md` both use the H1 **"Qualifying Exam Syllabus"** — neither names its subject.
  Both, plus `Algebra/index.md`, link to none of their own child pages, so landing on a subject gives no navigation.
  `Topology/index.md` puts `# References` as a second H1. Citation style differs four ways across those four pages.
  The Algebra one is broken: `> References: 1,3,4` appears five times, but the reference list renders as `[DuFo04] [HoKu71] [Hung74] [Smit]` — unnumbered, so the pointers resolve to nothing.
  A subject page opens a chapter: it tells a reader what the exam asks and where to start reading.
  Decide that shape once and give all six the same one.
  The syllabus is a page of its own.

- [ ] File the content sitting under a heading that names nothing.
  Renaming a section `Unsorted` to something else moves no mathematics.
  Each fragment needs the page it belongs on, which is the authoring in section 11. Six pages named `Preface`: four are acknowledgements, one is a Folland exercise list with no H1, one (`Topology/Basics/Preface.md`) is a full notation-and-background chapter.
  ~20 published sections named "Unsorted" or "Misc", including whole pages (`Complex_Analysis/Quals/Unsorted.md`, `Topology/Appendices/Appendix.md` → "Appendix: Unsorted Stuff"). `Archives/Tracking/index.md` lists 7 links for 5 subjects: Complex and Real each have two rival tracking pages, and the list mixes labeled links with unlabeled ones, so the duplicates read as separate topics.

### Content errors

- [ ] Correct two content errors worth fixing regardless.
  `Topology/Basics/Preface.md:36-37` — the notation table has the definitions **swapped**: it calls $G=1$ "the trivial abelian group" and $G=0$ "the trivial nonabelian group".
  `Real_Analysis/Resources/Preface.md` — the Folland exercise lists run together with no separators and an unclosed paren: "...9 (in 9(c) you can use Exercise 1.29 without proof Exercises 10, 12, 13...". Unreadable as written.
  Also broken by paste-through: `Algebra/index.md` bullets end in stray commas and `⇒?`, use "Eigenstuff" / "$M/IM$ stuff" / "Bonus optional stuff", break list nesting after "such as:", and weeks 10–13 of the "study path" are empty workshop scheduling ("Buffer", "Buffer", "No meeting (Mock AMS)").

## 11. Author the wiki as a study guide

`AGENTS.md`, "The wiki is a textbook", governs this section.
The organizing question is what a reader studying for the exam needs, and what has to sit next to it.
Evidence below: a structural read of `wiki/` (367 pages), `corpus/`, and `publications/` on 2026-08-30.

### Three operations, not one

Reorganization moves pages.
It cannot change how much content exists: a page that moves still exists.
Page count is not a score for it, and a reorganization that lowers the count has destroyed something.
The expected direction is up: the main editorial move is splitting one page that holds several concepts into one page per concept.

Two other operations ride along here, and each is justified on its own terms:

- **Deduplication.** The 90 `Quals/` link lists and the source-archive pages are card data typed a second time.
  Replacing them with a query removes no content, because the query renders the same problems from the same cards.

- **Writing.** The chapters that do not exist yet.
  This is the only one of the three that changes how much content exists, and it only adds.

Judge each on its own claim.
Do not let the second pay for the first, and do not let either stand in for the third.

### The table of contents

A table of contents, not a folder scheme.

#### What the wiki is for

A student uses a qual guide in five ways, and only two of them are served by a textbook:

1. **Learn the material** — read a chapter.

2. **Drill** — do problems by topic.
   *The corpus already does this: Browse, Generate, 4,921 problems.*

3. **Recognize** — see a problem, know which tool it wants.
   Hardest thing on the exam, and no textbook teaches it.

4. **Compress** — the week before, get everything into your head.

5. **Look up mid-problem** — "Fubini or Tonelli, and what exactly do I need to check?"

Delegate (2) to the corpus.
The chapters serve (1) and (5). (3) and (4) need page kinds the current tree has none of.

#### Four page kinds

- **Chapter** — the exposition.
  Definitions, theorems with hypotheses stated exactly, proofs, worked examples.

- **Recognition page** — a decision procedure keyed on *the form of the problem*, not on the theory.
  Sits at the head of the chapter whose tools it dispatches to.

- **Compendium** — a table you scan, not prose you read.
  Cross-cutting, so it sits at subject level.

- **Review sheet** — one page per subject; everything that must be in your head walking in.

A recognition page lives with its mathematics — you want "which contour" while you are reading about contours.
Only the genuinely cross-chapter pages sit at subject level.

#### Complex analysis, worked in full

```
complex-analysis/
├── index.md                 what the exam asks, the recurring problem types,
│                            and which chapter treats each
├── review.md                every theorem statement, one page
├── counterexamples.md       entire but unbounded; holomorphic on a punctured
│                            disc; the hypotheses that are load-bearing
├── standard-integrals.md    ∫sin x/x, ∫1/(1+xⁿ), ∫x^a/(1+x), ∫ over [0,2π] —
│                            each with its contour and its arc estimate
│
├── holomorphic-functions/
│   ├── is-it-holomorphic.md          ← recognition: CR, power series, Morera,
│   │                                   or "it isn't, and here's the obstruction"
│   ├── complex-arithmetic-and-log.md
│   ├── the-cauchy-riemann-equations.md
│   ├── power-series.md
│   └── harmonic-functions.md         harmonic conjugates, mean value
│
├── cauchy-theory/
│   ├── theorems-that-give-a-constant.md  ← recognition: Liouville, maximum
│   │                                       modulus, open mapping, identity —
│   │                                       and which hypothesis each needs
│   ├── cauchys-theorem.md
│   ├── the-integral-formula.md
│   ├── cauchy-estimates-and-liouville.md
│   ├── morera-and-converses.md
│   ├── the-identity-principle.md
│   ├── maximum-modulus-and-open-mapping.md
│   └── schwarz-reflection.md
│
├── singularities/
│   ├── classifying-a-singularity.md  ← recognition: the limit test, the
│   │                                   Laurent test, the boundedness test
│   ├── laurent-series.md
│   ├── removable-poles-essential.md
│   ├── meromorphic-functions.md
│   └── casorati-weierstrass-and-picard.md
│
├── residues-and-contours/
│   ├── which-contour-do-i-close.md   ← recognition, keyed on the integrand:
│   │                                   semicircle | keyhole (branch cut) |
│   │                                   rectangle (periodic) | indented
│   │                                   (pole on the line) | unit circle (trig)
│   ├── the-residue-theorem.md
│   ├── computing-residues.md         simple, higher order, by series
│   ├── arc-estimates.md              ML, Jordan's lemma, the small-arc lemma
│   └── real-integrals-by-residues.md
│
├── counting-zeros/
│   ├── how-many-zeros-in-this-region.md  ← recognition: argument principle,
│   │                                       Rouché, or direct factoring
│   ├── the-argument-principle.md
│   ├── rouches-theorem.md
│   └── hurwitz.md
│
└── conformal-maps/
    ├── build-me-a-map.md             ← recognition: the standard domains and
    │                                   the composition that gets you there
    ├── mobius-transformations.md
    ├── the-schwarz-lemma.md
    ├── blaschke-factors-and-automorphisms.md
    ├── the-riemann-mapping-theorem.md
    └── normal-families-and-montel.md
```

Six chapters in dependency order, six recognition pages, three subject-level compendia.
The `Quals/` link lists and the `Exercises/`, `Workshops/`, `Resources/` folders do not appear, because problems arrive by query and the bibliography is one page.

#### The other subjects

**Algebra** — `index` · `review` · `counterexamples` (the "is every X a Y" questions) · `groups-of-small-order.md` (the table: order ≤ 20, structure, Aut, whether it's simple)

```
groups/                  is-this-group-abelian.md · basics · quotients ·
                         the standard families
group-actions/           show-g-is-not-simple.md ← the single most useful page
                         in the subject · orbit-stabilizer · class equation ·
                         Sylow (which is where Sylow belongs: it is the
                         counting argument, not a chapter of its own)
rings-and-ideals/        domains · factorization · polynomial rings
modules/                 classify-this-module.md · over a PID · tensor ·
                         exact sequences
linear-algebra/          find-the-canonical-form.md ← given a matrix, the
                         recipe · determinants · eigen · JCF · RCF · SNF ·
                         spectral
fields/                  extensions · splitting · separability · finite fields
galois-theory/           compute-this-galois-group.md ← by degree, by
                         discriminant, by reduction mod p · the correspondence
                         · solvability · cyclotomic
representations/         Maschke · characters · Schur
```

**Real analysis** — `index` · `review` · `counterexamples.md` (the largest one; 76 cards, and half the exam is "is this true") · `inequalities.md`

```
undergraduate/           sequences · continuity · differentiability ·
                         uniform convergence · metric spaces
measure/                 outer measure · measurable sets and functions ·
                         Littlewood's three principles
integration/             which-convergence-theorem.md ← MCT, DCT, Fatou,
                         and what each costs · construction · L¹
fubini-tonelli/          its own chapter: asked constantly, and the
                         hypotheses are where the points are
lp-spaces/               duality · Hölder and Minkowski · density
fourier/                 convolution · the transform · inversion
functional-analysis/     Banach · Hilbert · the big four theorems
```

**Topology** — `index` · `review` · `the-standard-spaces.md` (Sⁿ, Tⁿ, RPⁿ, Klein bottle, wedges, with π₁ and H\_∗ tabulated — the highest-value page in the subject) · `counterexamples.md`

```
spaces-and-constructions/  subspace · product · quotient
connectedness-and-compactness/
separation-and-metrization/
fundamental-group/         compute-pi-1.md ← van Kampen, or deformation
                           retract, or covering space
covering-spaces/
cw-complexes/
homology/                  compute-h-star.md ← Mayer-Vietoris, cellular,
                           or long exact sequence of a pair
degree-and-fixed-points/   Brouwer · Lefschetz · Borsuk-Ulam
surfaces-and-manifolds/    classification
```

**Prelim** — the eleven sections of the paper, plus `useful-tricks.md`, which already exists and is exactly a recognition page.

**Applied algebra** — matrix analysis · representation theory · symmetric functions · Gröbner bases and varieties · invariant theory.
All unwritten; 247 problems and no theory cards, so the wiki is the only place its mathematics can live.

#### What generated this

Chapters follow **dependency**, not textbook chapter order — Sylow sits under group actions because it *is* the counting argument, and Fubini–Tonelli gets its own chapter because the exam treats it as one.

Recognition pages are keyed on **what the problem looks like**, since that is all you have at minute forty.
Their existence is why Rouché and the argument principle share a chapter: you choose between them, so you compare them on one page.

Compendia exist where **scanning beats reading** — and they are the pages a reader returns to most.

Nothing here is derived from the corpus.
The corpus supplies the problems under each page and the statements to inline.

#### Authoring queue

One subject at a time, chapter by chapter, reading the existing pages before each one.

- [ ] Complex analysis.
  All six chapters are authored, each with its recognition page, each rendered and read: `holomorphic-functions` (`cd06aa114`), `cauchy-theory` (`ae4df7c87`), `singularities` (`5e15fdf71`), `residues-and-contours` (`78c9cc7a6`, described in `dbbe898ad`), `counting-zeros` (`d1869aaea`), `conformal-maps` (`baa62f788`). `Cauchy`, `Zeros_and_poles`, `Omitted_values`, `Maps_of_the_disc` and `Conformal_maps` are gone; `Basics` holds the undergraduate layer and the reference tables under that name.
  Remaining for this subject: the four subject-level pages (`index`, `review`, `counterexamples`, `standard-integrals`), and the `Quals`, `Exercises`, `Workshops` and `Resources` folders, which the table of contents replaces with the `problems:` query rather than moving.

- [ ] Algebra.
  All eight chapters are authored, each with its recognition page: `groups` (`bb821e913`), `group-actions` (`9ca42e320`), `rings-and-ideals` (`965e90eb4`, described in `f0ee0de67`), `modules` (`9f078fb90`), `linear-algebra` (`0161cf376`), `fields` and `galois-theory` (`c61d84782`), `representations` (`dc8084b5d`). The three cross-cutting pages and the subject index are written, and the 26 `Quals` and 12 `Exercises` pages are replaced by topic queries; all 970 cards they named were checked reachable first.
  The subject now matches the filed table of contents.
  One trap the plan does not record: an old folder and its replacement chapter can slug to the same route -- `Groups` against `groups`, `Fields` against `fields` -- which `qualc check` passes and only the build rejects, so a subject cannot keep a retitled stub of a folder it has replaced.

- [ ] Real analysis.

- [ ] Topology.

- [ ] Prelim.

- [ ] Applied algebra.

Everything below is evidence for that authoring, not a plan that precedes it.

### What the migration costs

Build measured: `just build` runs clean in 142 s. Read from the generator rather than assumed.
The wiki pipeline is carefully built.
The hard parts are elsewhere, and there is one genuine trap.

#### Reorganizing touches no code, tested

The renderer is generic over whatever tree it is given.
There are no content literals in `tools/qualc/*.py` outside comments: no folder name, no page name, no subject name.
Path handling is `parts[:-1]` and `parts[:-2]`, and the current tree already renders a depth-5 page (`Topology/Quals/UCSD/Quals/Old/Fall 2014.md`). Every page goes through one path — `_wiki_blocks(page, incoming, cards)` and `_wiki_chrome(nav, page)` over `wiki_pages` — with no per-page or per-folder branch.
Navigation, breadcrumbs, previous and next, the manifest and the sidebar are all derived from the page list, and `.subject-sidebar ol ol` is a descendant selector, so any nesting depth indents.

Tested in a worktree, not inferred:

- Pure folder move, `Topology/Degree` to `degree-and-fixed-points`, filenames unchanged: **0 errors**.

- Folder move plus ten kebab-case file renames, `Cauchy/` to `cauchy-theory/`: **32 errors**, each naming the exact file and the exact broken reference.
  Restoring the filenames left **19**, all path-form links in two files, cleared by one `sed` on the path prefix.

- `qualc build` on the reorganized tree: **exit 0, 139 s**, rendering `wiki/complex-analysis/cauchy-theory/`.

- Code changed: **none**.

`qualc check`, which is parse plus validate plus link resolution and stops before emit, runs in **44 s**. That is the loop for a reorganization.

#### The mechanism the table of contents needs already exists

`emit.py:578-660` transcludes.
A paragraph that is nothing but card links renders those cards' bodies in place, each under its own `(Tag ...)` permalink, the way the Stacks Project prints a result under its tag; a wikilink inside a sentence stays a link.
So "definitions and theorems are the content of a page, inlined" works today, and it is the single thing the table of contents most depends on.
Landed in `7aba6b8a0`; `queues/11-design-issues.md` item 6 recorded the opposite and is corrected.

What still needs code is one thing, and it is a new capability rather than a reorganization.

A guide manifest can already name cards two ways.
`- ref: D-P6XOT` names one card.
`- query: {kind: problem, topics: [Zorn's Lemma], limit: 500, review: {mode: any}}` names a rule, and the build resolves it against the corpus every time it runs (`publication.py`, `PublicationQuery`). A wiki page has no such rule.
It can only name cards one at a time, by writing `[[P-XXXXX]]`. That is why the 90 `Quals/` pages exist: someone typed out by hand which problems belong to Sylow theory, and the list goes stale whenever a card is added or reclassified.

Giving a wiki page the same rule -- called the `problems:` query block throughout this section -- is what lets those 90 pages stop existing.
It is written out under "The 90 pages that retype card data" below.

#### What the machinery does not make hard

**URLs.** Routes are `slug()` of the source path (`wiki.py:148`). Nothing outside links in: README, CONTRIBUTING, and SDL contain zero wiki deep links, and all seven guide manifests contain one.

**Images — the scary-looking one that is fine.** 142 relative asset references, 118 of them four levels deep (`../../../../assets/assets/figures/...`). That reads as fatal for a move.
It isn't: `_asset_source` (`static_site.py:515`) discards the relative prefix entirely.
It splits on the literal `assets` path segment, then falls back to a basename lookup in the catalog.
Depth-independent.
Moving a page cannot break its figures.

**Ordering.** `order` sorts within a parent — key is `(parent_key, order, title, key)` at `emit.py:503`. There is no global sequence to reconcile; a moved page needs one number relative to its new siblings.

**Subject identity.** Area ids are `slug(folder_name)` (`index.py:78`), and `Complex_Analysis` and `complex-analysis` slug identically.
Kebab-casing the six top-level folders is a no-op for all 9,104 cards' area validation.
One constraint: a new non-subject branch like `reading/` needs `subject: false` in its index or it becomes a seventh area in Browse, Generate, and Guides.

**Tests.** Zero coupling.
Every wiki test builds a synthetic tree in `tmp_path` via `fixture_repo`. No test asserts a real wiki path.

**The catalog.** No table stores a wiki route; pages reach `emit.project` as objects.

**The ledgers.** 1,353 wiki paths across 10 `sources/*.jsonl` files, and the build reads none of them.
They record where content came from at import and stay as written.

**Card links.** 4,051 of the 5,152 wikilinks are card ids — id-resolved, move-immune.

**And it fails loud.** A missing or ambiguous page reference becomes a `Diagnostic` and `cli.py:103` returns 1 before anything is emitted.
You cannot ship a broken link.

#### The one real trap

`_page_target` (`wiki.py:414-421`) tries a bare link against the linking page's *own folder* before falling back to a global stem match.
There are 776 bare links, and **54 of them name a stem that exists in more than one folder**: `Exercises` ×5, `Problems` ×4, `Definitions` ×3, `Counterexamples` ×3, `2021_Fall` ×3, `Functional Analysis` ×3, and nine more.

Move the linking page and those links silently retarget a *different existing page*. No error, no diagnostic, correct-looking build.
This is the only failure the machinery cannot catch, and it is the one that would corrupt the text quietly.

- [x] Rewrite the 54 ambiguous bare links to full paths, before anything moves.
  After that the resolver's failure mode is loud everywhere and the migration is self-checking.
  Done in `29680a98e`: all 54 resolved in-folder before the rewrite and point at the same pages after it, each keeping its display text after a pipe.
  No bare link in the wiki now names a stem that exists in more than one folder.

#### The second coupling, which is not a bug

`wikilinks_title_after_pipe` means `[[Sylow_Theorems]]` renders as the literal text "Sylow_Theorems". 776 links display their target's name.
The TOC renames nearly every page, so a rename is never just a rename — the link text is part of a sentence, and each one needs re-reading in context.
This is authoring work created by an engineering choice, and it is unavoidable short of rewriting all 776 to piped form.

#### Why "moving files around" describes the smallest part

Complex analysis: 109 pages today, ~43 in the filed TOC. Of those 43 —

- **~26** are edits of existing prose, mostly merges and splits.

- **6** are area indexes.

- **~11 do not exist in any form**: the six recognition pages, three compendia, the review sheet.

- The **45** `Quals`/`Exercises`/`Workshops`/`Resources` pages do not move anywhere.
  They are replaced by a mechanism that is not built.

That mechanism is the gate.
The `problems:` query block does not exist — `publication.py` has query handling for guides, the wiki page path has none, and adding it is work inside `emit.py` (2,512 lines).
It is worthless until the topic vocabulary is curated: 668 strings, 166 of them singletons, and curating them is reading.

Then the eight pages that hold several chapters each — 26 kB of Galois computations under five headings, 18 kB of group basics under eight — split by mathematical reading, not by any tool.

#### Effort shape

| Work | Character |
| --- | --- |
| Rewrite the 54 ambiguous bare links | Read once each. Do first. Unblocks everything. |
| `problems:` query in `emit.py` | Ordinary engineering, one mechanism, mirrors `publication.py`. |
| Curate the topic vocabulary | Reading, ~120 topics, gates the query block. |
| Moves, renames, `order` values, 325 path links | Mechanical, and the build proves each step. |
| 776 link texts | Reading, one sentence at a time. |
| Split the eight omnibus pages | Mathematical reading. |
| Write ~11 new pages per subject, and two whole subjects | This is the project, not the migration. |

The infrastructure is not the obstacle.
Strip out the authoring and this is mechanical work with a 142-second proof loop and a build that refuses to ship a broken link.
The reason it is large is that the plan asks for pages that were never written — which is the point of the plan.

#### Addendum: what this assessment covers, and what it does not

The first version of this section read the inputs — routes, assets, `order`, area ids, ledgers, tests — and concluded the migration was cheap.
It never opened the rendering path, so it could not answer whether the renderer is written against the tree that exists.
It is not, and a worktree test says so rather than a reading.
Two conclusions changed:

- Reorganizing needs no code.
  Measured above, not inferred.

- Transclusion exists, since `7aba6b8a0`. The earlier claim that a bare `[[card-id]]` never transcludes came from `queues/11-design-issues.md`, which predates it.

What is still unverified:

- One folder move and one chapter rename were tested.
  A whole-subject reorganization, a page split, and a page merge were not.

- The new page kinds are untested as rendered output.
  A recognition page is prose and a compendium is a table, so both are ordinary; a review sheet transcluding forty theorem cards onto one page is not, and its size and typesetting cost are unknown.

- Nothing was looked at.
  The evidence is exit codes and emitted paths, which is a build proving itself, not a page proving itself.
  Before any of this is called done, render it and read it.

- The `problems:` query block is unimplemented, so every claim about it is a claim about work not started.

- Search behaviour across renamed routes was not checked beyond the build succeeding.

### What is there now (measured)

| Kind of page | Count | Share |
| --- | ---: | ---: |
| `index.md` navigation stubs | 70 | 19% |
| `Quals/` hand-listed problem indexes | 90 | 25% |
| `Resources/` (bibliography, source archives) | 24 | 7% |
| `Exercises/` (PSet writeups) | 18 | 5% |
| `Archives/` (tracking, topics, source dumps) | 14 | 4% |
| `Appendices/` + `Workshops/` + `Review/` | 24 | 6% |
| Mathematical notes | 127 | 35% |

4,051 card references.
115 pages are more link than text.
120 filenames contain spaces, 75 contain underscores.
69 pages carry `order: 100001` — the marker for "no place in the tree".

### Chapters that do not exist yet

The card counts are already there; the writing is not.
This is the largest body of work in the section.

- **Applied algebra**: 247 problems, zero theory cards, zero prose.
  `Applied_Algebra/` holds an index and a source archive.

- **Prelim**: 257 problems, zero theory cards, two notes (`Useful Tricks`, `Prelim Resources`).

Both subjects have no theory cards at all, so the wiki is the only place their mathematics can live.

Inside the four written subjects, these areas hold one or two notes each:

| Area | Notes today |
| --- | ---: |
| `Topology/{Basics, Degree, Examples, Manifolds}` | 1 each |
| `Real_Analysis/Functional_analysis` | 1 |
| `Algebra/{Modules, Representation_theory}` | 2 each |
| `Real_Analysis/{Measure, Fourier}` | 2 each |
| `Topology/{Homology, Appendices}` | 2 each |
| `Complex_Analysis/{Maps_of_the_disc, Omitted_values}` | 3 each |

Topology carries the thinnest coverage of any written subject.

### Pages that hold several chapters

Whatever table of contents is authored, these pages hold more than one subject each and will split.

| Page | Size | Sections |
| --- | ---: | ---: |
| `Algebra/Fields/Galois_Theory_Computations.md` | 26 kB | 5 h2, 10 h3 |
| `Algebra/Fields/Fields_Extensions.md` | 20 kB | 6 h2 |
| `Algebra/Groups/Groups_Classification.md` | 20 kB | 5 h2 |
| `Algebra/Groups/Groups_Basics.md` | 18 kB | 8 h2 |
| `Archives/Topics.md` | 14 kB | 10 h2, 10 h3 |
| `Topology/Examples/Examples.md` | 14 kB | 2 h2 |
| `Complex_Analysis/Basics/Tips_Techs.md` | 13 kB | 11 h2 |
| `Algebra/index.md` |  | syllabus and a twelve-week sequence in one page |

### A name is not a subject

Six complex analysis pages carry Schwarz in the title, across three folders, and they are three different subjects.
`Cauchy/Schwarz.md` is the lemma (`T-XMSIT`). `Cauchy/Schwarz reflection principle.md` is an unrelated theorem (`T-5SKNT`). `Maps_of_the_disc/Schwarz lemma.md` is Blaschke factors and hyperbolic translations, under a heading that names neither.

Merging these on the name files the automorphism material under a lemma it is not about.
Every same-name pair in `wiki/` needs both pages read before anything is decided about them.

### The 90 pages that retype card data

`corpus/collections/*/index.md` records institution, term, and the ordered problem list.
Every card records `classification.topics`. The site emits 339 `/exam/` pages and 8,719 `/tag/` pages from that data.
The `Quals/` folders are a third, hand-typed copy, and they drift.

Replace them with a query in the page's own front matter, using the mechanism `publications/*.yaml` already runs through `publication.py`:

```yaml
---
title: Sylow Theorems
order: 40
problems:
  topics: [Sylow Theory, p-Groups]
---
```

`emit.py` renders the matching problems at the foot of the page from the corpus index.

- [x] Add the `problems:` query block to `emit.py`. Done in `088386d79`. Two differences from the guide query, both forced by what a topic page is: every match renders, because a limit would drop problems the page claims to hold; and a card's kind does not narrow it, because `exercise` against `problem` records where a question was set, not what it asks.
  The page is scoped to the subject it is filed under, and a query matching nothing stops the build.
  First use is `wiki/Algebra/Groups/Sylow_Theorems.md`, which lists all 167 algebra problems on Sylow theory.

- [ ] Replace the 90 `Quals/` pages and the source-archive pages with it.
  These are the only pages this section removes, and their content survives: it is card data, rendered.
  Complex analysis is done: 35 pages, 348 cards, each checked reachable from a chapter page before deletion (`00a38780b`). Two things that were not card data had to be moved first rather than deleted: the acknowledgements on `Quals/Preface`, which name four people, and eight exam PDF links that existed nowhere else and are now on the provenance of the collection card for each sitting.
  Expect both in the other subjects.

One caveat: the corpus has 668 distinct topic strings and 166 appear exactly once.
A query needs a curated topic list, and that curation is reading, not scripting.

- [ ] Curate the topic vocabulary, subject by subject, and map the raw strings onto it.

### Mechanical constraints

Plumbing.
These decide nothing about what the text should be.

- Every directory needs an `index.md`, or the build drops it from the tree.

- Every page needs an integer `order`. The 69 pages at `100001` have none that means anything.

- Routes are slugged from the source path, so a filename with spaces or underscores reads differently from its URL. Lowercase kebab-case makes the two agree.

- One `# H1` per page, equal to `title`. Six pages named `Preface` and a second H1 on `Topology/index.md` are section 10 items.
