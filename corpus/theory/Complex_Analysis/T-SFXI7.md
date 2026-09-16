---
schema: qual/card@1
id: T-SFXI7
kind: theorem
title: $ML$ estimate for contour integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.theorem}
Let $\gamma$ be a piecewise smooth curve in $\CC$ of length $L\coloneqq\length(\gamma)$, and let $f$ be continuous on the image of $\gamma$.
Then, with $M\coloneqq\sup_{\xi\in\gamma}\abs{f(\xi)}$,
$$
\abs{\int_\gamma f(z)\dz}\leq ML.
$$
:::
