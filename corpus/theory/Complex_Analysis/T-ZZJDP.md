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

::: {.remark title="Variations"}
The equivalence (i)$\iff$(ii) alone is often stated as the Riemann extension theorem: an isolated singularity is removable exactly when the function stays bounded near it.
A removable singularity is sometimes called a pole of order zero: (i) holds exactly when $f(z)=(z-z_0)^{-n}h(z)$ near $z_0$ for an integer $n\le0$ and $h$ holomorphic near $z_0$, the factorization that defines a [[D-AUD6K|pole of order $n$]] for $n\ge1$.
:::
