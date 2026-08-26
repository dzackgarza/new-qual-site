---
schema: qual/card@1
id: P-RPSK2
kind: problem
title: Line integral of $[2x+y,y]$ from $(2,1)$ to $(3,5)$, and
  non-conservativeness
classification:
  areas:
  - prelim
  topics:
  - Line Integrals
relations: []
review: draft
---

::: problem
1. Choose a path $C$ from $(2,1)$ to $(3,5)$ and compute
\[
\int_C(2x+y)\,dx+y\,dy.
\]

2. Give and apply a criterion that shows whether this integral is path independent.
:::

::: solution
1. Parts
   1. We have
    $$ \int_C F_1 dx + F_2 dy + \cdots = 
    \int _ { C } \vec { F } \cdot d \vec { r } = \int _ { a } ^ { b } \vec { F } ( \vec { r } ( t ) ) \cdot \vec { r } ^ { \prime } ( t ) d t
    $$
    and we can parametrize the line segment by $r(t)=(1-t)[2,1]+t[3,5]=[2+t,1+4t]$, so
    $$
    \int_0^1 (9+22t)~dt = 20.
    $$

   2. $F = [P, Q] = [2x+y, y]$ is conservative iff there is a potential function $\phi$ satisfying $\nabla \phi = F$ iff $P_y = Q_x$. Here we see that $(2x+y)_y = 1$ but $(y)_x = 0$, so the integral is path-dependent.
:::
