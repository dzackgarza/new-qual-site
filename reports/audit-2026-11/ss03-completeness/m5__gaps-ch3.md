# Gaps — Chapter 3 (Meromorphic Functions and the Logarithm)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR layer). Page citations give the PDF page and, in parentheses, the printed page; on every page this audit used, PDF page = printed page + 19.

Method: the whole PDF was dumped once with `pdftotext -layout`; for every printed Exercises/Problems section I collected the item-start lines and their page, checked that the printed numbers run contiguously from 1 to the last item, and read the closing page of each block to confirm the terminal item. Numbers were then diffed against the card files on disk (`corpus/collections/SRC-TEXT-SS03/<dir>/E-SS<ch>.<EX|PR>-<n>.md`). Page ranges below run from the first to the last item's starting page.

## Printed sections in this chapter

| section | heading page (printed) | printed items | cards on disk | missing |
|---|---|---|---|---|
| 8 Exercises | p. 103 | 22 | 22 | 0 |
| 9 Problems | p. 108 | 5 | 2 | 3 |

## Missing items

### E-SS3.PR-3

- Printed at PDF p. 128 (printed p. 109), in "9 Problems" (heading printed p. 108).
- Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`.

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has a pole of order k at z0 , then we can write a−k a−1 f (z) = + ··· + + g(z) (z − z0 )k (z − z0 ) where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this expansion that holds even if z0 is an essential singularity. This is a special case of the Laurent series expansion, which is valid in an even more general setting. Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 } where 0 < r1 < r2 . Then, ∞  f (z) = an (z − z0 )n n=−∞ where the series converges absolutely in the interior of the annulus. To prove this, it suﬃces to write   1 f (ζ) 1 f (ζ) f (z) = dζ − dζ 2πi Cr2 ζ − z 2πi Cr1 ζ − z when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2. Here Cr1 and Cr2 are the circles bounding the annulus. LOGARITHM

- OCR caveat: this problem comes out of the text layer as continuous prose; the printed part structure, if any, is not recoverable from the OCR. The human adding the card should read printed p. 109 / PDF p. 128 for it. The wording above is exactly what the OCR gives.

### E-SS3.PR-4 — printed with the difficulty asterisk (preface, printed p. viii: "the ones that are most difficult, or go beyond the scope of the text, are marked with an asterisk")

- Printed at PDF p. 129 (printed p. 110), in "9 Problems" (heading printed p. 108).
- Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`.

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects Ω. Assume that Ω ∩ L is an interval I. Choosing an orientation for L, we can define Ωl and Ωr to be the subregions of Ω lying strictly to the left or right of L, with Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are simply connected, then Ω is simply connected.

### E-SS3.PR-5 — printed with the difficulty asterisk (preface, printed p. viii: "the ones that are most difficult, or go beyond the scope of the text, are marked with an asterisk")

- Printed at PDF p. 129 (printed p. 110), in "9 Problems" (heading printed p. 108).
- Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`.

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> Let  M 1 h(x) g(z) = dx 2πi −M x −z where h is continuous and supported in [−M, M ]. (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes at infinity, that is, lim|z|→∞ |g(z)| = 0. Moreover, the “jump” of g across [−M, M ] is h, that is, h(x) = lim g(x + iǫ) − g(x − iǫ). ǫ→0,ǫ>0 [Hint: Express the diﬀerence g(x + iǫ) − g(x − iǫ) in terms of a convolution of h with the Poisson kernel.] (b) If h satisfies a mild smoothness condition, for instance a Hölder condition with exponent α, that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all x, y ∈ [−M, M ], then g(x + iǫ) and g(x − iǫ) converge uniformly to functions g+ (x) and g− (x) as ǫ → 0. Then, g can be characterized as the unique holomorphic function that satisfies: (i) g is holomorphic outside [−M, M ], (ii) g vanishes at infinity, (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x) and g− (x) with g+ (x) − g− (x) = h(x). [Hint: If G is another function satisfying these conditions, g − G is entire.]

- The printed item carries a bracketed hint; it must be kept in the card.


## Fidelity note

The book’s own Notes and References (printed p. 365) say "Also, see Muskhelishvili [25] for more about the Cauchy integral introduced in Problem 5" — an independent confirmation, from this same PDF, that chapter 3 prints at least five Problems. So the missing PR-5 is a corpus gap, not a numbering artefact.
