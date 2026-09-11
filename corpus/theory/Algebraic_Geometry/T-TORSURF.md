---
schema: qual/card@1
id: T-TORSURF
kind: theorem
title: Smooth complete toric surfaces and their intersection numbers
classification:
  areas:
  - algebraic-geometry
  topics:
  - Toric Varieties
  - Surfaces
  - Intersection Theory
relations:
- kind: uses
  target: T-TORDIV
review: draft
prompts:
- Classify the smooth complete toric surfaces.
- How do you compute intersection numbers of the boundary divisors of a toric surface?
---

::: {.theorem title="Classification"}
A smooth complete toric surface is given by rays $v_0, v_1, \ldots, v_{d-1}, v_d = v_0$ in counterclockwise order such that each consecutive pair $\ts{v_i, v_{i+1}}$ is a basis of $N \cong \ZZ^2$.
Consecutive triples then satisfy a unique relation
\[
v_{i-1} + v_{i+1} = a_i v_i, \qquad a_i \in \ZZ ,
\]
and these integers are constrained by
\[
\prod_{i} \begin{bmatrix} 0 & -1 \\ 1 & a_i \end{bmatrix} = \id , \qquad \sum_i a_i = 3d - 12 .
\]
For $d = 3$ the surface is $\PP^2$; for $d = 4$ it is a Hirzebruch surface $\FF_a$; for $d \geq 5$ it is a blowup of $\PP^2$ or of some $\FF_a$ at torus-fixed points.
:::

::: {.proposition title="Intersection numbers"}
With the same labelling,
\[
D_i \cdot D_j = \begin{cases}
0 & \abs{i - j} > 1 , \\
1 & \abs{i - j} = 1 , \\
-a_i & i = j .
\end{cases}
\]
:::

::: {.remark}
Two adjacent rays span a cone, whose fixed point is the single transverse intersection of the two divisors, giving the $1$.
Non-adjacent rays span no cone, so the divisors are disjoint, giving the $0$.
The self-intersection comes from $\operatorname{div}(\chi^m) \cdot D_i = 0$ for every $m$: choose $m$ with $\inp{m}{v_i} = -1$ and $\inp{m}{v_{i\pm1}}$ determined by the relation, and $D_i^2 = -a_i$ drops out.

The sum rule $\sum a_i = 3d - 12$ is a useful check.
For $\PP^2$, $d = 3$ and each $a_i = -1$, so each line has $D_i^2 = 1$.
For $\FF_a$, $d = 4$ and the $a_i$ are $a, 0, -a, 0$, giving self-intersections $-a, 0, a, 0$.
:::
