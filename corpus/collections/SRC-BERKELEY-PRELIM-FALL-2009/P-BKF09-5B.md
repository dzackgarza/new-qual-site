---
schema: qual/card@1
id: P-BKF09-5B
kind: problem
title: Solution of $xy'+y=y^2$ with $y(1)=2$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Solve the differential equation
$$
xy'+y=y^2
$$
with initial condition $y(1)=2$.
:::

::: {.solution}
Separation of variables gives $dx/x=dy/(y^2-y)$, and integrating both sides of this gives $\log x=\log(y-1)-\log(y)+c$, or $y=1/(Kx+1)$, so using the initial condition we get $y=2/(2-x)$.
:::
