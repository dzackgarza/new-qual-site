---
schema: qual/card@1
id: E-HAT-4.3-9
kind: problem
title: "Linear projection is fibration but not fiber bundle"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Show that a linear projection of a 2-simplex onto one of its edges is a fibration but not a fiber bundle.
:::

::: {.solution}
Choose affine coordinates in which the simplex is
\[
\Delta=\{(x,y):0\le x\le1,\ 0\le y\le \lambda(x)\}
\]
for a continuous piecewise-linear function \(\lambda\ge0\), and the projection is
\[
p(x,y)=x
\]
onto the base edge \(I=[0,1]\). Embed \(\Delta\) in the trivial bundle
\[
I\times[0,M]\to I
\]
for \(M\ge\max\lambda\). There is a fiber-preserving retraction
\[
r:I\times[0,M]\to\Delta,
\qquad
r(x,y)=(x,\min\{y,\lambda(x)\}).
\]

Given any homotopy lifting problem for \(p:\Delta\to I\), first regard the initial lift as a map into the product bundle. Lift the base homotopy there, then compose the lift with \(r\). Since \(r\) preserves the base coordinate and restricts to the identity on \(\Delta\), this gives a lift with the prescribed initial map. Thus
\[
\boxed{p:\Delta\to I\text{ is a fibration}.}
\]

It is not a fiber bundle. For a linear projection onto an edge, the fibers over the endpoints of the edge are points, while fibers over interior points are nondegenerate closed intervals. These fibers are not homeomorphic, whereas all fibers of a bundle over the connected edge would be homeomorphic. Hence \(p\) is not a fiber bundle.
:::
