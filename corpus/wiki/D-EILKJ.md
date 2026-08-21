---
schema: qual/card@1
id: D-EILKJ
kind: definition
title: Compact space
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.definition title="Compact"}
A topological space $(X, \tau)$ is **compact** iff every open cover has a *finite* subcover.
That is, if $\theset{U_{j}}_{j\in J} \subseteq \tau$ is a collection of open sets such that $X = \Union_{j\in J} U_{j}$, then there exists a *finite* subset $J' \subset J$ such that $X \subseteq \Union_{j\in J'} U_{j}$.
:::
