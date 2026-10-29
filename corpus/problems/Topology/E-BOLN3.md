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

::: {.exercise}
Show that the diagonal map $\Delta(x) = (x, x)$ is continuous.
:::

::: {.solution}

::: pf

::: pf-step

For every topological space $X$, the map $\Delta: X\to X\times X$ is continuous.

::: pf-proof

The coordinate maps of $\Delta$ are $\pi_1\circ\Delta=\id_X$ and $\pi_2\circ\Delta=\id_X$, both continuous. By the universal property of the product topology, a map into $X\times X$ is continuous exactly when both coordinate maps are continuous.

:::

:::

:::

:::
