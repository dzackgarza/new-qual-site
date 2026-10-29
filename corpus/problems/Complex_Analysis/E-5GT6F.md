---
schema: qual/card@1
id: E-5GT6F
kind: problem
title: Radius of convergence of $\sqrt{z}$ about $4+3i$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: Typo corrected; the source reads "radius of convergences".
---

::: {.exercise}
Find the radius of convergence for the power series expansion of $\sqrt{z}$ about $z_0 = 4 +3i$.
:::

::: {.solution}
Let $f$ be a branch of $\sqrt{z}$ that is holomorphic near $z_0 = 4 + 3i$, and note $\abs{z_0}=\sqrt{4^2+3^2}=5$.

::: pf

::: {.pf-step #series}
$f(z)=\pm\sqrt{z_0}\displaystyle\sum_{n=0}^\infty \binom{1/2}{n} \left(\frac{z - z_0}{z_0}\right)^n$ near $z_0$, for a fixed square root $\sqrt{z_0}$.

::: pf-proof
Write $z = z_0 (1 + w)$ with $w=(z-z_0)/z_0$. The binomial series $\sum_n\binom{1/2}{n}w^n$ is a holomorphic square root of $1+w$ for $\abs w<1$, so $\sqrt{z_0}$ times it is a square root of $z$, and it agrees with $f$ up to the sign $\pm1$.
:::

:::

::: {.pf-step #binomial-radius}
The binomial series $\sum_{n\ge0} \binom{1/2}{n} w^n$ has radius of convergence exactly $1$.

::: pf-proof
Since $1/2\notin\NN$, no coefficient vanishes, and $\abs{\binom{1/2}{n+1}/\binom{1/2}{n}}=\abs{1/2-n}/(n+1)\to1$; the ratio test gives radius $1$.
:::

:::

::: pf-step
The radius of convergence is $\boxed{5}$, the distance from $z_0$ to the branch point $0$.

::: pf-proof
By steps [](#series){.pf-ref} and [](#binomial-radius){.pf-ref}, the Taylor series of $f$ about $z_0$ converges for $\abs{z-z_0}<\abs{z_0}=5$ and diverges for $\abs{z-z_0}>5$.
:::

:::

:::

:::
