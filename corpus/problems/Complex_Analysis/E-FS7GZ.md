---
schema: qual/card@1
id: E-FS7GZ
kind: problem
title: Taylor radii for the principal square root
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
The principal square root is holomorphic on
\[
\CC\setminus\RR_{\leq0}.
\]
The Taylor radius at a point is therefore the distance from the center to the branch cut.

For $z_0=4+3i$, the closest point of $\RR_{\leq0}$ is $0$, so
\[
R_0=|4+3i|=5.
\]

For $z_1=-4+3i$, the perpendicular projection $-4$ lies on the branch cut, so
\[
R_1=|(-4+3i)-(-4)|=3.
\]
:::
