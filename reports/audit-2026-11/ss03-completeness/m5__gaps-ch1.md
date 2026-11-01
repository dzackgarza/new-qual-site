# Gaps — Chapter 1 (Preliminaries to Complex Analysis)

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pages, OCR layer). Page citations give the PDF page and, in parentheses, the printed page; on every page this audit used, PDF page = printed page + 19.

Method: the whole PDF was dumped once with `pdftotext -layout`; for every printed Exercises/Problems section I collected the item-start lines and their page, checked that the printed numbers run contiguously from 1 to the last item, and read the closing page of each block to confirm the terminal item. Numbers were then diffed against the card files on disk (`corpus/collections/SRC-TEXT-SS03/<dir>/E-SS<ch>.<EX|PR>-<n>.md`). Page ranges below run from the first to the last item's starting page.

## Printed sections in this chapter

| section | heading page (printed) | printed items | cards on disk | missing |
|---|---|---|---|---|
| 4 Exercises | p. 24 | 26 | 26 | 0 |

## Missing items

None. Every printed item in this chapter has a card with the matching number.

- 4 Exercises, printed pp. 24–31 (PDF pp. 43–50), items start on those pages: 26 printed items, numbers 1–26, 26 cards, all present.

## Fidelity notes for this chapter (sampled)

Four chapter-1 exercises lose their printed hint. The cards exist and their statements match the print, but the bracketed `[Hint: ...]` is absent from the card file (verified by reading the card): `E-SS1.EX-15` (printed p. 28: "[Hint: Sum by parts.]"; the two printed sentences that follow it are also dropped — "In other words, if a series converges, then it is Abel summable with the same limit. For the precise definition of these terms, and more information on summability methods, we refer the reader to Book I, Chapter 2."); `E-SS1.EX-16` (printed p. 28: "[Hint: Use Stirling’s formula, which says that 1 n! ∼ c n n+ 2 e−n for some c > 0..]"); `E-SS1.EX-18` (printed p. 29: "[Hint: Write z = z0 + (z − z0 ) and use the binomial expansion for z n .]"); `E-SS1.EX-21` (printed p. 29: "[Hint: Use the dyadic expansion of an integer and the fact that 2k+1 − 1 = 1 + 2 + 22 + · · · + 2k .]"). The other five hint-bearing chapter-1 items (EX-4, EX-6, EX-7, EX-19, EX-22) do carry a hint block.
