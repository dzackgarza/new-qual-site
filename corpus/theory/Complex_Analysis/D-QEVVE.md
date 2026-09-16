---
schema: qual/card@1
id: D-QEVVE
kind: definition
title: Winding number
classification:
  areas:
  - complex-analysis
  topics:
  - Winding Number
  - Contour Integration
relations:
- kind: variant-of
  target: D-PJ7JM
review: draft
---

::: {.definition}
Let $\gamma$ be a closed piecewise $C^1$ curve in $\CC$ and let $z_0\in\CC$ be a point not on $\gamma$.
The \dfn{winding number}, or \dfn{index}, of $\gamma$ about $z_0$ is
$$
\Ind_{z=z_0}(\gamma)\coloneqq\frac{1}{2\pi i}\int_\gamma\frac{1}{\xi-z_0}\dxi.
$$
:::
