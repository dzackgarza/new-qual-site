---
schema: qual/card@1
id: P-IQPLX
kind: problem
title: An $m$-cycle is odd iff $m$ is even
classification:
  areas:
  - algebra
  topics:
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Show that an $m$-cycle is an odd permutation iff $m$ is even.
:::

::: {.solution}

::: pf

::: {.pf-step #product}

An $m$-cycle is a product of $m-1$ transpositions:
$$
(a_1\ a_2\ \cdots\ a_m)=(a_1\ a_m)(a_1\ a_{m-1})\cdots(a_1\ a_2).
$$

::: pf-proof

Composing the right side from the right, $a_i\mapsto a_{i+1}$ for $i<m$, $a_m\mapsto a_1$, and every other element is fixed.

:::

:::

::: pf-step

An $m$-cycle is odd if and only if $m$ is even.

::: pf-proof

By step [](#product){.pf-ref}, the sign of an $m$-cycle is $(-1)^{m-1}$. This equals $-1$ exactly when $m-1$ is odd, that is, when $m$ is even.

:::

:::

:::

:::
