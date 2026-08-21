---
schema: qual/card@1
id: D-2KICH
kind: definition
title: Weak Topology
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
  - Cell Complexes
relations: []
review: draft
---

::: {.definition title="Weak Topology"}
For $X = \Union_\alpha X_\alpha$ a space written as a union of subspaces, the **weak topology** determined by $\ts{X_\alpha}$ declares $A\subseteq X$ closed iff $A\intersect X_\alpha$ is closed in $X_\alpha$ for every $\alpha$.
It is the finest topology making every inclusion $X_\alpha\injects X$ continuous.
A CW complex carries the weak topology determined by its skeleta, equivalently by its closed cells.
:::

::: {.concept}
See Hatcher, pp. 5 and 520.
:::
