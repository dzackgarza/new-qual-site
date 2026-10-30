---
schema: qual/card@1
id: P-N6W5L
kind: problem
title: Number of zeros of $z^3-z+1$ in the right half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Argument Principle
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
Find the number of zeros $z$ with $\Re(z) > 0$ for the following function:
$$
f(z) \coloneqq z^3-z+1.
$$
:::

::: {.solution}
Let $M(z)=z^3+1$ and $m(z)=-z$, so $f=M+m$. For $R\ge2$ let $\Gamma_R$ be the boundary of the half-disk $\theset{\abs{z}<R,\ \Re z>0}$.

::: pf

::: {.pf-step #arc}
$\abs{M(z)}>\abs{m(z)}$ on the arc $\abs{z}=R$, $\Re z\ge0$.

::: pf-proof
$\abs{M(z)}\ge R^3-1>R=\abs{m(z)}$ for $R\ge2$.
:::

:::

::: {.pf-step #axis}
$\abs{M(it)}>\abs{m(it)}$ for all real $t$.

::: pf-proof
$\abs{M(it)}^2=\abs{1-it^3}^2=1+t^6$ and $\abs{m(it)}^2=t^2$. If $t^2\le1$, then $1+t^6>1\ge t^2$; if $t^2\ge1$, then $1+t^6>t^6\ge t^2$.
:::

:::

::: pf-step
$f$ has exactly $\boxed{2}$ zeros with $\Re z>0$.

::: pf-proof
By steps [](#arc){.pf-ref} and [](#axis){.pf-ref} and Rouché's theorem, $f$ and $M$ have the same number of zeros inside $\Gamma_R$ for every $R\ge2$, and neither has a zero on the imaginary axis. The zeros of $M$ are $e^{i\pi/3}$, $-1$, $e^{-i\pi/3}$, of which two have positive real part. Taking $R$ larger than the moduli of all zeros of $f$ gives the count in the whole half-plane.
:::

:::

:::
:::
