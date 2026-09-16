---
schema: qual/card@1
id: D-BQLJV
kind: definition
title: Removable singularities
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

::: {.theorem title="Riemann's removable singularity theorem"}
Let $f$ be holomorphic on $D_r(z_0)\setminus\{z_0\}$.
The following are equivalent.

(a) $z_0$ is a removable singularity of $f$.

(b) $\lim_{z\to z_0}(z-z_0)f(z)=0$.

(c) $f$ is bounded on $D_\rho(z_0)\setminus\{z_0\}$ for some $0<\rho\le r$.
:::

::: {.proof}
(a)$\Rightarrow$(c).
The function $g$ is continuous on $D_\rho(z_0)$, hence bounded on $D_{\rho/2}(z_0)$, and $f=g$ there away from $z_0$.

(c)$\Rightarrow$(b).
If $\abs{f}\le M$ near $z_0$, then $\abs{(z-z_0)f(z)}\le M\abs{z-z_0}\to0$.

(b)$\Rightarrow$(a).
Define $h(z)\coloneqq(z-z_0)^2f(z)$ for $0<\abs{z-z_0}<r$ and $h(z_0)\coloneqq0$.
Then $h$ is holomorphic away from $z_0$, and at $z_0$
$$
\frac{h(z)-h(z_0)}{z-z_0}=(z-z_0)f(z)\to0,
$$
so $h$ is holomorphic on $D_r(z_0)$ with $h(z_0)=h'(z_0)=0$.
Its Taylor expansion is therefore $h(z)=\sum_{k\ge2}a_k(z-z_0)^k$ on $D_r(z_0)$, and $g(z)\coloneqq\sum_{k\ge2}a_k(z-z_0)^{k-2}$ is holomorphic on $D_r(z_0)$ and equals $f$ on the punctured disc.
:::

::: {.remark}
In terms of the Laurent expansion $f(z)=\sum_{k\in\ZZ}c_k(z-z_0)^k$ on $D_r(z_0)\setminus\{z_0\}$, the point $z_0$ is a removable singularity if and only if $c_k=0$ for all $k<0$, that is, if and only if the [[D-IWIA5|order]] $v_{z_0}(f)$ satisfies $v_{z_0}(f)\ge0$.
:::
