---
schema: qual/card@1
id: P-PRACT20-W3-21
kind: problem
title: Work done by a constant force along the twisted cubic $(t,t^2,t^3)$
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Line Integrals
relations: []
review: draft
---

::: {.problem}
Let $F$ be a constant unit force in the direction of $(-1, 0, 1)$. Find the work done by $F$ on a particle which moves along the path $r(t) = (t, t^{2}, t^{3})$ for $t \in [0, 1]$.
:::

::: {.solution}
The unit force is $F=\frac{1}{\sqrt2}(-1,0,1)$ and $r'(t)=(1,2t,3t^2)$. The work is

$$
\int_{\mathcal{C}}F\cdot dr=\int_0^1F\cdot r'(t)\,dt=\frac{1}{\sqrt2}\int_0^1(-1+3t^2)\,dt=0.
$$
:::
