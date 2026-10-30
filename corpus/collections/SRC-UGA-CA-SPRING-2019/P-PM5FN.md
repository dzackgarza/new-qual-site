---
schema: qual/card@1
id: P-PM5FN
kind: problem
title: Bounds relating $\sup_{\abs{z}\le R}\abs{f}$ and $\sup_{\abs{z}\le R}\abs{f'}$ for holomorphic $f$ on $\abs{z}<3R$
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Maximum Modulus Principle
  - Cauchy Integral Formula
relations: []
review: draft
---

::: {.problem}
Let $R>0$.
Suppose $f$ is holomorphic on $\theset{z\st \abs{z} < 3R}$.
Let
$$
M_{R}:=\sup _{\abs{z} \leq R}\abs{f(z)}, \quad N_{R}:=\sup _{\abs{z} \leq R}\abs{f^{\prime}(z)}
$$

a.
Estimate $M_{R}$ in terms of $N_{R}$ from above.

b.
Estimate $N_{R}$ in terms of $M_{2 R}$ from above.

:::

::: {.solution}

::: pf

::: {.pf-step #a}
$M_R\le\abs{f(0)}+R\,N_R$. No bound by $N_R$ alone is possible.

::: pf-proof
For $\abs{z}\le R$, integrate $f'$ along the segment from $0$ to $z$: $f(z)=f(0)+\int_0^1f'(tz)\,z\,dt$, so $\abs{f(z)}\le\abs{f(0)}+\abs{z}N_R\le\abs{f(0)}+RN_R$. A nonzero constant $f$ has $N_R=0$ and $M_R>0$, so the term $\abs{f(0)}$ cannot be removed.
:::

:::

::: {.pf-step #b}
$N_R\le M_{2R}/R$.

::: pf-proof
Let $\abs{z_0}\le R$. The closed disk $\abs{\xi-z_0}\le R$ lies in $\abs{\xi}\le2R$, which lies in the domain $\abs{\xi}<3R$. Cauchy's formula gives
$$
f'(z_0)=\frac1{2\pi i}\oint_{\abs{\xi-z_0}=R}\frac{f(\xi)}{(\xi-z_0)^2}\,d\xi,
$$
and the ML estimate gives $\abs{f'(z_0)}\le\frac1{2\pi}\cdot2\pi R\cdot\frac{M_{2R}}{R^2}=\frac{M_{2R}}R$. Take the supremum over $\abs{z_0}\le R$.
:::

:::

::: pf-qed
Steps [](#a){.pf-ref} and [](#b){.pf-ref} answer parts a and b.
:::

:::

:::
