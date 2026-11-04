# Printed difficulty asterisks — summary for slice 1 (chapters 1, 2, 3)

Scope: every printed Exercise and Problem of chapters 1, 2, 3 of Stein–Shakarchi, *Complex Analysis*
(`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, 398 pp., printed page = PDF page − 19).
Statements only; no proof work. Nothing under `corpus/` was modified: the result is the three patch
specifications `stars-1.md`, `stars-2.md`, `stars-3.md` in this directory.

## How the asterisks were read

1. **Glyph layer (authority).** `mutool draw -F stext.json` over all 398 pages gives every typeset text run
   with its font, point size, baseline origin and bounding box. The book's own typeset layer is present and
   intact (CMR/CMBX/CMMI/CMSY fonts; the Tesseract `GlyphLessFont` layer survives only on the cover, PDF p. 1).
   A star marker is a `∗` (U+2217) set in CMSY6 at 5 pt, in superscript position — its 3×2 pt box sits at the
   top of the line, level with the top of the item number's box — and its x-origin lies 0–1 pt right of the
   bold item number's box (`2.` CMBX9, 8 pt, box at x = 43, w = 8, so the star's origin is x = 51); a starred
   sub-part is the same glyph with the same geometry immediately after the `(a)`/`(b)` label.
2. **Text layer (cross-check).** `pdftotext -layout` on the same PDF. It *does* carry the asterisk, as
   U+2217 `∗`, in exactly the starred places — so `pdftotext` renders it, just not as ASCII `*`. A search for
   `\*` therefore finds nothing while a search for `∗` finds every starred item. This is why
   `COMPLAINTS.md` item 4 ("the extraction has no ASCII `*`") is true but misleading, and why the corpus is
   missing the stars although the attachment has them.
3. **Exhaustive sweep.** All 136 occurrences of U+2217 in the book were classified by position. Exactly 29 of
   them stand at the left margin directly after an item number or sub-part label; the rest are mathematics
   (`t*`, `Λ*`, `F*`, `E*`, `σ*`, `D*`, `Γ*`, …). No other asterisk-like character (ASCII `*`, `⋆`, `★`) occurs
   anywhere in the layer.
4. **Per-item audit.** For each of the 26 + 15 + 5 + 22 + 5 printed items of chapters 1–3 the bold item number
   was located and tested for an adjacent raised glyph. Items found: chapter 1 Exercises 1–26,
   chapter 2 Exercises 1–15, chapter 2 Problems 1–5, chapter 3 Exercises 1–22, chapter 3 Problems 1–5, i.e.
   every item, none missing and none unreadable.

## Rendering convention (identical in all three patch files)

* The star is written in LaTeX, `$^{*}$` — every card in this collection writes its mathematics in LaTeX.
* No card in the corpus shows a star *glyph* to copy: the only existing records are prose (the `::: {.remark}`
  on `E-SS2.PR-5`, and the `audit:` note on `E-SS3.PR-4`/`E-SS3.PR-5` which claims the asterisk was
  preserved when it was not). So this is the first glyph convention in the collection, and it is
  `$^{*}$` — the same shape `E-SS2.PR-5`'s remark asserts.
* **Where.** The cards do not print the item number inside the statement block, so a printed `2.∗` has no
  number to follow on the card. For a starred **whole item** the star goes at the head of the statement, in
  the position the printed number occupies, as `$^{*}$ ` (star, one space) before the first word — giving
  `$^{*}$ Let $F(z) = …` for a card whose print reads `2.∗ Let F(z) = …`. For a starred **sub-part** the star
  goes immediately after the sub-part label, `(b) $^{*}$ Fix …`, which is exactly where the print puts it.
* Each `NEW` block differs from its `OLD` block by that insertion and nothing else; the `OLD` anchor is the
  `::: {.exercise}` line plus the statement's first line (or the sub-part's own line), which is unique in
  its card.

## Chapter 1 (printed pp. 24–31; the chapter has no Problems section)

| printed item | starred? | recorded on a card? | patch |
| --- | --- | --- | --- |
| Exercises 1–26 | no, none of them | — | none |

The only asterisks on PDF pp. 43–50 are the `t*` of Exercise 5(a) (twice, p. 44) — mathematics, not a marker.
`stars-1.md` consequently contains no `CARD:` block.

## Chapter 2 (Exercises printed pp. 64–67, Problems pp. 67–70)

| printed item | starred? | recorded on a card? | patch |
| --- | --- | --- | --- |
| Exercises 1–15 | no, none of them | — | none |
| Problem 1, part **(b)** | **yes** (`(b) ∗ Fix 0 < α < ∞`, p. 68) — part (a) is not | no | `stars-2.md` |
| Problem 2 | **yes** (`2.∗`, p. 68) | no | `stars-2.md` |
| Problem 3 | no | — | none |
| Problem 4 | no | — | none |
| Problem 5 | **yes** (`5.∗`, p. 69) | **prose only**: the card's remark says "The book marks this problem with an asterisk", but the statement shows no glyph | `stars-2.md` |

## Chapter 3 (Exercises printed pp. 103–108, Problems pp. 108–110)

| printed item | starred? | recorded on a card? | patch |
| --- | --- | --- | --- |
| Exercises 1–22 | no, none of them | — | none |
| Problem 1 | **yes** (`1.∗`, p. 108); its parts (a)–(g) are not | no | `stars-3.md` |
| Problem 2 | no | — | none |
| Problem 3 | no | — | none |
| Problem 4 | **yes** (`4.∗`, p. 110) | **claimed but absent**: the `audit:` note says "the asterisk marking a starred problem … preserved", the statement carries none | `stars-3.md` |
| Problem 5 | **yes** (`5.∗`, p. 110); its parts (a)–(b) are not | **claimed but absent**, as Problem 4 | `stars-3.md` |

## Unsettled items

**None in this slice.** The glyph layer and the poppler text layer agree on the presence and the position of
every asterisk of chapters 1–3; where they differ at all it is only in spacing — `pdftotext` writes
`(b) ∗` and `2.∗`, the glyph layer has the star 8 pt right of the number's origin in the first case and
glued to it in the second. Both readings say the same thing about which item is starred, so nothing is
guessed. No item was marked unsettled.

One judgement, recorded here because it is a judgement and not a reading: the *position* of the restored
star on a card (head of the statement) is a rendering decision, forced by the cards not printing their item
numbers. The *fact* that each of the items above is starred is read, not judged.

## Verification performed

* `python3 tools/apply_repairs.py --check .ultramath/smvy5dx9m/m2/stars-{1,2,3}.md` → exit 0, six blocks,
  each `OLD` occurring exactly once:
  `would patch corpus/collections/SRC-TEXT-SS03/ch2-problems/E-SS2.PR-2.md (1)` … `E-SS3.PR-5.md (1)`.
* The patches were also applied to copies of the six cards outside `corpus/` and diffed: each diff is a
  single changed line whose only difference is the inserted `$^{*}$ `.
* No file under `corpus/` was touched (`--check` only reads).

## Appendix — the same sweep over the whole book (outside my slice; not patched by me)

Recorded because the reading is mechanical and the other slices can be checked against it. Item numbers
only; starred sub-parts are noted separately. 28 starred items and 1 starred sub-part.

| chapter | printed items starred (printed page) |
| --- | --- |
| 1 | none |
| 2 | Problem 2 (68), Problem 5 (69); sub-part Problem 1(b) (68) |
| 3 | Problem 1 (108), Problem 4 (110), Problem 5 (110) |
| 4 | Problem 3 (133), Problem 4 (133) |
| 5 | Problem 2 (157), Problem 3 (157), Problem 4 (157) |
| 6 | Problem 2 (180), Problem 3 (180), Problem 4 (180) |
| 7 | Problem 2 (204), Problem 3 (204), Problem 4 (204) |
| 8 | Problem 3 (256), Problem 4 (257), Problem 6 (258), Problem 7 (258), Problem 8 (259), Problem 9 (259) |
| 9 | Problem 3 (281), Problem 4 (282); no exercise |
| 10 | Problem 1 (314), Problem 5 (316), Problem 6 (316); no exercise |
| Appendix A | Problem 5 (343) |

No exercise of any chapter is starred. This is consistent with the "26 to 28 starred printed items"
previously reported: 28 items if the starred sub-part of chapter 2 Problem 1 is not counted as an item,
29 marks if it is.
