---
schema: qual/card@1
id: P-TOP-WORKSHOP-D7-G06-TRIANGLE
kind: problem
title: The fundamental group of the triangular parachute
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Cell Complexes
  - van Kampen
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(June ’08) Let $X$ be the triangle parachute formed from the standard $2$-simplex $\Delta^2$ by identifying the three vertices with one another.
Compute a presentation for $\pi_1(X)$ and show that $\pi_1(X)$ is isomorphic to a free group $F_n$ (and identify which $n$!).
:::

::: {.solution}
After the three vertices of \(\Delta^2\) are identified, the three edges become three loops \(a,b,c\) based at the single vertex. The interior of the triangle is one \(2\)-cell. Orient the boundary cyclically; its attaching word is
\[
abc.
\]
Thus van Kampen gives
\[
\pi_1(X)\cong\langle a,b,c\mid abc=1\rangle.
\]
The relation eliminates \(c\): \(c=(ab)^{-1}\). Hence
\[
\pi_1(X)\cong\langle a,b\mid\ \rangle\cong F_2.
\]
Therefore the requested rank is
\[
\boxed{n=2}.
\]
:::
