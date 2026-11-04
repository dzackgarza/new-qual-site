# SRC-TEXT-SS03 — gap report, Chapter 10 (Applications of Theta Functions)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer).
Pages are cited as **PDF p.X (printed p.Y)**; throughout the exercise/problem pages Y = X − 19
(checked against the printed folios and running heads).

Method: whole-book `pdftotext` extraction in reading order and with `-layout`; section boundaries from the
printed headings (`4 Exercises`, `5 Problems`); item numbers by a monotone 1..N scan excluding the running
heads; both extractions agree on every count. Quotes are verbatim OCR. Nothing under `corpus/` was modified.

## Printed inventory and result: **no missing items**

| section | heading | printed pages | printed items | cards | missing |
|---|---|---|---|---|---|
| 4 Exercises | PDF p.328 (printed 309) | printed 309–314 | 1–12 | 12 (`E-SS10.EX-1`..`12`) | none |
| 5 Problems | PDF p.333 (printed 314) | printed 314–317 | **1–6** | 6 (`E-SS10.PR-1`..`6`) | none |

**Direct answer to the question in the brief: Chapter 10 prints six problems (1–6, printed pp.314–317).**
Problem 6 ("6.∗ Here we will deduce the formula for r8(n), which counts the number of representations of n as
a sum of eight squares …") is the last item; its closing sentence "… which must be 1. This gives the desired
result." is on printed p.317 (PDF p.336), and PDF p.337 (printed 318) is the title page of Appendix A.
Exercise 12 also ends on printed p.314, above the "5 Problems" heading — same page, two sections.

## Statement fidelity (3 cards read closely)

* `E-SS10.PR-2`: the printed fundamental domain is "F1 = {τ ∈ C : |τ| ≥ 1, |Re(τ)| ≤ 1/2 and |Im(τ)| ≥ 0}"
  (OCR); the card writes "Im(τ) > 0". Both conditions are automatic on the upper half-plane, so this is
  cosmetic, but it is a difference from the printed text.
* `E-SS10.PR-3`: the card's statement includes the parity definition of the group G (a and d same parity,
  b and c same parity, c and d opposite parity) and the fundamental domain F. That text *is* printed on
  printed p.315 (PDF p.334) — the OCR prints it out of order, before the "3." that opens the problem — so
  the card is faithful, not expanded.
* `E-SS10.PR-5`, `E-SS10.PR-6` keep their printed hints in `:::.hint` blocks (PR-6 keeps both) — present.
* `E-SS10.PR-1`, `PR-5`, `PR-6` are the starred printed problems; the cards do not record the star.
