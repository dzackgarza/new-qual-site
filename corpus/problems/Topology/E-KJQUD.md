---
schema: qual/card@1
id: E-KJQUD
kind: problem
title: Closure of a subspace
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
---

::: {.exercise}
- What is the **closure** of a subspace $E\subseteq X$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The closure $\overline E$ is the intersection of all closed subsets of $X$ containing $E$.

::: pf-proof

Arbitrary intersections of closed sets are closed, so this is the unique smallest closed subset containing $E$.

:::

:::

::: pf-step

Equivalently,
$$\boxed{\overline E=\{x\in X:U\cap E\ne\varnothing\text{ for every open neighborhood }U\ni x\}.}$$

::: pf-proof

A point fails to lie in the intersection from step [](#s1){.pf-ref} exactly when it has an open neighborhood contained in the complement of some closed set containing $E$, hence disjoint from $E$.

:::

:::

:::

:::
