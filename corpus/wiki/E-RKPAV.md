---
schema: qual/card@1
id: E-RKPAV
kind: exercise
title: Holomorphic functions satisfying $f^{2}=\overline{f}$ are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Cauchy-Riemann
  - Holomorphic Functions
relations: []
review: draft
solved: true
---

:::{.exercise title="?"}
Prove that if $f$ is holomorphic on a connected open set $\Omega$ and $f^2(z) = \bar{f(z)}$ then $f$ is constant.

:::

:::{.solution}
Write $F(z) \da f^3(z)$ so that
\[
F(z) = f^2(z) f(z) = \bar{f(z)}f(z) = \abs{f(z)}^2
.\]
Since $F$ is also holomorphic on $\Omega$ and this calculation shows $F(\Omega) \subseteq \Omega$, $F$ must be constant by the open mapping theorem.
So $f^3(z) = c$ for some $c$, forcing $f$ to be constant as well.
:::

