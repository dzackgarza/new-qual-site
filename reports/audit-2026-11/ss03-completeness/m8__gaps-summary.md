# SRC-TEXT-SS03 completeness audit — summary

Auditor: member m8. Book: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp.,
OCR'd). Cards: `corpus/collections/SRC-TEXT-SS03/`. Nothing under `corpus/` was edited.

## Bottom line

The book prints **215** numbered items in its **20** exercise/problem sections: 10 exercise
sections (one per chapter of Chapters 1-10), 9 problem sections (Chapters 2-10), and the problem
section of Appendix A. The corpus holds **206** cards. **9 printed items have no card:**

| item | printed page | status |
|---|---|---|
| Ch3 Problem 3 | p.109 | missing |
| Ch3 Problem 4 (starred) | p.110 | missing |
| Ch3 Problem 5 (starred) | p.110 | missing |
| Ch9 Problem 4 (starred) | p.282 | missing |
| AppA Problems 1-5 (5 starred) | pp.341-343 | missing; no appendix directory exists, so this is a scope decision |

**No exercise is missing anywhere.** All 165 exercises printed in Chapters 1-10 have cards, and
the enumeration is exhaustive: the whole-book scan for section headings finds exactly the 20
headings above, and every one of them was enumerated item by item.

The brief's "current inventory" is itself wrong and must not be used: it omits `ch1-exercises`
(26 cards), `ch3-exercises` (22), `ch6-exercises`/`ch6-problems` (17/4), `ch3-problems`,
`ch5-problems`, `ch7-problems`, `ch9-exercises`, and the exercise sections of Chapters 2, 4, 8, 9.
The re-derived inventory is in the table below.

## Per-chapter totals

| chapter | printed exercises | cards | printed problems | cards | missing |
|---|---|---|---|---|---|
| Ch1 Preliminaries | 26 (pp.24-31) | 26 | 0 (none printed) | 0 | — |
| Ch2 Cauchy's theorem | 15 (pp.64-67) | 15 | 5 (pp.67-70) | 5 | — |
| Ch3 Meromorphic functions | 22 (pp.103-108) | 22 | 5 (pp.108-110) | 2 | **PR-3, PR-4*, PR-5*** |
| Ch4 Fourier transform | 12 (pp.127-131) | 12 | 4 (pp.131-133) | 4 | — |
| Ch5 Entire functions | 17 (pp.153-156) | 17 | 4 (pp.156-158) | 4 | — |
| Ch6 Gamma and zeta | 17 (pp.174-179) | 17 | 4 (pp.179-180) | 4 | — |
| Ch7 Zeta and PNT | 12 (pp.199-203) | 12 | 4 (pp.203-204) | 4 | — |
| Ch8 Conformal mappings | 24 (pp.248-254) | 24 | 9 (pp.254-260) | 9 | — |
| Ch9 Elliptic functions | 8 (pp.278-280) | 8 | 4 (pp.281-282) | 3 | **PR-4*** |
| Ch10 Theta functions | 12 (pp.309-313) | 12 | 6 (pp.314-317) | 6 | — |
| Appendix A Asymptotics | 0 (none printed) | 0 | 5 (pp.341-343) | 0 | **PR-1 .. PR-5*** (scope) |
| Appendix B Simple connectivity | 0 (none printed) | 0 | 0 (none printed) | 0 | — |
| **total** | **165** | **165** | **50** | **42** | **9** |

Appendix B prints no exercise or problem section at all (the whole-book heading scan and the
Contents, PDF p.15, agree), so no cards are owed there.

## Direct answers to the questions in the brief

- **Is there a Chapter 5 exercise 19?** No. Chapter 5 prints 17 exercises (pp.153-156; the
  `7 Problems` heading is on p.156 and 17 is the last number above it). Cards go to 17.
- **Does Chapter 8 have problems beyond 9?** No. Chapter 8 prints 9 problems (pp.254-260);
  problem 9 ends at the foot of p.260 and Chapter 9 opens on p.261. Cards go to 9.
- **How many problems does Chapter 10 print?** Six (pp.314-317). Cards go to 6.
- **Chapters 2, 4, 7** are complete as printed: 15 ex + 5 pr, 12 ex + 4 pr, 12 ex + 4 pr.
- The real gaps are elsewhere: **Chapter 3 problems and Chapter 9 problem 4**, plus Appendix A.

## Method, and the checks behind those counts

- `pdftotext -layout` over the whole 398-page file; the printed Contents gives each section's
  printed page, and the offset **PDF = printed + 19** was confirmed at four anchors (printed 24
  "4 Exercises" = PDF 43; printed 32 = PDF 51 opening Chapter 2; printed 283 = PDF 302 opening
  Chapter 10; printed 318 = PDF 337 opening Appendix A).
- Every chapter-opening page in the book was located and matched to the Contents page number, so
  no section block was clipped at either end.
- All 20 `K Exercises` / `K Problems` heading lines in the book were enumerated mechanically
  (whole-book scan); there are exactly 20 and none in Appendix B or the end matter.
- Within each block, item starts were matched on the printed number, and the recovered sequences
  are contiguous and duplicate-free: 1..N with no holes for all 20 sections. A dropped or
  misread number would have shown as a hole or a repeat, so the counts are not "sampled".
- Both boundaries of every problem section were read on the page (the tail exercises printed
  above the `Problems` heading, and the last problem before the next chapter).
- The card inventory was re-derived by globbing the collection: 206 files, filenames
  `E-SS<n>.(EX|PR)-<k>.md`, all in the directory implied by chapter and kind, all frontmatter
  `id:` values equal to the filename stem, `kind: problem` throughout. No duplicates, no strays.

## Statement-fidelity findings (job 2, cheap checks only)

A mechanical screen compared every card with the printed item of the same number for the presence
of a printed `[Hint ...]`, and I read the flagged pages. Result: **5 cards lose a printed hint**,
and **1 card changes an exponent** (needs a human to look at the page):

| card | printed page | defect |
|---|---|---|
| Ch1 EX-15 | p.28 | drops "[Hint: Sum by parts.]" (and the pointer to Book I, Chapter 2) |
| Ch1 EX-16 | p.28 | drops "[Hint: Use Stirling's formula, which says that n! ~ cn^{n+1/2}e^{-n} for some c > 0.]" |
| Ch1 EX-18 | p.29 | drops "[Hint: Write z = z0 + (z − z0) and use the binomial expansion for z^n.]" |
| Ch1 EX-21 | p.29 | drops "[Hint: Use the dyadic expansion of an integer and the fact that 2^{k+1} − 1 = 1 + 2 + 2^2 + ⋯ + 2^k.]" |
| Ch1 EX-16(c) | p.28 | card has `a_n = n^2/(4^n+3n)`; the print OCRs as `4nn+3n` with both `4n` and `3n` superscripts (cf. (a) `(log n)2` for `(log n)^2`), so `3n` is very likely `3^n`; the fraction structure is not visible in the OCR. Verify against the page. |
| Ch8 EX-13 | p.251 | drops "[Hint: Consider the automorphism ψα(z) = (z − α)/(1 − αz) and apply the Schwarz lemma to ψ_{f(w)} ∘ f ∘ ψ_w^{−1}.]" |

Paraphrases seen and judged harmless: Ch1 EX-11 replaces the printed "Use Exercise 10" by "Use the
Wirtinger-operator identity for the Laplacian". Ch2 EX-15 keeps the printed `E'(z)` (a book typo)
faithfully.

**Printed difficulty stars are not recorded anywhere in the corpus** (no field, no `∗` in the
cards). Full catalogue from the print:

- Chapter 1: no starred item. No exercise in any chapter is starred.
- Ch2 problems 2, 5, and **part (b) of problem 1** (the only starred sub-part in the book).
- Ch3 problems 1, 4, 5. Ch4 problems 3, 4. Ch5 problems 2, 3, 4. Ch6 problems 2, 3, 4.
  Ch7 problems 2, 3, 4. Ch8 problems 3, 4, 6, 7, 8, 9. Ch9 problems 3, 4. Ch10 problems 1, 5, 6.
  Appendix A problem 5.

## Provenance / manifest notes (same audit, artifact side)

1. `corpus/collections/SRC-TEXT-SS03/index.md` declares `completion: complete`, and its
   `source.sections` list mirrors the files on disk exactly — including "Ch3 Problems" with only
   2 of the book's 5 problems and "Ch9 Problems" with 3 of 4, and with no appendix section at
   all. The manifest is consistent with the corpus and inconsistent with the book; the
   `completion: complete` claim is false.
2. 12 cards' `source-checked` notes write the location as "Chapter N, §M", where §M is a body
   section and not the section in which the item is printed (`K Exercises`/`K Problems`, see the
   per-chapter tables). In the ones I read, §M is the section the *material* belongs to (§3 =
   Infinite products for the Ch5 exercises, §3 = Riemann mapping for the Ch8 problems), so this is
   provenance wording, not a content error — but the string must not be read as the item's
   location. Affected: Ch2 PR-4 ("§5"), Ch2 PR-5 ("§5.5"), Ch5 EX-15, EX-16, EX-17 ("§3"),
   Ch8 PR-4, PR-5, PR-6, PR-7, PR-8, PR-9 ("§3"), Ch10 PR-6 ("§4"). No claim inside these notes
   was falsified by my checks.

## What I did NOT check — explicitly

- **No proof was audited, in any card** (out of scope for this pass).
- **Statement fidelity is not complete.** The hint screen covered all 206 cards mechanically, but
  word-by-word comparison was done for about 20 cards only (Ch1 EX-11/15/16/18/21, Ch2 PR-1/2/5,
  Ch8 EX-13, Ch9 PR-2, plus the boundary items I read on the page). The remaining ~185 cards are
  unchecked for dropped hypotheses, changed signs, lost cases.
- **Symbolic formulas were not verified against the print**, because the OCR mangles symbols;
  the single exception is Ch1 EX-16(c), flagged above as unresolved.
- **Appendix A's body text** (pp.318-343) was read only where the problems section sits
  (pp.341-343); its four body sections are unaudited.
- **Appendix B** (pp.344-364) was checked only for the absence of an exercise/problem section;
  its content, and the print page range 361-364 mentioned in the Contents ("2.1 Proof of a general
  form of Cauchy's theorem 361"), are unaudited.
- **Front matter, Notes and References (pp.365-368), Bibliography, Symbol Glossary, Index
  (pp.369-397)** were scanned for exercise/problem headings only; nothing else.
- **Sub-part stars**: only problem 1(b) of Chapter 2 was noticed among sub-parts; I did not sweep
  every sub-part of every item for a star.
- **Cross-collection duplication**, card render/div-syntax validity, and whether the `proofs/`
  tree references these ids were not checked.
- Scope caveat: "card present with the right number" is what I verified. A card holding the wrong
  item's text under the right number would not have been caught by the count method; the
  token-alignment screen I ran was too crude to settle formula-only items, so I am not claiming
  alignment beyond the cards I read.

## Files in this report

`gaps-ch1.md` … `gaps-ch10.md`, `gaps-appA.md` (per chapter: printed inventory with page ranges,
cards on disk, each missing item quoted with its page and target path, fidelity notes, and the
scope of that chapter's conclusion), and this `gaps-summary.md`.

`inventory.tsv` — the same inventory machine-readably: one row per printed item
(`chapter, section, number, printed_page, starred, card|MISSING`), 215 rows, 9 of them `MISSING`.
It is the table a human can work down when adding the missing cards.
