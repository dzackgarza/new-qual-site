---
schema: qual/card@1
id: E-HAT-3.3-33
kind: problem
title: Boundary of contractible manifold is a homology sphere
classification:
  areas:
  - topology
  topics:
  - Poincaré Duality
  - Manifolds
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that if $M$ is a compact contractible $n$-manifold then $\partial M$ is a homology $(n-1)$-sphere, that is, $H_i(\partial M; \ZZ) \approx H_i(S^{n-1}; \ZZ)$ for all $i$.
:::

::: {.solution}
Assume $n\ge1$. Since $M$ is contractible, it is orientable and $H^j(M;\ZZ)$ is $\ZZ$ for $j=0$ and zero for $j>0$. Lefschetz duality gives
$$
H_i(M,\partial M;\ZZ)\cong H^{n-i}(M;\ZZ)
=\begin{cases}\ZZ&i=n,\\0&i\ne n.\end{cases}
$$
The reduced homology of $M$ is zero. The reduced long exact sequence of $(M,\partial M)$ therefore gives
$$
\widetilde H_i(\partial M;\ZZ)\cong H_{i+1}(M,\partial M;\ZZ)
=\begin{cases}\ZZ&i=n-1,\\0&i\ne n-1.\end{cases}
$$
These are the reduced homology groups of $S^{n-1}$. This also covers $n=1$: $\widetilde H_0(\partial M)=\ZZ$, so $H_0(\partial M)=\ZZ^2$.
:::
