# SRC-TEXT-SS03 — gap report, Chapter 4 (The Fourier Transform)

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
| 4 Exercises | PDF p.146 (printed 127) | printed 127–131 | 1–12 | 12 (`E-SS4.EX-1`..`12`) | none |
| 5 Problems | PDF p.150 (printed 131) | printed 131–134 | 1–4 | 4 (`E-SS4.PR-1`..`4`) | none |

Evidence: exercise 12 ends on printed p.131 (PDF p.150), the same page on which the "5 Problems" heading
appears; problem 4 ends on printed p.134 and
PDF p.154 (printed 135) is the title page of Chapter 5. Four printed problems, four cards.

## Statement fidelity (3 cards read closely)

* `E-SS4.EX-12` drops a printed bracketed hint: printed (p.131) ends the exercise with
  "[Hint: To prove the result, use the inequality −ξ^p + ξu ≤ u^q , which is valid when ξ and u are
  non-negative. To establish this inequality, examine separately the cases ξ^p ≥ ξu and ξ^p < ξu; note
  also that the functions ξ = u^(q−1) and u = ξ^(p−1) are inverses of each other because (p−1)(q−1) = 1.]"
  No `::: {.hint}` block carries it either.
* `E-SS4.PR-3` prints the hint as a `::: {.hint}` block (the .exercise block itself has none) — the hint is
  present, not a defect.
* `E-SS4.PR-3`, `E-SS4.PR-4` are the starred printed problems ("3.∗", "4.∗"); the cards do not record the star.
