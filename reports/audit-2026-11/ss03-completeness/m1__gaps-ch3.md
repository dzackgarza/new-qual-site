# Gaps — Chapter 3 (SRC-TEXT-SS03)

> **Concurrent update (16:18, during this audit).** When the item census ran, `ch3-problems`
> held only `E-SS3.PR-1` and `E-SS3.PR-2`. While I was writing this file another worker created
> `E-SS3.PR-3.md`, `E-SS3.PR-4.md` and `E-SS3.PR-5.md` (untracked in git, mtime 16:18:20). I did
> not write them and have not touched them; I read their `.exercise` blocks and they transcribe
> the printed items 3, 4, 5 faithfully (PR-4 and PR-5 keep the two printed hints). Neither new
> card records the printed asterisk on problems 4\* and 5\*. So the three gaps below were real at
> census time and are now, as far as I can see, filled.

Pages are PDF pages of `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`; printed page =
PDF page − 19 (see `source-integrity.md` §1). Quotes are the OCR text as `pdftotext -layout`
produces it: `\x02` = ∑, `\x01` = ∫, `ǫ` for ε, `Ω`/`Ω` vary. No card was edited.

Printed section: **`9 Problems`, printed pp. 108–110 = PDF 127–129**, items **1–5**.
Cards on disk: `ch3-problems/E-SS3.PR-1.md`, `E-SS3.PR-2.md` only.

## Missing: Problem 3 — PDF p. 128 (printed p. 109)

> 3. If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has
> a pole of order k at z0 , then we can write
>     f (z) = a−k/(z − z0 )^k + · · · + a−1/(z − z0 ) + g(z)
> where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this
> expansion that holds even if z0 is an essential singularity. This is a special case of
> the Laurent series expansion, which is valid in an even more general setting.
>   Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 }
> where 0 < r1 < r2 . Then,
>     f (z) = \x02_{n=−∞}^{∞} an (z − z0 )^n
> where the series converges absolutely in the interior of the annulus. To prove this,
> it suﬃces to write
>     f (z) = (1/2πi)∫_{Cr2} f (ζ)/(ζ − z) dζ − (1/2πi)∫_{Cr1} f (ζ)/(ζ − z) dζ
> when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2.
> Here Cr1 and Cr2 are the circles bounding the annulus.

(OCR: the triple dots are the printed `\cdots`; the two integral signs are U+0001.)

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md`

## Missing: Problem 4 — PDF p. 129 (printed p. 110) — **starred in print**

> 4.∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects
> Ω. Assume that Ω ∩ L is an interval I. Choosing an orientation for L, we can define
> Ωl and Ωr to be the subregions of Ω lying strictly to the left or right of L, with
> Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are simply connected, then Ω is
> simply connected.

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md`
(the asterisk is part of the printed item; only `ch2-problems/E-SS2.PR-5.md` currently records
such a mark, in a prose note — no card carries a star field).

## Missing: Problem 5 — PDF p. 129 (printed p. 110) — **starred in print, two parts + two hints**

> 5.∗ Let
>     g(z) = (1/2πi) \x01_{−M}^{M} h(x)/(x − z) dx
> where h is continuous and supported in [−M, M ].
>   (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes
>       at infinity, that is, lim|z|→∞ |g(z)| = 0. Moreover, the “jump” of g across
>       [−M, M ] is h, that is,
>     h(x) = lim_{ǫ→0,ǫ>0} g(x + iǫ) − g(x − iǫ).
>       [Hint: Express the diﬀerence g(x + iǫ) − g(x − iǫ) in terms of a convolution
>       of h with the Poisson kernel.]
>   (b) If h satisfies a mild smoothness condition, for instance a Hölder condition
>       with exponent α, that is, |h(x) − h(y)| ≤ C|x − y|^α for some C > 0 and all
>       x, y ∈ [−M, M ], then g(x + iǫ) and g(x − iǫ) converge uniformly to functions
>       g+ (x) and g− (x) as ǫ → 0. Then, g can be characterized as the unique
>       holomorphic function that satisfies:
>            (i) g is holomorphic outside [−M, M ],
>           (ii) g vanishes at infinity,
>          (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x)
>                and g− (x) with g+ (x) − g− (x) = h(x).
>       [Hint: If G is another function satisfying these conditions, g − G is entire.]

Card should go to: `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md`

## Checked and complete in this chapter

* Chapter 3 **Exercises** (`8 Exercises`, printed pp. 103–107 = PDF 122–126, items **1–22**):
  cards `E-SS3.EX-1 … E-SS3.EX-22` exist, 22/22, numbers contiguous on the page.
* `Problem 2` on disk is the printed Poisson-integral problem (p. 109) and `Problem 1` is the
  Koebe–Bieberbach problem (p. 108) — no misnumbering of the two existing cards.

Scope: item presence only. I did not compare card statements to the printed wording for this
chapter (that axis is another member's).
