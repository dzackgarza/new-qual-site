# Gaps — Appendix A (Asymptotics)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR layer). Page citations give the PDF page and, in parentheses, the printed page; on every page this audit used, PDF page = printed page + 19.

Method: the whole PDF was dumped once with `pdftotext -layout`; for every printed Exercises/Problems section I collected the item-start lines and their page, checked that the printed numbers run contiguously from 1 to the last item, and read the closing page of each block to confirm the terminal item. Numbers were then diffed against the card files on disk (`corpus/collections/SRC-TEXT-SS03/<dir>/E-SS<ch>.<EX|PR>-<n>.md`). Page ranges below run from the first to the last item's starting page.

## Printed sections in this chapter

| section | heading page (printed) | printed items | cards on disk | missing |
|---|---|---|---|---|
| 5 Problems | p. 341 | 5 | 0 | 5 |

## Missing items

### E-SSA.PR-1

- Printed at PDF p. 360 (printed p. 341), in "5 Problems" (heading printed p. 341).
- Card should go in `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-1.md`. The directory does not exist yet; a new section "AppA Problems" would also have to be added to `corpus/collections/SRC-TEXT-SS03/index.md`, whose section list stops at "Ch10 Problems".

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> Let η be an indefinitely diﬀerentiable function supported in a finite interval, so that η(x) = 1 for x near 0. Then, if m > −1 and N > 0,  ∞ e−sx xm η(x) dx = s−m−1 Γ(m + 1) + O(s−N ) 0 for Re(s) ≥ 0, |s| → ∞. (a) Consider first the case −1 < m ≤ 0. It suﬃces to see that  ∞ e−sx xm (1 − η(x)) dx = O(s−N ), 0 and this can be done by repeated integration by parts since  d N −sx e−sx = (−1)N s−N dx (e ). (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write  $ k % d (x ) e−sx η(x) dx = ck,m s−m+k−1 + O(s−N ), m dx and integrate by parts k times.

### E-SSA.PR-2

- Printed at PDF p. 361 (printed p. 342), in "5 Problems" (heading printed p. 341).
- Card should go in `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-2.md`. The directory does not exist yet; a new section "AppA Problems" would also have to be added to `corpus/collections/SRC-TEXT-SS03/index.md`, whose section list stops at "Ch10 Problems".

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> The following is a more precise version of Stirling’s formula. There are real constant a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0 √  N  s log s −s 2π  −j −N Γ(s) = e e 1+ aj s + O(s ) when s ∈ Sδ . s1/2 j=1 This can be proved by using the results of Problem 1 in place of Proposition 1.3.

### E-SSA.PR-3

- Printed at PDF p. 361 (printed p. 342), in "5 Problems" (heading printed p. 341).
- Card should go in `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-3.md`. The directory does not exist yet; a new section "AppA Problems" would also have to be added to `corpus/collections/SRC-TEXT-SS03/index.md`, whose section list stops at "Ch10 Problems".

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> The Bessel functions and Airy function have the following power series expan- sions: m x2 x ∞ ν  (−1)m 4 Jν (x) = , 2 m=0 m!Γ(ν + m + 1) ∞ 1  xn Ai(−x) = sin(2π(n + 1)/3)3n/3−2/3 Γ(n/3 + 1/3). π n=0 n! (a) From this, verify that when x > 0,      x1/2 2 3/2 2 3/2 Ai(−x) = J1/3 x + J−1/3 x . 3 3 3 (b) The function Ai(x) extends to an entire function of order 3/2. [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for Ai. Compare also with Problem 1, Chapter 4.] 

- The printed item carries a bracketed hint; it must be kept in the card.

### E-SSA.PR-4

- Printed at PDF p. 361 (printed p. 342), in "5 Problems" (heading printed p. 341).
- Card should go in `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-4.md`. The directory does not exist yet; a new section "AppA Problems" would also have to be added to `corpus/collections/SRC-TEXT-SS03/index.md`, whose section list stops at "Ch10 Problems".

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> Suppose F (z) = ∞ n n=0 Fn w is meromorphic in a region containing the closed unit disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk , and their orders are r1 , . . . , rk respectively. Then for some ǫ > 0 k  Fn = Pj (n) + O(e−ǫn ) as n → ∞. j=1 Here  rj −1 1 d   Pj (n) = (w − αj )rj w−n−1 F (w) w=α . (rj − 1)! dw j Note that each Pj is of the form Pj (n) = Aj (α−1 j n) rj −1 + O(nrj −2 ). To prove this, use the residue formula (Theorem 1.4, Chapter 3).

### E-SSA.PR-5 — printed with the difficulty asterisk (preface, printed p. viii: "the ones that are most difficult, or go beyond the scope of the text, are marked with an asterisk")

- Printed at PDF p. 362 (printed p. 343), in "5 Problems" (heading printed p. 341).
- Card should go in `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-5.md`. The directory does not exist yet; a new section "AppA Problems" would also have to be added to `corpus/collections/SRC-TEXT-SS03/index.md`, whose section list stops at "Ch10 Problems".

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> The one shortcoming in our derivation of the asymptotic formula for p(n) arose iπ iπz from the fact that while f1 (z) = z/i e 12z e 12 is a good approximation to the generating function f (z) near z = 0, this fails near other points on the real axis, since f1 is regular there, but f is not. However, using the transformation law (24) and the identity f (z + 1) = f (z), one can derive the following generalization of (24): whenever p/q is a rational number in lowest form (so p and q are relatively prime) then   !   p zq 12zq iπ iπz 2 − 12 1 p′ f z− = ωp/q e e f − − , q i zq 2 q where pp′ = 1 mod q. Here ωp/q is an appropriate 24th root of unity. This formula leads to an analogous fp/q , approximating f at z = p/q. From this one can obtain for each p/q a contribution of the form  K 1 1/2  1 d e q (n− 24 ) cp/q √ 1 1/2 2π 2 dn (n − 24 ) to the asymptotic formula for p(n). When suitably modified, the resulting series, summed over all proper fractions p/q in [0, 1), actually converges and gives an exact formula for p(n).


## Fidelity note

Appendix A prints no "Exercises" section, only "5 Problems" (heading printed p. 341). Appendix B (printed pp. 344–364) prints neither Exercises nor Problems, so there is no card surface there.
