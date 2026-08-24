---
schema: qual/card@1
id: E-NZY3B
kind: exercise
title: Complement of a segment
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Complex Logarithm
  - Fractional Linear Transformations
relations: []
review: draft
---

:::{.exercise title="Complement of a segment"}
Map $\CC\sm[-1, 1]$ to $\DD$.

:::

:::{.solution}
In steps:

- Send $-1\to 0$ and $1\to \infty$ with $z\mapsto {z+1\over z-1}$.
  Checking that $f(0) = -1$, this yields $\CC\sm\RR_{\leq 0}$.

- Unwrap with $z\mapsto \sqrt{z}$ to obtain the right half-plane $-\pi/2<\Arg(z) < \pi/2$.
- Apply the rotated Cayley map $z\mapsto {z-1\over z+1}$ to map this to $\DD$.

Note that the composition is 
\[
{\sqrt{z+1\over z-1}  -1 \over \sqrt{z+1\over z-1} +1}
&= { \qty{ \sqrt{z+1} - \sqrt{z-1}}^2 \over (z+1)-(z-1) } \\
&= z - \sqrt{z^2-1}
,\]
which has inverse $z\mapsto {1\over 2}\qty{z+{1\over z}}$.
:::

