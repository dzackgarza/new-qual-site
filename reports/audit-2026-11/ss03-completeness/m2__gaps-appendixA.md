# SRC-TEXT-SS03 — gap report, Appendix A (Asymptotics)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer).
Pages are cited as **PDF p.X (printed p.Y)**; on these pages Y = X − 19 (checked against the printed folios).

Method: whole-book `pdftotext` extraction in reading order and with `-layout`; section boundary taken from
the printed heading "5 Problems" (PDF p.360, printed 341); item numbers by a monotone 1..N scan excluding
the running head "5. Problems"; both extractions agree. Quotes are verbatim OCR. Nothing under `corpus/`
was modified.

## Printed inventory

| section | heading | printed pages | printed items | cards present | missing |
|---|---|---|---|---|---|
| 5 Problems | PDF p.360 (printed 341) | printed 341–343 | **1–5** | **0 — no card directory exists** | **PR-1 … PR-5** |

`corpus/collections/SRC-TEXT-SS03/` contains `ch1-exercises` … `ch10-problems` only; there is no appendix
directory, and `index.md` has no section for Appendix A. Appendix A prints no Exercises section, only
Problems 1–5. (Appendix B, printed pp.344–364, prints no exercise or problem section at all — see
`gaps-summary.md`.)

Suggested destination, since the id scheme `E-SS<chapter>.<kind>-<n>` has no appendix convention:
`corpus/collections/SRC-TEXT-SS03/appendixA-problems/` with ids `E-SSA.PR-1` … `E-SSA.PR-5`.

## Missing items (5) — printed statements, OCR verbatim

### `E-SSA.PR-1` — PDF p.360 (printed p.341), runs to printed p.342
> "1. Let η be an indefinitely diﬀerentiable function supported in a finite interval, so that η(x) = 1 for x
> near 0. Then, if m > −1 and N > 0, ∫_0^∞ e^{−sx} x^m η(x) dx = s^{−m−1} Γ(m + 1) + O(s^{−N}) for
> Re(s) ≥ 0, |s| → ∞. (a) Consider first the case −1 < m ≤ 0. It suﬃces to see that
> ∫_0^∞ e^{−sx} x^m (1 − η(x)) dx = O(s^{−N}), and this can be done by repeated integration by parts since
> e^{−sx} = (−1)^N s^{−N} (d/dx)^N (e^{−sx}). (b) To extend this to all m, find an integer k so that
> k − 1 < m ≤ k, write ∫ (d/dx)^k (x^m) e^{−sx} η(x) dx = c_{k,m} s^{−m+k−1} + O(s^{−N}), and integrate by
> parts k times."

(OCR damage: the last display prints as "∫ $ d dx k % m (x ) e−sx η(x) dx = ck,m s−m+k−1 + O(s−N )";
the power x^m and the brackets are garbled there.)

### `E-SSA.PR-2` — PDF p.361 (printed p.342)
> "2. The following is a more precise version of Stirling's formula. There are real constant a1 = 1/12,
> a2 , . . ., an , . . ., so that for every N > 0 Γ(s) = e^{s log s −s} / (√(2π) s^{1/2}) ·
> (1 + ∑_{j=1}^{N} aj s^{−j} + O(s^{−N})) when s ∈ Sδ . This can be proved by using the results of Problem 1
> in place of Proposition 1.3."

### `E-SSA.PR-3` — PDF p.361 (printed p.342)
> "3. The Bessel functions and Airy function have the following power series expansions:
> Jν(x) = (x/2)^ν ∑_{m=0}^∞ (−1)^m (x^2/4)^m / (m! Γ(ν + m + 1)),
> Ai(−x) = (1/π) ∑_{n=0}^∞ (x^n/n!) sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3).
> (a) From this, verify that when x > 0, Ai(−x) = (x^{1/2}/3)(J_{1/3}((2/3)x^{3/2}) +
> J_{−1/3}((2/3)x^{3/2})). (b) The function Ai(x) extends to an entire function of order 3/2.
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for Ai.
> Compare also with Problem 1, Chapter 4.]"

### `E-SSA.PR-4` — PDF p.361 (printed p.342), runs to printed p.343
> "4. Suppose F (z) = ∑_{n=0}^∞ Fn w^n is meromorphic in a region containing the closed unit disc, and the
> only poles of F are on the unit circle at the points α1 , . . . , αk , and their orders are r1 , . . . , rk
> respectively. Then for some ǫ > 0 Fn = ∑_{j=1}^{k} Pj(n) + O(e^{−ǫn}) as n → ∞. Here
> Pj(n) = (1/(rj − 1)!) (d/dw)^{rj−1} ((w − αj)^{rj} w^{−n−1} F(w))|_{w=αj} . Note that each Pj is of the
> form Pj(n) = Aj (αj^{−1} n)^{rj−1} + O(n^{rj−2}). To prove this, use the residue formula (Theorem 1.4,
> Chapter 3)."

(OCR damage: the first display prints as "F (z) = ∞ n=0 Fn w" — argument and exponent lost; the poles on the
unit circle and the coefficient formula show the statement is about F(w) = ∑ Fn w^n.)

### `E-SSA.PR-5` — PDF p.362 (printed p.343)
> "5.∗ The one shortcoming in our derivation of the asymptotic formula for p(n) arose from the fact that while
> f1(z) = z/i · e^{iπ/12z} e^{iπz/12} is a good approximation to the generating function f(z) near z = 0,
> this fails near other points on the real axis, since f1 is regular there, but f is not. However, using the
> transformation law (24) and the identity f(z + 1) = f(z), one can derive the following generalization of
> (24): whenever p/q is a rational number in lowest form (so p and q are relatively prime) then
> f(z − p/q) = ω_{p/q} √(i/zq) e^{(iπ/12zq) − (iπzq)/12} f(−1/(zq^2) − p′/q), where pp′ = 1 mod q. Here
> ω_{p/q} is an appropriate 24th root of unity. This formula leads to an analogous f_{p/q}, approximating f
> at z = p/q. From this one can obtain for each p/q a contribution of the form
> (c_{p/q}/(2π√2)) (d/dn) ( e^{K(n − 1/24)^{1/2}} / (n − 1/24)^{1/2} ) to the asymptotic formula for p(n).
> When suitably modified, the resulting series, summed over all proper fractions p/q in [0, 1), actually
> converges and gives an exact formula for p(n)."

(Starred in print: "5.∗". The OCR mangles the two exponential factors and the 24th-root factor; the quotation
above repairs only the clearly recoverable structure, as flagged.)
