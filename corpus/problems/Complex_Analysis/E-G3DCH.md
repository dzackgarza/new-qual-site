---
schema: qual/card@1
id: E-G3DCH
kind: problem
title: Orders of the zeros of $(e^z-1)^3$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Power Series
relations: []
review: draft
---

::: {.exercise}
Find the orders of zeros of the following functions:

- $(e^z-1)^3$
:::

::: {.solution}

::: pf

::: {.pf-step #simple}
The zeros of $e^z-1$ are the points $2\pi ik$ with $k\in\ZZ$, and each is simple.

::: pf-proof
$e^z=1$ exactly when $z=2\pi ik$ with $k\in\ZZ$, and the derivative $e^z$ of $e^z-1$ equals $1\neq0$ at each of these points.
:::

:::

::: pf-step
The zeros of $(e^z-1)^3$ are the points $2\pi ik$ with $k\in\ZZ$, each of order $\boxed{3}$.

::: pf-proof
By step [](#simple){.pf-ref}, near $z_0=2\pi ik$ we have $e^z-1=(z-z_0)h(z)$ with $h$ holomorphic and $h(z_0)\neq0$.
Hence $(e^z-1)^3=(z-z_0)^3h(z)^3$ with $h(z_0)^3\neq0$.
:::

:::

:::

:::
