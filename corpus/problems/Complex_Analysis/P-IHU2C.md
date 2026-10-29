---
schema: qual/card@1
id: P-IHU2C
kind: problem
title: Number of roots of $z^7-4z^3-1$ in $\abs{z}<1$
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Zeros
  - Polynomials
relations: []
review: draft
---

::: {.problem}
How many roots does the following polynomial have in the open disc $\abs{z} < 1$?
$$
f(z) = z^7 - 4z^3 - 1
.$$
:::

::: {.solution}
::: pf

::: {.pf-step #rouche-bound}
On $\abs{z} = 1$, $\abs{z^7 - 1} < \abs{-4z^3}$.

::: pf-proof
For $\abs{z} = 1$,
$$
\abs{z^7-1} \leq \abs{z}^7 + 1 = 2 < 4 = \abs{-4z^3}.
$$
:::

:::

::: pf-step
$f$ has $\boxed{3}$ roots in $\abs{z} < 1$, counted with multiplicity.

::: pf-proof
Since $f = -4z^3 + (z^7 - 1)$, Rouché's theorem and step [](#rouche-bound){.pf-ref} show that $f$ and $-4z^3$ have the same number of zeros in $\abs{z} < 1$.
The function $-4z^3$ has a zero of order three at $0$ and no other zero.
:::

:::

:::
:::
