---
schema: qual/card@1
id: E-HK-SHA8
kind: problem
title: $AB$ not invertible when $n < m$
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze Exercise 1.6.10.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Prove the following generalization of Exercise 6. If A is an $m \times n$ matrix, B is an $n \times m$ matrix and n < m, then AB is not invertible.
:::


::: solution
The columns of $AB$ lie in the column space of $A$. Hence
\[
\operatorname{rank}(AB)\le \operatorname{rank}(A)\le n<m.
\]
But an invertible $m\times m$ matrix has rank $m$. Therefore $AB$ cannot be invertible.
:::
