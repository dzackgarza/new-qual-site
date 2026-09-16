---
schema: qual/card@1
id: D-C3JIU
kind: definition
title: Principal part and residue at a pole
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
Let $f$ be [[D-E7A5W|holomorphic]] on a punctured disc $D_r(z_0)\setminus\{z_0\}$ with a [[D-AUD6K|pole of order $n\ge1$]] at $z_0$, and let
$$
f(z)=\sum_{k\ge-n}a_k(z-z_0)^k
$$
be its Laurent expansion there.
The \dfn{principal part} of $f$ at $z_0$ is
$$
P(z)\coloneqq\frac{a_{-n}}{(z-z_0)^n}+\cdots+\frac{a_{-1}}{z-z_0},
$$
and the \dfn{residue} of $f$ at $z_0$ is $\Res_{z=z_0}f\coloneqq a_{-1}$.
:::

::: {.remark}
The function $G\coloneqq f-P$ equals $\sum_{k\ge0}a_k(z-z_0)^k$ on $D_r(z_0)\setminus\{z_0\}$, so it extends to a holomorphic function on $D_r(z_0)$, and
$$
f(z)=P(z)+G(z)\qquad\text{for } 0<\abs{z-z_0}<r.
$$
The principal part is the unique polynomial in $(z-z_0)^{-1}$ without constant term for which $f-P$ extends holomorphically across $z_0$.
:::
