# SRC-TEXT-SS03 (Stein–Shakarchi, *Complex Analysis*) — gap audit, summary

Auditor: m3. Method: **tail-truncation test** — for every printed exercise/problem set, find the
last printed item, decide from the text that immediately follows it whether the set has ended
(next text is a heading / new chapter) or has been cut short, then check the card directory against
that end. Counts were cross-checked by scanning the whole numeral stream of each set for
continuity 1..N (script, see `evidence.md`).

Page convention: **PDF page = printed page + 19** (checked on every running head quoted below, e.g.
PDF 336 carries the folio `317`). Both numbers are given; the first is the one to use with
`pdftotext` on `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`.

All quotes are the OCR text of that PDF, lightly normalised (the OCR gives `\u0001` for ∫, `\u0002` for Σ,
`\u0003`/`\u0004` for other symbols, `Ω` for Ω, `ﬀ`/`ﬁ` ligatures). Where OCR mangles a formula I say so
and give the reading in words.

## Result

**9 printed items have no card.** They are all in three places:

| chapter | section | missing cards | printed pages (PDF / printed) |
|---|---|---|---|
| 3 | Problems | **PR-3, PR-4, PR-5** | PDF 128–129 / 109–110 |
| 9 | Problems | **PR-4** | PDF 301 / 282 |
| App. A | Problems | **PR-1 … PR-5** (whole section, no directory exists) | PDF 360–362 / 341–343 |

Everything else in chapters 1–10 is complete at item level: 17 of the 20 printed sets have a
card count exactly equal to the printed count, and the three that do not are the ones listed above.
In particular the suspicions in the task are **negative**:

* Chapter 5 prints **17** exercises (1–17) and **4** problems (1–4\*). There is **no chapter 5
  exercise 18 or 19** — printed p. 156 (PDF 175) ends at exercise 17 with the Pringsheim formula
  and the next line is the heading `7 Problems`.
* Chapter 8 prints **exactly 9 problems** (1, 2, 3\*, 4\*, 5, 6\*, 7\*, 8\*, 9\*); problem 9\* ends on
  printed p. 260 (PDF 279) and is followed by the chapter 9 opening at printed p. 261 (PDF 280).
  There is no problem 10.
* Chapter 10 prints **6 problems** (1\*, 2, 3, 4, 5\*, 6\*) on printed pp. 314–317 (PDF 333–336), and
  **12 exercises** on printed pp. 309–313 (PDF 328–332). The card set PR-1..6 is correct.
* Chapter 2 prints 15 exercises (1–15) and 5 problems (1, 2\*, 3, 4, 5\*); chapter 4 prints 12
  exercises and 4 problems (1, 2, 3\*, 4\*); chapter 7 prints 12 exercises and 4 problems
  (1, 2\*, 3\*, 4\*). All four card sets are correct.

The stated inventory was accurate for seven of its eight sections (`ch2-problems`,
`ch4-problems`, `ch5-exercises`, `ch7-exercises`, `ch8-problems`, `ch10-problems`,
`ch10-exercises`) and wrong for `ch9-problems`, which stops at PR-3 although the book prints a
fourth problem.

## Printed vs. card count, chapter by chapter

`n.c.` = nothing to check. Card counts are files on disk in `corpus/collections/SRC-TEXT-SS03/`.

| chapter | section | PDF pages | printed pages | printed items | cards | missing |
|---|---|---|---|---|---|---|
| 1 | Exercises | 43–50 | 24–31 | 26 | 26 | none |
| 1 | Problems | — | — | n.c. (ch. 1 prints no Problems section) | — | — |
| 2 | Exercises | 83–86 | 64–67 | 15 | 15 | none |
| 2 | Problems | 86–89 | 67–70 | 5 | 5 | none |
| 3 | Exercises | 122–127 | 103–108 | 22 | 22 | none |
| 3 | Problems | 127–129 | 108–110 | 5 | 2 | **3, 4, 5** |
| 4 | Exercises | 146–150 | 127–131 | 12 | 12 | none |
| 4 | Problems | 150–152 | 131–133 | 4 | 4 | none |
| 5 | Exercises | 172–175 | 153–156 | 17 | 17 | none |
| 5 | Problems | 175–177 | 156–158 | 4 | 4 | none |
| 6 | Exercises | 193–198 | 174–179 | 17 | 17 | none |
| 6 | Problems | 198–199 | 179–180 | 4 | 4 | none |
| 7 | Exercises | 218–222 | 199–203 | 12 | 12 | none |
| 7 | Problems | 222–223 | 203–204 | 4 | 4 | none |
| 8 | Exercises | 267–273 | 248–254 | 24 | 24 | none |
| 8 | Problems | 273–279 | 254–260 | 9 | 9 | none |
| 9 | Exercises | 297–300 | 278–280 | 8 | 8 | none |
| 9 | Problems | 300–301 | 281–282 | 4 | 3 | **4** |
| 10 | Exercises | 328–333 | 309–313 | 12 | 12 | none |
| 10 | Problems | 333–336 | 314–317 | 6 | 6 | none |
| A | Problems | 360–362 | 341–343 | 5 | 0 | **1, 2, 3, 4, 5** |
| B | (none) | 363–364+ | 344–364 | n.c. (no Exercises/Problems section) | — | — |

Totals: the book prints **215** numbered items in these sets (chapters 1–10 plus Appendix A);
**206** cards exist, so **9 are missing**. (206 is also the exact number of cards in the whole
collection, so no card is a duplicate of a printed item either — the disk set is 1..N in every
directory, contiguous and without extras.)

Per-chapter files: `gaps-1.md` … `gaps-10.md`, `gaps-appendix-a.md`, `gaps-appendix-b.md`.
Statement-fidelity notes: `fidelity-notes.md`. Page map, method and reproduction: `evidence.md`.

## What I did NOT check (scope of these conclusions)

1. **Statements are not audited.** Only 9 cards were compared in full with the print, plus 13 more
   examined during the alignment check (all listed in `fidelity-notes.md`, `evidence.md`). Everything else in this report is about *numbering and
   coverage*, not about whether a card reproduces its item correctly. A card whose statement has
   drifted, dropped a hypothesis or lost a hint is invisible to this pass unless noted there.
2. **Proofs are out of scope** by the task's own instruction; none were read.
3. **Chapter body text is not audited** — no theorem, definition or displayed formula outside the
   exercise sections was checked.
4. **Not every word of the exercise sections was read.** For each of the 20 sections I read the
   heading page, the closing page and every page carrying a numeral boundary check; the
   continuity test over the full page range is scripted (`evidence.md`), but a statement-level
   error inside the middle of a long item would not be caught here.
5. **Other collections and the back matter** (Notes and References, Index, Symbol Glossary) were
   not audited. `corpus/collections/SRC-TEXT-HART77` mentions one of the missing chapter-3
   problems by title but holds no SS03 card.
6. **The `corpus/` tree was not modified** (task requirement). All files here are new, under
   `.ultramath/smvy0zst4/m3/`.
7. Chapters 11+: **there is no chapter 11** in this book. The TOC (PDF 12–15) ends the chapters at
   10 and then prints Appendix A (Asymptotics) and Appendix B (Simple Connectivity and Jordan
   Curve Theorem).

## Confidence

Counts: high. Each set's numerals form an unbroken run 1..N in the OCR and N is fixed by the
heading or chapter opening that follows the last item; both anchors agree in all 20 sets. The
failure mode that would survive this check is a shared OCR error in which the same numeral is
mangled in the *printed set* and in the card that was made from it — the count of cards equals the
count of numerals in all 17 complete sets, which would be a coincidence under that hypothesis, but
it is not a proof. A second, independent sanity check — matching each card's statement against the
printed item blocks by tf-idf cosine — puts 193 of 206 cards on their own printed number by itself;
the other 13 were examined by hand and all 13 are formula-only statements or near-duplicate
neighbours, not shifts (`evidence.md` §3). Item-level statements of the other 184 cards: unchecked.
