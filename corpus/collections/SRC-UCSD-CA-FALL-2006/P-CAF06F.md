---
schema: qual/card@1
id: P-CAF06F
kind: problem
title: "Uniform convergence of Taylor series on compact subsets of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $f(z)$ be a holomorphic function in the disk $|z| < 2$.
Show that $\sum_{n=1}^{\infty} \frac{f^{(n)}(z)}{n!}$ converges uniformly in any compact subset of the unit disk $|z| < 1$.
:::

::: solution
Let $K$ be a compact subset of $|z|<1$, and choose $r<1$ with
$K\subset\{|z|\le r\}$. Pick $\rho$ so that
\[
1<\rho<2-r.
\]
Then for every $z\in K$, the circle $|\zeta-z|=\rho$ lies in $|\zeta|<2$.
Set
\[
M=\max_{|\zeta|\le r+\rho}|f(\zeta)|.
\]
Cauchy's estimates give
\[
\frac{|f^{(n)}(z)|}{n!}\le \frac{M}{\rho^n}
\qquad(z\in K).
\]
Since $\rho>1$, the geometric series $\sum M/\rho^n$ converges. The
Weierstrass $M$-test therefore shows that
\[
\sum_{n=1}^\infty\frac{f^{(n)}(z)}{n!}
\]
converges uniformly on $K$. As $K$ was arbitrary, the convergence is uniform
on every compact subset of the unit disk.

Indeed, Taylor's theorem gives the sum explicitly as
\[
f(z+1)-f(z),
\]
because the disk of convergence of the Taylor series of $f$ about any
$z\in K$ has radius greater than $1$.
:::
