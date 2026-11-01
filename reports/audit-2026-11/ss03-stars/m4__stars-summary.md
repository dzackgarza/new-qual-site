# stars-summary.md — printed difficulty asterisks, Chapters 9, 10 and Appendix A

Slice worked: **chapters 9, 10 and Appendix A** of Stein–Shakarchi, *Complex Analysis*.
That is every printed Exercise and Problem item in those chapters —
8 + 4 + 12 + 6 + 5 = **35 items**, of which **6 are starred**.

Patches: [stars-ch9.md](stars-ch9.md), [stars-ch10.md](stars-ch10.md),
[stars-appendix-a.md](stars-appendix-a.md). Nothing under `corpus/` was edited;
`python3 tools/apply_repairs.py --check` on the three files reports 6 patches, each
`OLD` occurring exactly once.

## Method

* Page mapping: printed page = PDF page − 19, confirmed on each page from the running
  head and the printed folio (`PDF 300` carries `4. Problems` and `281`, etc.).
* Text and page: `pdftotext -layout -f A -l B`.
* Asterisk: `pdftotext -bbox-layout` **and** `mutool draw -F stext` (per-character
  boxes, font name and size).
* Independent cross-check of completeness: both extractors report exactly **136**
  asterisk glyphs in the whole book (U+2217, `∗`), on exactly the same pages; no
  glyph was lost by either. So no asterisk can have been silently missed in this
  slice.
* One correction to the repo's own account: `COMPLAINTS.md` says the extraction has
  "no ASCII `*`". True but misleading — the printed asterisks **are** in the text
  layer, as U+2217 ASTERISK OPERATOR, not as ASCII `*`. A search for `*` finds
  nothing; a search for `∗` finds all 136 asterisk glyphs, of which 29 are printed
  marks and the rest are mathematics (`Λ∗`, `σ₁*(n)`, `E₂*(τ)`, `Γ∗`, `t∗`, …).

## Rendering convention

`$^{*}$` — LaTeX superscript asterisk with an empty base, which is what the book sets
(TeX `^{*}`, glyph U+2217 in CMSY6 at superscript size, 5.98 pt). Placed immediately
after the printed item marker.

No card in the corpus renders a star in a statement, so there was no existing
convention to copy; the only card that mentions its star at all (`E-SS2.PR-5`,
chapter 2) says so in a `::: {.remark}` prose note, not as a mark. Since cards do not
reproduce the item number in the statement body, the item's marker is the start of
the statement block, so `$^{*}$` becomes the first thing after the `::: {.exercise}`
opener — exactly where the number stands in the book. For a starred sub-part the
marker is the sub-part label and the star would go directly after `(b)` on that line;
verified that this form parses and renders (`pandoc -f markdown`) but **no sub-part
in this slice is starred**, so no such patch is emitted.

## Chapter 9 — An Introduction to Elliptic Functions

Exercises, printed pp. 278–280 · Problems, printed pp. 281–282.

| Item | Starred? | Card | Card already showed the star? |
|---|---|---|---|
| Exercise 1 | no | `E-SS9.EX-1` | — |
| Exercise 2 | no | `E-SS9.EX-2` | — |
| Exercise 3 | no | `E-SS9.EX-3` | — |
| Exercise 4 | no | `E-SS9.EX-4` | — |
| Exercise 5 | no | `E-SS9.EX-5` | — |
| Exercise 6 | no | `E-SS9.EX-6` | — |
| Exercise 7 | no | `E-SS9.EX-7` | — |
| Exercise 8 | no | `E-SS9.EX-8` | — |
| Problem 1 | no | `E-SS9.PR-1` | — |
| Problem 2 | no | `E-SS9.PR-2` | — |
| **Problem 3** | **yes** | `E-SS9.PR-3` | no — patched |
| **Problem 4** | **yes** | `E-SS9.PR-4` | no — patched |

`E-SS9.PR-4` is the near miss: its `source-checked` audit note says "the asterisk
marking a starred problem … [is] preserved", but the statement carries no mark. The
patch makes the statement match the note. Both `(a)` and `(b)` of Problem 4 are
unstarred in the print, and so are `(a)`–`(c)` of Problem 1.

## Chapter 10 — Applications of Theta Functions

Exercises, printed pp. 309–313 · Problems, printed pp. 314–317.

| Item | Starred? | Card | Card already showed the star? |
|---|---|---|---|
| Exercises 1–12 | no (all twelve) | `E-SS10.EX-1` … `E-SS10.EX-12` | — |
| **Problem 1** | **yes** | `E-SS10.PR-1` | no — patched |
| Problem 2 | no | `E-SS10.PR-2` | — |
| Problem 3 | no | `E-SS10.PR-3` | — |
| Problem 4 | no | `E-SS10.PR-4` | — |
| **Problem 5** | **yes** | `E-SS10.PR-5` | no — patched |
| **Problem 6** | **yes** | `E-SS10.PR-6` | no — patched |

Parts `(a)`–`(f)` of Problem 6 and `(a)`–`(d)` of Problem 4 are unstarred. The many
`∗` glyphs on printed pp. 304–313 are the mathematics (`σ₁*(n)`, `E₂*(τ)`, `σ₃*(n)`,
`E₄*(τ)`), not difficulty marks.

## Appendix A — Asymptotics

Problems, printed pp. 341–343 (Appendix A has no Exercises section).

| Item | Starred? | Card | Card already showed the star? |
|---|---|---|---|
| Problem 1 | no | `E-SSA.PR-1` | — |
| Problem 2 | no | `E-SSA.PR-2` | — |
| Problem 3 | no | `E-SSA.PR-3` | — |
| Problem 4 | no | `E-SSA.PR-4` | — |
| **Problem 5** | **yes** | `E-SSA.PR-5` | no — patched |

Parts `(a)` and `(b)` of Problem 1 are unstarred; the `Γ*` glyphs in the Appendix A
body are the book's contour, not marks.

## Unsettled

**None in this slice.** `pdftotext -bbox-layout` and `mutool draw -F stext` agree on
every asterisk on every page of chapters 9 and 10 and Appendix A: identical pages,
identical positions, identical count. There is no item on which the OCR text and the
glyph layer disagree. (The book file is not, in fact, a scan: it carries 18 subset
TeX fonts and no page image, so both extractors read the same vector glyphs.)

## Appendix — whole-book inventory, for cross-checking by the other slices

Derived the same way; **not** patched here (they belong to chapters 1–8). Printed
item marks = 29: 28 starred items plus one starred **sub-part**, Chapter 2 Problem 1
part (b), printed p. 68. That is consistent with this week's "26 to 28 starred printed
items" reports: counting starred *items* gives 28, and the lower counts missed one or
two of the chapter 2–3 marks.

| PDF page | Printed page | Chapter | Mark |
|---|---|---|---|
| 87 | 68 | Ch. 2 Problems | Problem 1 `(b)∗` (a sub-part) and Problem `2.∗` |
| 88 | 69 | Ch. 2 Problems | Problem `5.∗` |
| 127 | 108 | Ch. 3 Problems | `1.∗` |
| 129 | 110 | Ch. 3 Problems | `4.∗`, `5.∗` |
| 152 | 133 | Ch. 4 Problems | `3.∗`, `4.∗` |
| 176 | 157 | Ch. 5 Problems | `2.∗`, `3.∗`, `4.∗` |
| 199 | 180 | Ch. 6 Problems | `2.∗`, `3.∗`, `4.∗` |
| 223 | 204 | Ch. 7 Problems | `2.∗`, `3.∗`, `4.∗` |
| 275 | 256 | Ch. 8 Problems | `3.∗` |
| 276 | 257 | Ch. 8 Problems | `4.∗` |
| 277 | 258 | Ch. 8 Problems | `6.∗`, `7.∗` |
| 278 | 259 | Ch. 8 Problems | `8.∗`, `9.∗` |
| 300 | 281 | Ch. 9 Problems | `3.∗` |
| 301 | 282 | Ch. 9 Problems | `4.∗` |
| 333 | 314 | Ch. 10 Problems | `1.∗` |
| 335 | 316 | Ch. 10 Problems | `5.∗`, `6.∗` |
| 362 | 343 | Appendix A Problems | `5.∗` |

Every mark in the book is on a **Problem**; no Exercise in any chapter is starred.

## Incidental, not a star issue and deliberately not changed

`E-SS10.PR-1` reads "$a$ and $k$ are nonnegative integers" and "The converse for
positive integers"; the print says "$a$ and $k$ are positive integers" and states the
converse as "every $n$ that is not of that form can be written as the sum of
three-squares". Out of scope for a star repair; recorded here so it is not lost.
