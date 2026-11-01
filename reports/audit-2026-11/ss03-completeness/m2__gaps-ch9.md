# SRC-TEXT-SS03 — gap report, Chapter 9 (An Introduction to Elliptic Functions)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer).
Pages are cited as **PDF p.X (printed p.Y)**; throughout the exercise/problem pages Y = X − 19
(checked against the printed folios and running heads).

Method: whole-book `pdftotext` extraction in reading order and with `-layout`; section boundaries from the
printed headings (`3 Exercises`, `4 Problems`); item numbers by a monotone 1..N scan excluding the running
heads; both extractions agree on every count. Quotes are verbatim OCR (symbols mangled by the OCR).
Nothing under `corpus/` was modified.

## Printed inventory

| section | heading | printed pages | printed items | cards present | missing |
|---|---|---|---|---|---|
| 3 Exercises | PDF p.297 (printed 278) | printed 278–281 | 1–8 | 8 (`E-SS9.EX-1`..`8`) | none |
| 4 Problems | PDF p.300 (printed 281) | printed 281–282 | **1–4** | 3 (`E-SS9.PR-1`..`3`) | **PR-4** |

Evidence: exercise 8 ends on printed p.281 just above the "4 Problems" heading; problems 1–4 run over
printed pp.281–282 and are followed by the title page of Chapter 10 (PDF p.302, printed 283).

## Missing item (1)

### `E-SS9.PR-4`
* Card path: `corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-4.md`
* Book page: **PDF p.301 (printed p.282)** — the problem begins at the top of the page.
* Starred in print ("4.∗").
* Printed statement (OCR verbatim):

> "4.∗ Suppose τ is purely imaginary, say τ = it with t > 0. Consider the division of the complex plane into
> congruent rectangles obtained by considering the lines x = n/2, y = tm/2 as n and m range over the
> integers. (An example is the rectangle whose vertices are 0, 1/2, 1/2 + τ /2, and τ /2.)
> (a) Show that ℘ is real-valued on all these lines, and hence on the boundaries of all these rectangles.
> (b) Prove that ℘ maps the interior of each rectangle conformally to the upper (or lower) half-plane."

## Statement fidelity

* `E-SS9.PR-1`, `PR-2`, `PR-3` were compared with printed problems 1, 2 and 3: aligned, part lettering
  matches. `PR-3` keeps its printed hint in a `:::.hint` block.
* `E-SS9.PR-3` is the starred printed problem "3.∗"; the card does not record the star.
