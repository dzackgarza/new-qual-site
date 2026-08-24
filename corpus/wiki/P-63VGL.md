---
schema: qual/card@1
id: P-63VGL
kind: problem
title: $\int_T f=0$ if $f$ is holomorphic and bounded near a puncture inside the triangle
  $T$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Morera
  - Contour Integration
relations: []
review: draft
---

:::{.problem title="?"}
Suppose that $f$ is holomorphic on a punctured open set $\Omega\setminus\theset{w_0}$ and let $T\subset \Omega$ be a triangle containing $w_0$.
Prove that if $f$ is bounded near $w_0$, then $\int_T f(z) ~dz = 0$.
:::

:::{.solution}
Without loss of generality assume $w_0 = 0$.
If $\abs{f(z)} \leq M$ for $\abs{z} < \eps$, pick $T$ contained in $\DD_\eps$, then
\[
\abs{\oint_T f(z)\dz } \leq \oint_T \abs{f(z)}\dz \leq \oint_T M \dz = M \mu(T)
,\]
and by homotopy invariance, this integral doesn't change as $T$ is perturbed.
Shrinking $T$, we can make $\mu(T)\to 0$.
:::

