---
schema: qual/card@1
id: P-CASP19E
kind: problem
title: "Taylor series partial sums converge in H(D) for functions analytic in B(0,2)"
classification:
  areas:
  - complex-analysis
  topics:
  - Taylor Series
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
---

::: {.problem}
Let $f$ be an analytic function in $B(0, 2)$.
Prove the sequence $g_N(z) := \sum_{n=1}^{N} \frac{f^{(n)}(z)}{n!}$, $N \geq 1$, converges in the space $H(\DD)$ of analytic functions on $\DD$.
:::

::: {.solution}
Fix a compact set $K\Subset\DD$. Choose $r$ with
$$
1<r<2-\sup_{z\in K}|z|.
$$
Then every circle $|\zeta-z|=r$, $z\in K$, lies in $B(0,2)$. Let
$$
M=\sup\{|f(\zeta)|:\operatorname{dist}(\zeta,K)\le r\}<\infty.
$$
Cauchy's estimate gives, uniformly for $z\in K$,
$$
\frac{|f^{(n)}(z)|}{n!}\le \frac{M}{r^n}.
$$
Since $r>1$, the geometric series $\sum M r^{-n}$ converges. Therefore
$$
\sum_{n=1}^\infty \frac{f^{(n)}(z)}{n!}
$$
converges uniformly on $K$. Because $K\Subset\DD$ was arbitrary, the
partial sums $g_N$ converge locally uniformly on $\DD$ to a holomorphic
function. Hence $g_N$ converges in $H(\DD)$.
:::
