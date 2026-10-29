---
schema: qual/card@1
id: E-6BH7D
kind: problem
title: A conformal map from the upper half-disk onto $\HH$
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Fractional Linear Transformations
relations: []
review: draft
---

::: {.exercise}
Find a conformal map from the upper half-disc to the upper half-plane.
:::

::: {.solution}
Let $D^+\coloneqq\DD\intersect\HH$ be the upper half-disc and $Q_1\coloneqq\theset{\Re w>0,\ \Im w>0}$ the open first quadrant.

::: pf

::: {.pf-step #cayley}
The map $T(z)\coloneqq\frac{1+z}{1-z}$ sends $D^+$ bijectively onto $Q_1$.

::: pf-proof
$T$ is a fractional linear transformation, hence injective, and it sends $\DD$ onto the right half-plane $\theset{\Re w>0}$.
Since $\Im T(z)=\frac{2\Im z}{\abs{1-z}^2}$, a point $z\in\DD$ has $T(z)\in Q_1$ exactly when $\Im z>0$.
:::

:::

::: pf-step
$\boxed{z\mapsto\qty{\frac{1+z}{1-z}}^2}$ is a conformal map of $D^+$ onto $\HH$.

::: pf-proof
The map $w\mapsto w^2$ is holomorphic and injective on $Q_1$, and it sends $Q_1$ onto $\HH$ because it doubles arguments in $(0,\pi/2)$.
Compose with step [](#cayley){.pf-ref}.
:::

:::

:::

:::
