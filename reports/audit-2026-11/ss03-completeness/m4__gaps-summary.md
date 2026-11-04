# SRC-TEXT-SS03 — gap audit summary

Auditor: member m4. Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`
(398 pages, OCR'd with ocrmypdf/Tesseract). Method: `pdftotext -layout` over the whole file,
split into PDF pages, then for every chapter the printed "Exercises"/"Problems" blocks were
read page by page and every top-level numbered item transcribed; each block's numbering was
checked for continuity 1..N, so an item the OCR had merged into its predecessor would appear
as a hole. The card inventory was re-derived from the files on disk (206 cards, matching the
collection's own `index.md`), not taken from the brief.
PDF page = printed folio + 19 throughout (PDF 43 = printed 24, PDF 360 = printed 341).

## Totals per chapter (printed vs cards)

| chapter | Exercises printed | EX cards | Problems printed | PR cards | missing |
|---|---|---|---|---|---|
| 1  | 26 | 26 | – (no Problems section) | – | — |
| 2  | 15 | 15 | 5 | 5 | — |
| 3  | 22 | 22 | 5 | **2** | **PR-3, PR-4, PR-5** |
| 4  | 12 | 12 | 4 | 4 | — |
| 5  | 17 | 17 | 4 | 4 | — |
| 6  | 17 | 17 | 4 | 4 | — |
| 7  | 12 | 12 | 4 | 4 | — |
| 8  | 24 | 24 | 9 | 9 | — |
| 9  | 8  | 8  | 4 | **3** | **PR-4** |
| 10 | 12 | 12 | 6 | 6 | — |
| App. A | – (no Exercises section) | – | 5 | **0** | **PR-1 … PR-5** (no directory at all) |
| **total** | **165** | **165** | **50** | **41** | **9 items** |

Block locations (PDF pages): ch1 EX 43–50; ch2 EX 83–86, PR 86–89; ch3 EX 122–127, PR 127–129;
ch4 EX 146–150, PR 150–152; ch5 EX 172–175, PR 175–177; ch6 EX 193–198, PR 198–199;
ch7 EX 218–222, PR 222–223; ch8 EX 267–273, PR 273–279; ch9 EX 297–300, PR 300–301;
ch10 EX 328–333, PR 333–336; Appendix A PR 360–362; Appendix B (PDF 363–383) prints no
numbered exercises or problems.
Layout trap for anyone recounting: **every chapter's exercise block runs over onto the first
page of its Problems block** (ch2 EX 13–15 sit on PDF 86 above "7 Problems"; likewise ch3
EX 22, ch4 EX 12, ch5 EX 16–17, ch6 EX 17, ch7 EX 11–12, ch8 EX 24). A count that stops at
the page carrying the "Problems" heading undercounts the exercises.

## The missing items (9)

Full statements, quoted from the OCR, are in the per-chapter files:

* `gaps-ch3.md` — PDF p. 128 (printed 109): `ch3-problems/E-SS3.PR-3.md` (Laurent expansion
  in an annulus). PDF p. 129 (printed 110): `ch3-problems/E-SS3.PR-4.md` (starred; separating
  a simply connected region by a line) and `ch3-problems/E-SS3.PR-5.md` (starred; a holomorphic
  function with prescribed jump across `[−M, M]`, two bracketed hints that must be carried
  over).
* `gaps-ch9.md` — PDF p. 300–301 (printed 281–282): `ch9-problems/E-SS9.PR-4.md` (starred; ℘
  real on the half-period lines and conformal onto a half-plane).
* `gaps-appendixA.md` — PDF p. 360–362 (printed 341–343): five problems of Appendix A
  "Asymptotics"; no directory exists. Recommended `appendixA-problems/E-SS-A.PR-1.md` …
  `E-SS-A.PR-5.md` (naming is a human decision — the `E-SS<chapter>` scheme has no appendix
  form) plus a new section entry in `index.md`.

The three suspicions named in the brief, answered from the block ends themselves:
* **Is there a chapter 5 exercise 19? No.** Chapter 5 prints exercises 1–17: EX-17 ends on
  PDF p. 175 (printed 156) and the same page carries the heading "7 Problems" and problem 1;
  problems 2–4 are on PDF p. 176 and PDF p. 178 opens chapter 6. The 17 cards are complete.
* **Does chapter 8 have problems beyond 9? No.** PR-9 (starred, Gauss/AGM) runs from PDF
  p. 278 to PDF p. 279 (printed 259–260) and ends "…is a consequence of the identity in (b)
  of Exercise 24."; PDF p. 280 opens chapter 9. Nine is the whole block.
* **How many problems does chapter 10 print? Six.** PR-1 … PR-6 on PDF p. 333–336 (printed
  314–317), PR-6 (starred, `r_8(n)`) ending on PDF p. 336 with its parts (a)–(f); PDF p. 337
  opens Appendix A. Six cards = complete.

## Statement fidelity — findings

Chapters verified **card by card** against the print (statement block, sub-parts, hints,
remarks and audit notes): **1, 3, 5, 6, 10** — that is 26+22+2+17+4+17+4+12+6 = 110 of the
206 cards. No proof was audited. Details in `gaps-ch1.md`, `gaps-ch3.md`, `gaps-ch5.md`,
`gaps-ch6.md`, `gaps-ch10.md`.

Important convention in this collection: several cards record a departure from the print in
a `::: {.remark}` block and/or a `source-corrected` / `source-checked` audit event with a
note naming the printed wording. A "difference" is therefore not automatically a defect; I
mark below whether it is recorded.

**Recorded repairs (10) — the card differs from the print, and says so.**
`E-SS1.EX-13` (print "open set" → card "region (open connected set)"), `E-SS6.EX-4`
(α restricted to `∉ {0,−1,−2,…}`), `E-SS6.EX-11` (strip `|y|<π` → `π/2`; `Γ(a+iξ)` →
`Γ(a−2πiξ)`), `E-SS6.EX-17(b)` (`I(0)=0` → `I(0)=f(0)`; `f^{(n+1)}(0)` → `f^{(n)}(0)`),
`E-SS6.PR-1(a)` (`−N^{s−1}/(s−1)` → `+N^{1−s}/(s−1)`) and `PR-1(c)` (cross-reference
replaced by the explicit `|ζ'(1+it)| = O((log|t|)^2)`), `E-SS5.EX-7(a)` (`a_n ≠ −1` added),
`E-SS10.EX-1` ("first two derivatives" → "first three"), `E-SS10.PR-1` (a,k "positive" →
"nonnegative"), `E-SS10.PR-2` (`|Im τ| ≥ 0` → `Im τ > 0`, and "distinct" added in (b)).
In every one of these the card's reading is the mathematically correct one.

**Undocumented differences (7 findings).**
1. `E-SS1.EX-15` — printed "[Hint: Sum by parts.]" and the printed sentence "For the precise
   definition of these terms, and more information on summability methods, we refer the
   reader to Book I, Chapter 2." are both gone; nothing on the card records it.
2. `E-SS1.EX-16` — printed part (d) hint "[Hint: Use Stirling's formula, which says that
   n! ∼ cn^{n+1/2}e^{−n} for some c > 0..]" is gone and the word Stirling appears nowhere in
   the card.
3. `E-SS1.EX-18` — printed "[Hint: Write z = z0 + (z − z0) and use the binomial expansion for
   z^n.]" gone.
4. `E-SS1.EX-21` — printed "[Hint: Use the dyadic expansion of an integer and the fact that
   2^{k+1} − 1 = 1 + 2 + 2² + ⋯ + 2^k.]" gone ("dyadic" survives only in the card's title).
5. `E-SS1.EX-11` — printed "Use Exercise 10" replaced by "Use the Wirtinger-operator identity
   for the Laplacian"; not recorded.
6. `E-SS5.EX-7(c)` — printed "Π(1+a_n) converges" strengthened to "converges to a non-zero
   limit"; not recorded.
7. `E-SS6.EX-14(b)` — printed "log Γ(n) ∼ n log n + O(n)" written as "= n log n + O(n)";
   not recorded. (Plus the trivial `E-SS10.EX-4` ellipsis sign `−⋯` → `+⋯`, which is right
   and unrecorded.)
No wrong sign, exponent or range was found in chapters 1, 3, 5, 6, 10 beyond these.

**Hints, checked across the whole book by text presence.** The twenty printed blocks (165
exercises + 50 problems) contain 116 bracketed `[Hint: …]` occurrences. For every one of
those items I checked whether the card mentions a hint at all (a `hint` block, "*Hint.*", or
the word): only **five** cards have no hint anywhere — `E-SS1.EX-15`, `E-SS1.EX-16`,
`E-SS1.EX-18`, `E-SS1.EX-21` (all four above) and **`E-SS8.EX-13`** (PDF p. 270), where the
printed part (a) hint "[Hint: Consider the automorphism ψα(z) = (z−α)/(1−ᾱz) and apply the
Schwarz lemma to ψ_{f(w)}^{−1} ∘ f ∘ ψ_w.]" is absent from the card, as is the printed
sentence "See Problem 3 for an important application of this lemma." This is a presence
check only; I did not compare hint *text* for the chapters listed as unverified below.

**Sub-part structure is complete for all 206 cards**: for every printed item the lettered
parts `(a),(b),(c),…` in the print are exactly the lettered parts in the card's statement
block; no card drops a part and none invents one.

**Asterisks are not recorded anywhere.** The print stars whole items and exactly one
sub-part; no card in the collection records starredness (no field, no marker). Starred whole
items: ch2 PR 2, 5; ch3 PR 1, 4, 5; ch4 PR 3, 4; ch5 PR 2, 3, 4; ch6 PR 2, 3, 4; ch7 PR 2,
3, 4; ch8 PR 3, 4, 6, 7, 8, 9; ch9 PR 3, 4; ch10 PR 1, 5, 6; App. A PR 5. Starred sub-part:
**ch2 PR-1(b)** ("(b) ∗ Fix 0 < α < ∞ …"). No exercise anywhere in the book is starred.

## What I did NOT check (explicit)

1. **Statement fidelity of chapters 2, 4, 7, 8** (85 cards: 15+5, 12+4, 12+4, 24+9). Their
   statements were **not** read against the print. What I have for them is only (i) the item
   counts in the table above, which are firm, (ii) the book-wide hint-presence check above,
   and (iii) a sub-part-structure check that passed for every card. Chapter 9's 11 cards are
   likewise not read, except `E-SS9.PR-3` once in passing (matches). An automated
   printed-word-coverage triage raised no case of a card matching a *different* printed item
   than its own number, but I did not adjudicate its low-coverage cases: treat
   statement-fidelity for those chapters as unverified by me.
2. **Proofs and solutions: not audited at all** (explicitly out of scope).
3. **Front matter, ids, page citations, duplicate coverage, topics/labels**: not audited
   (another worker's direction).
4. **OCR-ambiguous readings I could not resolve from the text layer.** These need a look at
   the page images, not at `pdftotext`: Appendix A PR-1(b), PR-3 and PR-5 displays (OCR too
   broken to quote as the printed formula; flagged in `gaps-appendixA.md`); ch6 PR-1(a)'s
   `N^{s−1}` vs `N^{1−s}` (resolved by the card's own remark, but the print reading is worth
   one glance); ch6 EX-4 whether the print carries a parenthetical excluding non-positive
   integers; ch10 EX-4's ellipsis sign.
5. **Nothing outside the exercise/problem blocks was audited** — not the worked examples, the
   chapter text, the "Notes and References", nor whether card titles/topics match the book's
   own naming.
6. **Chapter 11 does not exist in this book.** There are 10 chapters plus Appendices A and B;
   my registered direction promised a look at a "chapter 11", and Appendix A/B is what there
   is. Appendix B (PDF 363–383) prints no numbered exercises or problems — checked.

## Note on the collection metadata

`corpus/collections/SRC-TEXT-SS03/index.md` line 12 declares `completion: complete` while 9
printed items have no card and Appendix A has no section entry at all. Whatever the human
decides about the appendix, that flag and the `ch3-problems` / `ch9-problems` sections are
inaccurate as they stand.
