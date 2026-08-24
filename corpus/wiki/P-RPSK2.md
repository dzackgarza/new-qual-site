---
schema: qual/card@1
id: P-RPSK2
kind: problem
title: Line integral of $[2x+y,y]$ along the segment from $(3,5)$ to $(2,1)$, and
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
1. Parts
   1. We have
    $$ \int_C F_1 dx + F_2 dy + \cdots = 
    \int _ { C } \vec { F } \cdot d \vec { r } = \int _ { a } ^ { b } \vec { F } ( \vec { r } ( t ) ) \cdot \vec { r } ^ { \prime } ( t ) d t
    $$
    and we can paramaterize a line segment $r(t) = t[2, 1] + (1-t)[3, 5] = [3-t, 5-4t]$, so just plug everything in to get 
    $$
    \int_0^1 22t-31~dt = -20
    $$

   2. $F = [P, Q] = [2x+y, y]$ is conservative iff there is a potential function $\phi$ satisfying $\nabla \phi = F$ iff $P_y = Q_x$. Here we see that $(2x+y)_y = 1$ but $(y)_x = 0$, so the integral is path-dependent.
:::
