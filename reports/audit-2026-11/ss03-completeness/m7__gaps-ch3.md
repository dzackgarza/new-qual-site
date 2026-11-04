# Chapter 3 (Meromorphic Functions and the Logarithm) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Heading "8 Exercises" p. 103: exercises 1–22, last on p. 108
  (1–5 p103; 6–11 p104; 12–15 p105; 16–19 p106; 20–21 p107; 22 p108).
* Heading "9 Problems" p. 108: problems 1–5, last on p. 110 (1 p108; 2–3 p109; 4–5 p110).
* Cards on disk at 16:12 UTC: `ch3-exercises/` EX-1…EX-22 (22 cards), `ch3-problems/` **PR-1, PR-2
  only** (2 cards); `index.md` lists the same two. At 16:18 UTC three more problem cards appeared
  (see "Missing items").
* Inventory re-derived from the filesystem; printed numbering parsed as contiguous runs and the
  end of the Problems section read by eye (p. 110 is followed by the Chapter 4 title page).

## Missing items

**Status of this finding, read this first.** At the time of the inventory pass (16:12 UTC on
2026-11-01) the collection had two problem cards and the three items below were missing. At 16:18 UTC,
while this audit was still running, files `ch3-problems/E-SS3.PR-3.md`, `PR-4.md`, `PR-5.md` appeared
on disk (concurrent work by another worker — this audit did not create them). Their statements were
then compared with the printed text and **all three match, word for word** (see the end of this file).
`index.md` had not been updated at that point: it still listed only PR-1 and PR-2.

The chapter prints **five** problems; the collection originally had two. Missing then: PR-3, PR-4, PR-5.

| item | book page | printed statement (OCR text layer, symbols may be mangled) | card that should exist |
|---|---|---|---|
| Problem 3 | p. 109 | "3. If f (z) is holomorphic in the deleted neighborhood {0 < \|z − z0 \| < r} and has a pole of order k at z0 , then we can write f (z) = a−k /(z − z0 )^k + · · · + a−1 /(z − z0 ) + g(z) where g is holomorphic in the disc {\|z − z0 \| < r}. There is a generalization of this expansion that holds even if z0 is an essential singularity. This is a special case of the Laurent series expansion, which is valid in an even more general setting. Let f be holomorphic in a region containing the annulus {z : r1 ≤ \|z − z0 \| ≤ r2 } where 0 < r1 < r2 . Then, f (z) = Σ_{n=−∞}^{∞} an (z − z0 )^n where the series converges absolutely in the interior of the annulus. To prove this, it suffices to write f (z) = (1/2πi)∫_{Cr2} f (ζ)/(ζ − z) dζ − (1/2πi)∫_{Cr1} f (ζ)/(ζ − z) dζ when r1 < \|z − z0 \| < r2 , and argue as in the proof of Theorem 4.4, Chapter 2. Here Cr1 and Cr2 are the circles bounding the annulus." | `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-3.md` |
| Problem 4∗ | p. 110 | "4.∗ Suppose Ω is a bounded region. Let L be a (two-way infinite) line that intersects Ω. Assume that Ω ∩ L is an interval I. Choosing an orientation for L, we can define Ωl and Ωr to be the subregions of Ω lying strictly to the left or right of L, with Ω = Ωl ∪ I ∪ Ωr a disjoint union. If Ωl and Ωr are simply connected, then Ω is simply connected." | `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-4.md` |
| Problem 5∗ | p. 110 | "5.∗ Let g(z) = (1/2πi)∫_{−M}^{M} h(x)/(x − z) dx where h is continuous and supported in [−M, M ]. (a) Prove that the function g is holomorphic in C − [−M, M ], and vanishes at infinity, that is, lim_{\|z\|→∞} \|g(z)\| = 0. Moreover, the "jump" of g across [−M, M ] is h, that is, h(x) = lim_{ǫ→0,ǫ>0} g(x + iǫ) − g(x − iǫ). [Hint: Express the difference g(x + iǫ) − g(x − iǫ) in terms of a convolution of h with the Poisson kernel.] (b) If h satisfies a mild smoothness condition, for instance a Hölder condition with exponent α, that is, \|h(x) − h(y)\| ≤ C\|x − y\|^α for some C > 0 and all x, y ∈ [−M, M ], then g(x + iǫ) and g(x − iǫ) converge uniformly to functions g+ (x) and g− (x) as ǫ → 0. Then, g can be characterized as the unique holomorphic function that satisfies: (i) g is holomorphic outside [−M, M ], (ii) g vanishes at infinity, (iii) g(x + iǫ) and g(x − iǫ) converge uniformly as ǫ → 0 to functions g+ (x) and g− (x) with g+ (x) − g− (x) = h(x). [Hint: If G is another function satisfying these conditions, g − G is entire.]" | `corpus/collections/SRC-TEXT-SS03/ch3-problems/E-SS3.PR-5.md` |

All three also need entries under "Ch3 Problems" in
`corpus/collections/SRC-TEXT-SS03/index.md`, whose header currently claims `completion: complete`.

Note: the printed text of Problem 3 is not a question — it is a statement plus the instruction
"To prove this, it suffices to write …". The card must reproduce it as printed; a paraphrase that
turns it into a question would be a fidelity defect.

## Statement-fidelity findings (the 24 cards that exist)

No substantive difference found in EX-1…EX-22, PR-1, PR-2. Notes:

1. **E-SS3.EX-5 (p. 103)** — OCR gives `∫ e^{−2πixξ}/(1 + x^2)^2 dx = (1 + 2π|ξ|)e^{−2π|ξ|}` with a
   stray raised `2` above the line (the factor π/2, printed on the line above); the card's
   `(π/2)(1+2π|ξ|)e^{−2π|ξ|}` is the consistent reading.
2. **E-SS3.PR-1 (p. 108)** and **E-SS3.PR-2** — PR-1 is starred (∗); the card does not record the star.
3. **E-SS3.EX-22 (p. 108)** — printed "extends continuously to ∂D" (the OCR layer drops the ∂ symbol
   in places); the card has `\partial\DD`.

## Late-arriving cards (16:18 UTC) — statement check

* `E-SS3.PR-3` — matches the printed problem (deleted-neighbourhood expansion, the annulus
  hypothesis `0 < r1 < r2`, the two integrals over `C_{r2}` and `C_{r1}`, the reference to
  Theorem 4.4 of Chapter 2). No difference found.
* `E-SS3.PR-4` — matches (`Ω_l ∪ I ∪ Ω_r` a disjoint union; both subregions simply connected).
  The printed `∗` is still not recorded.
* `E-SS3.PR-5` — matches part (a) (holomorphic on `C ∖ [−M,M]`, vanishing at infinity, the jump
  formula, the Poisson-kernel hint) and part (b) (Hölder condition, uniform limits `g^±`, the three
  characterising properties, the `g − G` hint). The printed `∗` is still not recorded.

`index.md` must gain all three ids under "Ch3 Problems"; otherwise the cards are invisible to
anything that reads the collection index.

## Not checked

* Proofs and solutions.
* Statement fidelity of PR-3, PR-4, PR-5 was vacuous when the inventory was taken; the late cards are
  covered in the section above.
