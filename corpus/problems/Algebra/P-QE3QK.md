---
schema: qual/card@1
id: P-QE3QK
kind: problem
title: There is no simple group of order 148
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Simple Groups
  - Normal Subgroups
relations: []
review: draft
---

::: {.problem}
Prove that no group of order $148$ is simple.
:::

::: {.solution}
Let $|G|=148=2^2\cdot37$. If $n_{37}$ denotes the number of Sylow $37$-subgroups, Sylow's theorem gives
\[
n_{37}\equiv1\pmod{37},
\qquad
n_{37}\mid4.
\]
Among the divisors $1,2,4$ of $4$, only $1$ is congruent to $1$ modulo $37$. Hence
\[
n_{37}=1.
\]
Therefore the Sylow $37$-subgroup is unique and hence normal. It is nontrivial and proper, so $G$ is not simple.
:::
