# Gaps — Appendix A (SRC-TEXT-SS03)

PDF page = printed page + 19. Quotes are OCR as produced by `pdftotext -layout`; `\x01` = ∫,
`\x02` = ∑, `\x05 … \x06` = a large parenthesis pair whose contents the OCR splits onto the
neighbouring lines. No card was edited.

**The whole printed section is missing from the corpus.** Appendix A ("Asymptotics") ends with a
Problems section headed **`5 Problems`, printed p. 341 = PDF 360**, running to printed p. 343 =
PDF 362, items **1–5**, item **5 starred**. There is no `ch-appA-problems` (or any Appendix)
directory in `corpus/collections/SRC-TEXT-SS03/`, and `index.md` still declares
`completion: complete` over the ten chapter sections only.

Suggested destination (names are a proposal — the file stem must keep the
`E-SS<chapter>.PR-<n>.md` shape): `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/`.

## Missing: Problem 1 — PDF pp. 360–361 (printed pp. 341–342)

> 1. Let η be an indefinitely diﬀerentiable function supported in a finite interval, so
> that η(x) = 1 for x near 0. Then, if m > −1 and N > 0,
>     \x01_0^∞ e^{−sx} x^m η(x) dx = s^{−m−1} Γ(m + 1) + O(s^{−N})
> for Re(s) ≥ 0, |s| → ∞.
>   (a) Consider first the case −1 < m ≤ 0. It suﬃces to see that
>       \x01_0^∞ e^{−sx} x^m (1 − η(x)) dx = O(s^{−N}),
>       and this can be done by repeated integration by parts since
>       e^{−sx} = (−1)^N s^{−N} (d/dx)^N (e^{−sx}).
>   (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write
>       \x01 [ (d/dx)^k (x^m) ] e^{−sx} η(x) dx = c_{k,m} s^{−m+k−1} + O(s^{−N}),
>       and integrate by parts k times.

(Part (b)'s displayed line is badly mangled in the OCR — it prints as
`\x01 $\x05          \x06k              %` / `d` / `(x ) e−sx η(x) dx = ck,m s−m+k−1 + O(s−N ),` / `dx` —
so the transcription above is my reading of the layout, not a literal OCR string.)

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/E-SSappA.PR-1.md`

## Missing: Problem 2 — PDF p. 361 (printed p. 342)

> 2. The following is a more precise version of Stirling’s formula. There are real
> constant a1 = 1/12, a2 , . . ., an , . . ., so that for every N > 0
>     Γ(s) = e^{s log s} e^{−s} (2π/s)^{1/2} \x05 1 + \x02_{j=1}^{N} a_j s^{−j} + O(s^{−N}) \x06  when s ∈ Sδ .
> This can be proved by using the results of Problem 1 in place of Proposition 1.3.

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/E-SSappA.PR-2.md`

## Missing: Problem 3 — PDF p. 361 (printed p. 342), two parts + a hint

> 3. The Bessel functions and Airy function have the following power series expan-
> sions:
>     Jν (x) = (x/2)^ν \x02_{m=0}^{∞} (−1)^m (x²/4)^m / ( m! Γ(ν + m + 1) ),
>     Ai(−x) = (1/π) \x02_{n=0}^{∞} (x^n / n!) sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3).
>   (a) From this, verify that when x > 0,
>       Ai(−x) = (x^{1/2}/3) \x05 J_{1/3} ( (2/3) x^{3/2} ) + J_{−1/3} ( (2/3) x^{3/2} ) \x06 .
>   (b) The function Ai(x) extends to an entire function of order 3/2.
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power
> series for Ai. Compare also with Problem 1, Chapter 4.]

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/E-SSappA.PR-3.md`

## Missing: Problem 4 — PDF pp. 361–362 (printed pp. 342–343)

> 4. Suppose F (z) = \x02_{n=0}^{∞} F_n w^n is meromorphic in a region containing the closed
> unit disc, and the only poles of F are on the unit circle at the points α1 , . . . , αk ,
> and their orders are r1 , . . . , rk respectively. Then for some ǫ > 0
>     F_n = \x02_{j=1}^{k} P_j (n) + O(e^{−ǫn})   as n → ∞.
> Here
>     P_j (n) = (1/(r_j − 1)!) (d/dw)^{r_j −1} [ (w − α_j)^{r_j} w^{−n−1} F (w) ]_{w=α_j} .
> Note that each P_j is of the form P_j (n) = A_j (α_j^{−1} n)^{r_j −1} + O(n^{r_j −2}).
>   To prove this, use the residue formula (Theorem 1.4, Chapter 3).

(The OCR prints `F (z) = \x02 Fn w^n` and, in the exponent, `F_n`; the printed symbol is `w^n` in
the series and `F_n` for the coefficient — I flag this because the OCR literally shows `Fn w`.)

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/E-SSappA.PR-4.md`

## Missing: Problem 5 — PDF p. 362 (printed p. 343) — **starred in print**

> 5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose
> from the fact that while f1 (z) = (z/i)^{1/2} e^{iπ/12z} e^{iπz/12} is a good approximation to the
> generating function f (z) near z = 0, this fails near other points on the real axis,
> since f1 is regular there, but f is not.
>   However, using the transformation law (24) and the identity f (z + 1) = f (z),
> one can derive the following generalization of (24): whenever p/q is a rational
> number in lowest form (so p and q are relatively prime) then
>     f (z − p/q) = ω_{p/q} [ (zq/i)^{1/2} e^{iπ/12zq} e^{iπz q/12} ] f ( −1/zq² − p′/q ),
> where pp′ ≡ 1 mod q. Here ω_{p/q} is an appropriate 24th root of unity. This formula
> leads to an analogous f_{p/q} , approximating f at z = p/q.
>   From this one can obtain for each p/q a contribution of the form
>     c_{p/q} (1/2π²) d/dn \x05 e^{(K/q)(n−1/24)^{1/2}} / (n − 1/24)^{1/2} \x06
> to the asymptotic formula for p(n). When suitably modified, the resulting series,
> summed over all proper fractions p/q in [0, 1), actually converges and gives an
> exact formula for p(n).

(The transformation-law display is the most mangled line in this section — OCR gives
`\x05 p \x06 ... \x05 zq 12zq / iπ iπz 2 − 12 ...\x06`; the bracketed transcription above is a reading,
not a literal copy. Anyone transcribing this card should re-read the page image.)

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch-appA-problems/E-SSappA.PR-5.md`

## Checked and complete in this appendix

Appendix A prints **no Exercises section** (its sections are 1 Bessel functions, 2 Laplace's method;
Stirling's formula, 3 The Airy function, 4 The partition function, 5 Problems). Appendix B
(printed pp. 344–364 = PDF 363–383) prints **no Exercises and no Problems** heading on any page;
its sections are `1. Equivalent formulations of simple connectivity` and `2. The Jordan curve
theorem`.

Scope: item presence only; statements above are transcribed from OCR, not from page images.
