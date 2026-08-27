---
schema: qual/card@1
id: T-LA2UI
kind: theorem
title: Cauchy Integral Formula
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Power Series
  - Contour Integration
relations: []
review: draft
---

:::{.theorem ref="CauchyIntegral"}
Suppose $f$ is holomorphic on $\Omega$, then for any $z_0 \in \Omega$ and any open disc $\closure{D_R(z_0)}$ such that $\gamma \da \bd \closure{D_R(z_0)} \subseteq \Omega$,
\[
f(z_0) = {1 \over 2\pi i} \int_{\gamma} {f(\xi) \over \xi-z_0}\ \dxi
\]
and
\[
f^{(n)}(z_0) = {n! \over 2\pi i} \int_{\gamma} {f(\xi) \over (\xi - z_0)^{n+1}} \dxi
.\]
As a consequence, if $f(z) \sum_{k\geq 0} c_k (z-z_0)^k$,
\[
c_k = {f^{(n)}(z_0) \over n!} = {1\over 2\pi i} \int_\gamma { f(\xi) \over (\xi - z_0)^{n+1} } \dxi
.\]
:::
