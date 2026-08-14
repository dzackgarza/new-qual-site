---
schema: qual/card@1
id: T-ZZJDP
kind: theorem
title: "Riemann's removable singularity theorem"
classification:
  areas:
  - complex-analysis
  topics:
  - removable-singularities
  - singularities
  - laurent-series
  - principal-parts
relations: []
review: draft
---

::: {.theorem title="Riemann's removable singularity theorem"}
Suppose $f$ is holomorphic on $\Omega\sm\ts{z_0}$.
TFAE:

- $z_0$ is a pole of order $0$.

- $z_0$ is a removable singularity of $f$.

- There exists some neighborhood of $z_0$ on which $f$ is bounded.

- $(z-a)f(z) \convergesto{z\to z_0} 0$

- $f$ admits a holomorphic extension $F$ to all of $\Omega$

- $f$ admits a continuous extension $F$ to all of $\Omega$.

- $f$ admits a Laurent expansion about $z_0$ with vanishing principal part, i.e. $f(z) = \sum_{k\geq 0}c_k (z-z_0)^k$.
:::
