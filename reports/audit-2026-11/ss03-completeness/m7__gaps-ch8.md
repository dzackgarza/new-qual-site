# Chapter 8 (Conformal Mappings) — completeness and statement fidelity

Source: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, OCR text layer
(`pdftotext -layout`); printed page = PDF page − 19.

## Scope

* Heading "5. Exercises" p. 248: exercises 1–24, last on p. 254
  (1–7 p248; 8–10 p249; 11–12 p250; 13–15 p251; 16–20 p252; 21–23 p253; 24 p254).
* Heading "6 Problems" p. 254: problems 1–9, last on p. 259 (1 p254; 2 p255; 3 p256; 4 p257;
  5–7 p258; 8–9 p259). Problem 9's parts (a) and (b) run on p. 259–260.
* Cards on disk: `ch8-exercises/` EX-1…EX-24 (24), `ch8-problems/` PR-1…PR-9 (9).
* Printed numbering parsed as contiguous runs; the end of the Problems section read by eye.

## Missing items

**None.**

**Explicit answer to the suspected gap:** the chapter prints **exactly nine problems**; there is no
problem 10. Problem 9 ("9.∗ Gauss found a connection between elliptic integrals and the familiar
operations of forming arithmetic and geometric means…") ends with part (b) at the top of p. 260
("…and that the relation (6) is a consequence of the identity in (b) of Exercise 24."), and p. 261
is the Chapter 9 title page. Note also that the exercise section really has 24 items: exercise 24
("The elliptic integrals K and K ′ …") begins on p. 254 **above** the "6 Problems" heading, which is
why a naive page split suggests 23.

## Statement-fidelity findings (all 33 cards compared)

Substantive:

1. **E-SS8.EX-13 (p. 251)** — the card drops the printed bracketed hint
   "[Hint: Consider the automorphism ψα (z) = (z − α)/(1 − ᾱz) and apply the Schwarz lemma to
   ψ_{f(w)}^{−1} ◦ f ◦ ψ_w .]" and also drops the printed sentence "See Problem 3 for an important
   application of this lemma."
2. **E-SS8.PR-8 (p. 259)** — the card drops two printed sentences: "then Problem 1 in Chapter 3
   shows that |a2 | ≤ 2" and "Bieberbach conjectured that in fact |an | ≤ n for all n ≥ 2; this was
   proved by deBranges." It also changes "This problem **outlines an argument** to prove the
   conjecture under the additional assumption that the coefficients an are real" into "This problem
   proves |a_n| ≤ n under the additional assumption that every a_n is real".

OCR-ambiguity (the OCR text layer loses the negation stroke; the cards are right):

3. **E-SS8.EX-1 (p. 248)** — printed OCR "if and only if f ′ (z) = 0 for all z ∈ U"; the card has
   `f'(z)\neq 0`. A holomorphic map is a local bijection iff its derivative **never** vanishes; the
   OCR has dropped the slash of ≠.
4. **E-SS8.EX-2 (p. 248)** — printed OCR "F (z0 ) = F ′ (z0 ) = 0, while F ′′ (z0 ) = 0"; the card has
   `F''(z_0)\neq 0`. Same OCR loss of the negation stroke; the card is right.
5. **E-SS8.EX-20(b) (p. 252)** — printed OCR "side lengths are Γ2√ (1/4) 2π"; the card's
   `\Gamma^2(1/4)/(2\sqrt{2\pi})` is the standard value and the consistent reading, but the OCR
   cannot confirm it.

Notes:

6. **E-SS8.PR-9 (p. 259–260)** — the card reproduces the printed problem, including the printed
   relation `I(a,b) = (1/a)K(k) = (1/a)∫_0^1 dx/\sqrt{(1−x²)(1−k²x²)}`. The card's remark that this
   printed relation is missing the factor 2/π is a claim about the **book**, not a card defect; the
   OCR text layer does print the factor-less identity. Whoever applies the fixes should treat that
   remark as an erratum note, not as a deviation to correct.
7. **E-SS8.PR-3, PR-4, PR-6, PR-7, PR-8, PR-9** are starred (∗); the cards do not record the star.
   `E-SS8.PR-4`'s hint reproduces the printed 2×2 matrix (up to the printed square roots of
   `1−|α|²`, which the card factors out) — same content.
8. **E-SS8.EX-18 (p. 252)** — printed "extends to a continuous bijection of D to Ω" with bars that
   the OCR loses; the card's closures `\overline{\DD}\to\overline{\Omega}` are the printed reading.

Compared and found faithful: EX-3 … EX-12, EX-14 … EX-19, EX-21 … EX-24, PR-1, PR-2, PR-3, PR-4,
PR-5, PR-6, PR-7, PR-9.

## Not checked

* Proofs and solutions.
* Nothing in this chapter was left unexamined: all 33 printed items and all 33 cards were compared.
