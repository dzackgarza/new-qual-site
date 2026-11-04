# SRC-TEXT-SS03 — gap report, Chapter 3 (Meromorphic Functions and the Logarithm)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer).
Pages are cited as **PDF p.X (printed p.Y)**; throughout the exercise/problem pages Y = X − 19.

Method: whole-book `pdftotext` extraction in reading order and with `-layout`; section boundaries from the
printed headings; item numbers by a monotone 1..N scan excluding the running heads (`8. Exercises`,
`9. Problems`); both extractions agree on every count. Quotes are verbatim OCR — symbols are mangled by
the OCR (∑, ∫, subscripts, exponents); the flattening of displayed formulas is the OCR's, not mine.

## Printed inventory

| section | heading | printed pages | printed items | cards present | missing |
|---|---|---|---|---|---|
| 8 Exercises | PDF p.122 (printed 103) | printed 103–108 | 1–22 | 22 (`E-SS3.EX-1`..`22`) | none |
| 9 Problems | PDF p.127 (printed 108) | printed 108–110 | **1–5** | 2 (`E-SS3.PR-1`, `PR-2`) | **PR-3, PR-4, PR-5** |

Evidence: exercise 22 is the last item on printed p.108, immediately above the "9 Problems" heading;
the problems run 1–5 on printed pp.108–110 and are followed by the title page of Chapter 4
(PDF p.130, printed 111). The book's own text cross-refers to this section's problem 5:
printed p.133 (PDF p.152) reads "… f̂ (x) = lim ǫ→0,ǫ>0 g(x + iǫ) − g(x − iǫ). **See Problem 5 in
Chapter 3.**" — so a printed problem 5 certainly exists.

## Missing items (3)

### 1. `E-SS3.PR-3`
* Card path: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`
* Book page: **PDF p.128 (printed p.109)**, text runs onto printed p.110.
* Not starred.
* Printed statement (OCR verbatim, line breaks normalised):

> "3. If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has a pole of order k
> at z0 , then we can write f (z) = a−1 a−k + g(z) + · · · + (z − z0 )k (z − z0 ) where g is holomorphic in
> the disc {|z − z0 | < r}. There is a generalization of this expansion that holds even if z0 is an
> essential singularity. This is a special case of the Laurent series expansion, which is valid in an even
> more general setting. Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 }
> where 0 < r1 < r2 . Then, f (z) = ∞ ∑ n=−∞ an (z − z0 )n where the series converges absolutely in the
> interior of the annulus. To prove this, it suﬃces to write f (z) = (1/2πi)∫_{Cr2} f (ζ)/(ζ − z) dζ −
> (1/2πi)∫_{Cr1} f (ζ)/(ζ − z) dζ when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4,
> Chapter 2. Here Cr1 and Cr2 are the circles bounding the annulus."

(The displayed fractions are flattened by the OCR: the first display is the principal part
a−k/(z−z0)^k + … + a−1/(z−z0); the last is the difference of the two circle integrals.)

### 2. `E-SS3.PR-4`
* Card path: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`
* Book page: **PDF p.129 (printed p.110)**.
* Starred in print ("4.∗").
* Printed statement (OCR verbatim):

> "4.∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects Ω. Assume that
> Ω ∩ L is an interval I. Choosing an orientation for L, we can define Ωl and Ωr to be the subregions of Ω
> lying strictly to the left or right of L, with Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are
> simply connected, then Ω is simply connected."

### 3. `E-SS3.PR-5`
* Card path: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`
* Book page: **PDF p.129 (printed p.110)**.
* Starred in print ("5.∗").
* Printed statement (OCR verbatim; the two bracketed hints are printed hints and belong in the card):

> "5.∗ Let g(z) = (1/2πi) ∫_{−M}^{M} h(x)/(x − z) dx where h is continuous and supported in [−M, M ].
> (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes at infinity, that is,
> lim|z|→∞ |g(z)| = 0. Moreover, the "jump" of g across [−M, M ] is h, that is, h(x) = lim ǫ→0,ǫ>0
> g(x + iǫ) − g(x − iǫ). [Hint: Express the diﬀerence g(x + iǫ) − g(x − iǫ) in terms of a convolution of
> h with the Poisson kernel.] (b) If h satisfies a mild smoothness condition, for instance a Hölder
> condition with exponent α, that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all x, y ∈ [−M, M ],
> then g(x + iǫ) and g(x − iǫ) converge uniformly to functions g+ (x) and g− (x) as ǫ → 0. Then, g can be
> characterized as the unique holomorphic function that satisfies: (i) g is holomorphic outside [−M, M ],
> (ii) g vanishes at infinity, (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions
> g+ (x) and g− (x) with g+ (x) − g− (x) = h(x). [Hint: If G is another function satisfying these
> conditions, g − G is entire.]"

## Statement fidelity

* `E-SS3.PR-1` and `E-SS3.PR-2` were compared with printed problems 1 and 2: both are the right items,
  part lettering (a)–(g) and (a)–(b) matches, hints preserved (`PR-1` keeps 6 of the printed hints).
* Note that `E-SS3.PR-1` is the starred printed problem "1.∗" and, like every card in the collection,
  does not record the star.
