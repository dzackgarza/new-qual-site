---
schema: qual/card@1
id: P-RPSK2
kind: problem
title: The line integral of $(2x+y)\,dx+y\,dy$ from $(2,1)$ to $(3,5)$ and path independence
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
---

::: {.problem}
(a) Choose a path $C$ from $(2,1)$ to $(3,5)$ and compute
$$
\int_C(2x+y)\,dx+y\,dy.
$$

(b) Give and apply a criterion that shows whether this integral is path independent.
:::

::: {.solution}
Parametrize the line segment by
$$
r(t)=(1-t)(2,1)+t(3,5)=(2+t,1+4t),\qquad 0\leq t\leq1.
$$
Then
$$
\int_C(2x+y)\,dx+y\,dy
=\int_0^1(9+22t)\,dt
=20.
$$

For $F=(P,Q)=(2x+y,y)$, path independence on $\RR^2$ would require $P_y=Q_x$.
Here $P_y=1$ and $Q_x=0$, so the integral is path dependent.
:::
