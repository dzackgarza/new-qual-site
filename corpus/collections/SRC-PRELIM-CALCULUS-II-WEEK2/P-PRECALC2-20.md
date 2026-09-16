---
schema: qual/card@1
id: P-PRECALC2-20
kind: problem
title: Convergence of a series with products of square roots of 3 in the denominators
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the garbled series of Problem 20 on page 7 of Week2_solns.pdf, restoring the cube and n-th roots, and added a remark on the source's plus signs in the general denominator.
---

::: {.problem}
Does the series
\[
\frac{1}{3} + \frac{1}{3\sqrt{3}} + \frac{1}{3\sqrt{3}\sqrt[3]{3}} + \cdots + \frac{1}{3\sqrt{3}\sqrt[3]{3} + \cdots + \sqrt[n]{3}} + \cdots
\]
converge or diverge?
:::

::: {.remark}
The general denominator in the source is printed as $3\sqrt{3}\sqrt[3]{3} + \cdots + \sqrt[n]{3}$, with plus signs; the pattern of the first three terms and the source's solution, which writes the series as $\sum_{n=1}^{\infty} 3^{-H_n}$ with $H_n = \sum_{k=1}^{n} \frac{1}{k}$, show that the intended $n$-th denominator is the product $3\sqrt{3}\sqrt[3]{3}\cdots\sqrt[n]{3}$.
:::
