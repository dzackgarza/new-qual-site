# SRC-TEXT-SS03 — Appendix A (Asymptotics): printed Problem block with no cards at all

This is one of the "exercise sections not listed in the brief". Appendix A prints a
Problem section and **no** Exercise section; there is no card directory for it. Appendix B
(pdf 363–383 / printed 344–364) prints **neither** exercises nor problems — checked, nothing
numbered there; the "Notes and References" (pdf 385+) print none either.

Counts: Appendix A prints **5 problems** (1, 2, 3, 4, 5∗) on PDF pages 360–362
(printed 341–343). Cards present: **0**. PDF page = printed folio + 19.

Recommended target (a naming decision the human must make, since the collection's id scheme
`E-SS<chapter>.<KIND>-<n>` has no appendix form):
`corpus/collections/SRC-TEXT-SS03/appendixA-problems/`, cards `E-SS-A.PR-1.md` …
`E-SS-A.PR-5.md` (alternative: `ch11-appendix-problems/` with `E-SS11.PR-<n>`), and a new
`- name: Appendix A Problems` block in `corpus/collections/SRC-TEXT-SS03/index.md`.

## MISSING: `E-SS-A.PR-1` — PDF page 360 (printed 341)

Not starred. Printed statement (OCR verbatim; the display is broken across lines by the OCR
and the supremum-style limits are displaced):

> 1. Let η be an indefinitely diﬀerentiable function supported in a finite interval, so
> that η(x) = 1 for x near 0. Then, if m > −1 and N > 0,
>                  ∫ ∞
>                      e−sx xm η(x) dx = s−m−1 Γ(m + 1) + O(s−N )
>                     0
>
> for Re(s) ≥ 0, |s| → ∞.
>   (a) Consider first the case −1 < m ≤ 0. It suffices to see that
>                           ∫ ∞
>                               e−sx xm (1 − η(x)) dx = O(s−N ),
>                                0
>
>       and this can be done by repeated                                 integration     by       parts    since
>                       d N −sx
>       e−sx = (−1)N s−N dx   (e   ).
>
>   (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write
>
>                 ∫ (d/dx)^k (x^m ) e−sx η(x) dx = ck,m s−m+k−1 + O(s−N ),
>
>       and integrate by parts k times.

OCR note: in (a) the printed chain is `e^{-sx} = (−1)^N s^{-N} (d/dx)^N (e^{-sx})`; the OCR
float gives the `N` on the derivative and a stray `(e)` — the reading above is the only one
consistent with the two sides. In (b) the OCR emits `$\u0005 … \u0006k %` where the printed
page has a bracket/parenthesis pair around `(d/dx)^k (x^m)`; the displayed identity is
therefore reconstructed, not quoted, and should be eyeballed on the page image.

## MISSING: `E-SS-A.PR-2` — PDF page 361 (printed 342)

Not starred.

> 2. The following is a more precise version of Stirling’s formula. There are real
> constant a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0
>
>                     Γ(s) = e^{s log s −s} e^{2π}/s^{1/2} ( 1 + Σ_{j=1}^{N} aj s^{−j} + O(s^{−N}) )   when s ∈ Sδ .
>
> This can be proved by using the results of Problem 1 in place of Proposition 1.3.

OCR note: the OCR overprints the square root and the fraction, giving
`√ 2π / s1/2` with `s log s −s` as a superscript block; the printed formula is
Γ(s) = e^{s log s − s} √(2π)/s^{1/2} · (1 + Σ a_j s^{−j} + O(s^{−N})). The symbol `Sδ` is
clear in the OCR and is the sector of Appendix A. The word "constant" (singular) is printed
as such.

## MISSING: `E-SS-A.PR-3` — PDF page 361 (printed 342)

Not starred. Has a bracketed hint (must be carried over).

> 3. The Bessel functions and Airy function have the following power series expan-
> sions:
>
>              Jν (x) = (x/2)^ν Σ_{m=0}^{∞} (−1)^m (x^2 /4)^m / (m! Γ(ν + m + 1)),
>
>              Ai(−x) = (1/π) Σ_{n=0}^{∞} (x^n /n!) sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3).
>
>   (a) From this, verify that when x > 0,
>
>              Ai(−x) = (x^{1/2}/3) ( J_{1/3} ( (2/3) x^{3/2} ) + J_{−1/3} ( (2/3) x^{3/2} ) ).
>
>   (b) The function Ai(x) extends to an entire function of order 3/2.
>
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power
> series for Ai. Compare also with Problem 1, Chapter 4.]

OCR note: the two series are badly displaced by the OCR (the `(x^2/4)^m` block floats above
the summation) — the reconstruction above uses the standard forms and the visible glyphs; the
Ai series as OCR'd reads `(1/π) Σ x^n/n! sin(2π(n+1)/3) 3^{n/3−2/3} Γ(n/3+1/3)`, which is
what is quoted. Check the exponents on the page image before freezing a card.

## MISSING: `E-SS-A.PR-4` — PDF page 361 (printed 342), continues on PDF page 362 (printed 343)

Not starred.

> 4. Suppose F (z) = Σ_{n=0}^{∞} Fn w^n is meromorphic in a region containing the closed
> unit disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk ,
> and their orders are r1 , . . . , rk respectively. Then for some ǫ > 0
>
>                         Fn = Σ_{j=1}^{k} Pj (n) + O(e−ǫn )                     as n → ∞.
>
> Here
>                       1        (   d   )^{rj −1} [                                   ]
>           Pj (n) =  ---------- ( ----- )         (w − αj )^{rj } w^{−n−1} F (w) |_{w=αj} .
>                     (rj − 1)!   (  dw  )
>
> Note that each Pj is of the form Pj (n) = Aj (α_j^{−1} n)^{rj −1} + O(n^{rj −2}).
>   To prove this, use the residue formula (Theorem 1.4, Chapter 3).

OCR note: the OCR prints `(α−1 j n) rj −1` with the sub/superscripts interleaved; read as
`Aj (α_j^{−1} n)^{rj−1}`. Also note the print uses `w` in `F (z) = Σ Fn w^n` (a mismatch
of variable, quoted as printed — `z` vs `w`), which a card should reproduce or flag rather
than silently repair.

## MISSING: `E-SS-A.PR-5` — PDF page 362 (printed 343)

**Starred** ("5.∗"). Last item of the appendix.

> 5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose
> from the fact that while f1 (z) = √(z/i) e^{iπ/12z} e^{iπz/12} is a good approximation to the
> generating function f (z) near z = 0, this fails near other points on the real axis,
> since f1 is regular there, but f is not.
>    However, using the transformation law (24) and the identity f (z + 1) = f (z),
> one can derive the following generalization of (24): whenever p/q is a rational
> number in lowest form (so p and q are relatively prime) then
>
>       f ( z − p/q ) = ω_{p/q} √( (zq/ i)^{12zq^2 − 12iπ} ) e^{iπzq^2/12} f ( 1/(zq^2) − p'/q ),
>
> where pp′ = 1 mod q. Here ωp/q is an appropriate 24th root of unity. This formula
> leads to an analogous fp/q , approximating f at z = p/q.
>    From this one can obtain for each p/q a contribution of the form
>
>                       c_{p/q} (1/2π^2) (d/dn) ( e^{(K/q)(n−1/24)^{1/2}} / (n − 1/24)^{1/2} )
>
> to the asymptotic formula for p(n). When suitably modified, the resulting series,
> summed over all proper fractions p/q in [0, 1), actually converges and gives an
> exact formula for p(n).

OCR note: the transformation law is the most mangled display in the appendix — the OCR
gives `(zq/i)^{12zq^2 − 12iπ} e^{iπzq^2/12}` as a floating block with `12zq^2` and `− iπ/12`
split across lines, and the argument of the right-hand `f` as `1/(zq^2) − p'/q`. A card for
this item must be written from the page image, not from this quote; I flag it rather than
assert the exact exponents.
