---
schema: qual/card@1
id: E-USHMH
kind: problem
title: $2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=n$ via $n$th roots of unity
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Polynomials
relations: []
review: draft
---

::: {.exercise}
Use $n$th roots of unity to show that $2^{n-1}\sin\frac{\pi}{n}\sin\frac{2\pi}{n}\cdots\sin\frac{(n-1)\pi}{n}=n$.
:::

::: {.solution}
Let $\zeta=e^{2\pi i/n}$.

::: pf

::: {.pf-step #product}
$n=\prod_{k=1}^{n-1}(1-\zeta^k)$.

::: pf-proof
The roots of $z^n-1$ are $1,\zeta,\ldots,\zeta^{n-1}$, so
$$
1+z+\cdots+z^{n-1}=\frac{z^n-1}{z-1}=\prod_{k=1}^{n-1}(z-\zeta^k).
$$
Setting $z=1$ gives the claim.
:::

:::

::: {.pf-step #modulus}
$\abs{1-\zeta^k}=2\sin\frac{k\pi}{n}$ for $1\le k\le n-1$.

::: pf-proof
For real $\theta$, $1-e^{i\theta}=-2i\,e^{i\theta/2}\sin\frac\theta2$, so $\abs{1-e^{i\theta}}=2\abs{\sin\frac\theta2}$.
With $\theta=2\pi k/n$ we have $0<k\pi/n<\pi$, so the sine is positive.
:::

:::

::: pf-step
$2^{n-1}\prod_{k=1}^{n-1}\sin\frac{k\pi}{n}=n$.

::: pf-proof
Take absolute values in step [](#product){.pf-ref} and apply step [](#modulus){.pf-ref} to each factor.
:::

:::

:::

:::
