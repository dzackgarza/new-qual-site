---
schema: qual/card@1
id: P-2CKBC
kind: problem
title: $\int_{-\infty}^\infty\frac{1+x^2}{1+x^4}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
relations: []
review: draft
---

::: {.problem}
Calculate
$$
\int_{-\infty}^\infty {1+x^2 \over 1+x^4}\, dx
.$$

:::

::: {.solution}

Let $I$ denote the integral and $J\coloneqq\int_0^\infty\frac{dx}{1+x^4}$.

::: pf

::: {.pf-step #reduce}
$I=4J$.

::: pf-proof
The integrand is even, so $I=2\int_0^\infty\frac{1+x^2}{1+x^4}\,dx$.
The substitution $x=1/t$ gives $\int_0^\infty\frac{x^2}{1+x^4}\,dx=\int_0^\infty\frac{dt}{1+t^4}=J$, so $I=2(J+J)$.
:::

:::

::: {.pf-step #residues}
$\int_{-\infty}^{\infty}\frac{dx}{1+x^4}=\frac{\pi}{\sqrt2}$, so $J=\frac{\pi}{2\sqrt2}$.

::: pf-proof
Close $[-R,R]$ by the upper semicircle of radius $R>1$.
On the semicircle the integrand is $O(R^{-4})$, so that integral is $O(R^{-3})\to 0$.
The poles of $1/(1+z^4)$ in the upper half-plane are $z_1=e^{i\pi/4}$ and $z_2=e^{3i\pi/4}$, simple, with residues $\frac{1}{4z_k^3}=-\frac{z_k}{4}$.
Since $z_1+z_2=i\sqrt2$, the residue theorem gives $2\pi i\cdot\left(-\frac{i\sqrt2}{4}\right)=\frac{\pi}{\sqrt2}$, and $J$ is half of this because the integrand is even.
:::

:::

::: pf-step
$I=\boxed{\sqrt2\,\pi}$.

::: pf-proof
Combine steps [](#reduce){.pf-ref} and [](#residues){.pf-ref}.
:::

:::

:::

:::
