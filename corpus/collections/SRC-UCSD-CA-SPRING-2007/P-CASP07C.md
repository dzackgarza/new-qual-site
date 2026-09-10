---
schema: qual/card@1
id: P-CASP07C
kind: problem
title: "Convergence of the series of derivatives of an analytic function"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f(z)$ be analytic in the disk $B(0, 2)$.
Show that there is a function $g(z)$, analytic in the unit disk $\mathbb{D}$, such that the series $\sum_{n=1}^{\infty} f^{(n)}(z)$ converges to $g$ in $\mathcal{O}(\mathbb{D})$.
:::

::: solution
The statement is false as printed. Take
\[
f(z)={1\over3-z},
\]
which is analytic on $B(0,2)$. Then
\[
f^{(n)}(0)={n!\over3^{n+1}},
\]
so the terms of $\sum_{n\ge1}f^{(n)}(0)$ do not even tend to zero.

The likely normalized version
\[
\sum_{n=1}^\infty {f^{(n)}(z)\over n!}
\]
does converge in $\mathcal O(\DD)$, and its sum is
\[
\boxed{f(z+1)-f(z)}.
\]
Indeed, if $K\Subset\DD$, choose $r<1$ with $|z|\le r$ on $K$. For every
$z\in K$, the disk of radius $2-r>1$ centered at $z$ lies inside $B(0,2)$.
Taylor's theorem at $z$, evaluated at $z+1$, therefore gives
\[
f(z+1)=\sum_{n=0}^\infty {f^{(n)}(z)\over n!},
\]
and Cauchy estimates on any fixed circle of radius $\rho$ with
$1<\rho<2-r$ give a geometric majorant $C_K\rho^{-n}$, proving uniform
convergence on $K$.
:::
