# SRC-TEXT-SS03 (Stein–Shakarchi, *Complex Analysis*) — completeness and statement-fidelity summary

Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (398 pp., OCR text layer
by Tesseract 4.1.1 as embedded by ocrmypdf 11.0.1). All book page numbers below are **printed** page
numbers; PDF page = printed page + 19. Calibration: PDF p. 44 carries the running head
"4. Exercises 25", PDF p. 268 carries "5. Exercises 249".

## Method (so the numbers can be re-derived)

1. Whole book extracted with `pdftotext -layout`; the book prints exactly **20** headings of the
   form `N Exercises` / `N Problems` (searched as `^\s*\d+\s+(Exercises|Problems)\s*$` over all 398
   pages). No other exercise or problem section exists — Chapter 1 has Exercises only, Appendix A
   has Problems only, Appendix B has neither, and there is no Chapter 11.
2. Each section's text was split into items by its own printed numbering, accepting an item only
   when the number equals the expected successor, so that cross-references and figure labels inside
   an item cannot be mistaken for new items. Every section's run came out contiguous 1…N.
   The end of every section was then read by eye to make sure the last detected number is the last
   printed item.
3. The card inventory was re-derived from the filesystem (`corpus/collections/SRC-TEXT-SS03/*/*.md`),
   **not** from `index.md`. There were **206** card files when the inventory was taken (16:12 UTC on
   2026-11-01), and every one of them names a number that the book prints (no orphan numbers, no
   duplicate numbers). At 16:18 UTC, while this audit was still running, **nine more** card files
   appeared — the exact nine items this audit had found missing (another worker's concurrent work;
   this audit created none of them). Both states are reported below.
4. Statement fidelity: the `::: {.exercise}` statement of each of the 206 cards was compared with the
   printed item's OCR text, plus its `.hint` block (or inline `[Hint: …]`) against the printed hint.
   Signs, exponents, constants, hypotheses, quantifiers and starred parts were read individually.

## Counts per chapter

Cards as found at 16:12 UTC, i.e. before the concurrent additions:

| chapter | exercises printed | exercise cards | problems printed | problem cards | missing |
|---|---|---|---|---|---|
| 1 (pp. 24–31) | 26 | 26 | — (none printed) | — | 0 |
| 2 (EX 64–67, PR 67–70) | 15 | 15 | 5 | 5 | 0 |
| 3 (EX 103–108, PR 108–110) | 22 | 22 | **5** | **2** | **3** |
| 4 (EX 127–131, PR 131–133) | 12 | 12 | 4 | 4 | 0 |
| 5 (EX 153–156, PR 156–157) | 17 | 17 | 4 | 4 | 0 |
| 6 (EX 174–179, PR 179–180) | 17 | 17 | 4 | 4 | 0 |
| 7 (EX 199–203, PR 203–204) | 12 | 12 | 4 | 4 | 0 |
| 8 (EX 248–254, PR 254–260) | 24 | 24 | 9 | 9 | 0 |
| 9 (EX 278–280, PR 281–282) | 8 | 8 | **4** | **3** | **1** |
| 10 (EX 309–313, PR 314–317) | 12 | 12 | 6 | 6 | 0 |
| Appendix A (PR 341–343) | — (none printed) | — | **5** | **0** | **5** |
| **total** | **165** | **165** | **50** | **41** | **9** |

The filesystem now holds 215 cards: the nine items below exist, added at 16:18 UTC. `index.md` is
still the old one — 206 ids, no Appendix A section, `completion: complete` — so it does not list the
nine new cards.

## The nine items that were missing at 16:12 UTC (book page, and where the card belongs)

1. `ch3-problems/E-SS3.PR-3.md` — Ch. 3, Problem 3, **p. 109**: Laurent expansion in an annulus
   ("Let f be holomorphic in a region containing the annulus {z : r1 ≤ |z − z0 | ≤ r2 } where
   0 < r1 < r2 …"). Full quote in `gaps-ch3.md`.
2. `ch3-problems/E-SS3.PR-4.md` — Ch. 3, Problem 4∗, **p. 110**: "Suppose Ω is a bounded region.
   Let L be a (two-way infinite) line that intersects Ω … If Ωl and Ωr are simply connected, then Ω
   is simply connected."
3. `ch3-problems/E-SS3.PR-5.md` — Ch. 3, Problem 5∗, **p. 110**: the "jump" of
   g(z) = (1/2πi)∫_{−M}^{M} h(x)/(x − z) dx across [−M, M ], parts (a) and (b).
4. `ch9-problems/E-SS9.PR-4.md` — Ch. 9, Problem 4∗, **p. 282**: "Suppose τ is purely imaginary, say
   τ = it with t > 0 … (a) Show that ℘ is real-valued on all these lines … (b) Prove that ℘ maps the
   interior of each rectangle conformally to the upper (or lower) half-plane."
5.–9. `appendix-a-problems/E-SSA.PR-1.md` … `E-SSA.PR-5.md` — Appendix A, Problems 1–5,
   **pp. 341–343**. At 16:12 UTC no appendix directory existed at all; the directory with these five
   ids was created at 16:18 UTC. See `gaps-appendixA.md` for the full printed statements and the
   id-convention question.

`corpus/collections/SRC-TEXT-SS03/index.md` says `completion: complete` and lists Ch3 Problems as
PR-1..PR-2 and Ch9 Problems as PR-1..PR-3; it must gain the four chapter entries and an Appendix A
section.

## Answers to the specific suspicions in the task

* **Chapter 5 exercise 19?** No. Chapter 5 prints exercises **1–17 only** (pp. 153–156). Exercise 15's
  last sentence spills onto p. 156, where exercises 16–17 and the "7 Problems" heading also sit; the
  table of contents' "7 Problems 156" refers to that heading, not to problem 1.
* **Chapter 8 problems beyond 9?** No. Chapter 8 prints exactly **nine** problems (pp. 254–260);
  problem 9 ends at the top of p. 260. The exercise section has 24 items, the 24th printing on p. 254
  above the "6 Problems" heading.
* **How many problems does Chapter 10 print?** **Six** (pp. 314–317), plus 12 exercises.
* **Chapter 2, 4, 7, 9, 10 gaps?** Chapters 2, 4, 7 and 10 are complete (and faithful apart from the
  items listed below). At 16:12 UTC Chapter 9 was missing Problem 4; a card for it appeared at 16:18 UTC
  and matches the printed statement.

## The nine late-arriving cards (16:18 UTC) — statement check

They were compared with the printed text quoted in `gaps-ch3.md`, `gaps-ch9.md`,
`gaps-appendixA.md`:

* **Match word for word:** `E-SS3.PR-3`, `E-SS3.PR-4`, `E-SS3.PR-5`, `E-SS9.PR-4`, `E-SSA.PR-1`,
  `E-SSA.PR-2`, `E-SSA.PR-3`.
* **`E-SSA.PR-4` — statement loss.** The printed problem gives the explicit
  `P_j (n) = (1/(r_j − 1)!) (d/dw)^{r_j −1} ((w − α_j)^{r_j} w^{−n−1} F (w))|_{w=α_j}`, the note
  `P_j (n) = A_j (α_j^{−1} n)^{r_j −1} + O(n^{r_j −2})`, and the instruction "To prove this, use the
  residue formula (Theorem 1.4, Chapter 3)"; the card replaces all of that by "each $P_j$ is a
  polynomial of degree $r_j-1$". Must be fixed.
* **`E-SSA.PR-5` — two symbols need a page-image check:** the card's `f_1(z) = (z/i)e^{…}` where the
  OCR shows a possible radical before `z/i`, and the exponents of the transformation law. The rest of
  the statement (ω_{p/q}, pp′ ≡ 1 mod q, the contribution formula, the closing paragraph) is present.
* None of the nine records the book's `∗` marker.

## Statement-fidelity: summary of the 206 comparisons

Every existing card was compared. All 206 match the *content* of the item they are numbered after —
**no card carries a neighbouring item's statement**, and there is no off-by-one anywhere.

Findings that change mathematics (7):

| card | page | difference |
|---|---|---|
| E-SS1.EX-12 | 27 | card has √(\|x\|\|y\|); printed `f (x + iy) = \|x\|\|y\|` |
| E-SS4.PR-1 | 131 | card `A e^{C\|z\|^q}`; printed `A e^{a\|z\|^q}` |
| E-SS6.EX-4 | 175 | card adds "α ∉ {0,−1,−2,…}"; printed says only "α is a fixed complex number" |
| E-SS6.PR-1(c) | 179 | card turns the printed instruction "The second conclusion of Proposition 2.7 can be similarly refined" into a specific estimate to prove |
| E-SS7.PR-2 | 204 | card `E(x) = c_1x − c_0 + …`; printed `E(x) = c1 x + c0 + …` (sign of c0) |
| E-SS10.EX-1 | 309 | card "first three derivatives"; printed "first two derivatives" |
| E-SS10.PR-1 | 314 | card "nonnegative integers"; printed "positive integers" |

Hypothesis/wording changes that are defensible but are not what the book prints (4):
E-SS1.EX-13 ("open set" → "region (open connected)"), E-SS5.EX-7 (adds a_n ≠ −1; adds "non-zero
limit" in (c)), E-SS10.PR-2 (`|Im τ| ≥ 0` → `Im τ > 0`), E-SS8.PR-8 (drops the two background
sentences and "Problem 1 in Chapter 3 shows |a2| ≤ 2").

Dropped bracketed hints (5): **E-SS1.EX-15** ("Sum by parts."), **E-SS1.EX-16** (Stirling's formula),
**E-SS1.EX-18** (binomial expansion of z^n), **E-SS1.EX-21** (dyadic expansion), **E-SS8.EX-13**
(the ψ_α/Schwarz-lemma hint, plus the sentence "See Problem 3 …"). The nine cards that do have
`.hint` blocks (E-SS4.PR-3, E-SS7.EX-8, E-SS7.EX-10, E-SS8.PR-4, E-SS8.PR-7, E-SS8.PR-9,
E-SS9.PR-3, E-SS10.PR-5, E-SS10.PR-6) reproduce the printed hints.

Dropped trailing text or cross-references (6): E-SS1.EX-11 (loses "Use Exercise 10"),
E-SS1.EX-15 (loses the Book I reference), E-SS4.PR-2 (loses "Note that the solution u depends on the
choice c."), E-SS5.EX-4 (loses the triple-product remark), E-SS8.EX-13 (loses "See Problem 3 …"),
E-SS10.EX-4 (loses "The next two exercises … Appendix A.").

Systemic: **no card records the book's `∗` (most difficult) marks.** Starred items in print include
Ch2 PR-1(b), PR-2, PR-5; Ch3 PR-1, PR-4, PR-5; Ch4 PR-3, PR-4; Ch5 PR-2, PR-3, PR-4; Ch6 PR-2,
PR-3, PR-4; Ch7 PR-2, PR-3, PR-4; Ch8 PR-3, PR-4, PR-6, PR-7, PR-8, PR-9; Ch9 PR-3, PR-4;
Ch10 PR-1, PR-5, PR-6; Appendix A PR-5. If the collection wants the stars recorded, that is a new
convention (a field such as `starred: true`), not a per-card typo.

OCR-ambiguous, flagged for a page-image check rather than an automatic edit (8):
E-SS4.EX-12 (β→π vs β↓1; γ formula), E-SS5.PR-4 (`u^{−n}e^u` vs `u^{−n}e^{u^ρ}`),
E-SS6.EX-11 (strip `|y| < π` vs `π/2`; `Γ(a+iξ)` vs `Γ(a−2πiξ)`), E-SS6.EX-17 (`I(0)=0` and
`f^{(n+1)}(0)` vs `f(0)` and `f^{(n)}(0)`), E-SS8.EX-1 and E-SS8.EX-2 (OCR drops the slash of ≠),
E-SS8.EX-20(b) (Γ²(1/4)/(2√(2π))), E-SS10.EX-12(b) ("divisors of d" vs "of n"),
E-SS10.EX-6 (hint's second sum). In each of these the card's reading is the mathematically correct
one, so the OCR is the likelier culprit — but the audit standard here is the printed page, so they
are reported rather than resolved.

Book errata that cards correctly flag (not defects): E-SS8.PR-9 notes that the printed
`I(a,b) = (1/a)K(k)` omits the factor 2/π (the OCR layer does print the factor-less identity, p. 260);
E-SS4.EX-5 replaces the book's "roots of R" by "roots of Q".

## What I did NOT check

* **Proofs and solutions.** Only statements were audited, as instructed.
* **Page images.** All book quotations come from the PDF's OCR text layer, not from the rendered
  page. Where the layer mangles a symbol I say so and mark the case ambiguous; I did not attempt to
  read the images, so the eight OCR-ambiguous cases above are open.
* **The five missing chapter/appendix items have no fidelity audit** (nothing to audit); their full
  printed text is quoted in `gaps-ch3.md`, `gaps-ch9.md`, `gaps-appendixA.md`.
* **Other collections.** `SRC-TEXT-SS03-FOURIER/index.md` (which has only Ch2/Ch5 exercise entries
  and no card files) and the two collections that merely reference SS03 (`SRC-CA-ART-T34TG3` and `SRC-CA-ART-E3SXDB`) were not audited.
* **The front/back matter** (Notes and References, Bibliography, Symbol Glossary, Index) was not
  searched for exercises; the 20 printed section headings are exhaustive for the body of the book.
* **Any chapter/file metadata**: `title:`, `classification:`, `relations:`, `audit:` blocks were not
  reviewed; nor were the `::: {.solution}` blocks.

## Caveat on scope

Each chapter file states its own coverage. In short: **all 20 printed exercise/problem sections of
the book were located and counted, all 215 printed items were enumerated with page anchors, all 206 cards that existed at 16:12 UTC were compared
statement-by-statement, and the nine cards that appeared at 16:18 UTC were compared too**. Nothing in the book's exercise/problem
apparatus was sampled rather than covered — the residual uncertainty is in the OCR text layer, not in
the coverage.
