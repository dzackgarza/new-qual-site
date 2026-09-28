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
---

::: {.exercise}
Find the radius of convergences for the power series expansion of $\sqrt{z}$ about $z_0 = 4 +3i$.
:::

::: {.solution}
Let $f(z)$ be a branch of $\sqrt{z}$ defined and holomorphic in a neighborhood of $z_0 = 4 + 3i$ (for example, the principal branch).

1. The branch $f$ is holomorphic on the disk $\abs{z-z_0}<\abs{z_0}$, which does not contain the branch point $0$, so the Taylor series of $f$ about $z_0$ has radius of convergence at least
   $$
   |z_0| = |4 + 3i| = \sqrt{4^2 + 3^2} = 5.
   $$

2. Writing $z = z_0 \left(1 + \frac{z - z_0}{z_0}\right)$,
   $$
   \sqrt{z} = \sqrt{z_0} \left(1 + \frac{z - z_0}{z_0}\right)^{1/2} = \sqrt{z_0} \sum_{n=0}^\infty \binom{1/2}{n} \left(\frac{z - z_0}{z_0}\right)^n.
   $$
   Since $1/2\notin\NN$, the ratio $\abs{\binom{1/2}{n+1}/\binom{1/2}{n}}=\abs{1/2-n}/(n+1)$ tends to $1$, so the binomial series $\sum_{n=0}^\infty \binom{1/2}{n} w^n$ has radius of convergence exactly $1$.
   With $w = \frac{z - z_0}{z_0}$, the series converges for $|z - z_0| < |z_0| = 5$ and diverges for $|z-z_0|>5$.

Thus, the radius of convergence is $R = 5$, the distance from $z_0$ to the branch point $0$.
:::
