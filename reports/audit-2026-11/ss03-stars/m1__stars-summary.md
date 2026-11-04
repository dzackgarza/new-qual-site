# stars-summary.md — printed difficulty asterisks, Stein–Shakarchi *Complex Analysis*

Slice 2 of the swarm (`m1`): **chapters 4, 5, 6**, exercises and problems.
Statements only; nothing under `corpus/` was edited. The repairs are in
`stars-ch4.md`, `stars-ch5.md`, `stars-ch6.md`, in the `CARD:`/`OLD:`/`NEW:` form
that `tools/apply_repairs.py` parses (verified with `--check`: 8 blocks, every
`OLD` occurs exactly once).

## Rendering convention

`$^{*}$` immediately before the first word of the statement block, followed by
one space: the card then reads like the print's `3.∗ In this problem, …`. No card
in the corpus renders a star inline — the only star on record anywhere is
`E-SS2.PR-5`, which mentions it in a `::: {.remark}` rather than in the statement
— so there was no existing inline convention to copy, and the head of the
statement is where the printed item number sits (the cards carry no item number:
it lives in the card id and in the collection index `comment: Ch. 4, Problem 3`).
A starred sub-part would be patched on its own line as `(b) ` + `$^{*}$`; this slice has
none.

## Method

Three independent readings, which agreed everywhere:

1. **Two copies of the book.** The repository scan
   (`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`, ocrmypdf 11.0.1 /
   Tesseract 4.1.1 text layer) and a second, independently produced PDF of the
   same edition (`dvips` + Acrobat Distiller, no OCR layer) were read separately.
   Every starred item found in one is starred in the other, at the same printed
   page; neither copy has a star the other lacks.
2. **Two text engines.** Poppler (`pdftotext -layout`, `-bbox` word boxes) and
   MuPDF (`mutool draw -F stext`, per-glyph char, font, size, baseline). The
   difficulty star has a fixed typographic signature: glyph `U+2217` in **CMSY6**,
   5.98 pt against an 8.97 pt body, baseline raised 3.7–3.9 pt above the line's
   body baseline, sitting immediately after the item number. A math exponent
   (`e^{−2πixξ}`, `sin²`, `|a_n|^{1/n}`) has the same small size and raise but
   never follows an item number at the left margin; every such case was listed and
   discarded individually.
3. **The rendered page.** 300 dpi bitmap of the page; ink is present in exactly
   the bbox of each star word (39 pixels for ch4 Problem 3) and absent in the same
   column beside unstarred item numbers.

The Preface (printed p. viii) states the rule the print follows: "*There are also
more involved and challenging 'Problems'; the ones that are most difficult, or go
beyond the scope of the text, are marked with an asterisk.*" So stars attach to
Problems, not to Exercises — which is what the geometry shows for every chapter:
no Exercise anywhere in the book carries one, and the only starred sub-part
(ch. 2 Problem 1(b)) sits inside a Problem.

## Chapter 4 — printed pp. 111–133

12 Exercises (printed pp. 127–131), 4 Problems (pp. 131–133).

| printed item | star? | evidence | recorded on card? |
| --- | --- | --- | --- |
| Exercise 1–12 | no | no star glyph after any item number on pp. 127–131, in either copy | — |
| Problem 1 | no | `1.` followed by body-size `Suppose` on p. 131 | — |
| Problem 2 | no | `2.` on p. 132 | — |
| **Problem 3** | **yes** | `3.∗` p. 133 (PDF p. 152) | no |
| **Problem 4** | **yes** | `4.∗` p. 133 (PDF p. 152) | no |

Patched: `E-SS4.PR-3`, `E-SS4.PR-4`. Unsettled: none.

## Chapter 5 — printed pp. 134–158

17 Exercises (pp. 153–156), 4 Problems (pp. 156–158).

| printed item | star? | evidence | recorded on card? |
| --- | --- | --- | --- |
| Exercise 1–17 | no | no star glyph on pp. 153–156 | — |
| Problem 1 | no | `1.` on p. 156 | — |
| **Problem 2** | **yes** | `2.∗` p. 157 (PDF p. 176) | no |
| **Problem 3** | **yes** | `3.∗` p. 157 | no |
| **Problem 4** | **yes** | `4.∗` p. 157 | no |

Patched: `E-SS5.PR-2`, `E-SS5.PR-3`, `E-SS5.PR-4`. Unsettled: none.

## Chapter 6 — printed pp. 159–180

17 Exercises (pp. 174–178), 4 Problems (pp. 179–180).

| printed item | star? | evidence | recorded on card? |
| --- | --- | --- | --- |
| Exercise 1–17 | no | no star glyph on pp. 174–178 | — |
| Problem 1 | no | `1.` on p. 179 | — |
| **Problem 2** | **yes** | `2.∗` p. 180 (PDF p. 199) | no |
| **Problem 3** | **yes** | `3.∗` p. 180 | no |
| **Problem 4** | **yes** | `4.∗` p. 180 | no |

Patched: `E-SS6.PR-2`, `E-SS6.PR-3`, `E-SS6.PR-4`. Unsettled: none.

## OCR / glyph disagreements

None in chapters 4–6: at every one of the 58 printed items the two text engines
and the two copies agree on the presence or absence of a star, so nothing in this
slice is marked unsettled.

Two near-misses were checked and cleared:

- **ch. 4 Exercise 5, part (b)** (printed p. 128). `pdftotext -layout` emits a
  stray `0x08` before "In particular", which looks like a dropped glyph. The
  per-glyph stream shows `(b)` then a body-size space and `I` of "In"; the gap
  between the label and "In" is 5.18 pt and contains 0 ink pixels. The `0x08` is
  an artefact of the big integral sign on the display line, not a star.
- **ch. 4 Problem 1 and ch. 6 Exercise 11.** The pixel sweep saw ink inside the
  6 pt window after the item number; in both cases it is the first letter of the
  next word (`Suppose`, `Let`) at body size and body baseline. Not a star.

## Cross-check outside the slice (not patched here)

Both copies were scanned end to end for a star after an item number, mostly to
check the slice against the 26–28 figure in `COMPLAINTS.md`. The two copies agree
exactly on **29 marks: 28 starred items plus one starred sub-part**.

ch2 Problems 2, 5 and Problem 1 part (b) · ch3 Problems 1, 4, 5 · ch4 Problems 3, 4 ·
ch5 Problems 2, 3, 4 · ch6 Problems 2, 3, 4 · ch7 Problems 2, 3, 4 · ch8 Problems 3, 4, 6, 7, 8, 9 ·
ch9 Problems 3, 4 · ch10 Problems 1, 5, 6 · Appendix A Problem 5. Chapter 1 has none.

So 28 whole starred items (the figure the reports converged on), 29 printed marks
if the ch. 2 Problem 1(b) star is counted separately, and 27 if the ch. 2 sub-part
is counted with its item — which brackets the reported 26–28. Other members own
those chapters; this list is offered only as an independent check.
