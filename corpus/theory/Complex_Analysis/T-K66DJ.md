---
schema: qual/card@1
id: T-K66DJ
kind: theorem
title: Cauchy integral formula on a bounded domain
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
Let $U\subseteq\CC$ be a bounded open set whose boundary $\partial U$ consists of finitely many piecewise smooth closed curves, oriented positively with respect to $U$, and let $f$ be [[D-E7A5W|holomorphic]] on an open set containing $\overline{U}$.
Then for every $p\in U$,
$$
f(p)=\frac{1}{2\pi i}\int_{\partial U}\frac{f(z)}{z-p}\dz.
$$
:::
