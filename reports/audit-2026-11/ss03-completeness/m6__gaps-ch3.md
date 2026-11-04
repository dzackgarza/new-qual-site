# Chapter 3 (Meromorphic Functions and the Logarithm) — gaps

> **Status note (added after the audit).** When this audit was run, `ch3-problems` held only
> PR-1 and PR-2. A later applying pass has since added `E-SS3.PR-3.md`, `E-SS3.PR-4.md` and
> `E-SS3.PR-5.md`; I re-read them against the printed items quoted below and their statements
> match (E-SS3.PR-3 restores `a_{-k}/(z-z_0)^k + ⋯ + a_{-1}/(z-z_0) + g(z)`, E-SS3.PR-5 keeps
> both printed hints). The gap described here is therefore closed; the quotations remain the
> reference for what the print says.

Printed sections:
* `8 Exercises`, PDF 122–127 (printed pp. 103–108), items 1–22, contiguous.
  Item 22 is on PDF 127 (printed 108), the page on which `9 Problems` begins.
* `9 Problems`, PDF 127–129 (printed pp. 108–110), items 1–5, contiguous
  (1∗, 4∗, 5∗ starred).

Cards on disk: `ch3-exercises` EX-1 … EX-22 (**22 = 22, no exercise gap**) and
`ch3-problems` PR-1, PR-2 only (**2 of 5**).

## Missing items: printed Problems 3, 4, 5 — three cards

I checked that the two cards that do exist are correctly numbered: E-SS3.PR-1 is the printed
`1.∗ Consider a holomorphic map on the unit disc f : D → C which satisfies f (0) = 0. …`
(Koebe–Bieberbach, parts (a)–(g)) and E-SS3.PR-2 is the printed
`2. Let u be a harmonic function in the unit disc that is continuous on its closure. Deduce
Poisson's integral formula …`. So the missing ones are exactly printed 3, 4, 5.

---
### Chapter 3, Problem 3 — PDF p. 128–129 (printed p. 109–110)

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`

Printed statement (OCR, verbatim; line breaks collapsed, the OCR's fraction order in the
first display is garbled — it reads `a−1 … a−k` where the printed display presumably is
$a_{-k}/(z-z_0)^k+\cdots+a_{-1}/(z-z_0)+g(z)$, and I make no claim about the order):

> 3. If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has
> a pole of order k at z0 , then we can write
> f (z) = a−1/(z − z0) + · · · + a−k/(z − z0 )k + g(z)
> where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this
> expansion that holds even if z0 is an essential singularity. This is a special case of
> the Laurent series expansion, which is valid in an even more general setting.
> Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 }
> where 0 < r1 < r2 . Then,
> f (z) = Σ (n = −∞ … ∞) an (z − z0 )n
> where the series converges absolutely in the interior of the annulus. To prove this,
> it suffices to write
> f (z) = (1/2πi) ∫Cr2 f (ζ)/(ζ − z) dζ − (1/2πi) ∫Cr1 f (ζ)/(ζ − z) dζ
> when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2.
> Here Cr1 and Cr2 are the circles bounding the annulus.

Suggested title: “Laurent expansion in an annulus”.

---
### Chapter 3, Problem 4 — PDF p. 129 (printed p. 110). Starred in print.

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`

Printed statement (OCR, verbatim):

> 4.∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects
> Ω. Assume that Ω ∩ L is an interval I. Choosing an orientation for L, we can define
> Ωl and Ωr to be the subregions of Ω lying strictly to the left or right of L, with
> Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are simply connected, then Ω is
> simply connected.

Suggested title: “Gluing two simply connected regions along a cross-cut”.

---
### Chapter 3, Problem 5 — PDF p. 129 (printed p. 110). Starred in print.

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`

Printed statement (OCR, verbatim except the display, which the OCR scatters):

> 5.∗ Let
> g(z) = (1/2πi) ∫(−M … M) h(x)/(x − z) dx
> where h is continuous and supported in [−M, M ].
> (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes
> at infinity, that is, lim|z|→∞ |g(z)| = 0. Moreover, the “jump” of g across
> [−M, M ] is h, that is,
> h(x) = lim (ǫ→0,ǫ>0) g(x + iǫ) − g(x − iǫ).
> [Hint: Express the difference g(x + iǫ) − g(x − iǫ) in terms of a convolution
> of h with the Poisson kernel.]
> (b) If h satisfies a mild smoothness condition, for instance a Hölder condition
> with exponent α, that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all
> x, y ∈ [−M, M ], then g(x + iǫ) and g(x − iǫ) converge uniformly to functions
> g+ (x) and g− (x) as ǫ → 0. Then, g can be characterized as the unique
> holomorphic function that satisfies:
> (i) g is holomorphic outside [−M, M ],
> (ii) g vanishes at infinity,
> (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x)
> and g− (x) with g+ (x) − g− (x) = h(x).
> [Hint: If G is another function satisfying these conditions, g − G is entire.]

Suggested title: “Jump formulas for a Cauchy-type integral (Sokhotski–Plemelj)”.

Note: both hints are part of the printed statement and must be carried into the new cards.
