# Chapter 9 (An Introduction to Elliptic Functions) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Heading "3. Exercises" p. 278: exercises 1–8, last on p. 280 (1–2 p278; 3–5 p279; 6–8 p280).
* Heading "4. Problems" p. 281: problems 1–4, last on p. 282 (1–3 p281; 4 p282).
* Cards on disk at 16:12 UTC: `ch9-exercises/` EX-1…EX-8 (8), `ch9-problems/` **PR-1…PR-3 only**
  (3). At 16:18 UTC a card for PR-4 appeared (see "Missing items").
* Printed numbering parsed as contiguous runs; the end of the Problems section read by eye
  (p. 282 is the last page of the chapter).

## Missing items

**Status of this finding.** At the inventory pass (16:12 UTC) the collection had three problem cards
and PR-4 was missing. At 16:18 UTC, while this audit was still running, `ch9-problems/E-SS9.PR-4.md`
appeared on disk (concurrent work by another worker — not created by this audit). Its statement was
then compared with the printed text and **matches word for word** (see the end of this file).
`index.md` had not been updated at that point.

The chapter prints **four** problems; the collection originally had three. Missing then: PR-4.

| item | book page | printed statement (OCR text layer, symbols may be mangled) | card that should exist |
|---|---|---|---|
| Problem 4∗ | p. 282 | "4.∗ Suppose τ is purely imaginary, say τ = it with t > 0. Consider the division of the complex plane into congruent rectangles obtained by considering the lines x = n/2, y = tm/2 as n and m range over the integers. (An example is the rectangle whose vertices are 0, 1/2, 1/2 + τ /2, and τ /2.) (a) Show that ℘ is real-valued on all these lines, and hence on the boundaries of all these rectangles. (b) Prove that ℘ maps the interior of each rectangle conformally to the upper (or lower) half-plane." | `corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-4.md` |

It also needs an entry under "Ch9 Problems" in `corpus/collections/SRC-TEXT-SS03/index.md`, whose
header currently claims `completion: complete`.

## Statement-fidelity findings (the 11 cards that exist)

No substantive difference found in EX-1…EX-8, PR-1…PR-3. Notes:

1. **E-SS9.PR-1 (p. 281)** — the printed hint's inner sum is typeset with a broken `\b` and a
   comparison integral `∫_{1≤x²+y²≤R²} dx/(x+yτ)² = I(R)`; the card reproduces the hint faithfully.
2. **E-SS9.PR-3 (p. 281)** is starred (∗); the card does not record the star. The card keeps the
   printed hint.
3. **E-SS9.EX-3 (p. 279)** — OCR "n+mτ ∈Λ∗" and "1/(n2 + m2 ) = 2π log R + O(1)"; the card's
   `\sum_{n+m\tau\in\Lambda^*}` and `2\pi\log R+O(1)` are the consistent readings.

## Late-arriving card (16:18 UTC) — statement check

* `E-SS9.PR-4` — matches: purely imaginary `τ = it`, the lines `x = n/2`, `y = tm/2`, the example
  rectangle with vertices `0, 1/2, 1/2 + τ/2, τ/2`, part (a) real-valued on the lines, part (b)
  conformal onto the upper (or lower) half-plane. The printed `∗` is not recorded.

`index.md` must gain the id under "Ch9 Problems".

## Not checked

* Proofs and solutions.
* Statement fidelity of PR-4 was vacuous when the inventory was taken; the late card is covered above.
