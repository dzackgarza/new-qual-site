---
schema: qual/card@1
id: E-AMD-4SSSVQJY
kind: solution
title: Every element of a finite ring is a unit or a zero-divisor
classification:
  areas:
  - algebra
  topics:
  - Integral Domains
  - Rings
  - Fields
relations: []
review: draft
---

::: {.solution}

- Let $a\in R$ and define $\phi(x) = ax$.

- If $\phi$ is injective, then it is surjective, so $1 = ax$ for some $x \implies x\inv = a$.

- Otherwise, $ax_1 = ax_2$ with $x_1 \neq x_2 \implies a(x_1 - x_2) = 0$ and $x_1 - x_2 \neq 0$

- So $a$ is a zero divisor.
:::
