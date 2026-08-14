---
schema: qual/card@1
id: T-4XPWL
kind: theorem
title: "Laurent expansion on an annulus"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - principal-parts
  - singularities
relations: []
review: draft
---

::: {.theorem title="Laurent expansion on an annulus"}
Let $f$ be holomorphic on the annulus
\[
A \da \ts{ z \in \CC \st r < \abs{z - z_0} < R }, \qquad 0 \leq r < R \leq \infty
.\]
Then $f$ has a two-sided expansion
\[
f(z) = \sum_{n\in\ZZ} c_n (z-z_0)^n
\]
converging locally uniformly on $A$, with coefficients
\[
c_n = {1\over 2\pi i}\int_{\abs{z - z_0} = \rho} {f(z) \over (z-z_0)^{n+1}}\dz
\]
for any $r < \rho < R$, independent of $\rho$.
The expansion is unique.

The terms with $n < 0$ form the **principal part**.
For an isolated singularity, i.e. the case $r = 0$, the principal part has no terms iff $z_0$ is removable, finitely many iff $z_0$ is a pole, and infinitely many iff $z_0$ is essential; this is what the classification of isolated singularities rests on.
:::

::: {.concept}
See Ahlfors, *Complex Analysis*, ch. 5 §1.3, p. 184.
:::
