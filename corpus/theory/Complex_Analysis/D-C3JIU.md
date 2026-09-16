---
schema: qual/card@1
id: D-C3JIU
kind: definition
title: Principal part and residue at an isolated singularity
classification:
  areas:
  - complex-analysis
  topics:
  - Principal Parts
  - Residues
  - Poles
  - Laurent Series
relations: []
review: draft
---

::: {.definition}
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$, so that $z_0$ is an [[D-IWIA5|isolated singularity]] of $f$, and let
$$
f(z)=\sum_{k=-\infty}^{\infty}a_k(z-z_0)^k \qquad (0<\abs{z-z_0}<r)
$$
be its Laurent expansion there.
The \dfn{principal part} of $f$ at $z_0$ is $\sum_{k\le -1}a_k(z-z_0)^k$, and the \dfn{residue} of $f$ at $z_0$ is $\Res_{z=z_0}f\coloneqq a_{-1}$ [@Ahl79].
:::

::: {.remark}
For every $0<\rho<r$ one has $\Res_{z=z_0}f=\frac{1}{2\pi i}\int_{\abs{z-z_0}=\rho}f(z)\dz$.
If $z_0$ is a [[D-AUD6K|pole of order $n\ge1$]], then $a_k = 0$ for $k<-n$ and the principal part is
$$
P(z)=\frac{a_{-n}}{(z-z_0)^n}+\cdots+\frac{a_{-1}}{z-z_0};
$$
the function $f-P$ equals $\sum_{k\ge0}a_k(z-z_0)^k$ on $D_r(z_0)\setminus\{z_0\}$, so it extends to a holomorphic function on $D_r(z_0)$, and $P$ is the unique polynomial in $(z-z_0)^{-1}$ without constant term with this property.
:::
