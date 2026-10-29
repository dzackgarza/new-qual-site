---
schema: qual/card@1
id: T-ZZJDP
kind: theorem
title: Riemann's removable singularity theorem
slogan: 'Removability is exactly the absence of a principal part, equivalently boundedness or holomorphic extension across the point.'
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Singularities
  - Laurent Series
  - Principal Parts
relations: []
review: draft
---

::: {.theorem}
Let $\Omega\subseteq\CC$ be open, let $z_0\in\Omega$, and let $f$ be [[D-E7A5W|holomorphic]] on $\Omega\setminus\{z_0\}$.
The following are equivalent.

(i) $z_0$ is a [[D-BQLJV|removable singularity]] of $f$.

(ii) $f$ is bounded on $\{z : 0<\abs{z-z_0}<\delta\}$ for some $\delta>0$.

(iii) $(z-z_0)f(z)\to0$ as $z\to z_0$.

(iv) $f$ extends to a holomorphic function on $\Omega$.

(v) $f$ extends to a continuous function on $\Omega$.

(vi) $\lim_{z\to z_0}f(z)$ exists in $\CC$.

(vii) The Laurent expansion of $f$ on a punctured disc $\{z : 0<\abs{z-z_0}<\delta\}\subseteq\Omega$ has vanishing principal part: $f(z)=\sum_{k\geq0}c_k(z-z_0)^k$ there.

The extension in (iv) is unique.
:::

::: {.proof}
(i)$\Rightarrow$(iv): if $f=g$ on $D_\rho(z_0)\setminus\{z_0\}$ with $g$ holomorphic on $D_\rho(z_0)$, then $F\coloneqq f$ on $\Omega\setminus\{z_0\}$ and $F(z_0)\coloneqq g(z_0)$ is holomorphic on $\Omega$.
It is unique because two continuous extensions agree on $\Omega\setminus\{z_0\}$, whose closure in $\Omega$ contains $z_0$.
(iv)$\Rightarrow$(v)$\Rightarrow$(vi)$\Rightarrow$(ii)$\Rightarrow$(iii) are immediate: a continuous extension has a limit at $z_0$, a finite limit forces boundedness near $z_0$, and $\abs{(z-z_0)f(z)}\le M\abs{z-z_0}$.

(iii)$\Rightarrow$(i): choose $r>0$ with $D_r(z_0)\subseteq\Omega$, and define $h(z)\coloneqq(z-z_0)^2f(z)$ for $0<\abs{z-z_0}<r$ and $h(z_0)\coloneqq0$.
Then $h$ is holomorphic away from $z_0$, and at $z_0$
$$
\frac{h(z)-h(z_0)}{z-z_0}=(z-z_0)f(z)\to0,
$$
so $h$ is holomorphic on $D_r(z_0)$ with $h(z_0)=h'(z_0)=0$.
Its Taylor expansion is $h(z)=\sum_{k\ge2}a_k(z-z_0)^k$ on $D_r(z_0)$, and $g(z)\coloneqq\sum_{k\ge2}a_k(z-z_0)^{k-2}$ is holomorphic on $D_r(z_0)$ and equals $f$ on the punctured disc.

(i)$\iff$(vii) is part (a) of the proposition on [[D-IWIA5]].
:::

::: {.remark title="Variations"}
The equivalence (i)$\iff$(ii) alone is often stated as the Riemann extension theorem: an isolated singularity is removable exactly when the function stays bounded near it.
A removable singularity is sometimes called a pole of order zero: (i) holds exactly when $f(z)=(z-z_0)^{-n}h(z)$ near $z_0$ for an integer $n\le0$ and $h$ holomorphic near $z_0$, the factorization that defines a [[D-AUD6K|pole of order $n$]] for $n\ge1$.
:::
