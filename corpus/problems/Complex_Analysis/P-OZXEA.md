---
schema: qual/card@1
id: P-OZXEA
kind: problem
title: An entire function with $f(z)/z\to 0$ as $z\to\infty$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Cauchy Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Suppose $f(z)$ is entire and
$$
\lim_{z\to\infty} {f(z) \over z} = 0.
$$

Show that $f(z)$ is a constant.
:::

::: {.solution}
Let $g(z)\definedas\frac{f(z)-f(0)}{z}$ for $z\neq0$ and $g(0)\definedas f'(0)$.

::: pf

::: {.pf-step #entire}
$g$ is entire.

::: pf-proof
$g$ is holomorphic on $\CC\setminus\theset{0}$, and continuous at $0$ by the definition of $f'(0)$, so the singularity at $0$ is removable.
:::

:::

::: {.pf-step #vanishes}
$g(z)\to0$ as $z\to\infty$.

::: pf-proof
$g(z)=\frac{f(z)}{z}-\frac{f(0)}{z}$, and both terms tend to $0$.
:::

:::

::: pf-step
$f$ is constant.

::: pf-proof
By step [](#vanishes){.pf-ref}, $\abs{g}\le1$ outside some disk, and $g$ is bounded on that compact disk by continuity, so $g$ is a bounded entire function by step [](#entire){.pf-ref}. By Liouville's theorem it is constant, and by step [](#vanishes){.pf-ref} the constant is $0$. Hence $f(z)=f(0)$ for all $z$.
:::

:::

:::
:::
