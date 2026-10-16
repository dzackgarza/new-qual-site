---
schema: qual/card@1
id: P-Z8MQR
kind: problem
title: Taylor coefficients of $f$ are bounded when $f$ has finitely many simple poles on $\abs{z}=1$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Poles
relations: []
review: draft
---

::: {.problem}
Let $D$ contain the closed unit disk in its interior, and let $f$ be
analytic in $D$ except for finitely many simple poles $z_1,\dots,z_k$ on
$|z|=1$, with residues $s_1,\dots,s_k$. If
\[
f(z)=\sum_{n=0}^\infty a_nz^n\qquad(|z|<1),
\]
prove that there is $M>0$ such that $|a_n|\le M$ for all $n$.
:::

::: {.solution}
Define
\[
H(z)=f(z)-\sum_{j=1}^k\frac{s_j}{z-z_j}.
\]
The simple poles are removed, so $H$ is holomorphic on a neighborhood of the
closed unit disk. Hence there is $\rho>1$ such that $H(z)=\sum b_nz^n$ on
$|z|<\rho$, and Cauchy's estimates give $|b_n|\le C\rho^{-n}$ for some $C$.
For $|z|<1$ and $|z_j|=1$,
\[
\frac{s_j}{z-z_j}
=-\sum_{n=0}^\infty\frac{s_j}{z_j^{n+1}}z^n.
\]
Thus
\[
a_n=b_n-\sum_{j=1}^k\frac{s_j}{z_j^{n+1}},
\]
and therefore
\[
|a_n|\le C+\sum_{j=1}^k|s_j|.
\]
This constant is independent of $n$.
:::