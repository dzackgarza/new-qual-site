# SRC-TEXT-SS03 (Stein–Shakarchi, *Complex Analysis*) — completeness audit, summary

Auditor: swarm member m2 (direction d3). Source of truth: `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf`
(398 pp., OCR text layer). Pagination below is **PDF p.X (printed p.Y)**; Y = X − 19 on every
exercise/problem page (checked against printed folios and running heads). Per-chapter detail:
`gaps-ch1.md` … `gaps-ch10.md`, `gaps-appendixA.md`. Nothing under `corpus/` was modified.

## Headline

**Nine printed items have no card**: Chapter 3 problems 3, 4, 5; Chapter 9 problem 4;
Appendix A problems 1–5. Every other printed exercise and problem in Chapters 1–10 has a card with the
matching number, including all the items the brief suspected: there is **no Chapter 5 exercise 19** (the
chapter prints 1–17), **no Chapter 8 problem beyond 9** (it prints 1–9), and **Chapter 10 prints six
problems** (1–6, printed pp.314–317).

| chapter | section | printed pages | printed items | cards | missing |
|---|---|---|---|---|---|
| 1 | 4 Exercises | 24–31 | 1–26 | 26 | — |
| 1 | (no Problems section is printed) | — | — | — | — |
| 2 | 6 Exercises | 64–67 | 1–15 | 15 | — |
| 2 | 7 Problems | 67–70 | 1–5 | 5 | — |
| 3 | 8 Exercises | 103–108 | 1–22 | 22 | — |
| 3 | 9 Problems | 108–110 | 1–5 | 2 | **PR-3, PR-4, PR-5** |
| 4 | 4 Exercises | 127–131 | 1–12 | 12 | — |
| 4 | 5 Problems | 131–134 | 1–4 | 4 | — |
| 5 | 6 Exercises | 153–156 | 1–17 | 17 | — |
| 5 | 7 Problems | 156–158 | 1–4 | 4 | — |
| 6 | 3 Exercises | 174–179 | 1–17 | 17 | — |
| 6 | 4 Problems | 179–180 | 1–4 | 4 | — |
| 7 | 3 Exercises | 199–203 | 1–12 | 12 | — |
| 7 | 4 Problems | 203–204 | 1–4 | 4 | — |
| 8 | 5 Exercises | 248–254 | 1–24 | 24 | — |
| 8 | 6 Problems | 254–260 | 1–9 | 9 | — |
| 9 | 3 Exercises | 278–281 | 1–8 | 8 | — |
| 9 | 4 Problems | 281–282 | 1–4 | 3 | **PR-4** |
| 10 | 4 Exercises | 309–314 | 1–12 | 12 | — |
| 10 | 5 Problems | 314–317 | 1–6 | 6 | — |
| A | 5 Problems | 341–343 | 1–5 | 0 (no directory) | **PR-1 … PR-5** |
| B | no exercise/problem section printed | 344–364 | 0 | — | — |

**Total missing: 9 items** (3 in ch3, 1 in ch9, 5 in Appendix A). Nothing is missing in Chapters
1, 2, 4, 5, 6, 7, 8, 10 or Appendix B.

## Corrections to the inventory given in the brief

The brief listed eight directories. Re-derived from disk, the collection actually contains **nineteen**
directories, one for every printed section except Appendix A:

* listed and confirmed: `ch2-problems` (5), `ch4-problems` (4), `ch5-exercises` (17), `ch7-exercises` (12),
  `ch8-problems` (9), `ch10-problems` (6), `ch10-exercises` (12) — all match the printed counts;
  `ch9-problems` does **not** (3 cards against 4 printed);
* present but not listed: `ch1-exercises` (26), `ch2-exercises` (15), `ch3-exercises` (22),
  `ch3-problems` (2 of 5), `ch4-exercises` (12), `ch5-problems` (4), `ch6-exercises` (17),
  `ch6-problems` (4), `ch7-problems` (4), `ch8-exercises` (24), `ch9-exercises` (8);
* absent altogether: any appendix directory — Appendix A prints Problems 1–5.

`corpus/collections/SRC-TEXT-SS03/index.md` claims `completion: complete`. That is false as of this audit.
It also has no section for Appendix A.

## How the counts were derived (and why they can be trusted)

1. The 398-page PDF was extracted once in reading order and once with `pdftotext -layout`. Section headings
   (`k Exercises` / `k Problems`) were located in the body text — 20 of them, Appendix A's included — and the
   item numbers extracted by a monotone scan 1..N that rejects the running heads (`8. Exercises`,
   `9. Problems`, …).
2. Both extractions give identical counts for all 20 sections. The number 1..N appears without a gap in
   every section, and each section's last item ends exactly at the next heading or chapter title page.
3. Independent check by the book's own cross-references (26 distinct citations of the form
   "Exercise n in Chapter m" / "Problem n of Chapter m"). Every cited number lies within the counts above and
   none exceeds them. In particular printed p.133 (PDF p.152) says "**See Problem 5 in Chapter 3.**", which
   confirms that Chapter 3 prints a problem 5 — the largest single gap.
4. Two traps that produced wrong counts on the first pass, recorded so that no one repeats them:
   * running heads such as "3. Exercises" (Chapter 6) or "4. Problems" read as item numbers, which **splits**
     an item in two (printed ch6 exercise 2 was split into "2" and "3");
   * PDF page ranges that stop at a page boundary instead of the next heading, which **truncates** a section
     (Chapter 5 looked like 15 exercises when it prints 17; the last two are on printed p.156).

## Statement fidelity (job 2), scope: partial

Screening covered all 206 cards: printed statement of the same number compared to the card's
`:::.exercise` block by rare-token alignment, part-letter inventory and hint presence; number/statement
misalignment of the form "card n holds printed n±1" would have been caught. About twenty cards were then
read against the printed text. Findings:

1. **Six cards drop a bracketed hint printed in the statement** and carry no `:::.hint` block:
   `E-SS1.EX-15` ("[Hint: Sum by parts.]", printed p.28),
   `E-SS1.EX-16` ("[Hint: Use Stirling's formula …]", p.28),
   `E-SS1.EX-18` ("[Hint: Write z = z0 + (z − z0) and use the binomial expansion for z^n.]", p.29),
   `E-SS1.EX-21` ("[Hint: Use the dyadic expansion of an integer …]", pp.29–30),
   `E-SS4.EX-12` ("[Hint: … −ξ^p + ξu ≤ u^q …]", p.131),
   `E-SS8.EX-13` ("[Hint: Consider the automorphism ψα(z) = (z − α)/(1 − αz) …]", p.251).
   In the other hint-bearing cards examined the hint is preserved, usually as a `:::.hint` block
   (`E-SS4.PR-3`, `E-SS5.PR-1`, `E-SS7.EX-8`, `E-SS7.EX-10`, `E-SS8.PR-4`, `E-SS8.PR-7`, `E-SS8.PR-9`,
   `E-SS9.PR-3`, `E-SS10.PR-5`, `E-SS10.PR-6`).
2. **No card records the book's ★** ("∗") difficulty marker. 28 printed items carry it — ch2 PR-2, PR-5;
   ch3 PR-1, PR-4, PR-5; ch4 PR-3, PR-4; ch5 PR-2, PR-3, PR-4; ch6 PR-2, PR-3, PR-4; ch7 PR-2, PR-3, PR-4;
   ch8 PR-3, PR-4, PR-6, PR-7, PR-8, PR-9; ch9 PR-3, PR-4; ch10 PR-1, PR-5, PR-6; App. A PR-5 — and 0 of 206
   cards contain "∗". This looks like a schema convention rather than 28 separate slips, but it is a
   statement-level difference from the printed text.
3. `E-SS1.EX-13`: printed hypothesis "holomorphic in an **open set** Ω"; the card says "in a region Ω
   (**an open connected set**)" — the card strengthens the hypothesis.
4. `E-SS10.PR-2`: printed domain is "F1 = {τ ∈ C : |τ| ≥ 1, |Re(τ)| ≤ 1/2 and |Im(τ)| ≥ 0}" (OCR);
   the card writes "Im(τ) > 0". Cosmetic, but not what is printed.
5. `E-SS10.PR-3`: the card's extra setup (parity definition of G, fundamental domain F) is printed on
   p.315; the OCR prints it out of order. Card is faithful, not expanded.
6. No number misalignment found anywhere: every card's statement matched its own printed number best.

## What I did NOT check

* **Proofs and solutions.** Not read, not audited — out of scope by instruction. Card bodies beyond the
  `:::.exercise` block were only inspected for hint blocks.
* **Statement fidelity of the other ~186 cards.** They were screened automatically (token alignment, part
  letters, hint presence) and showed no gross deviation, but an automated screen cannot certify prose-level
  fidelity: for weight-symbol-only statements (e.g. `E-SS3.EX-3`, `EX-4`, `EX-7`, `E-SS5.EX-9`, `E-SS7.EX-7`)
  the token signal is too weak to say anything, and those cards were not read by hand.
* **Appendix B (printed pp.344–364).** Verified only that it prints no Exercises/Problems section: the table
  of contents (printed p.xiv) lists §§1, 2, 2.1 and no exercise section, and a scan of its pages finds the
  word "Exercise" only in the cross-reference on printed p.352 ("… pathwise connected (Exercise 5,
  Chapter 1)"). Its pages were not read.
* **Front and back matter** (Foreword, Introduction, Notes and References p.365, Bibliography p.369,
  Symbol Glossary p.373, Index p.375): searched for exercise/problem headings, none found; not read.
* **Books I and II of the series.** Citations qualified as "in Book I" were excluded from the cross-reference
  check and not followed up.
* **Page images.** All quotations come from the PDF text layer; I did not view the scanned page images, so a
  number that the OCR mangled identically in both extraction modes would be invisible to this audit. The
  numbering-continuity and cross-reference checks are the mitigation, and the OCR text is quoted verbatim
  where it is damaged so the reader can judge (see the Appendix A quotes).
* **The section assignment of cards**: chapter directories and ids agree by construction; I did not check
  whether any card's *title* or *topics* metadata is wrong.
