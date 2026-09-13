---
schema: qual/card@1
id: P-UGAP09F-03
kind: problem
title: Prove a weighted finite geometric-sum formula by induction
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Fix $x\in\mathbb R$. Using mathematical induction, show that if $x\ne1$, then for every $n\ge1$,
\[
x+2x^2+3x^3+\cdots+nx^n
=
\frac{nx^{n+2}-(n+1)x^{n+1}+x}{(x-1)^2}.
\]
:::
