# SRC-TEXT-SS03 — gap report, Chapter 5 (Entire Functions)

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
| 6 Exercises | PDF p.172 (printed 153) | printed 153–156 | **1–17** | 17 (`E-SS5.EX-1`..`17`) | none |
| 7 Problems | PDF p.175 (printed 156) | printed 156–158 | 1–4 | 4 (`E-SS5.PR-1`..`4`) | none |

**Direct answer to the question in the brief: there is no Chapter 5 exercise 19, and no exercise 18.**
The exercises print 1–17 and nothing else. Items 16 and 17 are printed on PDF p.175 (printed p.156), and the
"7 Problems" heading follows on the same page; item 17 ("Given two countably infinite sequences of complex
numbers {ak}∞k=0 and {bk}∞k=0, with limk→∞ |ak| = ∞ … Pringsheim interpolation formula.") is the last
exercise. A count of 15 comes from a naive scan that stops at the PDF page boundary: the section continues
past printed p.154 onto pp.155–156.

## Statement fidelity (4 cards read closely)

* `E-SS5.PR-1` prints the hint as "*Hint.* Use Jensen's formula." (prose form, not a `:::.hint` block);
  the hint is present.
* `E-SS5.PR-2`, `PR-3`, `PR-4` are the starred printed problems ("2.∗", "3.∗", "4.∗"); the cards do not
  record the star.
* No statement-level differences found in the cards compared.
