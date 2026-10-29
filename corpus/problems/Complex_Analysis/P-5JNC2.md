---
schema: qual/card@1
id: P-5JNC2
kind: problem
title: Laurent expansions of $\frac{z+1}{z(z-1)}$ about $0$ and $1$
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

::: {.problem}
Find the Laurent expansion of
$$
f(z) = \frac{z + 1}{z(z-1)}
$$
about $z=0$ and $z=1$ respectively.
:::

::: {.solution}

::: pf

::: {.pf-step #partial-fractions}
$f(z) = -\frac{1}{z} + \frac{2}{z-1}$.

::: pf-proof
Write $\frac{z+1}{z(z-1)} = \frac{A}{z} + \frac{B}{z-1}$.
Multiplying by $z$ and setting $z=0$ gives $A=-1$; multiplying by $z-1$ and setting $z=1$ gives $B=2$.
:::

:::

::: pf-step
On $0<\abs{z}<1$,
$$
\boxed{f(z) = -\frac{1}{z} - 2\sum_{n=0}^\infty z^n = -\frac{1}{z} - 2 - 2z - 2z^2 - \cdots}.
$$

::: pf-proof
For $\abs{z}<1$, $\frac{1}{z-1} = -\frac{1}{1-z} = -\sum_{n\ge0} z^n$.
Substitute this into step [](#partial-fractions){.pf-ref}.
:::

:::

::: pf-step
On $0<\abs{z-1}<1$,
$$
\boxed{f(z) = \frac{2}{z-1} + \sum_{n=0}^\infty (-1)^{n+1}(z-1)^n = \frac{2}{z-1} - 1 + (z-1) - (z-1)^2 + \cdots}.
$$

::: pf-proof
For $\abs{z-1}<1$, $\frac{1}{z} = \frac{1}{1+(z-1)} = \sum_{n\ge0}(-1)^n(z-1)^n$.
Substitute this into step [](#partial-fractions){.pf-ref}.
:::

:::

:::

:::
