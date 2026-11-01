# Source-artifact audit of `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`

Direction d8 (member m1). Object of study: the PDF itself — pagination, scan completeness,
text-layer health — so that every other gap/fidelity claim in this swarm has a stated error bar.
Nothing here edits `corpus/`.

## Method

```
pdftotext -layout Stein-Shakarchi-Complex-Analysis.pdf book_layout.txt   # 905,731 bytes
pdftotext           Stein-Shakarchi-Complex-Analysis.pdf book_raw.txt    # 631,747 bytes
```
Both dumps split on form feed: **399 chunks = 398 pages + one empty trailing chunk**, matching
`pdfinfo` (`Pages: 398`). Every statistic below was computed on the `-layout` dump and spot-checked
against the plain dump; they agree on all pages cited here.

## 1. Pagination: printed folio = PDF page − 19, with no exception

For each page I parsed the top line (running head), which in this book carries the folio at the
outer edge: verso heads read `NN   Chapter k. TITLE`, recto heads read `k. Section title   NN`.

* Body pages: PDF 20–398 = **printed pages 1–379** (379 pages, offset +19 throughout).
* 362 body pages print an arabic folio; **all 362 satisfy folio = pdfpage − 19 exactly, zero
  exceptions.**
* 18 body pages print no folio and are accounted for: the 10 chapter/appendix title pages
  (printed 32, 71, 111, 134, 159, 181, 205, 261, 283, 318, 344 — PDF 51, 90, 130, 153, 178, 200,
  224, 280, 302, 337, 363), 4 back-matter title pages (365 Notes and References, 369 Bibliography,
  373 Symbol Glossary, 375 Index), 2 blank pages (368, 372), and PDF 52 = printed 33, where the
  folio is printed alone as `33` with no running head.
* Front matter: PDF 1–18 = roman i–xviii (e.g. PDF 9 prints `viii   FOREWORD`, PDF 13 prints
  `xii   CONTENTS`, PDF 17 prints `xvi   INTRODUCTION`); PDF 19 is blank.

Consequence for this swarm: a citation "printed p. N" is PDF page **N+19**, and a citation
"PDF p. M" is printed page **M−19**. The task asks for PDF page numbers, so the gap files give
PDF page first and printed page in brackets.

## 2. No missing and no duplicated scans

* Pages with an empty text layer: PDF **7, 11, 19, 387, 391** only. All five are genuine blanks:
  the folio arithmetic closes across each one (365 → 366 → 367 → [368 blank] → 369 Bibliography →
  370 …; 371 → [372 blank] → 373 Symbol Glossary → 374 …). No page of the book is absent from the
  scan and no printed page number is unaccounted for in 1–379.
* Duplicate detection: MD5 over whitespace-normalised page text found **no repeated page**; the
  highest consecutive-page similarity (difflib `quick_ratio` on normalised text) over the whole book
  is below 0.93, so no page is scanned twice.
* Text-layer density: mean 2,202 chars/page (`-layout`). The four sparsest body pages are printed
  158 (374 chars), 367 (476), 31 (567, the last page of Ch. 1 Exercises) and 282 (683) — each the
  last page of a section or chapter, not an OCR failure. The only page with a large figure and
  little text (printed 339, PDF 358) still carries its caption and equation text. No page is a
  picture-only page with no OCR.

## 3. Exercise / Problem sections: page map (derived from running heads, not from counting text)

The heading line in the body is written without a period (`4 Exercises`, `5 Problems`), while the
running head uses one (`4. Exercises`). Every chapter's exercises and problems are the last two
numbered sections of the chapter; Chapter 1 prints Exercises only, Appendix A prints Problems only,
Appendix B prints neither.

| section | heading at (PDF p. / printed p.) | items run to | last item on (PDF p.) | cards |
|---|---|---|---|---|
| Ch. 1 Exercises | 43 / 24 | 1–26 | 50 (26) | 26 |
| Ch. 2 Exercises | 83 / 64 | 1–15 | 86 (15) | 15 |
| Ch. 2 Problems | 86 / 67 | 1–5 (2\*, 5\* starred) | 89 | 5 |
| Ch. 3 Exercises | 122 / 103 | 1–22 | 126 | 22 |
| Ch. 3 Problems | 127 / 108 | 1–5 (1\*, 4\*, 5\*) | 129 | **2** |
| Ch. 4 Exercises | 146 / 127 | 1–12 | 149 | 12 |
| Ch. 4 Problems | 150 / 131 | 1–4 (3\*, 4\*) | 152 | 4 |
| Ch. 5 Exercises | 172 / 153 | 1–17 | 174 | 17 |
| Ch. 5 Problems | 175 / 156 | 1–4 (2\*, 3\*, 4\*) | 177 | 4 |
| Ch. 6 Exercises | 193 / 174 | 1–17 | 198 | 17 |
| Ch. 6 Problems | 198 / 179 | 1–4 (2\*, 3\*, 4\*) | 199 | 4 |
| Ch. 7 Exercises | 218 / 199 | 1–12 | 221 | 12 |
| Ch. 7 Problems | 222 / 203 | 1–4 (2\*, 3\*, 4\*) | 223 | 4 |
| Ch. 8 Exercises | 267 / 248 | 1–24 | 273 | 24 |
| Ch. 8 Problems | 273 / 254 | 1–9 (3\*, 4\*, 6\*, 7\*, 8\*, 9\*) | 279 | 9 |
| Ch. 9 Exercises | 297 / 278 | 1–8 | 299 | 8 |
| Ch. 9 Problems | 300 / 281 | 1–4 (3\*, 4\*) | 301 | **3** |
| Ch. 10 Exercises | 328 / 309 | 1–12 | 332 | 12 |
| Ch. 10 Problems | 333 / 314 | 1–6 (1\*, 5\*, 6\*) | 336 | 6 |
| Appendix A Problems | 360 / 341 | 1–5 (5\*) | 362 | **0 (no dir)** |
| Appendix B | — | no Exercises/Problems heading on any of PDF 363–383 | — | — |

Two boundary facts worth recording because they were the suspicions in the task:
* Chapter 5 Exercises end at **17** (item 17, Pringsheim interpolation, PDF 174; the `7 Problems`
  heading follows on PDF 175). There is **no Chapter 5 Exercise 18 or 19**.
* Chapter 8 Problems end at **9** (PDF 279), and Chapter 10 prints **6** problems (PDF 333–336).

## 4. Why these counts are trustworthy, and where they are not

Item numerals in the exercise sections are clean ASCII (`1.`, `5.∗`) at the left margin, and the
parsed number sequence inside every section is contiguous 1..N with no gap and no duplicate. A
number dropped or misread by OCR would break contiguity; none did. Independent corroboration: the
book's own cross-references ("see Problem 5 in Chapter 3", p. 133; "Problem 5 in Chapter 8", p. 315;
"Problem 4 in Chapter 10", p. 258; "Exercises 15 and 16", p. 174; …) — **26 internal citations of
the form "Exercise/Problem n … Chapter m", all 26 consistent with the maxima above, 0 violations.**

Not verified: I did not render page images (no `pdftoppm`/OCR cross-check), so a *symbol-level*
claim rests only on the Tesseract text layer. The PDF metadata says the layer was produced by
`ocrmypdf 11.0.1 / Tesseract OCR-PDF 4.1.1` (ModDate 2022-02-13) — it is OCR, not publisher text.

## 5. OCR artefact key (needed by anyone quoting this text)

`pdftotext` emits private control characters where the OCR font had no Unicode mapping. Verified by
context (counts from the `-layout` dump):

| code point | occurrences | means | evidence |
|---|---|---|---|
| U+0001 | 616 | ∫ | `\x01 f (z)dz = 0` after "closed curve γ" |
| U+0002 | 439 | ∑ (inline) | `\x02 1`, `\x02 zn` under an `∞` |
| U+0003 | 170 | ∑ (display) | `\x03∞ … n=0 an z n` |
| U+0004 | 102 | ≠ (also once ⊂) | `z \x04= 0`; `\x04 ⏎ Ω ⊂ Uα` |
| U+0005 / U+0006 | 129 / 129 | large ( / ) | `\x05 … \x06` around a matrix or a fraction |
| U+0007 | 643 | | (absolute value) | `\x07 ∂u \x072` |
| U+0008 | 69 | ∂ (partial) — *not certain* | `′ on \x08 D` |
| U+0014 | 19 | ∏ (inline) | `\x14N k=1 fk` |
| U+0015 / U+0016 | 23 / 23 | large ( / ) | `d \x15 −F (z) \x16` |
| U+0017 | 92 | ∏ (display) | `\x17 (1 + an )` |
| U+0019 / U+001A | 25 / 25 | large [ / ] | `\x19 ∞ \x1a` |
| U+0012 | 15 | ‖ (norm) | `\x12f \x12L2 (U )` |
| U+F8F1…U+F8F4 | 4–8 | pieces of big braces { } | `\uf8f1 … \uf8f2` two-case definitions |

So: an OCR quote of an integral reads `\x01`, a sum reads `\x02`/`\x03`, and `≠` reads `\x04`.
Quotes elsewhere in my gap files keep the artefact and gloss it, e.g. `\x02` = ∑.
