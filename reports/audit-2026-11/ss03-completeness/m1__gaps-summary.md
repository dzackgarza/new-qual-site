# SRC-TEXT-SS03 — gap summary (member m1)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR text
layer by ocrmypdf 11.0.1 / Tesseract 4.1.1). **PDF page = printed page + 19** for the whole body
(printed 1–379 = PDF 20–398); verified on all 362 body pages that print a folio, with no
exception — see `source-integrity.md`.

## Totals

| chapter | Exercises printed | EX cards | Problems printed | PR cards | missing items |
|---|---|---|---|---|---|
| 1 | 1–26 (p. 24–31) | 26 | — (none printed) | — | **0** |
| 2 | 1–15 (p. 64–67) | 15 | 1–5 (p. 67–70) | 5 | **0** |
| 3 | 1–22 (p. 103–107) | 22 | 1–5 (p. 108–110) | 2 | **3** → `gaps-ch3.md` |
| 4 | 1–12 (p. 127–130) | 12 | 1–4 (p. 131–133) | 4 | **0** |
| 5 | 1–17 (p. 153–156) | 17 | 1–4 (p. 156–158) | 4 | **0** |
| 6 | 1–17 (p. 174–179) | 17 | 1–4 (p. 179–180) | 4 | **0** |
| 7 | 1–12 (p. 199–203) | 12 | 1–4 (p. 203–204) | 4 | **0** |
| 8 | 1–24 (p. 248–254) | 24 | 1–9 (p. 254–260) | 9 | **0** |
| 9 | 1–8 (p. 278–280) | 8 | 1–4 (p. 281–282) | 3 | **1** → `gaps-ch9.md` |
| 10 | 1–12 (p. 309–313) | 12 | 1–6 (p. 314–317) | 6 | **0** |
| Appendix A | — (none printed) | — | 1–5 (p. 341–343) | 0 (no dir) | **5** → `gaps-appendixA.md` |
| Appendix B | — | — | — | — | **0** (prints neither) |
| **total** | **165** | 165 | **50** | 45 printed-item cards | **9** |

Printed items 215, cards 206: 215 − 206 = 9 = the nine missing items listed above.

## The nine missing items

**Status note.** This list is the state at census time (~16:10). Four of the nine were created by
another worker at 16:18:20 during this audit (`E-SS3.PR-3/4/5`, `E-SS9.PR-4`, all untracked in
git); I did not write them and did not touch them, and their `.exercise` blocks do match the
printed items. **Still missing at the time of writing: the five Appendix A problems** (items 5–9
below). None of the four new cards records the printed asterisk.

1. `ch3-problems/E-SS3.PR-3.md` — Ch. 3 Problem 3, PDF p. 128 (p. 109): the Laurent expansion on an annulus.
2. `ch3-problems/E-SS3.PR-4.md` — Ch. 3 Problem 4\*, PDF p. 129 (p. 110): bounded region cut by a line, simple connectivity.
3. `ch3-problems/E-SS3.PR-5.md` — Ch. 3 Problem 5\*, PDF p. 129 (p. 110): jump formula for `g(z) = (1/2πi)∫ h(x)/(x−z) dx`.
4. `ch9-problems/E-SS9.PR-4.md` — Ch. 9 Problem 4\*, PDF pp. 300–301 (pp. 281–282): `℘` real on the half-lattice lines, conformal on rectangles.
5. `ch-appA-problems/E-SSappA.PR-1.md` — Appendix A Problem 1, PDF pp. 360–361 (pp. 341–342): Watson-type asymptotic expansion.
6. `ch-appA-problems/E-SSappA.PR-2.md` — Appendix A Problem 2, PDF p. 361 (p. 342): sharper Stirling series.
7. `ch-appA-problems/E-SSappA.PR-3.md` — Appendix A Problem 3, PDF p. 361 (p. 342): Bessel/Airy series, two parts + hint.
8. `ch-appA-problems/E-SSappA.PR-4.md` — Appendix A Problem 4, PDF pp. 361–362 (pp. 342–343): partial-fraction asymptotic `F_n`.
9. `ch-appA-problems/E-SSappA.PR-5.md` — Appendix A Problem 5\*, PDF p. 362 (p. 343): Rademacher-type exact formula.

Full quotes with page numbers are in `gaps-ch3.md`, `gaps-ch9.md`, `gaps-appendixA.md`. Directory
names for the Appendix cards are a proposal; there is no Appendix directory today.

## Answers to the questions the task raised

* **Is there a Chapter 5 Exercise 19?** No. The section is `6 Exercises`, PDF 172–174 (pp. 153–156),
  items **1–17**; item 17 is the Pringsheim interpolation formula and `7 Problems` begins on PDF 175.
* **Does Chapter 8 have problems beyond 9?** No. `6 Problems`, PDF 273–279 (pp. 254–260), items
  **1–9** (3\*, 4\*, 6\*, 7\*, 8\*, 9\*), ending on p. 260 with the Gauss elliptic-integral problem.
* **How many problems does Chapter 10 print?** **6**, PDF 333–336 (pp. 314–317): 1\*–6\*, with 5\*
  and 6\* on p. 316–317. The corpus has all six.
* **Are the suspected chapters 2, 4, 7, 9 gap-free?** Chapters 2, 4 and 7 yes (Problem 5 of Ch. 2,
  Problem 3–4 of Ch. 4, Problems 2–4 of Ch. 7 are all present). Chapter 9 is missing Problem 4.

## The inventory in the task brief is itself out of date

Re-derived from disk (`ls` of `corpus/collections/SRC-TEXT-SS03/`), the collection had **19
directories and 206 cards** at census time (210 after the four concurrent additions noted above),
not the eight dirs the brief lists:

`ch1-exercises` 1–26; `ch2-exercises` 1–15, `ch2-problems` 1–5; `ch3-exercises` 1–22,
`ch3-problems` 1–2; `ch4-exercises` 1–12, `ch4-problems` 1–4; `ch5-exercises` 1–17,
`ch5-problems` 1–4; `ch6-exercises` 1–17, `ch6-problems` 1–4; `ch7-exercises` 1–12,
`ch7-problems` 1–4; `ch8-exercises` 1–24, `ch8-problems` 1–9; `ch9-exercises` 1–8,
`ch9-problems` 1–3; `ch10-exercises` 1–12, `ch10-problems` 1–6.

So chapters 1, 3 and 6, and the exercises of chapters 2, 4, 9 and 10, do have cards; the brief's
list omits them. `index.md` declares `completion: complete`, which is wrong in three places
(Ch. 3 problems, Ch. 9 problems, Appendix A), and neither `index.md` nor any card records the
printed stars except one prose note in `ch2-problems/E-SS2.PR-5.md`.

## Scope — what I verified and what I did not

Verified at item level (numbers, section boundaries, presence/absence of a card):

* All ten chapters' **Exercises** sections (165 items) and all ten chapters' **Problems** sections
  (45 items) — every printed item number was matched against the card files.
* **Appendix A Problems** (5 items, no cards) and a heading scan of **Appendix B** (no Exercises or
  Problems section) and of the front/back matter (none there).
* Item sequences are contiguous 1..N in every section, so no numeral was lost to OCR; 26 internal
  book cross-references ("Problem 5 in Chapter 3", etc.) are all consistent with these maxima.

Not checked (state of the evidence):

* **No page-image verification.** Everything rests on the PDF's OCR text layer; I did not rasterise
  pages, so a symbol-level reading (sign, exponent, subscript) is unverified beyond the OCR.
* **Statement fidelity only where it was cheap**: one mechanical check over all 206 cards — does a
  card keep the printed `[Hint: …]`? **14 cards drop a printed hint**, listed with page and quote in
  `fidelity-hints.md` (Ch. 1 EX-15, 16, 18, 21; Ch. 4 PR-3; Ch. 7 EX-8, EX-10; Ch. 8 EX-13, PR-4,
  PR-7, PR-9; Ch. 9 PR-3; Ch. 10 PR-5, PR-6). Every other hint-bearing item kept its hint, and no
  card invents one. Beyond hints I compared no card text to the printed text — dropped hypotheses,
  wrong signs and wrong exponents in the other 192 cards are **not** covered by this report.
* **No proof audit.** I did not read any `.solution` block.
* **No check of other collections** in `corpus/collections/`, and no check of the repo's build,
  schema validation or CI for these cards.
* Chapter body text (as opposed to the Exercises/Problems sections) was read only where needed for
  pagination and for the two starred-item checks.
