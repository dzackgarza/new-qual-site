---
schema: qual/card@1
id: E-2JGJL
kind: exercise
title: Line integrals
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.exercise}
Compute $\int_\Gamma \Re(z) \dz$ for $\Gamma$ the unit square.
:::

::: {.solution}
Write $\Gamma = \sum_{1\leq k \leq 4}\gamma_k$, starting at zero and traversing clockwise:

![](../../assets/30_Complex_Analysis/010_Basics/figures/2021-12-19_03-22-20.png)

Compute:

- $\gamma_1$: parameterize to get $\int_0^1t1\dt = 1/2$.

- $\gamma_2$: $\int_0^1 i \dt = i$

- $\gamma_2$: $-\int_0^1 (1-t)\dt = -1/2$

- $\gamma_2$: $- \int_0^1 0 \dt = 0$

So $\int_\Gamma \Re(z) \dz = i$.
:::
