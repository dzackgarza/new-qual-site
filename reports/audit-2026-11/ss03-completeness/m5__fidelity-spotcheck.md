# Statement-fidelity spot check — `SRC-TEXT-SS03`

Scope: this is the "only where cheap" part of the audit. It is a **sample**, not a verification of all 206
cards. Nothing here touches proofs; statements only. Page numbers are printed pages of
`assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page = printed page + 19). Quotations are from
the OCR text layer (`pdftotext -layout`), which mangles formula layout — that is stated wherever it matters.

## 1. Numbering correspondence — all 206 cards

For every card I extracted its id and the contents of its `::: {.exercise}` block, and matched it to the
printed item with the same chapter, section and number. Results:

- 206 cards, 206 distinct (chapter, EX/PR, number) triples; no duplicate, no card whose number exceeds the
  printed maximum for its section, no card for a non-existent item.
- Printed maxima (exercises / problems): ch1 26/–; ch2 15/5; ch3 22/5; ch4 12/4; ch5 17/4; ch6 17/4;
  ch7 12/4; ch8 24/9; ch9 8/4; ch10 12/6; App A –/5.
- 18 cards were then read against the printed item side by side: the ones whose statement vocabulary
  overlapped the printed item least, plus every hint-loss candidate —
  `E-SS1.EX-15`, `E-SS1.EX-16`, `E-SS1.EX-18`, `E-SS1.EX-21`, `E-SS2.EX-4`, `E-SS4.EX-3`, `E-SS5.EX-10`,
  `E-SS5.PR-1`, `E-SS5.PR-4`, `E-SS6.EX-7`, `E-SS7.EX-10`, `E-SS8.EX-13`, `E-SS8.PR-4`, `E-SS8.PR-9`,
  `E-SS9.PR-3`, `E-SS10.EX-5`, `E-SS10.PR-5`, `E-SS10.PR-6`.
  All 18 hold the statement of the printed item bearing their number: **no misnumbering was found in the
  sample.**
- Not checked: the other ~188 cards at word level, and part-by-part completeness within any card.

## 2. Bracketed hints dropped from five cards

Of the 96 printed items that carry a `[Hint: …]`, five cards for existing items contain no hint at all
(the card file was read in full: no `{.hint}` block, no "[Hint", no "*Hint.*"). The printed hint is quoted
below; each should be restored.

| card | printed page | printed hint (OCR) |
|---|---|---|
| `ch1-exercises/E-SS1.EX-15.md` | 28 | "[Hint: Sum by parts.]" — the card also drops the two printed sentences that follow it: "In other words, if a series converges, then it is Abel summable with the same limit. For the precise definition of these terms, and more information on summability methods, we refer the reader to Book I, Chapter 2." |
| `ch1-exercises/E-SS1.EX-16.md` | 28 | "[Hint: Use Stirling's formula, which says that 1 n! ∼ c n n+ 2 e−n for some c > 0..]" (the OCR doubles the full stop; the formula is Stirling's formula, mangled) |
| `ch1-exercises/E-SS1.EX-18.md` | 29 | "[Hint: Write z = z0 + (z − z0 ) and use the binomial expansion for z n .]" |
| `ch1-exercises/E-SS1.EX-21.md` | 29 | "[Hint: Use the dyadic expansion of an integer and the fact that 2k+1 − 1 = 1 + 2 + 22 + · · · + 2k .]" |
| `ch8-exercises/E-SS8.EX-13.md` | 251 | "[Hint: Consider the automorphism ψα (z) = (z − α)/(1 − αz) and apply the −1 Schwarz lemma to ψf (w) ◦ f ◦ ψw .]" — OCR has lost the bar and split the superscript; printed, this is the hint to compose the two disc automorphisms ψ_{f(w)}^{-1} ∘ f ∘ ψ_w |

Five chapter-1 items whose printed text has a hint do keep one in the card (`E-SS1.EX-4`, `EX-6`, `EX-7`,
`EX-19`, `EX-22`), so the loss is per-card, not systematic.

Two chapter-5 cards keep their hint but not in the corpus's `{.hint}` block: `E-SS5.PR-1` writes
"*Hint.* Use Jensen's formula." inside the exercise block, and `E-SS5.PR-4` does the same for both halves of
its (long) printed hint. Content present, formatting inconsistent — flagged only so a normaliser does not
mistake them for losses.

## 3. The difficulty asterisk is not recorded

The preface (printed p. viii) says: "There are also more involved and challenging "Problems"; the ones that
are most difficult, or go beyond the scope of the text, are marked with an asterisk." The book prints an
asterisk on 28 items, all of them Problems (ch2 PR-2, PR-5; ch3 PR-1, PR-4, PR-5; ch4 PR-3, PR-4;
ch5 PR-2, PR-3, PR-4; ch6 PR-2, PR-3, PR-4; ch7 PR-2, PR-3, PR-4; ch8 PR-3, PR-4, PR-6, PR-7, PR-8, PR-9;
ch9 PR-3, PR-4; ch10 PR-1, PR-5, PR-6; App A PR-5). No exercise is starred.

Of those, 24 have cards. **Only one of the 24 records the asterisk**: `E-SS2.PR-5` says "The book marks this
problem with an asterisk." The other 23 carry no star/asterisk/difficulty field or note; where a `*` does
occur in them it is a formula character (`E_4^*`, `\sigma_3^*`). So the difficulty information the book prints
is lost at card level for 23 cards (and for the four starred problems that have no card at all:
`ch3-problems/E-SS3.PR-4`, `E-SS3.PR-5`, `ch9-problems/E-SS9.PR-4`, `appA-problems/E-SSA.PR-5`).

## 4. What this file does not claim

No statement was re-derived mathematically; I only compared card text with printed text. Formula-level
fidelity is unchecked wherever the OCR is mangled — which, for the five hints above and for most items
containing displayed mathematics, means the wording and the page are reliable but the symbols in the OCR
quotation are not. Where a card looked different from the OCR text, I checked by reading the card's own
LaTeX rather than treating OCR noise as a defect.
