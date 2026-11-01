# Appendix A — Asymptotics: gaps (whole problem set missing)

The appendix prints a `5 Problems` section, on printed pp. 341–343 = **PDF 360–362**. The
collection has **no directory and no card** for it: `corpus/collections/SRC-TEXT-SS03/` contains
`ch1-exercises` … `ch10-problems` and nothing for either appendix, and `index.md` lists only the
ten chapters' sections.

* Tail test: problem 5\* is the last item. After it, PDF 362 (printed 343) ends and PDF 363
  (printed 344) is the Appendix B title page. Nothing is truncated — the appendix simply has no
  cards at all.
* Proposed destination (naming is a decision for whoever applies this, since no precedent
  exists): `corpus/collections/SRC-TEXT-SS03/appA-problems/E-SSA.PR-<n>.md` for n = 1..5, plus a
  new `Appendix A Problems` section in `index.md` and in the collection front matter.
* Printed count: **5**; cards: **0**.

Quotes below are the OCR text of PDF 360–362, normalised only in whitespace and in the OCR's
symbol substitutes (∫ for `\u0001`, Σ for `\u0002`). Several displays are linearised by the OCR; where the
result is ambiguous I say so.

## Missing: Appendix A, Problem 1 — PDF 360–361 (printed 341–342)

> 1. Let η be an indefinitely differentiable function supported in a finite interval, so that
> η(x) = 1 for x near 0. Then, if m > −1 and N > 0,
> ∫ (0 … ∞) e−sx xm η(x) dx = s−m−1 Γ(m + 1) + O(s−N )
> for Re(s) ≥ 0, |s| → ∞.
> (a) Consider first the case −1 < m ≤ 0. It suffices to see that
> ∫ (0 … ∞) e−sx xm (1 − η(x)) dx = O(s−N ),
> and this can be done by repeated integration by parts since
> e−sx = (−1)N s−N (d/dx)N (e−sx ).
> (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write
> ∫ (d/dx)k (xm ) e−sx η(x) dx = ck,m s−m+k−1 + O(s−N ),
> and integrate by parts k times.

(Part (b) is on PDF 361.) Unstarred.

## Missing: Appendix A, Problem 2 — PDF 361 (printed 342)

> 2. The following is a more precise version of Stirling’s formula. There are real constant
> a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0
> Γ(s) = e s log s −s e √(2π) / s1/2 ( 1 + Σ (j = 1 … N) aj s−j + O(s−N ) )
> when s ∈ Sδ .
> This can be proved by using the results of Problem 1 in place of Proposition 1.3.

OCR ambiguity: the stray `e` between `es log s −s` and `√(2π)` is OCR noise; the printed formula is
the standard Γ(s) = e^{s log s − s} (√(2π)/s^{1/2})(1 + Σ a_j s^{−j} + O(s^{−N})). Unstarred.

## Missing: Appendix A, Problem 3 — PDF 361 (printed 342)

> 3. The Bessel functions and Airy function have the following power series expansions:
> Jν (x) = (x/2)ν Σ (m = 0 … ∞) (−1)m / (m! Γ(ν + m + 1)) (x2 /4)m ,
> Ai(−x) = (1/π) Σ (n = 0 … ∞) (xn /n!) sin(2π(n + 1)/3) 3n/3−2/3 Γ(n/3 + 1/3).
> (a) From this, verify that when x > 0,
> Ai(−x) = (x1/2 /3) ( J1/3 ((2/3) x3/2 ) + J−1/3 ((2/3) x3/2 ) ) .
> (b) The function Ai(x) extends to an entire function of order 3/2.
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for
> Ai. Compare also with Problem 1, Chapter 4.]

OCR ambiguity: the two series were set as displayed fractions and the OCR interleaved them
(the `x/2`, `x2 /4` and `1/π`, `xn /n!` fragments are the OCR's line order). Unstarred.

## Missing: Appendix A, Problem 4 — PDF 361–362 (printed 342–343)

> 4. Suppose F (z) = Σ (n = 0 … ∞) Fn wn is meromorphic in a region containing the closed unit
> disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk , and their
> orders are r1 , . . . , rk respectively. Then for some ǫ > 0
> Fn = Σ (j = 1 … k) Pj (n) + O(e−ǫn )
> as n → ∞.
> Here
> Pj (n) = 1/(rj − 1)! ( (d/dw)rj −1 [ (w − αj )rj w−n−1 F (w) ] ) at w = αj .
> Note that each Pj is of the form Pj (n) = Aj (α−1
> j n)
> rj −1
> + O(nrj −2 ).
> To prove this, use the residue formula (Theorem 1.4, Chapter 3).

OCR ambiguity: the OCR prints the series variable as `w` in `F (z) = Σ Fn wn`; on the page it is
almost certainly `z`. The evaluation point `w = αj` is on the subscript line and was lifted by the
OCR. Unstarred.

## Missing: Appendix A, Problem 5∗ — PDF 362–363 (printed 343–344)

Starred in print (`5.∗`).

> 5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose from the
> fact that while f1 (z) = √(z/i) eiπ/12z eiπ/12 is a good approximation to the generating function
> f (z) near z = 0, this fails near other points on the real axis, since f1 is regular there, but
> f is not.
> However, using the transformation law (24) and the identity f (z + 1) = f (z), one can derive
> the following generalization of (24): whenever p/q is a rational number in lowest form (so p and
> q are relatively prime) then
> f (z − p/q) = ωp/q √(zq/i) e(iπ/12)(zq) e−(iπ/12)/(zq) f (−1/(zq) − p′ /q) ,
> where pp′ = 1 mod q. Here ωp/q is an appropriate 24th root of unity. This formula leads to an
> analogous fp/q , approximating f at z = p/q.
> From this one can obtain for each p/q a contribution of the form
> (cp/q / (2π2)) (d/dn) [ e(K/q)(n − 1/24)1/2 / (n − 1/24)1/2 ]
> to the asymptotic formula for p(n). When suitably modified, the resulting series, summed over all
> proper fractions p/q in [0, 1), actually converges and gives an exact formula for p(n).

OCR ambiguity, stated plainly: the transformation-law display is badly mangled in the OCR — it
prints `f (z − p/q) = ωp/q` followed by a scattered `iπ/iπz`, `zq 12zq`, `2 − 12`, `e`, `f`, `e`, `i`
and `− p′/q − 1/(zq2)` on separate lines. My reading above is the standard formula and should be
checked against the page image before the card is written; the surrounding prose (the `pp′ = 1 mod q`
condition, the 24th root of unity, the contribution `c_{p/q}/(2π√2) · d/dn[...]`) is unambiguous.
The constant is `2π 2` or `2π√2` in the OCR (`2π 2` on the page) — also worth a look at the image.
