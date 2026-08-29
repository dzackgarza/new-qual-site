---
schema: qual/card@1
id: P-Q67AG
kind: problem
title: Units or Zero Divisors
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

::: {.problem}
Every $a\in R$ for a finite ring is either a unit or a zero divisor.
:::

::: {.solution}

- Let $a\in R$ and define $\phi(x) = ax$.

- If $\phi$ is injective, then it is surjective, so $1 = ax$ for some $x \implies x\inv = a$.

- Otherwise, $ax_1 = ax_2$ with $x_1 \neq x_2 \implies a(x_1 - x_2) = 0$ and $x_1 - x_2 \neq 0$

- So $a$ is a zero divisor.
:::
