---
schema: qual/card@1
id: E-FS7GZ
kind: problem
title: Radii of convergence of the principal $\sqrt z$ about $4+3i$ and $-4+3i$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Convergence Tests
  - Complex Logarithm
relations: []
review: draft
---

::: {.exercise}
Find the radius of convergence of the Taylor series of the principal branch of $\sqrt z$ about $z_0=4+3i$.
Repeat with $z_1=-4+3i$.
:::

::: {.solution}

::: pf

::: {.pf-step #general-radius}
For $c\neq0$, the Taylor series of the principal branch of $\sqrt z$ about $c$ has radius of convergence $\abs c$.

::: pf-proof
The series is the binomial expansion $\sqrt z=\sqrt c\sum_{n\ge0}\binom{1/2}n\qty(\frac{z-c}c)^n$, with $\sqrt c$ the principal value.
The ratio of consecutive coefficients $\abs{\binom{1/2}{n+1}}/\abs{\binom{1/2}n}=\frac{\abs{1/2-n}}{n+1}\to1$, so the series converges exactly for $\abs{z-c}<\abs c$.
:::

:::

::: pf-step
$R_0=\abs{4+3i}=\boxed5$ and $R_1=\abs{-4+3i}=\boxed5$.

::: pf-proof
This is step [](#general-radius){.pf-ref} with $c=z_0$ and $c=z_1$.
For $z_1$ the branch cut $\RR_{\le0}$ meets the disk: the sum of the series equals the principal branch on the part of the disk above the cut, which contains $\abs{z-z_1}<3$, and equals its analytic continuation across the cut below it.
:::

:::

:::

:::
