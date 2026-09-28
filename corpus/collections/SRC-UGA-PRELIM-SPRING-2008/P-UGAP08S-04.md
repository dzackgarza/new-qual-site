---
schema: qual/card@1
id: P-UGAP08S-04
kind: problem
title: A basis adapted to the kernel maps to a basis of the range
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops T, V, k, and several repeated T/V symbols; the basis/kernel/range statement uniquely determines those missing symbols.
---

::: {.problem}
Let $T$ be a linear transformation on a finite-dimensional vector space $V$. Suppose
\[
x_1,x_2,\ldots,x_n
\]
is a basis for $V$, with the first $k$ of these vectors forming a basis for $\ker T$.
Prove that
\[
Tx_{k+1},Tx_{k+2},\ldots,Tx_n
\]
is a basis for $\operatorname{range}T$.
:::
