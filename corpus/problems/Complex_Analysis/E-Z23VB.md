---
schema: qual/card@1
id: E-Z23VB
kind: problem
title: A Möbius transformation sending $1\mapsto 3$, $i\mapsto 0$, $2\mapsto -1$
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
---

::: {.exercise}
Find a Möbius transformation sending

- $1\to 3$

- $i\to 0$

- $2\to -1$

:::

::: {.solution}

::: pf

::: {.pf-step #cross-ratio}
The Möbius map $w = T(z)$ with $T(1)=3$, $T(i)=0$, $T(2)=-1$ is determined by
$$
\frac{z-i}{z-2}\cdot\frac{1-2}{1-i} = \frac{w-0}{w+1}\cdot\frac{3+1}{3-0}.
$$

::: pf-proof
Each side is the Möbius map sending the three given points, in order, to $1, 0, \infty$; a Möbius map is determined by the images of three distinct points, so $T$ composed with the right-hand map equals the left-hand map.
:::

:::

::: pf-step
$$
\boxed{T(z) = \frac{-3z+3i}{(7-4i)z+(-8+5i)}}.
$$

::: pf-proof
Solving step [](#cross-ratio){.pf-ref} for $w$ gives this map, which is checked directly: $T(i) = 0$, $T(1) = \frac{-3+3i}{-1+i} = 3$, and $T(2) = \frac{-6+3i}{6-3i} = -1$.
Its determinant $-3(-8+5i) - 3i(7-4i) = 12 - 36i$ is nonzero, so $T$ is a Möbius transformation.
:::

:::

:::

:::
