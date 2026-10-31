---
schema: qual/card@1
id: P-PRACT20-W3-22
kind: problem
title: Integrating $e^{y^2}$ over a triangle by reversing the order of integration
classification:
  areas:
  - prelim
  topics:
  - Multivariable Calculus
  - Multiple Integrals
relations: []
review: draft
---

::: {.problem}
Find the integral of $f(x, y) = e^{y^{2}}$ over the triangular region bounded by the graph of $y = \abs{x}$ for $x \in [-2, 2]$ and the line $y = 2$.
:::

::: {.solution}
Integrate in $x$ first, since $e^{y^2}$ has no elementary antiderivative in $y$. The region is $\{(x,y):0\le y\le2,\ -y\le x\le y\}$, so the integral is

$$
\int_0^2\int_{-y}^{y}e^{y^2}\,dx\,dy=\int_0^2 2ye^{y^2}\,dy=e^{y^2}\evalfrom_{y=0}^{y=2}=e^4-1.
$$
:::
