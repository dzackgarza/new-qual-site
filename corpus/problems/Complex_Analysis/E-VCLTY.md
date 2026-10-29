---
schema: qual/card@1
id: E-VCLTY
kind: problem
title: Laurent expansions about different points
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: {.exercise}
Find the Laurent expansion about $z=0$ and $z=1$ respectively of the following function:
$$
f(z) \definedas {z+1 \over z(z-1)}.
$$

:::

::: {.hint}
Split $f$ into partial fractions; each piece is either a principal part at the given point or a geometric series there.
:::

::: {.solution}
::: pf

::: {.pf-step #partial-fractions}
$f(z) = -\frac1z + \frac{2}{z-1}$.

::: pf-proof
$-(z-1) + 2z = z+1$.
:::

:::

::: pf-step
On $0<\abs z<1$,
$$
\boxed{f(z) = -\frac1z - 2\sum_{k\geq 0} z^k.}
$$

::: pf-proof
In step [](#partial-fractions){.pf-ref}, $-\frac1z$ is already a Laurent term at $0$, and $\frac{2}{z-1} = -\frac{2}{1-z} = -2\sum_{k\geq0}z^k$ for $\abs z<1$.
:::

:::

::: pf-step
On $0<\abs{z-1}<1$,
$$
\boxed{f(z) = \frac{2}{z-1} - \sum_{k\geq 0} (-1)^k (z-1)^k.}
$$

::: pf-proof
In step [](#partial-fractions){.pf-ref}, $\frac{2}{z-1}$ is already a Laurent term at $1$, and $-\frac1z = -\frac{1}{1+(z-1)} = -\sum_{k\geq0}(-1)^k(z-1)^k$ for $\abs{z-1}<1$.
:::

:::

:::

:::
