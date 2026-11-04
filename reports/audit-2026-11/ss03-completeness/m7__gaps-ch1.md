# Chapter 1 (Preliminaries to Complex Analysis) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`). Page numbers below are **printed** page numbers; the PDF page is
printed + 19 (calibration: PDF p. 44 carries the running head "4. Exercises 25").

## Scope

* Chapter 1 prints one exercise section and **no Problems section**: heading "4 Exercises"
  on p. 24, exercises 1–26, last item on p. 31. There is no "Problems" heading anywhere in
  the chapter (checked over pp. 1–31).
* Cards on disk (`ch1-exercises/`): `E-SS1.EX-1` … `E-SS1.EX-26` — 26 cards.
* Inventory re-derived from the filesystem, not from `index.md`; the printed numbering was
  parsed as one contiguous run 1…26 and the end of the section was read by eye.

Printed numbering with page anchors (OCR text): 1–2 p24; 3–5 p25; 6–7 p26; 8–12 p27;
13–16 p28; 17–21 p29; 22–25 p30; 26 p31.

## Missing items

**None.** Every printed exercise 1–26 has a card `corpus/collections/SRC-TEXT-SS03/ch1-exercises/E-SS1.EX-<n>.md`.

## Statement-fidelity findings (all 26 cards compared against the printed item)

Substantive:

1. **E-SS1.EX-12 (p. 27)** — printed (OCR): `12. Consider the function defined by
   f (x + iy) = |x||y|, whenever x, y ∈ R.` The card states
   `f(x+iy)=\sqrt{\abs{x}\abs{y}}`. The square root is **not** in the printed text.
2. **E-SS1.EX-15 (p. 28)** — the card drops the bracketed hint
   `[Hint: Sum by parts.]` and the closing sentences
   "For the precise definition of these terms, and more information on summability methods,
   we refer the reader to Book I, Chapter 2."
3. **E-SS1.EX-16 (p. 28)** — the card drops the bracketed hint
   `[Hint: Use Stirling's formula, which says that n! ∼ c n^{n+1/2} e^{-n} for some c > 0.]`
   (OCR; the exponent is a raised `n+1/2`).
4. **E-SS1.EX-18 (p. 29)** — the card drops the bracketed hint
   `[Hint: Write z = z0 + (z − z0 ) and use the binomial expansion for z^n .]`
5. **E-SS1.EX-21 (p. 29)** — the card drops the bracketed hint
   `[Hint: Use the dyadic expansion of an integer and the fact that 2^{k+1} − 1 = 1 + 2 + 2^2 + · · · + 2^k .]`

Minor / wording:

6. **E-SS1.EX-11 (p. 27)** — printed "**Use Exercise 10** to prove that if f is holomorphic in
   the open set Ω, then the real and imaginary parts of f are harmonic"; the card replaces the
   reference by "Use the Wirtinger-operator identity for the Laplacian". The cross-reference is lost.
7. **E-SS1.EX-13 (p. 28)** — printed "Suppose that f is holomorphic in an **open set** Ω";
   the card strengthens this to "in a region Ω (an open connected set)". (The printed statement is
   the book's own imprecision; the card's version is what makes the conclusion true.)

Compared and found faithful (no difference in hypotheses, constants or quantifiers):
EX-1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 17, 19, 20, 22, 23, 24, 25, 26.

## Not checked

* Proofs and solutions (statements only, by design).
* Nothing in this chapter was left unexamined: all 26 printed exercises and all 26 cards were compared.
