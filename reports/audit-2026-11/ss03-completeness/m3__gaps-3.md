# Chapter 3 — Meromorphic Functions and the Logarithm: gaps

Printed sets: `8 Exercises` on printed pp. 103–108 (PDF 122–127); `9 Problems` on printed
pp. 108–110 (PDF 127–129).
Cards on disk: `ch3-exercises/` = 22 (E-SS3.EX-1..22); `ch3-problems/` = **2** (E-SS3.PR-1,
E-SS3.PR-2).

## Exercises: printed 1..22, cards 1..22 — no missing items

Tail test: the last printed item is "22. Show that there is no holomorphic function f in the unit
disc D that extends continuously to ∂D such that f (z) = 1/z for z ∈ ∂D." (PDF 127 = printed 108);
the heading `9 Problems` follows it on the same page, so the set ends at 22.
Numeral continuity: 1, 2, …, 22 all present, no break (script, `evidence.md`).

## Problems: printed 1..5, cards 1..2 — THREE MISSING

Tail test: the last printed item is problem 5\* (PDF 129 = printed 110), followed by the chapter-4
title page (PDF 130 = printed 111). Nothing is truncated at the top end — the card directory stops
early, at problem 2, and problems 3, 4, 5 were never carded.

## Missing: Chapter 3, Problem 3

* Book page: **PDF 128 = printed 109**.
* Destination: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`
* Starred in print: **no**.
* Printed statement (OCR, PDF 128; the fractions are displayed formulas that the OCR linearises —
  the reading in words follows):

> 3. If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has a pole of
> order k at z0 , then we can write
> f (z) = a−k /(z − z0 )k + · · · + a−1 /(z − z0 ) + g(z)
> where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this expansion
> that holds even if z0 is an essential singularity. This is a special case of the Laurent series
> expansion, which is valid in an even more general setting.
> Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 } where
> 0 < r1 < r2 . Then,
> f (z) = Σ (n = −∞ … ∞) an (z − z0 )n
> where the series converges absolutely in the interior of the annulus. To prove this, it suffices
> to write
> f (z) = (1/2πi) ∫Cr2 f (ζ)/(ζ − z) dζ − (1/2πi) ∫Cr1 f (ζ)/(ζ − z) dζ
> when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2. Here Cr1 and Cr2
> are the circles bounding the annulus.

Raw OCR of the first and last lines, for verification:
`3. If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has`
… `when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2.`
The card should be titled for the Laurent expansion on an annulus; the disc expansion of the first
paragraph is stated as the known special case, not as the content.

## Missing: Chapter 3, Problem 4∗

* Book page: **PDF 129 = printed 110**.
* Destination: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`
* Starred in print: **yes** (`4.∗`).
* Printed statement (OCR, PDF 129):

> 4.∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects Ω. Assume
> that Ω ∩ L is an interval I. Choosing an orientation for L, we can define Ωl and Ωr to be the
> subregions of Ω lying strictly to the left or right of L, with Ω = Ωl ∪ I ∪ Ωr a disjoint
> union. If Ωl and Ωr are simply connected, then Ω is simply connected.

## Missing: Chapter 3, Problem 5∗

* Book page: **PDF 129 = printed 110**.
* Destination: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`
* Starred in print: **yes** (`5.∗`).
* Printed statement (OCR, PDF 129; the integral sign is OCR'd as `\u0001`, restored as ∫):

> 5.∗ Let
> g(z) = (1/2πi) ∫ (−M … M) h(x)/(x − z) dx
> where h is continuous and supported in [−M, M].
> (a) Prove that the function g is holomorphic in C − [−M, M], and vanishes at infinity, that is,
> lim|z|→∞ |g(z)| = 0. Moreover, the “jump” of g across [−M, M] is h, that is,
> h(x) = lim (ε → 0, ε > 0) g(x + iε) − g(x − iε).
> [Hint: Express the difference g(x + iε) − g(x − iε) in terms of a convolution of h with the
> Poisson kernel.]
> (b) If h satisfies a mild smoothness condition, for instance a Hölder condition with exponent α,
> that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all x, y ∈ [−M, M], then g(x + iε) and
> g(x − iε) converge uniformly to functions g+ (x) and g− (x) as ε → 0. Then, g can be
> characterized as the unique holomorphic function that satisfies:
> (i) g is holomorphic outside [−M, M],
> (ii) g vanishes at infinity,
> (iii) g(x + iε) and g(x − iε) converge uniformly as ε → 0 to functions g+ (x) and g− (x) with
> g+ (x) − g− (x) = h(x).
> [Hint: If G is another function satisfying these conditions, g − G is entire.]

Independent corroboration that problem 5 exists, from outside the problem section itself: Chapter 4
Problem 4\* ends "See Problem 5 in Chapter 3." (PDF 152 = printed 133).

## Fidelity

Numbering only was audited. The starred markers are not represented in the two existing
`ch3-problems` cards and would be lost by the two new ones too unless the convention is decided —
see `fidelity-notes.md`.
