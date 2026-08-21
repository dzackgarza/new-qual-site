---
schema: qual/card@1
id: E-ZCPKK
kind: exercise
title: Purely imaginary if on circle
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
  - Fractional Linear Transformations
relations: []
review: draft
solved: true
---

:::{.exercise title="Purely imaginary if on circle"}
Show that ${z-1\over z+1}$ is purely imaginary $\iff z\in S^1$.

> Hint: $z$ is real iff $\bar{z} = z$ and purely imaginary iff $\bar{z} = -z$.

:::

:::{.solution}

\[
{z-1\over z+1} = -\qty{\bar z - 1 \over \bar z + 1} \iff (z-1)(1+z) = (1-\bar z)(1+\bar z) \iff2-2\abs{z}^2 = 0 \iff \abs{z}^2 = 1
.\]

:::
