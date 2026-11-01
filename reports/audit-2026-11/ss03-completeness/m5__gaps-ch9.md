# Gaps — Chapter 9 (An Introduction to Elliptic Functions)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR layer). Page citations give the PDF page and, in parentheses, the printed page; on every page this audit used, PDF page = printed page + 19.

Method: the whole PDF was dumped once with `pdftotext -layout`; for every printed Exercises/Problems section I collected the item-start lines and their page, checked that the printed numbers run contiguously from 1 to the last item, and read the closing page of each block to confirm the terminal item. Numbers were then diffed against the card files on disk (`corpus/collections/SRC-TEXT-SS03/<dir>/E-SS<ch>.<EX|PR>-<n>.md`). Page ranges below run from the first to the last item's starting page.

## Printed sections in this chapter

| section | heading page (printed) | printed items | cards on disk | missing |
|---|---|---|---|---|
| 3 Exercises | p. 278 | 8 | 8 | 0 |
| 4 Problems | p. 281 | 4 | 3 | 1 |

## Missing items

### E-SS9.PR-4 — printed with the difficulty asterisk (preface, printed p. viii: "the ones that are most difficult, or go beyond the scope of the text, are marked with an asterisk")

- Printed at PDF p. 301 (printed p. 282), in "4 Problems" (heading printed p. 281).
- Card should go in `corpus/collections/SRC-TEXT-SS03/ch9-problems/E-SS9.PR-4.md`.

- Printed statement, quoted from the OCR (`pdftotext -layout`; line breaks collapsed; symbols and formula layout are mangled by the OCR as usual — words and numbers are what I am quoting):

> Suppose τ is purely imaginary, say τ = it with t > 0. Consider the division of the complex plane into congruent rectangles obtained by considering the lines x = n/2, y = tm/2 as n and m range over the integers. (An example is the rect- angle whose vertices are 0, 1/2, 1/2 + τ /2, and τ /2.) (a) Show that ℘ is real-valued on all these lines, and hence on the boundaries of all these rectangles. (b) Prove that ℘ maps the interior of each rectangle conformally to the upper (or lower) half-plane.


## Fidelity note

The book’s own Notes and References (printed p. 366) say "Problems 2, 3, and 4 are in Saks and Zygmund [34]" for Chapter 9 — an independent confirmation, from this same PDF, that chapter 9 prints four Problems, so PR-4 is a real gap.
