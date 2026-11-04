# SRC-TEXT-SS03 — Chapter 6 (The Gamma and Zeta Functions)

**No missing cards.** Printed: 17 exercises (§3, PDF pages 193–198) and 4 problems (§4,
PDF pages 198–199); cards present: 17 and 4 (`E-SS6.EX-1..17`, `E-SS6.PR-1..4`).
PDF page 200 opens chapter 7. PDF page = printed folio + 19 (PDF 193 = printed 174,
PDF 199 = printed 180). Numbering verified contiguous in the print.

Scope of the fidelity claim: **all 21 cards**, statement blocks read against the printed
items, plus their `remark` blocks and audit notes. No proof audited.

Headline: this chapter is the cleanest of the three I verified in full. Four printed
formulas are defective and the cards correct them — **and each correction is documented in
the card itself** (a `::: {.remark}` block explaining what the source prints), so none is a
silent departure. Only one small difference is undocumented.

## Differences from the print, all documented in the card

### `E-SS6.EX-11` (PDF p. 196) — strip and Fourier transform differ from the print
Print (OCR verbatim; the superscript `z` of `e^{-e^z}` floats onto its own line just below
"Figure 1. The contour in Exercise 10"):

> 11. Let f (z) = eaz e−e where a > 0. Observe that in the strip {x + iy : |y| < π}
> the function f (x + iy) is exponentially decreasing as |x| tends to infinity. Prove
> that
>
>                             fˆ(ξ) = Γ(a + iξ),     for all ξ ∈ R.

Card statement: "… in the strip $\{x + iy : \abs{y} < \pi/2\}$ … $\hat{f}(\xi) = \Gamma(a - 2\pi i\xi)$".
Card remark: "The source prints the strip |y| < π and the answer Γ(a + iξ). Since
|f(x+iy)| = e^{ax}e^{−e^x cos y} grows as x → ∞ when cos y < 0, the decay holds only for
|y| < π/2. With the book's convention f̂(ξ) = ∫ f(x)e^{−2πixξ}dx, the transform is
Γ(a − 2πiξ); Γ(a + iξ) is the transform for the kernel e^{ixξ}." — the divergence and its
reason are on the card.

### `E-SS6.EX-17(b)` (PDF p. 198) — both displayed formulas differ from the print
Print (OCR verbatim): "(b) Prove that I(0) = 0, and more generally
I(−n) = (−1)n f (n+1) (0) for all n ≥ 0."
Card: "(b) Prove that $I(0) = f(0)$, and more generally $I(-n) = (-1)^n f^{(n)}(0)$ for all
$n \geq 0$."
Card remark: "The source prints I(0) = 0 and I(−n) = (−1)^n f^{(n+1)}(0). The hint with
k = n+1 gives I(−n) = (−1)^{n+1}∫_0^∞ f^{(n+1)}(x)dx = (−1)^n f^{(n)}(0); for f(x) = e^{−x²},
I(0) = 1." Documented.

### `E-SS6.EX-4` (PDF p. 194) — hypothesis added
Print: "… where α is a fixed complex number, then f (z) = Σ an (α)z n with
an (α) ∼ (1/Γ(α)) n^{α−1} as n → ∞."
Card: "… where $\alpha$ is a fixed complex number not in $\{0, -1, -2, \ldots\}$ …".
Card remark: "The source allows every complex α. For α ∈ {0,−1,−2,…}, 1/Γ(α) = 0 and f is a
polynomial, so a_n(α) = 0 for large n and the relation ∼ has no meaning; the statement
excludes these α." Documented.

### `E-SS6.PR-1` (PDF p. 198) — middle term of (a) differs, and (c) is expanded
Print (OCR verbatim, summands displaced above the line):

>                                      N s−1
>                            ζ(s) =           n−s −         +   δn (s)
>                                                    s−1
>                                     1≤n<N                   n≥N

Card (a): `ζ(s) = Σ_{1≤n<N} n^{-s} + N^{1-s}/(s-1) + Σ_{n≥N} δ_n(s)`, plus the definition
`δ_n(s) = n^{-s} − ∫_n^{n+1} x^{-s}dx` imported from (9) of §2.1.
Card remark: "The source prints the middle term as −N^{s−1}/(s−1); summing
∫_n^{n+1} x^{−s}dx over n ≥ N gives +N^{1−s}/(s−1). Part (c) in the source says only that the
second conclusion of Proposition 2.7, the bound for ζ′, can be refined in the same way; the
statement gives that refinement." Documented — both the sign/exponent and the replacement of
the cross-reference in (c) by the explicit estimate `|ζ'(1+it)| = O((log|t|)^2)`.
The OCR's `−N^{s−1}` against the card's `+N^{1−s}` is therefore resolved by the card's own
note; I record the print reading for the human, not as a defect.

## The one undocumented difference

`E-SS6.EX-14(b)` (PDF p. 197). Print: "In fact, prove that log Γ(n) ∼ n log n + O(n) as
n → ∞." Card: "$\log\Gamma(n) = n\log n + O(n)$". The printed relation mixes `∼` with an
error term and is not well formed; the card's `=` is the standard reading. No note anywhere
in the card. Minor, but it is the only statement change in this chapter that the card does
not record.

## Checked and faithful (no action)

EX-1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14(a), 15, 16, EX-17(a) and its hint, PR-2, PR-3,
PR-4 reproduce the print, all sub-parts, and all ten bracketed hints of the exercise block
(EX-1, 7, 8, 9, 10, 12, 14, 15, 16, 17). Signs/exponents spot-checked and correct, e.g.
`|Γ(1/2+it)| = √(2π/(e^{πt}+e^{−πt}))` (EX-5), the Wallis form `√(π/2)` (EX-3), duplication
`Γ(s)Γ(s+1/2) = √π 2^{1−2s}Γ(2s)` (EX-3), the Mellin pair `Γ(z)cos(πz/2)`, `Γ(z)sin(πz/2)`
with `∫_0^∞ x^{−3/2} sin x = √(2π)` (EX-10), `Q_k(x) = B_{k+1}(x)/(k+1)!` and
`2ζ(2k) = (−1)^{k+1}(2π)^{2k}B_{2k}/(2k)!` (PR-4). The cards restore the overlines,
absolute-value bars and the `Σ`/`∫` limits that the OCR drops or displaces.
