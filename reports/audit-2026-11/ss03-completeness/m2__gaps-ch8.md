# SRC-TEXT-SS03 — gap report, Chapter 8 (Conformal Mappings)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer).
Pages are cited as **PDF p.X (printed p.Y)**; throughout the exercise/problem pages Y = X − 19
(checked against the printed folios and running heads).

Method: the whole PDF was extracted once with `pdftotext` in reading order and once with `-layout`.
Section boundaries were taken from the printed headings (`k Exercises` / `k Problems`), item numbers by a
monotone 1..N scan that excludes the running heads (`8. Exercises`, `9. Problems`, …). The two extractions
agree on every count below. Quotes are verbatim OCR: the OCR mangles symbols (√, π, ∑, ∫ and exponents are
often lost or displaced); where that affects the reading it is flagged. Nothing under `corpus/` was modified.

## Printed inventory and result: **no missing items**

| section | heading | printed pages | printed items | cards | missing |
|---|---|---|---|---|---|
| 5 Exercises | PDF p.267 (printed 248) | printed 248–254 | 1–24 | 24 (`E-SS8.EX-1`..`24`) | none |
| 6 Problems | PDF p.273 (printed 254) | printed 254–260 | **1–9** | 9 (`E-SS8.PR-1`..`9`) | none |

**Direct answer to the question in the brief: there is no Chapter 8 problem beyond 9.** Problem 9 ("9.∗
Gauss found a connection between elliptic integrals and the familiar operations of forming arithmetic and
geometric means …") begins on printed p.259 (PDF p.278) and its part (b) ends on printed p.260 (PDF p.279)
with "… the relation (6) is a consequence of the identity in (b) of Exercise 24." The next page, PDF p.280
(printed 261), is the title page of Chapter 9. The section prints exactly nine problems, and the nine cards
are complete.

Note also that exercise 24 ends on printed p.254 and the "6 Problems" heading follows on the *same* page; a
page boundary at printed 254 must not be read as a missing exercise.

## Statement fidelity (3 cards read closely)

* `E-SS8.EX-13` drops its printed bracketed hint ("[Hint: Consider the automorphism ψα(z) = (z − α)/(1 − αz)
  and apply the Schwarz lemma to ψ_{f(w)}^(−1) ◦ f ◦ ψw.]", printed p.251) and has no `:::.hint` block.
* `E-SS8.PR-4`, `E-SS8.PR-7`, `E-SS8.PR-9` keep their printed hints in `:::.hint` blocks (PR-7 keeps four)
  — present, not defects.
* The starred printed problems of this chapter (`PR-3`, `PR-4`, `PR-6`, `PR-7`, `PR-8`, `PR-9`) are not
  marked as starred in their cards.
