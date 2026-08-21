---
schema: qual/card@1
id: E-WYJ7K
kind: exercise
title: Lune, one intersection
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
solved: true
---

::: {.problem title="Lune, one intersection"}
Find a conformal map from the region bounded by $\abs{z - {i\over 2}} = {1\over 2}$ and $\abs{z-i} = 1$ to $\DD$.
:::

::: {.solution}
This is a lune with a single intersection vertex at $z=i$.
Orient the circles positively.

- Take $f(z) = {z+i\over z-i}$ to send

  - $i\to \infty$

  - $-i\to 0$

  - $1\to {1+i\over 1-i} = i$

  - $0\to -1$

  So $\abs{z} = 1$ is sent to the imaginary axis $\ts{it}$ for $t\in (-\infty, \infty)$ oriented positively and $\abs{z- {i\over 2}} = {1\over 2}$ is sent to $\ts{-1 + it}$ also oriented positively.
  The region then maps to $-1 < \Re(z) < 0$.

- Rotate by $z\mapsto -i\pi z$ to get $0 < \Im(z) < \pi$.

- Take $z\mapsto e^z$ to get $\HH$.

- Take $z\mapsto {z-i\over z+i}$ to get $\DD$.
:::
