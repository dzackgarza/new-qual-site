---
schema: qual/card@1
id: E-BOLN3
kind: problem
title: The diagonal map $\Delta(x)=(x,x)$ is continuous
classification:
  areas:
  - topology
  topics:
  - Continuity
  - Product Topology
relations: []
review: draft
---

::: exercise
Show that the diagonal map $\Delta(x) = (x, x)$ is continuous.
:::

::: {.solution}
<1>1. The diagonal is the product map $(\operatorname{id}_X,\operatorname{id}_X):X\to X\times X$.
::: {.proof}
Both component maps are continuous. By the universal property of the product topology, a map into $X\times X$ is continuous exactly when both coordinate maps are continuous.
:::
:::
