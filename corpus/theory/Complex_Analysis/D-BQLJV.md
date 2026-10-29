---
schema: qual/card@1
id: D-BQLJV
kind: definition
title: Removable singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
relations: []
review: draft
---

::: {.definition}
Let $z_0\in\CC$, let $r>0$, and let $f$ be [[D-E7A5W|holomorphic]] on the punctured disc $D_r(z_0)\setminus\{z_0\}$.
The point $z_0$ is a \dfn{removable singularity} of $f$ if there exist $0<\rho\le r$ and a holomorphic function $g\colon D_\rho(z_0)\to\CC$ such that $f(z)=g(z)$ for $0<\abs{z-z_0}<\rho$.
:::

::: {.remark}
In terms of the Laurent expansion $f(z)=\sum_{k\in\ZZ}c_k(z-z_0)^k$ on $D_r(z_0)\setminus\{z_0\}$, the point $z_0$ is a removable singularity if and only if $c_k=0$ for all $k<0$, that is, if and only if the [[D-IWIA5|order]] $v_{z_0}(f)$ satisfies $v_{z_0}(f)\ge0$.
:::
