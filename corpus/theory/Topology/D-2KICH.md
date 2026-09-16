---
schema: qual/card@1
id: D-2KICH
kind: definition
title: Weak topology determined by a family of subspaces
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and let $(X_\alpha)_{\alpha}$ be a family of subspaces with $X = \Union_\alpha X_\alpha$.
The \dfn{weak topology} determined by $(X_\alpha)_\alpha$ is the topology on $X$ in which a subset $A\subseteq X$ is closed if and only if $A\intersect X_\alpha$ is closed in $X_\alpha$ for every $\alpha$.
:::

::: {.remark}
The weak topology is the finest topology on the set $X$ for which every inclusion $X_\alpha\injects X$ is continuous.
A [[D-ZOU5G|CW complex]] $X$ carries the weak topology determined by its skeleta $X^n$, equivalently by its closed cells.
:::

::: {.concept}
[@Hat02, pp. 5 and 520].
:::
