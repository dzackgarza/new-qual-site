---
schema: qual/card@1
id: P-TRIV-LA36
kind: problem
title: Lie--Trotter product formula
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 36, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed the difficulty-glyph residue from Linear Algebra Problem 36 on page 5 of the source PDF.
---

::: {.problem}
"Trotter product formula".
Consider $n \times n$ complex matrices $A$, $B$.
Prove that $e^{A+B} = \lim_{N \to \infty} \left(e^{A/N} e^{B/N}\right)^N$, $N \in \mathbb{R}$.
:::
