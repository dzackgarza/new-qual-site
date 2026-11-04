# Appendix A: Asymptotics — gap report (SRC-TEXT-SS03)

**Source of truth.** `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR'd).
The whole file was extracted with `pdftotext -layout`; the whole-book page map was then taken
from the printed Contents (PDF pp.12-15). Offset: **PDF page = printed page + 19** (checked at
several anchors: printed "4 Exercises 24" -> PDF 43; printed p.32 opens Chapter 2 -> PDF 51;
printed p.318 opens Appendix A -> PDF 337). Quotations below are the OCR as it comes out,
including its mangling of symbols; I say where the OCR is ambiguous.

## 1. Printed inventory of this chapter

| section | heading line | printed pp. | PDF pp. | printed items | starred |
|---|---|---|---|---|---|
| Exercises | — none printed — | — | — | 0 | — |
| Problems | `5 Problems` (p.341) | 341-343 | 360-362 | 1-5 (5 items) | 5* |

The Contents (PDF p.15) lists for Appendix A only `5 Problems 341`; the appendix has no exercise
section. Appendix B (printed pp.344-364) prints neither exercises nor problems: the whole-book scan
for `Exercises`/`Problems` section headings finds exactly 20 such headings in the book (10 exercise
sections, ch1-ch10; 9 problem sections, ch2-ch10; 1 problem section in Appendix A), and none in
Appendix B.

## 2. Cards on disk (re-derived from the filesystem, not from the brief)

| directory | files | numbers |
|---|---|---|
| `chA-problems/` (or whatever name the collection chooses for appendices) | **absent** | — |

There is no directory for the appendix in `corpus/collections/SRC-TEXT-SS03/`, and `index.md`
declares no `ChA Problems` section. Whether the collection is meant to cover the appendices is a
scope decision for a human; if it is, all five problems are missing.

## 3. Missing items

**All five problems of Appendix A have no card: PR-1 .. PR-5 (5 is starred).** Cards, if wanted,
would go to `corpus/collections/SRC-TEXT-SS03/chA-problems/E-SSA.PR-<n>.md` (the chapter
directory name for appendices is not fixed by any existing convention in this collection).

### appA problem 1 — printed pp.341-342 (PDF pp.360-361), not starred
> Let η be an indefinitely differentiable function supported in a finite interval, so that
> η(x) = 1 for x near 0. Then, if m > −1 and N > 0,
> ∫_0^∞ e^{−sx} x^m η(x) dx = s^{−m−1} Γ(m + 1) + O(s^{−N})
> for Re(s) ≥ 0, |s| → ∞.
> (a) Consider first the case −1 < m ≤ 0. It suffices to see that
> ∫_0^∞ e^{−sx} x^m (1 − η(x)) dx = O(s^{−N}), and this can be done by repeated integration by
> parts since e^{−sx} = (−1)^N s^{−N} (d/dx)^N (e^{−sx}).
> (b) To extend this to all m, find an integer k so that k − 1 < m ≤ k, write
> ∫ (d/dx)^k (x^m) e^{−sx} η(x) dx = c_{k,m} s^{−m+k−1} + O(s^{−N}), and integrate by parts k times.
(The OCR of (b) is garbled — ` $ k %` — and the exact powers must be read off the page.)

### appA problem 2 — printed p.342 (PDF p.361), not starred
> The following is a more precise version of Stirling's formula. There are real constant a1 = 1/12,
> a2 , . . ., an , . . ., so that for every N > 0
> Γ(s) = e^{s log s} e^{−s} √(2π)/s^{1/2} (1 + Σ_{j=1}^{N} aj s^{−j} + O(s^{−N})) when s ∈ Sδ.
> This can be proved by using the results of Problem 1 in place of Proposition 1.3.

### appA problem 3 — printed p.342 (PDF p.361), not starred
> The Bessel functions and Airy function have the following power series expansions:
> Jν (x) = (x/2)^ν Σ_{m=0}^{∞} ((−1)^m (x^2/4)^m) / (m! Γ(ν + m + 1)),
> Ai(−x) = (1/π) Σ_{n=0}^{∞} (x^n / n!) sin(2π(n + 1)/3) 3^{n/3−2/3} Γ(n/3 + 1/3).
> (a) From this, verify that when x > 0,
> Ai(−x) = x^{1/2}/3 (J_{1/3}((2/3)x^{3/2}) + J_{−1/3}((2/3)x^{3/2})).
> (b) The function Ai(x) extends to an entire function of order 3/2.
> [Hint: For (b), use (a), or alternatively, apply Problem 4 in Chapter 5 to the power series for
> Ai. Compare also with Problem 1, Chapter 4.]

### appA problem 4 — printed p.342 (PDF p.361), not starred
> Suppose F (z) = Σ_{n=0}^{∞} Fn w^n is meromorphic in a region containing the closed unit disc,
> and the only poles of F are on the unit circle at the points α1 , . . . , αk , and their orders
> are r1 , . . . , rk respectively. Then for some ǫ > 0
> Fn = Σ_{j=1}^{k} Pj (n) + O(e^{−ǫn}) as n → ∞.
> Here Pj (n) = (1/(rj − 1)!) (d/dw)^{rj −1} ((w − αj )^{rj} w^{−n−1} F (w))|_{w=αj}.
> Note that each Pj is of the form Pj (n) = Aj (αj^{−1} n)^{rj −1} + O(n^{rj −2}).
> To prove this, use the residue formula (Theorem 1.4, Chapter 3).
(The printed `F(z) = Σ Fn w^n` versus `F` appearing again as the meromorphic function is the
book's own inconsistency; the OCR shows `F (z) = ∞ n=0 Fn w n`.)

### appA problem 5 — printed p.343 (PDF p.362), **starred** (`5.∗`)
> The one shortcoming in our derivation of the asymptotic formula for p(n) arose from the fact that
> while f1 (z) = √(z/i) e^{iπ/12z} e^{iπz/12} is a good approximation to the generating function
> f (z) near z = 0, this fails near other points on the real axis, since f1 is regular there, but f
> is not.
> However, using the transformation law (24) and the identity f (z + 1) = f (z), one can derive the
> following generalization of (24): whenever p/q is a rational number in lowest form (so p and q
> are relatively prime) then
> f (z − p/q) = ω_{p/q} √(zq/i) e^{iπ/12zq} e^{iπzq^{2}/12} f(−1/(zq^{2}) − p′/q),
> where pp′ ≡ 1 mod q. Here ω_{p/q} is an appropriate 24th root of unity. This formula leads to an
> analogous f_{p/q} , approximating f at z = p/q.
> From this one can obtain for each p/q a contribution of the form
> c_{p/q} (1/2π^2) (d/dn) ( e^{(K/q)(n − 1/24)^{1/2}} / (n − 1/24)^{1/2} )
> to the asymptotic formula for p(n). When suitably modified, the resulting series, summed over all
> proper fractions p/q in [0, 1), actually converges and gives an exact formula for p(n).
(The OCR of the transformation law is badly broken — `zq 12zq iπ iπz 2 − 12` on several lines —
and the exponents must be read off the page.)

## 4. Statement-fidelity notes (cheap checks only)

Nothing to compare: no card exists for any Appendix A item.

## 5. Scope of this conclusion

Complete for existence and numbering of Appendix A's problem section (5 printed, 0 cards).
Not checked: the appendix body text; proof of any kind. Appendix B (pp.344-364) was checked only
for the existence of exercise/problem sections (there are none) and is otherwise unaudited.
