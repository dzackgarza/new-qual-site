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

::: exercise
- What is the **closure** of a subspace $E\subseteq X$?
:::

::: {.solution}
<1>1. The closure $\overline E$ is the intersection of all closed subsets of $X$ containing $E$.
::: {.proof}
Arbitrary intersections of closed sets are closed, so this is the unique smallest closed subset containing $E$.
:::

<1>2. Equivalently,
$$\boxed{\overline E=\{x\in X:U\cap E\ne\varnothing\text{ for every open neighborhood }U\ni x\}.}$$
::: {.proof}
A point fails to lie in the intersection from <1>1 exactly when it has an open neighborhood contained in the complement of some closed set containing $E$, hence disjoint from $E$.
:::
:::
