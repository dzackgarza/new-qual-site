# SRC-TEXT-SS03 — gap report, Chapter 1 (Preliminaries to Complex Analysis)

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
| 4 Exercises | PDF p.43 (printed 24) | printed 24–31 | 1–26 | 26 (`E-SS1.EX-1`..`26`) | none |
| — Problems | *no Problems section is printed in this chapter* | — | — | — | — |

Evidence for the chapter end: item 26 ("Suppose f is continuous in a region Ω. Prove that any two
primitives of f (if they exist) diﬀer by a constant.") is the last text on PDF p.50 (printed 31);
PDF p.51 (printed 32) is the **title page of Chapter 2** ("2 Cauchy's Theorem and Its Applications"), so
Chapter 1 prints no Problems. This matches the table of contents (printed p.xii, which lists
"4 Exercises" for Chapter 1 and no Problems entry).

## Statement fidelity (5 cards read closely)

* `E-SS1.EX-13`: printed hypothesis is "holomorphic in an **open set** Ω"; the card says
  "in a region Ω (**an open connected set**)". The card strengthens the hypothesis. Harmless for the
  conclusion (it holds componentwise) but it is not what the book prints.
* Four cards drop a printed bracketed hint that appears in the statement (no `::: {.hint}` block either):
  * `E-SS1.EX-15` (printed p.28): printed "[Hint: Sum by parts.]" — absent from the card.
  * `E-SS1.EX-16` (printed p.28): printed "[Hint: Use Stirling's formula, which says that
    n! ∼ cn^(n+1/2) e^(−n) for some c > 0.]" — absent from the card.
  * `E-SS1.EX-18` (printed p.29): printed "[Hint: Write z = z0 + (z − z0 ) and use the binomial
    expansion for z^n .]" — absent from the card.
  * `E-SS1.EX-21` (printed pp.29–30): printed "[Hint: Use the dyadic expansion of an integer and the
    fact that 2^(k+1) − 1 = 1 + 2 + 2^2 + · · · + 2^k .]" — absent from the card.
  Elsewhere in these four the hint's method is used inside the *solution*; the printed hint is still
  missing from the transcribed statement.
* No number/statement misalignment found in the chapter's 26 cards.
