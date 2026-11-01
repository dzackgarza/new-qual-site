# SS03 — inventory re-derived from disk and from the PDF

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, 398 pages,
text layer produced by ocrmypdf 11.0.1 / Tesseract 4.1.1. Whole file extracted once with
`pdftotext` (631,747 bytes), split on form feed into 399 pages (one trailing empty page).

**Page numbers.** Every page number cited in my files is the **PDF page index**, i.e. the page
number that `pdftotext -f <a> -l <b>` takes. The printed folio is given in parentheses;
in the body of the book `PDF page = printed folio + 19` (checked on every section boundary,
e.g. PDF 43 = printed 24, PDF 336 = printed 317).

## 1. What is actually on disk (not what the task statement lists)

The task statement lists 8 directories. The collection has **20** directories and **206 cards**:

| directory | cards | numbers present |
|---|---|---|
| `ch1-exercises` | 26 | EX-1 … EX-26 |
| `ch2-exercises` | 15 | EX-1 … EX-15 |
| `ch2-problems` | 5 | PR-1 … PR-5 |
| `ch3-exercises` | 22 | EX-1 … EX-22 |
| `ch3-problems` | 2 | PR-1, PR-2 |
| `ch4-exercises` | 12 | EX-1 … EX-12 |
| `ch4-problems` | 4 | PR-1 … PR-4 |
| `ch5-exercises` | 17 | EX-1 … EX-17 |
| `ch5-problems` | 4 | PR-1 … PR-4 |
| `ch6-exercises` | 17 | EX-1 … EX-17 |
| `ch6-problems` | 4 | PR-1 … PR-4 |
| `ch7-exercises` | 12 | EX-1 … EX-12 |
| `ch7-problems` | 4 | PR-1 … PR-4 |
| `ch8-exercises` | 24 | EX-1 … EX-24 |
| `ch8-problems` | 9 | PR-1 … PR-9 |
| `ch9-exercises` | 8 | EX-1 … EX-8 |
| `ch9-problems` | 3 | PR-1 … PR-3 |
| `ch10-exercises` | 12 | EX-1 … EX-12 |
| `ch10-problems` | 6 | PR-1 … PR-6 |

No directory exists for the two appendices.

`index.md` contains exactly 206 `- id: E-SS…` entries and they are in bijection with the
206 files (no entry without a file, no file without an entry). `index.md` line 12 declares
`completion: complete`; that claim is false for the collection as a whole (see gaps summary).

## 2. What the book prints

Found by scanning every page for the body headings (`N Exercises` / `N Problems`, printed
without a full stop — the running heads `N. Exercises` / `N. Problems` carry a full stop and
were excluded), then segmenting each section into items by their leading numbers.

| chapter | section printed | PDF pages | printed folios | items | star-marked items |
|---|---|---|---|---|---|
| 1 | `4 Exercises` | 43–50 | 24–31 | 26 | – |
| 2 | `6 Exercises` | 83–86 | 64–67 | 15 | – |
| 2 | `7 Problems` | 86–89 | 67–70 | 5 | 2, 5 |
| 3 | `8 Exercises` | 122–127 | 103–108 | 22 | – |
| 3 | `9 Problems` | 127–129 | 108–110 | 5 | 1, 4, 5 |
| 4 | `4 Exercises` | 146–150 | 127–131 | 12 | – |
| 4 | `5 Problems` | 150–152 | 131–133 | 4 | 3, 4 |
| 5 | `6 Exercises` | 172–175 | 153–156 | 17 | – |
| 5 | `7 Problems` | 175–177 | 156–158 | 4 | 2, 3, 4 |
| 6 | `3 Exercises` | 193–198 | 174–179 | 17 | – |
| 6 | `4 Problems` | 198–199 | 179–180 | 4 | 2, 3, 4 |
| 7 | `3 Exercises` | 218–222 | 199–203 | 12 | – |
| 7 | `4 Problems` | 222–223 | 203–204 | 4 | 2, 3, 4 |
| 8 | `5 Exercises` | 267–273 | 248–254 | 24 | – |
| 8 | `6 Problems` | 273–279 | 254–260 | 9 | 3, 4, 6, 7, 8, 9 |
| 9 | `3 Exercises` | 297–299 | 278–280 | 8 | – |
| 9 | `4 Problems` | 300–301 | 281–282 | 4 | 3, 4 |
| 10 | `4 Exercises` | 328–332 | 309–313 | 12 | – |
| 10 | `5 Problems` | 333–336 | 314–317 | 6 | 1, 5, 6 |
| App A | `5 Problems` | 360–362 | 341–343 | 5 | 5 |
| App B | — | 363–383 | 344–364 | 0 | – |

Totals: **215 printed items** = 165 exercises + 50 problems (45 in chapters 2–10 plus the
5 of Appendix A). Item numbers run 1…N without a hole in every one of the 20 sections, so a
missing number would have shown up as a break in an otherwise contiguous run; none did.

Chapter 1 prints **only** an Exercises section (no Problems); Appendix A prints **only** a
Problems section; Appendix B prints neither. There are no exercise sets at section level —
all exercises/problems of this book are the chapter-end blocks above.

Star marking: the book marks harder items with a star immediately after the item number
(`2.∗`, `4.∗`, …), 28 items in all, listed in the last column above. The only star on a
*part* of an item is Chapter 2, Problem 1, part (b) (`(b) ∗ Fix 0 < α < ∞.`, PDF 87).

## 3. Files backing this

`.scratch/items.json` — every printed item: text, PDF pages, star flag (working data, not a
deliverable). `.scratch/book.txt` — the full pdftotext output.

## 4. Page-integrity check on the scan itself

Because a missing or duplicated scan page would silently corrupt every count, I checked the
page numbering rather than trusting the file length: for each of the 364 pages PDF 20–383, the
leading printed folio was extracted and compared with `PDF page − 19`.
**341 pages carry a folio; all 341 satisfy the constant offset exactly, with zero deviations.**
The 23 pages without a folio in the first two lines are the chapter/appendix title pages
(PDF 20, 51, 90, 130, 153, 178, 200, 224, 280, 302, 337, 363) and pages of the Notes section
where the folio sits at the foot of the page (PDF 365, 367, …, 383). A dropped or repeated
page would show up as a jump of the offset; none does, so the item counts rest on a complete,
in-order scan of the body.
