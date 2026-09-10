---
schema: qual/card@1
id: E-FZLDN
kind: problem
title: Holomorphic functions of unit modulus on the circle are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Cauchy Integral Formula
relations: []
review: draft
---

::: exercise
Suppose $f$ is continuous and non-zero on $\overline{\DD}$ and holomorphic on $\DD$ such that $|f(z)|=1$ for all $|z|=1$.
Show that $f$ is constant.

![image_2021-05-17-11-54-14](../../assets/Complex_Analysis/Review%20Doc/sections/figures/image_2021-05-17-11-54-14.png)
:::

::: solution
Since $f$ has no zeros on $\overline{\mathbb D}$, the function $1/f$ is
holomorphic on $\mathbb D$ and continuous on $\overline{\mathbb D}$. On the
unit circle,
\[
|f|=1,
\qquad
|1/f|=1.
\]
The maximum modulus principle applied to $f$ gives $|f(z)|\le1$ in
$\mathbb D$, while applied to $1/f$ it gives $|f(z)|\ge1$. Hence
\[
|f(z)|=1
\qquad(z\in\mathbb D).
\]
A nonconstant holomorphic function is an open map, but the unit circle has
empty interior. Therefore $f$ must be constant.
:::
