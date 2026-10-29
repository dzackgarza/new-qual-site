---
schema: qual/card@1
id: P-43AXY
kind: problem
title: Roots of $z^3+2z+4$ lie outside the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Rouché
  - Polynomials
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Prove that the following polynomial has its roots outside of the unit circle:
$$
p(z) = z^3 + 2z + 4
.$$
:::

::: {.hint}
What is the maximum value of the modulus of the first two terms if $\abs{z} \leq 1$?
:::

::: {.solution}

::: pf

::: {.pf-step #bound}
For $\abs{z}\leq1$, $\abs{z^3+2z}\leq3<4$.

::: pf-proof
By the triangle inequality, $\abs{z^3 + 2z} \leq \abs{z}^3 + 2\abs{z} \leq 3$.
:::

:::

::: pf-step
Every root $z$ of $p$ satisfies $\abs{z}>1$.

::: pf-proof
For $\abs{z}\leq1$, step [](#bound){.pf-ref} gives $\abs{p(z)}\geq4-\abs{z^3+2z}\geq1>0$.
:::

:::

:::

:::
