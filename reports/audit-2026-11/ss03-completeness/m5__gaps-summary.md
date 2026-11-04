# Completeness audit of `SRC-TEXT-SS03` (Stein–Shakarchi, *Complex Analysis*)

**Result: 215 exercises/problems are printed in the book; 206 cards exist; 9 printed items have no card.**
The nine are in three places: chapter 3 Problems 3, 4, 5; chapter 9 Problem 4; and the whole of
Appendix A's Problems section, 1–5 (the corpus has no appendix directory at all).

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, 398 pages with a Tesseract
OCR text layer (`pdftotext` of the whole file, plain and `-layout`). Every page citation below gives the
PDF page and, in parentheses, the printed page. On every page this audit used, **PDF page = printed page + 19**
(checked against the running heads, e.g. PDF p. 44 carries "4. Exercises 25", PDF p. 279 carries "260").

## Per-section counts

| chapter | printed section (heading page) | printed items | cards on disk | missing |
|---|---|---|---|---|
| 1 | 4 Exercises (p. 24) | 26 | 26 | 0 |
| 2 | 6 Exercises (p. 64) | 15 | 15 | 0 |
| 2 | 7 Problems (p. 67) | 5 | 5 | 0 |
| 3 | 8 Exercises (p. 103) | 22 | 22 | 0 |
| 3 | 9 Problems (p. 108) | **5** | **2** | **3** (PR-3, PR-4, PR-5) |
| 4 | 4 Exercises (p. 127) | 12 | 12 | 0 |
| 4 | 5 Problems (p. 131) | 4 | 4 | 0 |
| 5 | 6 Exercises (p. 153) | 17 | 17 | 0 |
| 5 | 7 Problems (p. 156) | 4 | 4 | 0 |
| 6 | 3 Exercises (p. 174) | 17 | 17 | 0 |
| 6 | 4 Problems (p. 179) | 4 | 4 | 0 |
| 7 | 3 Exercises (p. 199) | 12 | 12 | 0 |
| 7 | 4 Problems (p. 203) | 4 | 4 | 0 |
| 8 | 5 Exercises (p. 248) | 24 | 24 | 0 |
| 8 | 6 Problems (p. 254) | 9 | 9 | 0 |
| 9 | 3 Exercises (p. 278) | 8 | 8 | 0 |
| 9 | 4 Problems (p. 281) | **4** | **3** | **1** (PR-4) |
| 10 | 4 Exercises (p. 309) | 12 | 12 | 0 |
| 10 | 5 Problems (p. 314) | 6 | 6 | 0 |
| App A | 5 Problems (p. 341) | **5** | **0** | **5** (PR-1 … PR-5) |
| App B | — (no Exercises, no Problems) | 0 | 0 | 0 |
| **total** | 20 sections | **215** | **206** | **9** |

Per-chapter totals (printed / cards / missing): ch1 26/26/0, ch2 20/20/0, ch3 27/24/**3**,
ch4 16/16/0, ch5 21/21/0, ch6 21/21/0, ch7 16/16/0, ch8 33/33/0, ch9 12/11/**1**,
ch10 18/18/0, App A 5/0/**5**.

Per-chapter detail, with the printed statements quoted, is in `gaps-ch1.md` … `gaps-ch10.md` and
`gaps-appendix-a.md`.

## The three named suspicions, settled

- **Is there a chapter 5 exercise 19?** No. Chapter 5 prints Exercises 1–17 (heading printed p. 153; item 15
  on printed p. 155, items 16 and 17 on printed p. 156, immediately above the "7 Problems" heading) and
  Problems 1–4 (printed pp. 156–158). The corpus's 17 chapter-5 exercise cards are complete; chapter 5 has no gap.
- **Does chapter 8 have problems beyond 9?** No. Chapter 8 prints Problems 1–9: the "6 Problems" heading is on
  printed p. 254, Problem 9 (Gauss, arithmetic–geometric mean) runs to the bottom of printed p. 260
  (PDF p. 279, closing sentence "…the relation (6) is a consequence of the identity in (b) of Exercise 24"),
  and chapter 9 opens on printed p. 261 (PDF p. 280). Chapter 8 is complete: 24 exercises + 9 problems.
- **How many problems does chapter 10 print?** Six, Problems 1–6 (heading printed p. 314, last item on printed
  p. 317 = PDF p. 336, ending with the `E4*` transformation laws before Appendix A opens on printed p. 318).
  The corpus's six chapter-10 problem cards are complete.

## Inventory re-derived (the brief's list is out of date)

The task brief listed 8 directories holding 68 cards. The tree actually holds **19 card directories and
206 cards**: `ch1-exercises` (26), `ch2-exercises` (15), `ch2-problems` (5), `ch3-exercises` (22),
`ch3-problems` (2), `ch4-exercises` (12), `ch4-problems` (4), `ch5-exercises` (17), `ch5-problems` (4),
`ch6-exercises` (17), `ch6-problems` (4), `ch7-exercises` (12), `ch7-problems` (4), `ch8-exercises` (24),
`ch8-problems` (9), `ch9-exercises` (8), `ch9-problems` (3), `ch10-exercises` (12), `ch10-problems` (6).
`index.md` claims `completion: complete` and lists exactly those 206 ids in 19 sections, stopping at
"Ch10 Problems" — so the collection manifest itself carries the same two holes (ch3 Problems 3–5,
ch9 Problem 4) and has no Appendix A section.

## How the count was established (not by trusting the corpus)

1. One dump of the PDF: `pdftotext -layout` (398 pages, 906 KB of text).
2. Every `Exercises`/`Problems` section heading was located in the text layer by its section number
   (e.g. "9 Problems" on PDF p. 127). There are exactly 20 such headings; the table of contents
   (PDF pp. 12–15) lists the same 20, and the typeset contents of an independent copy of the book
   (PDF hosted at `unina2.on-line.it`) lists them identically, including "Appendix A … 5 Problems 341".
3. Inside each section, item-start lines were collected with their page, and the printed numbers were checked
   to run contiguously 1, 2, 3, … with no gap and no repeat. A missing number would have shown as a break in
   the sequence; there is none in any of the 20 sections.
4. Because a *trailing* item could in principle be missed if its number line were unreadable, the last page of
   every section was read in full, to see the closing words of the final item and the next chapter's opening on
   the following page. Those closing printed pages are: ch1 p. 31; ch2 Exercises p. 67, Problems p. 70;
   ch3 Exercises p. 108, Problems p. 110; ch4 Exercises p. 131, Problems p. 133; ch5 Exercises p. 156,
   Problems p. 158; ch6 Exercises p. 179, Problems p. 180; ch7 Exercises p. 203, Problems p. 204;
   ch8 Exercises p. 254, Problems p. 260; ch9 Exercises p. 280, Problems p. 282; ch10 Exercises p. 313,
   Problems p. 317; App A Problems p. 343.
5. The resulting number sets were diffed against the card filenames on disk.

## Independent corroboration from inside the same PDF

The book's own *Notes and References* cite problems by number, which confirms counts independently of my
reading of the item lists: for Chapter 3, "see Muskhelishvili [25] for more about the Cauchy integral
introduced in **Problem 5**" (printed p. 365) — so chapter 3 has five Problems, and the missing PR-5 is a
real gap; for Chapter 9, "**Problems 2, 3, and 4** are in Saks and Zygmund" (printed p. 366) — so chapter 9
has four Problems, and PR-4 is a real gap. Others that match the corpus: ch2 Problem 5 (p. 365), ch4 Problem 4,
ch6 Problems 2–4, ch7 Problems 2–4, ch8 Problems 6 and 7 (p. 366), ch10 Problems 1 and 6 (p. 366).

## Fidelity (job 2, only where cheap) — see `fidelity-spotcheck.md`

- Every one of the 206 cards corresponds to a printed item at the same number, and no card exists for a
  number the book does not print (printed maxima: ch1 26; ch2 15/5; ch3 22/5; ch4 12/4; ch5 17/4;
  ch6 17/4; ch7 12/4; ch8 24/9; ch9 8/4; ch10 12/6).
- 18 cards were compared against the print line by line (the ones whose vocabulary overlapped the printed
  item least, plus every hint-loss candidate); all 18 hold the statement of the printed item at their number —
  no misnumbering found.
- Five printed bracketed hints are missing from the cards that exist: `E-SS1.EX-15`, `E-SS1.EX-16`,
  `E-SS1.EX-18`, `E-SS1.EX-21`, `E-SS8.EX-13`. Printed hints quoted in `fidelity-spotcheck.md`.
- The asterisk the book uses to mark its hardest problems (preface, printed p. viii) is not recorded on
  23 of the 24 existing cards whose problem is starred; only `E-SS2.PR-5` mentions it.

## What was NOT checked (scope statement)

- **No proofs or solutions were audited** — out of scope for this task by instruction.
- Word-level fidelity was **not** verified for the remaining ~188 cards. For those, the statement was checked
  only mechanically: that an `{.exercise}` block exists, that its number matches a printed number, and whether
  it carries a hint/asterisk. Part-by-part ((a)/(b)/(c)) completeness across the corpus was not systematically
  checked.
- Card frontmatter (page references, `audit:` notes, section labels, titles, `kind:`) was not audited.
- Exercise figures ("Figure 14. The contour in Exercise 1", printed p. 64) were not checked for presence in a card.
- No page images were viewed: formulas are as the OCR gives them, and I did not verify the OCR against the
  print for any formula. Statements quoted in the gap files are quoted from the OCR and marked as such.
- A *sub*-item the book prints without its own number (a lettered part, say) could be missing from a card
  without showing up in any count in this audit.
- I did not sweep all of *Notes and References*; I used it only where it bears on a count above.
- **Nothing under `corpus/` was modified**; the nine additions are left for a human to apply.
