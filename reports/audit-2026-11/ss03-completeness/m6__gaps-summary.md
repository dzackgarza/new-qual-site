# SS03 (Stein–Shakarchi, *Complex Analysis*) — completeness audit: summary

Companion files: `inventory-derived.md` (how the inventory and the printed counts were
re-derived), `gaps-ch1.md` … `gaps-ch10.md`, `gaps-appendixA.md`, `gaps-appendixB.md`,
`fidelity-spotcheck.md`. Nothing under `corpus/` was touched.

Page numbers are **PDF page indices**; the printed folio is in parentheses
(body of the book: PDF page = printed folio + 19).

## Status when these files were written

The audit was run against the working tree as it stood at the start of the run; the nine items
below were **absent** then and these files describe them as gaps. While the audit was being
written, another pass applied the additions: `git status` now shows
`ch3-problems/E-SS3.PR-3.md`, `E-SS3.PR-4.md`, `E-SS3.PR-5.md`, `ch9-problems/E-SS9.PR-4.md`
and `appendix-a-problems/E-SSA.PR-1.md` … `E-SSA.PR-5.md` as new files, plus 20 added lines in
`index.md`. I re-read those nine cards against the printed items (token overlap with the print:
0.58–1.00, the 0.58 being the OCR-scrambled Appendix A Problem 4) and their statements match
the quotations below; in particular E-SS3.PR-3 restores the correct
`a_{-k}/(z−z_0)^k + ⋯ + a_{-1}/(z−z_0) + g(z)` display, and both printed hints of Chapter 3
Problem 5 are present. So the collection is, as of that pass, complete against the 215 printed
items. Everything else in this report stands: the counts, the page citations and the
fidelity findings.

## Result

The book prints **215** items in 20 chapter-end sections (165 exercises + 50 problems,
the last 5 of them in Appendix A). The collection holds **206** cards. **9 printed items have
no card**, and one whole section (Appendix A) has no card directory:

| # | chapter | item | PDF page (folio) | target card |
|---|---|---|---|---|
| 1 | Ch3 | Problem 3 | 128–129 (109–110) | `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md` |
| 2 | Ch3 | Problem 4 (∗) | 129 (110) | `…/ch3-problems/E-SS3.PR-4.md` |
| 3 | Ch3 | Problem 5 (∗) | 129 (110) | `…/ch3-problems/E-SS3.PR-5.md` |
| 4 | Ch9 | Problem 4 (∗) | 301 (282) | `…/ch9-problems/E-SS9.PR-4.md` |
| 5 | App A | Problem 1 | 360–361 (341–342) | `…/appA-problems/E-SSA.PR-1.md` |
| 6 | App A | Problem 2 | 361 (342) | `…/appA-problems/E-SSA.PR-2.md` |
| 7 | App A | Problem 3 | 361 (342) | `…/appA-problems/E-SSA.PR-3.md` |
| 8 | App A | Problem 4 | 361–362 (342–343) | `…/appA-problems/E-SSA.PR-4.md` |
| 9 | App A | Problem 5 (∗) | 362 (343) | `…/appA-problems/E-SSA.PR-5.md` |

The `appA-problems/` directory does not exist yet and the id scheme `E-SSA.PR-n` is my
proposal — the existing scheme only knows chapters 1–10. Someone has to choose the appendix
naming (`appA-problems`/`appB-problems`, id `E-SSA`/`E-SS11`) before adding those five cards.
No Appendix B items: that appendix prints no Exercises and no Problems.

Per-chapter totals (printed vs cards vs missing):

| chapter | exercises printed/cards | problems printed/cards | missing |
|---|---|---|---|
| 1 | 26 / 26 | – (none printed) | 0 |
| 2 | 15 / 15 | 5 / 5 | 0 |
| 3 | 22 / 22 | 5 / 2 | **3** |
| 4 | 12 / 12 | 4 / 4 | 0 |
| 5 | 17 / 17 | 4 / 4 | 0 |
| 6 | 17 / 17 | 4 / 4 | 0 |
| 7 | 12 / 12 | 4 / 4 | 0 |
| 8 | 24 / 24 | 9 / 9 | 0 |
| 9 | 8 / 8 | 4 / 3 | **1** |
| 10 | 12 / 12 | 6 / 6 | 0 |
| App A | – (none printed) | 5 / 0 | **5** |
| App B | – (none printed) | – (none printed) | 0 |

## The specific suspicions in the brief — answered

* **Is there a Chapter 5 exercise 19?** No. Chapter 5 prints exercises 1–17 only. Item 17
  (Pringsheim interpolation) ends on printed p. 156 = PDF 175, and the heading `7 Problems`
  and Problem 1 begin on that same page; nothing numbered 18 or 19 follows. The 17 cards are
  complete and correctly numbered.
* **Does Chapter 8 have problems beyond 9?** No. `6 Problems` on printed pp. 254–260
  (PDF 273–279) contains exactly 1–9; Problem 9 (Gauss, arithmetic–geometric mean) ends on
  printed p. 260 = PDF 279 and the Chapter 9 title page is PDF 280. All 9 are carded.
* **How many problems does Chapter 10 print?** Six (printed pp. 314–317, PDF 333–336,
  items 1∗, 2, 3, 4, 5∗, 6∗). Chapter 10 also prints 12 exercises (pp. 309–313). Both sets
  are fully carded.
* Chapters 2, 4, 5, 7, 8, 10 are **complete**; among the chapters the brief suspected, only
  Chapter 9 has a gap (Problem 4). The largest gap is in a chapter the brief did not flag
  (Chapter 3, three problems), plus the entirely uncarded Appendix A.

## Scope of these conclusions, and what was not checked

Full coverage: all 20 exercise/problem sections of the book were parsed and compared
item-by-item with the 206 cards. There is no section of this book I did not check for printed
items — the book has no other exercise material:

* Appendix B (PDF 363–383, printed pp. 344–364): verified it prints no Exercises/Problems
  heading and no numbered item run. Nothing to card.
* Front matter (PDF 1–19, folios i–xviii), Notes and References, Bibliography, Symbol
  Glossary, Index (PDF 384–398): page-by-page heading scan found no exercise/problem section.
* The book's in-text cross-references ("see Exercise 12 in Chapter 3", "Problem 4 in
  Chapter 10") were **not** audited for dangling or wrong numbers — that is a different pass.
* Statement fidelity: **not** a word-by-word audit. What was done mechanically over all 206
  cards: (i) every card's printed item was re-located and its number checked by token overlap
  against the printed text (no card was found holding the text of a neighbouring item);
  (ii) presence of every printed `[Hint: …]`; (iii) presence of every printed part label
  (a), (b), …; (iv) star annotations. Results in `fidelity-spotcheck.md`; the cards carrying
  findings are E-SS1.EX-15, E-SS1.EX-16, E-SS1.EX-18, E-SS1.EX-21, E-SS8.EX-13 (dropped
  hints) and E-SS2.PR-1 (starred part (b) not marked). Ten cards were additionally read
  closely against the print.
* Proofs/solutions inside the cards were not audited (out of scope by the brief).

## Caveat on the OCR

All quotations in these files are verbatim from the Tesseract text layer, which mangles
mathematics (`\u0001` for integral signs, broken superscripts, dropped braces). Where the OCR
is ambiguous I quote it as it stands and say so; no claim about a symbol is made from an
ambiguous passage unless the surrounding prose settles it. Item *numbers* are OCR-reliable
here because every run is contiguous, which is why the counts can be trusted even where the
formulas cannot.
