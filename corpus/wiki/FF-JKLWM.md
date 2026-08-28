---
schema: qual/card@1
id: FF-JKLWM
kind: fact
title: 'Inverting series: for $A(z) = \sum c_k z^k$ and $1/A(z) = \sum b_k z^k$, the formula for the $b_k$ in terms of $c_k$.'
prompts:
- For $A(z) = \sum c_k z^k$, how are the coefficients of $1/A(z)$ computed from the $c_k$?
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Series of Functions
relations: []
review: draft
---

::: {.fact}
- $b_0 = c_0\inv$

- $b_1 = -c_0\inv(c_1 b_0 )$

- $b_2 = -c_0\inv(c_2b_0 + c_1b_1)$

- $\cdots$
:::
