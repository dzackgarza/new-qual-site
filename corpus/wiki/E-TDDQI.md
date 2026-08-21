---
schema: qual/card@1
id: E-TDDQI
kind: exercise
title: Area of the image of an annulus under a univalent Laurent series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $f(z) = \sum_{n= -\infty}^\infty c_n z^n$ be analytic and one-to-one in $r_0< |z| < R_0$.
For $r_0<r<R<R_0$, let $D(r,R)$ be the annulus $r<|z|<R$.
Show that the area of $f(D(r,R))$ is finite and is given by $$S = \pi \sum_{n=- \infty}^\infty n |c_n|^2 (R^{2n} - r^{2n}).$$
:::

::: {.solution}
See above solution: all goes identically up until the integral over $r$ values, just replace $\int_0^R$ with $\int_r^R$.
:::
