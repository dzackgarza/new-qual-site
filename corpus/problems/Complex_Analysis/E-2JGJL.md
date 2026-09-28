---
schema: qual/card@1
id: E-2JGJL
kind: problem
title: $\int_\Gamma\Re(z)\,dz$ around the unit square
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
Write $\Gamma = \sum_{1\leq k \leq 4}\gamma_k$, starting at zero and traversing counterclockwise through $0$, $1$, $1+i$, $i$:

![](../../assets/Complex_Analysis/010_Basics/figures/2021-12-19_03-22-20.png)

For $t\in[0,1]$:

- $\gamma_1(t)=t$: $\int_0^1 t\dt = 1/2$.

- $\gamma_2(t)=1+it$: $\int_0^1 1\cdot i \dt = i$.

- $\gamma_3(t)=(1-t)+i$: $-\int_0^1 (1-t)\dt = -1/2$.

- $\gamma_4(t)=i(1-t)$: $-i\int_0^1 0 \dt = 0$.

So $\int_\Gamma \Re(z) \dz = i$.
:::
