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
analytic in $D$ except for finitely many simple poles $z_1,\ldots,z_k$ on
$\abs{z}=1$, with residues $s_1,\ldots,s_k$. If
$$
f(z)=\sum_{n=0}^\infty a_nz^n\qquad(\abs{z}<1),
$$
prove that there is $M>0$ such that $\abs{a_n}\le M$ for all $n$.
:::

::: {.solution}
Let $H(z)=f(z)-\sum_{j=1}^k\frac{s_j}{z-z_j}$.

::: pf

::: {.pf-step #H}
$H(z)=\sum b_nz^n$ on $\abs{z}<1$ with $\abs{b_n}\le C$ for some $C$ and all $n$.

::: pf-proof
Subtracting the principal parts removes the simple poles, so $H$ is holomorphic on a neighborhood of the closed unit disk, hence on $\abs{z}<\rho$ for some $\rho>1$. Cauchy's estimates on a circle of radius $r\in(1,\rho)$ give $\abs{b_n}\le C r^{-n}\le C$.
:::

:::

::: {.pf-step #poles}
For $\abs{z}<1$, $\dfrac{s_j}{z-z_j}=-\displaystyle\sum_{n=0}^\infty\frac{s_j}{z_j^{n+1}}z^n$.

::: pf-proof
Expand $\dfrac{s_j}{z-z_j}=-\dfrac{s_j}{z_j}\dfrac{1}{1-z/z_j}$ as a geometric series, valid since $\abs{z/z_j}=\abs{z}<1$.
:::

:::

::: pf-step
$\abs{a_n}\le C+\sum_{j=1}^k\abs{s_j}$ for all $n$.

::: pf-proof
By steps [](#H){.pf-ref} and [](#poles){.pf-ref}, $a_n=b_n-\sum_{j=1}^ks_jz_j^{-(n+1)}$, and $\abs{z_j}=1$.
:::

:::

:::

:::
