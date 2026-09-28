---
schema: qual/card@1
id: P-WPFNX
kind: problem
title: No simple group of order $40$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
relations: []
review: draft
---

::: {.problem}
Prove that there is no simple group of order $40$.
:::

::: {.solution}
Let $G$ have order
\[
|G|=40=2^3\cdot5.
\]
Let $n_5$ be the number of Sylow $5$-subgroups. Sylow's theorem gives
\[
n_5\mid8,
\qquad
n_5\equiv1\pmod5.
\]
The divisors of $8$ are $1,2,4,8$, and only $1$ is congruent to $1$ modulo $5$. Hence
\[
n_5=1.
\]
Therefore the Sylow $5$-subgroup is unique and hence normal. It is nontrivial and proper, so $G$ is not simple.
:::
