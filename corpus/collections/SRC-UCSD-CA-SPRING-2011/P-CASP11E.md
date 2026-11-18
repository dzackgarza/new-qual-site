---
schema: qual/card@1
id: P-CASP11E
kind: problem
title: 'The integral of $e^{iz}/\log z$ over a quarter circle of radius $R$ tends to $0$'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
For $R > 1$ let $C_R$ be the quarter circle parametrized by $z = Re^{i\theta}$, $0 \leq \theta \leq \pi/2$.
Prove that $$\lim_{R \to \infty} \int_{C_R} \frac{e^{iz}}{\log z}\,dz = 0,$$ where $\log z$ is the principal branch of the logarithm.

Hint: You may use the inequality $\sin\theta \geq c\theta$ for $0 \leq \theta \leq \pi/2$, with some constant $c > 0$.
Then evaluate an appropriate integral.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own estimate follows, with the three pointwise bounds, the sine estimate and the limit as separate steps.

::: pf

::: {.pf-step #bounds}
On $C_R$, $z=Re^{i\theta}$ with $0\le\theta\le\pi/2$, one has $\abs{e^{iz}}=e^{-R\sin\theta}$, $\abs{\log z}\ge\log R$ and $\abs{dz}=R\,d\theta$.

::: pf-proof
$e^{iz}=e^{iR\cos\theta}e^{-R\sin\theta}$ has modulus $e^{-R\sin\theta}$. The principal logarithm is $\log z=\log R+i\theta$, whose modulus is at least $\log R>0$ because $R>1$. And $\abs{dz/dt}=\abs{iRe^{i\theta}}=R$.
:::

:::

::: {.pf-step #estimate}
$\abs{\displaystyle\int_{C_R}\frac{e^{iz}}{\log z}dz}\le\dfrac{R}{\log R}\int_{0}^{\pi/2}e^{-R\sin\theta}d\theta\le\dfrac{1}{c\log R}$.

::: pf-proof
The modulus of the integral is at most the integral of the modulus, which by step [](#bounds){.pf-ref} is at most $\int_{0}^{\pi/2}\frac{e^{-R\sin\theta}}{\log R}R\,d\theta=\frac{R}{\log R}\int_{0}^{\pi/2}e^{-R\sin\theta}d\theta$. With $\sin\theta\ge c\theta$ on $[0,\pi/2]$ the integrand is at most $e^{-cR\theta}$, so the integral is at most $\int_{0}^{\infty}e^{-cR\theta}d\theta=\frac{1}{cR}$, giving $\frac{R}{\log R}\cdot\frac{1}{cR}=\frac{1}{c\log R}$.
:::

:::

::: {.pf-qed}
As $R\to\infty$ the bound $\dfrac{1}{c\log R}$ tends to $0$, so $\displaystyle\lim_{R\to\infty}\int_{C_R}\frac{e^{iz}}{\log z}dz=0$.
:::

:::

:::
