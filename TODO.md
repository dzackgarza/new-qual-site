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

- [ ] Make source pages and emitted routes set-equal.

- [ ] Retain all authored prose and references.

- [ ] Validate every emitted fragment.

- [ ] Inspect the real pages for remaining publisher defects.

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

- [ ] Make the reader and generator use the same complete catalog.

- [ ] Compare browser and generator problem sets with that catalog.

- [ ] Exercise each supported facet and combined filter.

- [ ] Inspect a statements-only generated exam.

- [ ] Inspect a diagram, citation, collection link, hint, and solution.

- [ ] Decide the supported `tikzcd` boundary.

- [ ] Decide whether facets need separate typed controls.

### Repair rendered-page residue

Owner: [issue #41](https://github.com/dzackgarza/new-qual-site/issues/41)

- [ ] Reproduce each remaining rendered-page defect.

- [ ] Repair one defect at a time.

- [ ] Render and inspect the affected page after each repair.

### Prove the deployed site

Owner: [issue #30](https://github.com/dzackgarza/new-qual-site/issues/30)

- [ ] Verify the route and catalog manifests.

- [ ] Visit every subject branch root and terminal route.

- [ ] Exercise search, filters, disclosures, diagrams, citations, and generation.

- [ ] Inspect widths of 375, 768, 1024, and 1440 CSS pixels.

- [ ] Inspect browser console and network results.

- [ ] Confirm that local and deployed artifacts use the same revision.

- [ ] Record every unexercised path and nonclaim.

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

- [ ] Decide whether collection and problem pages satisfy reachability for every problem.

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

- [ ] State the difference between Guides and Wiki on both landing pages.
  The header offers both.
  Both organise the same subjects.
  Both hold pages titled `Algebra` and `Topology`. `guides.html` is six bare links with no description.
  `wiki/index.html` titles itself `Index`. Guide pages link into the wiki.
  No wiki page links back.

- [ ] Reconcile the four subject vocabularies.
  Browse filter: Algebra, Applied Algebra, Complex Analysis, Prelim, Real Analysis, Topology.
  Generate: the same six in a different order.
  Guides: drops Applied Algebra, adds Workshops.
  Wiki: adds Applied Algebra and Archives, drops Workshops, says `Prelims`. Workshops is a top-level subject in Guides and a subsection of every subject in the wiki.

### Collections

- [x] Give the 43 non-exam collections an index.
  `exam/` holds 381 collection pages.
  `exams.html` lists 338. The remainder are 6 textbooks, 17 homework sets, and 20 compiled scans.
  `exam/SRC-TEXT-MUN00.html` (Munkres, 586 problems) is the largest collection on the site and appears on no listing.
  A reader reaches it only from a problem card, through `Sources`. Fixed: the page lists all 381 under a heading for the kind of thing each is, and is titled `Sources` because that is now what it holds.
  A source kind with no heading fails the build rather than going unlisted.

- [ ] Move the textbook, homework, and compilation collections off the `exam/` URL prefix, or rename the prefix.

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

- [ ] Name one canonical page per concept.
  The query `Sylow` returns `Sylow Theorems` as a card, `Sylow Theorems` as a wiki page, `Sylow theorems` as a problem, and `Sylow Theory` as a guide page.
  Across the site 375 titles are shared by 836 pages: 5 pages are titled `Closed subsets of compact spaces are compact`, 4 `Cauchy's theorem`. A search row separates them only by a small grey path.

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

- [ ] Give breadcrumbs one meaning.
  In the wiki a breadcrumb is the folder path (`Algebra / Groups / Sylow Theorems`). In a guide it is the prerequisite chain (`Algebra / Preliminaries / Rings and Ideals / Modules / Linear Algebra`), although the guide index presents those pages as a flat numbered list.
  No crumb links up to the wiki or guides root.
  On a subject landing page the breadcrumb is one item that repeats the heading.

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
  Whether the site should carry both remains open above.
  Every figure is still counted off the catalog.
