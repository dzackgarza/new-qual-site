---
schema: qual/card@1
id: P-43KOX
kind: problem
title: The product of two connected spaces is connected
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Product Topology
relations: []
review: draft
---

::: {.problem title="?"}
Prove that the product of two connected topological spaces is connected.
:::

::: {.solution}
\envlist

- Use the fact that a union of spaces containing a common point is still connected.

- Fix a point $(a, b) \in X \cross Y$.

- Since the horizontal slice $X_b\definedas X \cross \theset{b}$ is homeomorphic to $X$ which is connected, as are all of the vertical slices $Y_x \definedas \theset{x} \cross Y \cong Y$ (for any $x$), the "T-shaped" space $T_x \definedas X_b \union Y_x$ is connected for each $x$.

- Note that $(a, b) \in T_x$ for every $x$, so $\union_{x\in X} T_x = X \cross Y$ is connected.

![Image](../../assets/figures/2020-01-21-20%3A53.png)
:::
