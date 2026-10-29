---
schema: qual/card@1
id: E-ZCPKK
kind: problem
title: $(z-1)/(z+1)$ is purely imaginary exactly on the unit circle
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
For $z\in\CC\smts{-1}$, show that
$$
\frac{z-1}{z+1}\in i\RR
\iff
\abs z=1.
$$
:::

::: {.hint}
$z$ is real iff $\bar{z} = z$ and purely imaginary iff $\bar{z} = -z$.
:::

::: {.solution}
Write $w\coloneqq(z-1)/(z+1)$.

::: pf

::: pf-step
$w\in i\RR \iff \abs z=1$.

::: pf-proof
$w\in i\RR$ exactly when $w = -\bar w$, that is, when $\frac{z-1}{z+1} = \frac{1-\bar z}{1+\bar z}$.
Clearing the nonzero denominators, this is $(z-1)(1+\bar z) = (1-\bar z)(1+z)$.
The two sides are $z - \bar z + \abs z^2 - 1$ and $z - \bar z + 1 - \abs z^2$, so the equation is $2\abs z^2 - 2 = 0$.
:::

:::

:::

:::
