# Statement fidelity — cheap checks only (SS03)

This is **not** a word-by-word audit of all 206 cards. It is what could be checked mechanically
over the whole collection plus a close reading of ten cards. Point numbers are PDF page
indices (printed folio = PDF page − 19). Quotes are verbatim from the Tesseract text layer;
where the OCR mangles mathematics I say so and make no claim from the ambiguous part.

## What was checked mechanically over all 206 cards

1. **Numbering alignment.** Each card's `::: {.exercise}` block was compared by token overlap
   with the printed item of the same number in the same section (mean Jaccard 0.86). No card
   was found holding the text of a neighbouring item, and every card's best match is inside
   its own section. Two cards score low for OCR reasons only, and both were read by hand:
   `E-SS2.EX-2` (the OCR of printed item 2 is just `2. Show that` — the display and hint were
   swallowed into the previous item's text; the card's content is what the OCR shows for that
   material) and `E-SS3.EX-7` (the OCR prints `(a − 1)3/2` where the card has `(a² − 1)^{3/2}`;
   the OCR has lost the superscript `2`, and the card's version is the correct one, so no
   defect).
2. **Printed parts.** For every printed item whose parts are labelled `(a) (b) (c) …`, the
   card's statement contains at least the same labels. **No card drops a part.**
3. **Printed hints.** Every printed `[Hint: …]` was checked against the card's statement and
   its `::: {.hint}` block. 5 cards drop it — listed below. Cards that keep the hint as a
   paraphrased `.hint` block instead of the printed bracket (e.g. E-SS7.EX-8, E-SS7.EX-10,
   E-SS8.PR-4, E-SS8.PR-7, E-SS8.PR-9, E-SS10.PR-5, E-SS10.PR-6, E-SS9.PR-3, E-SS4.PR-3)
   are not counted as defects: the content is present.
4. **The book's star marks.** 28 printed items carry `∗` after the number, and Chapter 2
   Problem 1 has a starred *part*, `(b) ∗`. Of those 28, 24 had a card at audit time and **23 of
   them do not record the star anywhere**; the single exception is **E-SS2.PR-5**, whose remark
   says `The book marks this problem with an asterisk.` (The nine cards added after this audit
   do record it.) The no-card-at-audit starred items were Chapter 3 Problems 4 and 5, Chapter 9
   Problem 4 and Appendix A Problem 5. This is a collection-wide omission, not 23 separate
   errors; one concrete consequence is finding 6 below.

## Findings

All five hint findings are the same kind of defect: the printed `[Hint: …]` is part of the
printed item, and the card's statement (and its `.hint` block, if any) does not reproduce it.
Where the card's *solution* happens to use the same idea I say so, because it changes how much
work the fix is; the printed statement is the thing that is short either way.

### 1. E-SS1.EX-15 — printed hint dropped (PDF 47, printed p. 28)

Printed, after the display: `[Hint: Sum by parts.]`
Card statement: `Suppose Σ an converges. Prove that lim_{r→1−} Σ r^n an = Σ an. In other
words, a convergent series is Abel summable to its ordinary sum.` — no hint.
Also dropped: the printed closing sentence `For the precise definition of these terms, and more
information on summability methods, we refer the reader to Book I, Chapter 2.`
The idea survives in the solution (line 77 of the card: `This is the summation-by-parts formula
of [[E-SS1.EX-14]] …`).
(The OCR of this item is scrambled — a fragment `lim Σ (an+1 − an )Bn` floats in the middle —
so I claim only the hint and the closing sentence, both unambiguous in the OCR.)

### 2. E-SS1.EX-16 — printed hint dropped (PDF 47–48, printed pp. 28–29)

Printed: `[Hint: Use Stirling’s formula, which says that n! ∼ c n^{n+½} e^{−n} for some c > 0.]`
Card statement: parts (a)–(f), no hint. This one is not absorbed anywhere: the word `Stirling`
does not occur in the card at all, the solutions use the ratio test instead.
(Unrelated ambiguity, not a finding: the print's part (c) reads `an = 4nn+3n` in the OCR; the
card has `n²/(4^n + 3n)`. Only the page image can settle that one.)

### 3. E-SS1.EX-18 — printed hint dropped (PDF 48, printed p. 29)

Printed: `[Hint: Write z = z0 + (z − z0 ) and use the binomial expansion for z n .]`
Card statement: `Let f be a power series centered at the origin. Prove that f has a
power-series expansion around every point in its disc of convergence.` — no hint. The idea
survives in the solution (`By the binomial theorem, the inner sum equals …`).

### 4. E-SS1.EX-21 — printed hint dropped (PDF 48–49, printed pp. 29–30)

Printed: `[Hint: Use the dyadic expansion of an integer and the fact that
2^{k+1} − 1 = 1 + 2 + 2² + · · · + 2^k .]`
Card statement: the two identities plus `Justify any change in the order of summation.` — no hint.
The idea survives in the solution (the dyadic expansion `Σ_j z^{2^k(2j+1)}` is used).

### 5. E-SS8.EX-13 — printed hint dropped (PDF 270, printed p. 251)

Printed, after part (a): `[Hint: Consider the automorphism ψα (z) = (z − α)/(1 − αz) and apply
the Schwarz lemma to ψf−1(w) ◦ f ◦ ψw .]` (the OCR prints the composition's factors in the
wrong order — `ψf−1(w) ◦ f ◦ ψw` is what it gives; the meaning is the standard conjugation).
Card statement: parts (a) and (b), no hint and no `.hint` block. The solution does use a disk
automorphism and Schwarz's lemma, so only the labelled hint is missing.

### 6. E-SS2.PR-1 — starred part not marked (PDF 86–87, printed pp. 67–68)

Printed: `(b) ∗ Fix 0 < α < ∞. Show that the analytic function f defined by …` — part (b) is
starred (the harder part).
Card E-SS2.PR-1 reproduces part (b) and its hint correctly but marks nothing. Minor: the
mathematical content is intact; only the book's difficulty marking is lost. No card records a
starred *part* (the whole-item marks are covered in §4: 23 of the 24 old starred cards lose
them, E-SS2.PR-5 being the exception).

## Close reading that found nothing (recorded so the ground is covered)

These cards were read against the print and match, including hypotheses and part structure:
`E-SS3.PR-1` (parts (a)–(g), three hints, all present), `E-SS3.PR-2` (Poisson integral,
hint present), `E-SS9.PR-1`, `E-SS9.PR-2`, `E-SS9.PR-3` (hint present as a `.hint` block),
`E-SS2.EX-2` (hint present), `E-SS7.EX-8` and `E-SS7.EX-10` (hints present, paraphrased),
`E-SS10.PR-5` and `E-SS8.PR-4` (long printed hints present as `.hint` blocks).

## Two passages that need the page image before any claim is made

* **E-SS4.PR-3, hint** (PDF 152): OCR `Fǫ (z) = F (z)e−ǫz`; the card's `.hint` block has
  `F(z)e^{-εz²}`. A lost superscript `2` in the OCR is the likely explanation, but if the print
  really has `e^{-εz}` then the card has silently corrected the book's hint.
* **E-SS1.EX-16(c)** (PDF 47–48): OCR `an = 4nn+3n`; card `n²/(4^n + 3n)`.

## Not done

Proofs and solutions in the cards were not audited. Titles were not checked against the print.
No card was checked for *added* material (extra hypotheses not in the book) beyond the token
comparison above.
