---
schema: qual/card@1
id: P-CASP18E
kind: problem
title: A bounded Blaschke product with zeros $\alpha_n=1-1/n^2$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Products
  - Bounded Holomorphic Functions
  - Zeros
relations: []
review: draft
---

::: problem
Let $\alpha_n := 1 - \frac{1}{n^2}$.
Construct a function $f \in H(\mathbb{D})$ whose sequence of zeros (counting multiplicity) is precisely $\{\alpha_n\}$ and for which $|f(z)| \leq 1$ in $\mathbb{D}$.
:::

::: solution
We have
\[
\alpha_1=0,
\qquad
\alpha_n=1-\frac1{n^2}\in(0,1)\quad(n\ge2),
\]
and
\[
\sum_{n=1}^\infty(1-|\alpha_n|)
=\sum_{n=1}^\infty\frac1{n^2}<\infty.
\]
Hence the Blaschke product with these zeros converges:
\[
f(z)=z\prod_{n=2}^\infty
\frac{\alpha_n-z}{1-\alpha_n z}.
\]
Each factor has modulus $1$ on $|z|=1$ and modulus at most $1$ in
$\mathbb D$. Standard convergence of Blaschke products shows that the product
defines a holomorphic function on $\mathbb D$, bounded in modulus by $1$, and
its zeros, with multiplicity, are exactly the points $\alpha_n$.
:::
