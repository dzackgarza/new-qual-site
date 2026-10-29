---
schema: qual/card@1
id: P-2VQDC
kind: problem
title: Liouville's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Cauchy Estimates
  - Entire Functions
relations: []
review: draft
---

::: {.problem}
Prove Liouville's theorem: suppose $f:\CC\to\CC$ is entire and bounded. 
Use Cauchy's formula to prove that $f'\equiv 0$ and hence $f$ is constant.
:::

::: {.solution}

Let $M$ bound $\abs{f}$ on $\CC$.

::: pf

::: {.pf-step #derivative-vanishes}
$f'(z)=0$ for every $z\in\CC$.

::: pf-proof
Fix $z$ and $R>0$.
Cauchy's formula for the derivative on the circle $\abs{\xi-z}=R$ gives
$$
\abs{f'(z)}=\abs{\frac1{2\pi i}\oint_{\abs{\xi-z}=R}\frac{f(\xi)}{(\xi-z)^2}\,d\xi}\leq\frac1{2\pi}\cdot\frac{M}{R^2}\cdot2\pi R=\frac MR,
$$
and $M/R\to0$ as $R\to\infty$.
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
