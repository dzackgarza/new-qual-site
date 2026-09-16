---
schema: qual/card@1
id: P-GRECH2-01
kind: problem
title: Limit of $(\cos n\pi)(\sin^2 n)/\sqrt[e]{n}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 1 of the Chapter 2 review questions in assets/attachments/extracted/chapter-2.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction. Both extractions garbled the root index; the book's Chapter 8 solution bounds the term by 1/n^(1/e), fixing the e-th root.
---

::: {.problem}
Consider the sequence $(x_n)$ whose terms are given by the formula

\[
x_n = \frac{(\cos n\pi)(\sin^2 n)}{\sqrt[e]{n}}
\]

for each integer $n \ge 1$. Given that this sequence converges, what is its limit?

(A) $0$
(B) $1$
(C) $\log 2$
(D) $\sqrt[4]{2}$
(E) $\sqrt[4]{e}$
:::
