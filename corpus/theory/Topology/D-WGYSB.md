---
schema: qual/card@1
id: D-WGYSB
kind: definition
title: Uniformly continuous map
classification:
  areas:
  - topology
  topics:
  - Uniform Continuity
  - Metric Spaces
  - Continuity
relations: []
review: draft
---

::: {.definition}
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces.
A map $f\colon X\to Y$ is \dfn{uniformly continuous} if for every $\varepsilon > 0$ there exists $\delta > 0$ such that for all $x_1, x_2\in X$,
$$
d_X(x_1, x_2) < \delta \implies d_Y(f(x_1), f(x_2)) < \varepsilon.
$$
:::
