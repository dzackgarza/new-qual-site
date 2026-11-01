# SRC-TEXT-SS03 — gap report, Chapter 6 (The Gamma and Zeta Functions)

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
| 3 Exercises | PDF p.193 (printed 174) | printed 174–179 | 1–17 | 17 (`E-SS6.EX-1`..`17`) | none |
| 4 Problems | PDF p.198 (printed 179) | printed 179–180 | 1–4 | 4 (`E-SS6.PR-1`..`4`) | none |

Caution recorded for future audits: this chapter's exercise section is numbered **3** and its running head
is "3. Exercises". A naive item scan reads that running head as item "3." and splits printed exercise 2 into
two items (2 and 3). Printed exercise 2 really does end with "… = Γ(a + 1)Γ(b + 1)/Γ(a + b + 1) whenever a
and b are positive. Using the product formula for sin πs, give another proof that Γ(s)Γ(1 − s) =
π/ sin πs."; printed exercise 3 begins "Show that Wallis's product formula can be written as …". The
`E-SS6.EX-2` card is correct on this point.

## Statement fidelity (2 cards read closely)

* `E-SS6.EX-2` and `E-SS6.EX-6` compared with the printed items: aligned, no dropped parts. (In printed
  exercise 6 the OCR prints "− 1/2 log n" with the fraction lost; the card's "− (1/2) log n" is the correct
  reading.)
* `E-SS6.PR-2`, `PR-3`, `PR-4` are the starred printed problems; the cards do not record the star.
