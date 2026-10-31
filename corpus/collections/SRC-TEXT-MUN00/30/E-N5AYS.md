---
schema: qual/card@1
id: E-N5AYS
kind: problem
title: Disjoint open collections in separable spaces are countable
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
---

::: {.exercise}

Show that if $X$ has a countable dense subset, every collection of disjoint open sets in $X$ is countable.
:::

::: {.solution}
Let $D\subset X$ be countable and dense, and let $\mathcal U$ be a collection of pairwise disjoint open sets. Remove $\varnothing$ if it occurs; this removes at most one member. For each remaining $U\in\mathcal U$, density gives a point $d_U\in D\cap U$. Since the nonempty members of $\mathcal U$ are disjoint, the points $d_U$ are distinct. Thus
$$
U\longmapsto d_U
$$
injects the nonempty members of $\mathcal U$ into $D$. Hence $\mathcal U$ is countable.
:::
