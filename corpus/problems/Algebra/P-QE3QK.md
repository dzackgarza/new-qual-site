---
schema: qual/card@1
id: P-QE3QK
kind: problem
title: There is no simple group of order $148$
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
Let $\abs{G}=148=2^2\cdot37$, and let $n_{37}$ be the number of Sylow $37$-subgroups of $G$.

::: pf

::: {.pf-step #n37}
$n_{37}=1$.

::: pf-proof
By the Sylow theorems, $n_{37}\mid4$ and $n_{37}\equiv1\pmod{37}$. Of the divisors $1,2,4$ of $4$, only $1$ is congruent to $1$ modulo $37$.
:::

:::

::: pf-step
$G$ is not simple.

::: pf-proof
By step [](#n37){.pf-ref}, the Sylow $37$-subgroup $P$ equals each of its conjugates, so it is normal. Since $1<\abs{P}=37<148$, it is proper and nontrivial.
:::

:::

:::

:::
