---
schema: qual/card@1
id: P-2DXZW
kind: problem
title: An entire function with $|f(z)|\le|z|^{1/2}$ for $|z|>10$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
  - Cauchy Estimates
relations: []
review: draft
---

::: {.problem}
Suppose $f: \CC\to \CC$ is entire and
$$
\abs{f(z)} \leq \abs{z}^{1\over 2} \quad\text{ when } \abs{z} > 10
.$$

Prove that $f$ is constant.
:::

::: {.solution}

::: pf

::: {.pf-step #derivative-vanishes}
$f'(z)=0$ for every $z\in\CC$.

::: pf-proof
Fix $z$ and let $R>10+\abs{z}$.
Every $\xi$ with $\abs{\xi-z}=R$ satisfies $10<\abs{\xi}\leq\abs{z}+R$, so $\abs{f(\xi)}\leq(\abs{z}+R)^{1/2}$.
The Cauchy estimate on the circle $\abs{\xi-z}=R$ gives
$$
\abs{f'(z)}\leq\frac{(\abs{z}+R)^{1/2}}{R}\convergesto{R\to\infty}0.
$$
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#derivative-vanishes){.pf-ref}, $f'\equiv 0$ on the connected set $\CC$.
:::

:::

:::

:::
