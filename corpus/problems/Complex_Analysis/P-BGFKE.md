---
schema: qual/card@1
id: P-BGFKE
kind: problem
title: Roots of $z^3+2z+4$ lie outside the unit disk
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
Prove that the following polynomial has its roots outside of the unit circle:
$$
p(z) = z^3 + 2z + 4.
$$
:::

::: {.hint}
What is the maximum value of the modulus of the first two terms if $\abs{z} \leq 1$?
:::

::: {.solution}

::: pf

::: {.pf-step #bound}
For $\abs{z}\le1$, $\abs{z^3+2z}\le3<4$.

::: pf-proof
$\abs{z^3+2z}\le\abs{z}^3+2\abs{z}\le3$.
:::

:::

::: pf-step
$p$ has no roots in $\abs{z}\le1$.

::: pf-proof
For $\abs{z}\le1$, step [](#bound){.pf-ref} gives $\abs{p(z)}\ge4-\abs{z^3+2z}\ge1>0$.
:::

:::

:::

:::
