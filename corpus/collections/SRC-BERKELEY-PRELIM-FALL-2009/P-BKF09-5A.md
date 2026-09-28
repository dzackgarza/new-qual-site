---
schema: qual/card@1
id: P-BKF09-5A
kind: problem
title: Minkowski sum of closed connected subsets of $\mathbb R^2$ need not be closed
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Is it possible to find two closed and connected subsets $A$ and $B$ in $\RR^2$ such that
$$
A+B=\{(x_1+x_2,y_1+y_2)\in\RR^2\mid(x_1,y_1)\in A,\ (x_2,y_2)\in B\}
$$
is not closed?
:::

::: {.solution}
Yes; take $A$ to be the $x$-axis and $B$ to be one of the components of $xy=1$, so that $A+B$ is an open half-plane ($y>0$ or $y<0$).
:::
