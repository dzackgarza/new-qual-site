---
schema: qual/card@1
id: E-IYBZP
kind: problem
title: A holomorphic function with a vanishing Taylor coefficient at every point is
  a polynomial
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
If $f$ is holomorphic on a region $\Omega$ and for each $z_0\in\Omega$ at least one coefficient in the power series $f(z)=\sum_{n=0}^\infty c_n(z-z_0)^n$ is zero, show that $f$ is a polynomial.

![image_2021-05-17-11-53-33](../../assets/Complex_Analysis/Review%20Doc/sections/figures/image_2021-05-17-11-53-33.png)
:::

::: solution
For each $n\ge0$, let
\[
Z_n=\{z\in\Omega:f^{(n)}(z)=0\}.
\]
Each $Z_n$ is closed in $\Omega$. The hypothesis says that for every
$z_0\in\Omega$ at least one Taylor coefficient at $z_0$ vanishes, i.e.
$f^{(n)}(z_0)=0$ for some $n$. Hence
\[
\Omega=\bigcup_{n=0}^\infty Z_n.
\]

Choose a closed disk $\overline D\Subset\Omega$. Since $\overline D$ is a
complete metric space, Baire's theorem implies that one of the closed sets
$Z_n\cap\overline D$ has nonempty interior in $\overline D$. Thus
$f^{(n)}$ vanishes on a nonempty open subset of $\Omega$. By the identity
theorem,
\[
f^{(n)}\equiv0\quad\text{on }\Omega.
\]
Therefore $f$ is a polynomial of degree at most $n-1$ (with the case $n=0$
giving $f\equiv0$).
:::
