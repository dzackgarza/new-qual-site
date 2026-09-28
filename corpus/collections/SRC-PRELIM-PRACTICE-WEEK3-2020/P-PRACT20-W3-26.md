---
schema: qual/card@1
id: P-PRACT20-W3-26
kind: problem
title: Area of an ellipse as the line integral $\oint -y\,dx+x\,dy$
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

::: {.problem}
Let C be the ellipse given by $( x / a ) ^ { 2 } + ( y / b ) ^ { 2 } = 1$ (where $a , b > 0 )$ . Calculate

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y .
$$
:::

::: {.solution}
Let $D$ be the region bounded by $\mathcal{C}$, oriented counterclockwise. By Green's theorem the line integral equals $\int_D \left(\frac{\partial x}{\partial x} - \frac{\partial(-y)}{\partial y}\right) dx\,dy = \int_D 2\,dx\,dy$, which we evaluate with the elliptic polar coordinates $x = a r \cos ( \theta ) , y = b r \sin ( \theta )$, whose Jacobian is $abr$:

$$
\oint _ { \mathcal { C } } ( - y ) d x + x d y = \int _ { D } 2 d x d y = \int _ { 0 } ^ { 2 \pi } \int _ { 0 } ^ { 1 } 2 a b r d r d \theta = 2 \pi a b .
$$
:::
