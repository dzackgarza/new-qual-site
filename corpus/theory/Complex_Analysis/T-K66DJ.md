---
schema: qual/card@1
id: T-K66DJ
kind: theorem
title: Cauchy integral formula on a bounded domain
slogan: 'A holomorphic function is reconstructed from its boundary values by the Cauchy kernel.'
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Contour Integration
relations: []
review: draft
---

::: {.theorem}
Let $U\subseteq\CC$ be a bounded open set whose boundary $\bd U$ consists of finitely many piecewise smooth closed curves, oriented positively with respect to $U$, and let $f$ be [[D-E7A5W|holomorphic]] on an open set containing $\overline{U}$.
Then for every $p\in U$,
$$
f(p)=\frac{1}{2\pi i}\int_{\bd U}\frac{f(z)}{z-p}\dz.
$$

The general form is [@Ahl73, ch. 4, §2.2, Theorem 6]: for $f$ analytic in an open disc $\Delta$ and $\gamma$ a closed curve in it, $n(\gamma,a)f(a)=\frac{1}{2\pi i}\int_\gamma\frac{f(z)}{z-a}\dz$, where $n$ is the index. The display above is that identity with $\gamma=\bd U$ and $n(\bd U,p)=1$, the positive orientation of the boundary with respect to $U$ being the one that makes the index $1$ at each interior point, and the disc of the theorem taken about $p$ large enough to contain $\bd U$ and small enough to lie where $f$ is analytic.
:::
