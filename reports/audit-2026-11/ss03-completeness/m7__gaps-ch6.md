# Chapter 6 (The Gamma and Zeta Functions) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Heading "3 Exercises" p. 174: exercises 1–17, last on p. 179
  (1–2 p174; 3–7 p175; 8–10 p176; 11–12 p177; 13–16 p178; 17 p179).
* Heading "4. Problems" p. 179: problems 1–4, last on p. 180 (1 p179; 2–4 p180).
* Cards on disk: `ch6-exercises/` EX-1…EX-17 (17), `ch6-problems/` PR-1…PR-4 (4).
* Printed numbering parsed as contiguous runs; the end of the Problems section read by eye
  (p. 180 is the last page before Chapter 7).

## Missing items

**None.**

## Statement-fidelity findings (all 21 cards compared)

Substantive:

1. **E-SS6.EX-4 (p. 175)** — the card adds a hypothesis that is not printed: "where $\alpha$ is a
   fixed complex number **not in $\{0,-1,-2,\ldots\}$**". Printed: "where α is a fixed complex number".
   (The card's restriction is what makes `1/Γ(α)` meaningful, but it is not in the book.)
2. **E-SS6.PR-1(c) (p. 179)** — printed: "(c) The second conclusion of Proposition 2.7 can be
   similarly refined." The card replaces this instruction by a specific assertion to prove,
   "Show that $|\zeta'(1+it)| = O((\log|t|)^2)$". That is a content change, not a transcription.

Substantive, but the OCR layer is itself doubtful (report, do not silently "fix"):

3. **E-SS6.EX-11 (p. 177)** — printed OCR: "11. Let f (z) = e^{az} e^{−e^z} where a > 0. Observe
   that in the strip **{x + iy : |y| < π}** the function f (x + iy) is exponentially decreasing as
   |x| tends to infinity. Prove that **f̂(ξ) = Γ(a + iξ)**, for all ξ ∈ R."
   The card has the strip `|y| < π/2` and `\hat f(\xi)=\Gamma(a-2\pi i\xi)`. Both differences are
   substantive. The card's pair is the one that is consistent with the book's own Fourier convention
   `f̂(ξ)=∫f(x)e^{-2πixξ}dx` (change of variable t = e^x gives Γ(a − 2πiξ)) and with the decay of
   `e^{−e^z}` on `|Im z| < π/2`; the OCR layer most likely lost "`/2`" and misread "−2πi" as "+i".
   Needs a look at the page image.
4. **E-SS6.EX-17 (p. 179)** — printed OCR: "(b) Prove that **I(0) = 0**, and more generally
   I(−n) = (−1)^n **f^{(n+1)}(0)** for all n ≥ 0." The card has `I(0)=f(0)` and
   `I(-n)=(-1)^n f^{(n)}(0)`. With the hint's formula `I(s) = ((−1)^k/Γ(s+k))∫_0^∞ f^{(k)}(x)x^{s+k−1}dx`
   and k = n+1, the card's form is the correct one (the integral becomes ∫f^{(n+1)}(x)dx =
   −f^{(n)}(0)); the OCR has dropped an "f(" and turned the superscript n into n+1. Ambiguous —
   page image needed.

Minor:

5. **E-SS6.EX-2 (p. 174)** — the card correctly drops the printed footnote marker
   "3 The reader should recall the O notation which was introduced at the end of Chapter 1."
   (a footnote, not part of the exercise).
6. **E-SS6.PR-2, PR-3, PR-4** are starred (∗) in print; the cards do not record the star.

Compared and found faithful: EX-1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, PR-1(a)(b)(d),
PR-2, PR-3, PR-4 (with the note in 4 above for EX-17).

## Not checked

* Proofs and solutions.
* Nothing in this chapter was left unexamined: all 21 printed items and all 21 cards were compared.
