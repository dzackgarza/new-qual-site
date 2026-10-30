---
schema: qual/card@1
id: P-OBO4F
kind: problem
title: $g^{\cardinality{ G}}=e$ for every $g\in G$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Cyclic Groups
relations: []
review: draft
---

::: {.problem}
Let $G$ be a finite group of order $n$. Prove that
$$
g^n=e
$$
for every $g\in G$.
:::

::: {.solution}
Let $g\in G$, and let $\abs{g}$ denote its order.

::: pf

::: {.pf-step #divides}

$\abs{g}\mid n$.

::: pf-proof

The cyclic subgroup $\langle g\rangle$ has order $\abs{g}$, and by Lagrange's theorem its order divides $\abs{G}=n$.

:::

:::

::: pf-step

$g^n=e$.

::: pf-proof

By step [](#divides){.pf-ref}, write $n=k\abs{g}$. Then
$$
g^n=\bigl(g^{\abs{g}}\bigr)^k=e^k=e.
$$

:::

:::

:::

:::
