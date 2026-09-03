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

1. **Distance to the nearest singularity:** The function $\sqrt{z} = \exp\left(\frac{1}{2} \log z\right)$ has a branch point (algebraic singularity) at $z = 0$.
   By the general theory of power series in complex analysis, the radius of convergence $R$ of the Taylor series of a holomorphic function about $z_0$ equals the distance from $z_0$ to the nearest singularity of $f(z)$ (or the boundary of the domain of holomorphy).

2. **Calculation:** The nearest singularity to $z_0 = 4 + 3i$ is the branch point at $z = 0$.
   The Euclidean distance is:
   $$
   R = |z_0 - 0| = |4 + 3i| = \sqrt{4^2 + 3^2} = \sqrt{16 + 9} = \sqrt{25} = 5.
   $$

3. **Explicit Taylor Series Expansion Check:** Writing $z = z_0 + (z - z_0) = z_0 \left(1 + \frac{z - z_0}{z_0}\right)$:
   $$
   \sqrt{z} = \sqrt{z_0} \left(1 + \frac{z - z_0}{z_0}\right)^{1/2} = \sqrt{z_0} \sum_{n=0}^\infty \binom{1/2}{n} \left(\frac{z - z_0}{z_0}\right)^n.
   $$
   The binomial series $\sum_{n=0}^\infty \binom{1/2}{n} w^n$ has radius of convergence $|w| < 1$.
   Setting $w = \frac{z - z_0}{z_0}$, the series converges for:
   $$
   \left|\frac{z - z_0}{z_0}\right| < 1 \iff |z - z_0| < |z_0| = 5.
   $$

Thus, the radius of convergence is $R = 5$.
:::
