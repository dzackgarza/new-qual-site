---
schema: qual/card@1
id: E-CLSFF
kind: exercise
title: Meromorphic functions on $\mathbb{CP}^1$
classification:
  areas:
  - complex-analysis
  topics:
  - Meromorphic Functions
  - Principal Parts
  - Poles
  - Liouville's Theorem
  - Riemann Surfaces
relations: []
review: draft
solved: true
---

:::{.exercise title="Meromorphic functions on $\mathbb{CP}^1$ "}
Show that the only meromorphic functions on $\CP^1$ are rational functions.

:::

:::{.solution}
Any such $f$ can only have finitely many poles, so enumerate them as $\ts{z_k}_{k\leq n}$.
Write $P_k$ for the principal part of $f$ at $z_k$, so there is a decomposition
\[
f(z) = \sum_{k \leq n} P_k(z) + Q(z)
,\]
where $Q(z)$ is now entire. 
Note that $f(z)-Q(z)$ is evidently a rational function, and the claim is that $Q$ is constant.
Indeed, $\CP^1$ is compact and $g$ is continuous, thus bounded, so Liouville applies.
Thus $f(z) = \sum_{k\leq n}P_k(z) + c$ is rational.
:::
