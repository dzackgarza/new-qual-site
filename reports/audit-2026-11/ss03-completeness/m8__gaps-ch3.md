# Chapter 3: Meromorphic Functions and the Logarithm — gap report (SRC-TEXT-SS03)

**Source of truth.** `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR'd).
The whole file was extracted with `pdftotext -layout`; the whole-book page map was then taken
from the printed Contents (PDF pp.12-15). Offset: **PDF page = printed page + 19** (checked at
several anchors: printed "4 Exercises 24" -> PDF 43; printed p.32 opens Chapter 2 -> PDF 51;
printed p.318 opens Appendix A -> PDF 337). Quotations below are the OCR as it comes out,
including its mangling of symbols; I say where the OCR is ambiguous.

## 1. Printed inventory of this chapter

| section | heading line | printed pp. | PDF pp. | printed items | starred |
|---|---|---|---|---|---|
| Exercises | `8 Exercises` (p.103) | 103-108 | 122-127 | 1-22 (22 items) | none |
| Problems | `9 Problems` (p.108) | 108-110 | 127-129 | 1-5 (5 items) | 1*, 4*, 5* |

Exercise 22 is printed on p.108 **above** the `9 Problems` heading, on the same page.

## 2. Cards on disk (re-derived from the filesystem, not from the brief)

| directory | files | numbers |
|---|---|---|
| `ch3-exercises/` | 22 | E-SS3.EX-1 .. E-SS3.EX-22 |
| `ch3-problems/` | **2** | E-SS3.PR-1, E-SS3.PR-2 |

## 3. Missing items

**Three problems have no card: PR-3, PR-4 (starred) and PR-5 (starred).** Chapter 3 prints
5 problems and the corpus holds 2.

The collection's own manifest (`corpus/collections/SRC-TEXT-SS03/index.md`) lists "Ch3 Problems"
with only `PR-1` and `PR-2` while declaring `completion: complete`, so the manifest agrees with
the missing files and disagrees with the book.

### ch3 problem 3 — printed p.109 (PDF p.128), not starred
Printed text (OCR, verbatim; `dζ`/fraction bars come out garbled):
> If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has a pole of order
> k at z0 , then we can write
> f (z) = a−k/(z − z0)k + · · · + a−1/(z − z0) + g(z)
> where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this expansion
> that holds even if z0 is an essential singularity. This is a special case of the Laurent series
> expansion, which is valid in an even more general setting.
> Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 } where
> 0 < r1 < r2 . Then, f (z) = Σ_{n=−∞}^{∞} an (z − z0 )n where the series converges absolutely in
> the interior of the annulus. To prove this, it suffices to write
> f (z) = (1/2πi)∫_{Cr2} f (ζ)/(ζ − z) dζ − (1/2πi)∫_{Cr1} f (ζ)/(ζ − z) dζ
> when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2. Here Cr1 and Cr2
> are the circles bounding the annulus.

Target: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`

### ch3 problem 4 — printed p.110 (PDF p.129), **starred** (`4.∗`)
> Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects Ω. Assume
> that Ω ∩ L is an interval I. Choosing an orientation for L, we can define Ωl and Ωr to be the
> subregions of Ω lying strictly to the left or right of L, with Ω = Ωl ∪ I ∪ Ωr a disjoint
> union. If Ωl and Ωr are simply connected, then Ω is simply connected.

Target: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`

### ch3 problem 5 — printed p.110 (PDF p.129), **starred** (`5.∗`)
> Let g(z) = (1/2πi)∫_{−M}^{M} h(x)/(x − z) dx where h is continuous and supported in [−M, M ].
> (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes at infinity, that is,
> lim_{|z|→∞} |g(z)| = 0. Moreover, the "jump" of g across [−M, M ] is h, that is,
> h(x) = lim_{ǫ→0,ǫ>0} g(x + iǫ) − g(x − iǫ).
> [Hint: Express the difference g(x + iǫ) − g(x − iǫ) in terms of a convolution of h with the
> Poisson kernel.]
> (b) If h satisfies a mild smoothness condition, for instance a Hölder condition with exponent α,
> that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all x, y ∈ [−M, M ], then g(x + iǫ) and
> g(x − iǫ) converge uniformly to functions g+ (x) and g− (x) as ǫ → 0. Then, g can be
> characterized as the unique holomorphic function that satisfies:
> (i) g is holomorphic outside [−M, M ], (ii) g vanishes at infinity, (iii) g(x + iǫ) and
> g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x) and g− (x) with g+ (x) − g− (x) = h(x).
> [Hint: If G is another function satisfying these conditions, g − G is entire.]

Target: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`

## 4. Statement-fidelity notes (cheap checks only)

Screened all 24 existing cards for a dropped `[Hint ...]`: none lost. Notes:

- The corpus holds only problems 1 and 2 of the five (problem 1 is starred in the print: `1.∗
  Consider a holomorphic map on the unit disc ...`; problem 2 is not starred). The three absent
  problems are 3 (unstarred) and 4*, 5*, so the missing cards include both starred ones, i.e. the
  harder half of the section.
- Exercise 22 is printed above the Problems heading on p.108; its card exists as EX-22, i.e. it
  was not mistaken for a problem. Good.

No other statement comparison was made for this chapter.

## 5. Scope of this conclusion

Complete for existence and numbering of both sections (27 printed items, 24 cards).
Not checked: statement wording of the 24 existing cards except the hint screen; proofs.
