---
schema: qual/card@1
id: T-AL6OT
kind: theorem
title: Riemann's removable singularity theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations: []
review: draft
---

::: {.theorem title="Riemann's removable singularity theorem"}
If $z_0$ is an isolated singularity of $f(z)$ and $\abs{f(z)}$ is bounded near $z_0$, then $z_0$ is removable.

More generally, TFAE:

- $f$ extends holomorphically over $z_0$, i.e. there is a function $F$ such that $\ro{F}{\Omega\sm\ts{z_0}} = f$

- $f$ extends continuously over $z_0$.

- There exists *some* neighborhood of $z_0$ on which $f$ is bounded.

- $\lim_{z\to z_0}(z-z_0)f(z) = 0$.
:::
