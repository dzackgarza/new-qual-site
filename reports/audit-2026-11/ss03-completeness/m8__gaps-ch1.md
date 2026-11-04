# Chapter 1: Preliminaries to Complex Analysis — gap report (SRC-TEXT-SS03)

**Source of truth.** `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR'd).
The whole file was extracted with `pdftotext -layout`; the whole-book page map was then taken
from the printed Contents (PDF pp.12-15). Offset: **PDF page = printed page + 19** (checked at
several anchors: printed "4 Exercises 24" -> PDF 43; printed p.32 opens Chapter 2 -> PDF 51;
printed p.318 opens Appendix A -> PDF 337). Quotations below are the OCR as it comes out,
including its mangling of symbols; I say where the OCR is ambiguous.

## 1. Printed inventory of this chapter

| section | heading line | printed pp. | PDF pp. | printed items |
|---|---|---|---|---|
| Exercises | `4 Exercises` (p.24) | 24-31 | 43-50 | 1-26 (26 items) |
| Problems | — none printed — | — | — | 0 |

The Contents (PDF p.12) lists for this chapter only `4 Exercises 24`; Chapter 2 opens on
printed p.32 (PDF 51) directly after exercise 26, so there is no Problems section to card.
No exercise is starred: the only `*` characters on pp.24-31 belong to mathematics
(`t* = sup {...}` in exercise 5).

## 2. Cards on disk (re-derived from the filesystem, not from the brief)

| directory | files | numbers |
|---|---|---|
| `ch1-exercises/` | 26 | E-SS1.EX-1 .. E-SS1.EX-26 |
| `ch1-problems/` | — directory absent, correctly | — |

## 3. Missing items

**None.** Every one of the 26 printed exercises has a card with the matching number.

## 4. Statement-fidelity notes (cheap checks only)

Mechanical screen of all 26 cards for a printed `[Hint ...]` that the card loses, plus manual
reads of the flagged cards. Four cards lose a printed hint outright, and one card changes an
exponent:

1. **EX-15, printed p.28.** Print: "Abel's theorem. Suppose Σ a_n converges. Prove that
   lim_{r->1, r<1} Σ r^n a_n = Σ a_n. **[Hint: Sum by parts.]** In other words, if a series
   converges, then it is Abel summable with the same limit. For the precise definition of these
   terms, and more information on summability methods, we refer the reader to Book I,
   Chapter 2." The card has the display and one sentence ("In other words, a convergent series
   is Abel summable to its ordinary sum"), and **no hint**; the pointer to Book I, Chapter 2 is
   also dropped.
2. **EX-16, printed p.28.** Print carries, attached to part (d),
   "**[Hint: Use Stirling's formula, which says that** n! ~ cn^{n+1/2}e^{-n} **for some c > 0.]**"
   (OCR: "n! ∼ cnn+ 2 e−n for some c > 0.."). The card has no hint at all.
3. **EX-18, printed p.29.** Print: "**[Hint: Write** z = z_0 + (z − z_0) **and use the binomial
   expansion for** z^n**.]**" The card has no hint.
4. **EX-21, printed p.29.** Print: "**[Hint: Use the dyadic expansion of an integer and the fact
   that** 2^{k+1} − 1 = 1 + 2 + 2^2 + ⋯ + 2^k**.]**" The card has no hint.
5. **EX-16(c), printed p.28 — possible exponent loss.** The printed line OCRs as
   `(c) an = 4nn+3n`. In this book's OCR a superscript is rendered inline with no marker
   (compare part (a), printed `an = (log n)2` for (log n)^2), so `4n` and `3n` are 4^n and 3^n.
   The card prints `$a_n=\dfrac{n^2}{4^n+3n}$`: a denominator `3n` where the print has a
   superscript, and a numerator/fraction bar that the OCR does not show at all. **Unverified
   against the print** (OCR cannot settle the fraction); the card's (c) should be re-read off
   the page by a human before it is trusted.
6. **EX-11, printed p.27 — paraphrase only.** Print: "**Use Exercise 10** to prove that if f is
   holomorphic in the open set Ω, then the real and imaginary parts of f are harmonic; that is,
   their Laplacian is zero." The card replaces the printed cross-reference by "Use the
   Wirtinger-operator identity for the Laplacian ...". Content equivalent, but the printed
   pointer to Exercise 10 is gone.

Nothing else in this chapter was compared statement by statement: 21 of the 26 cards were only
screened for hint presence.

## 5. Scope of this conclusion

Complete for **existence and numbering**: all 26 printed exercises of Chapter 1 were located in
the book and each has a card. Not checked: the wording of 21 of the 26 cards (screened only);
symbolic formulas against the print (OCR cannot be trusted to settle them, see EX-16(c));
proofs (out of scope for this pass).
