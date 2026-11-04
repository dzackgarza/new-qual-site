# SRC-TEXT-SS03 — Chapter 3 (Meromorphic Functions and the Logarithm): missing cards

Scope: FULL check of both chapter 3 sections. The printed Exercise block (§8, PDF pages
122–127) and Problem block (§9, PDF pages 127–129) were read page by page from
`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, every top-level numbered item
transcribed, and the numbering checked for continuity (Exercises 1–22 and Problems 1–5
were all found, so no item is invisible to OCR inside the block).
Counts: printed 22 exercises / 5 problems; cards present 22 exercises / **2** problems.
PDF page = printed folio + 19.

## MISSING: 3 printed problems have no card

### 1. `E-SS3.PR-3` — PDF page 128 (printed page 109)
Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/` as `E-SS3.PR-3.md`.
Not starred in the print. Third item of the §9 block ("9 Problems", PDF p. 127); the file
`ch3-problems/` currently jumps from PR-2 (printed PDF p. 128, = printed problem 2) to
nothing, while the block continues with this item.

Printed statement, quoted from the OCR (line breaks as OCR gives them):

> If f (z) is holomorphic in the deleted neighborhood {0 < |z − z0 | < r} and has
> a pole of order k at z0 , then we can write
>
>                      a−k               a−1
>        f (z) =               + ··· +           + g(z)
>                   (z − z0 )k         (z − z0 )
>
> where g is holomorphic in the disc {|z − z0 | < r}. There is a generalization of this
> expansion that holds even if z0 is an essential singularity. This is a special case of
> the Laurent series expansion, which is valid in an even more general setting.
>   Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 }
> where 0 < r1 < r2 . Then,
>                                             ∞
>                                             Σ
>                                 f (z) =           an (z − z0 )n
>                                           n=−∞
>
> where the series converges absolutely in the interior of the annulus. To prove this, it
> suffices to write
>                               ∫                     ∫
>                             1       f (ζ)       1         f (ζ)
>                    f (z) =                dζ −                  dζ
>                           2πi Cr2 ζ − z       2πi Cr1 ζ − z
>
> when r1 < |z − z0 | < r2 , and argue as in the proof of Theorem 4.4, Chapter 2.
> Here Cr1 and Cr2 are the circles bounding the annulus.

Note on the OCR: the summation and integral limits come out displaced (the Σ appears after
its summand, "n=−∞…∞" on separate lines), and the printed `r1 ≤ |z − z0 | ≤ r2` may be
`r1 ≤ |z − z0 | ≤ r2` or `<` on the inner inequality — the OCR glyph is `≤` twice and I
could not distinguish it further. The exercise has no imperative verb: as printed, the
task is to prove the Laurent expansion in the annulus by the two-circle decomposition.

### 2. `E-SS3.PR-4` — PDF page 129 (printed page 110)
Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/` as `E-SS3.PR-4.md`.
**Starred** in the print ("4. ∗ Suppose Ω is a bounded region. …").

Printed statement (OCR verbatim):

> 4. ∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects
> Ω. Assume that Ω ∩ L is an interval I. Choosing an orientation for L, we can define
> Ωl and Ωr to be the subregions of Ω lying strictly to the left or right of L, with
> Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are simply connected, then Ω is
> simply connected.

### 3. `E-SS3.PR-5` — PDF page 129 (printed page 110)
Card should go in `corpus/collections/SRC-TEXT-SS03/ch3-problems/` as `E-SS3.PR-5.md`.
**Starred**. Final item of the chapter; PDF page 130 opens chapter 4, so 5 is the last
problem in the block.

Printed statement (OCR verbatim; two bracketed hints quoted in full):

> 5. ∗ Let
>                                                  ∫ M
>                                             1         h(x)
>                                 g(z) =                     dx
>                                            2πi     −M x −z
>
> where h is continuous and supported in [−M, M ].
>
>   (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes
>       at infinity, that is, lim|z|→∞ |g(z)| = 0. Moreover, the “jump” of g across
>       [−M, M ] is h, that is,
>
>                              h(x) =       lim      g(x + iǫ) − g(x − iǫ).
>                                          ǫ→0,ǫ>0
>
>       [Hint: Express the diﬀerence g(x + iǫ) − g(x − iǫ) in terms of a convolution
>       of h with the Poisson kernel.]
>
>   (b) If h satisfies a mild smoothness condition, for instance a Hölder condition
>       with exponent α, that is, |h(x) − h(y)| ≤ C|x − y|α for some C > 0 and all
>       x, y ∈ [−M, M ], then g(x + iǫ) and g(x − iǫ) converge uniformly to functions
>       g+ (x) and g− (x) as ǫ → 0. Then, g can be characterized as the unique
>       holomorphic function that satisfies:
>
>            (i) g is holomorphic outside [−M, M ],
>           (ii) g vanishes at infinity,
>          (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x)
>                and g− (x) with
>
>                                           g+ (x) − g− (x) = h(x).
>
>       [Hint: If G is another function satisfying these conditions, g − G is entire.]

## No missing exercises in chapter 3

All 22 printed exercises have cards `E-SS3.EX-1` … `E-SS3.EX-22`, and every card was read
against the print. Statement fidelity: **no dropped hypothesis, no dropped hint, no wrong
constant found**. All seven bracketed hints printed in the exercise block (EX-9, EX-10,
EX-14, EX-17, EX-18, EX-19, EX-20) and all three in the problem block that exists as cards
(PR-1, with seven part-hints, and PR-2) are reproduced in the corresponding cards, and the
overlines that OCR drops (EX-19 `Ω̄`; PR-2 `z̄0` in the definition of `T`) are correctly
restored.
Two harmless divergences, recorded for completeness rather than as defects:
* `E-SS3.EX-5`: the card writes the constant as `(π/2)(1+2π|ξ|)e^{-2π|ξ|}`; the print's
  fraction is rendered by OCR as a bare `π` over `2` on the following line, so this is an
  OCR reading, not a card change.
* `E-SS3.EX-11`: the print has no bracketed hint (the contour figure belongs to the
  hint of EX-10); the card likewise has none. Faithful.
* Starredness is not recorded anywhere in the cards (the print stars only PR-1, PR-4,
  PR-5 in this chapter — see the note in `gaps-summary.md`).
