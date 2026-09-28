---
schema: qual/card@1
id: P-CASP17G
kind: problem
title: "cos(sqrt(z)) is entire: determine order, rank, and genus"
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Order
  - Genus
  - Weierstrass Theorem
relations: []
review: draft
---

::: {.problem}
Show that the function $f(z) = \cos(\sqrt{z})$ is entire.
Determine the order, rank and genus of $f$.
:::

::: {.solution}
The power series of cosine gives
\[
\cos(\sqrt z)=\sum_{k=0}^\infty\frac{(-1)^k z^k}{(2k)!},
\]
which has infinite radius of convergence. Hence $f$ is entire.

Its zeros are
\[
z_k=\pi^2\left(k+\frac12\right)^2,
\qquad k=0,1,2,\ldots,
\]
all simple. Since $z_k\asymp k^2$, the exponent of convergence of the zeros
is $1/2$, and
\[
\sum_k\frac1{|z_k|}<\infty.
\]
Thus the canonical product has rank $0$ and genus $0$:
\[
\cos(\sqrt z)
=\prod_{k=0}^\infty
\left(1-\frac{z}{\pi^2(k+1/2)^2}\right).
\]
Also $\log M(r)\asymp\sqrt r$, so the order is
\[
\boxed{\rho=\frac12},
\]
while the rank and genus are both
\[
\boxed{0}.
\]
:::
