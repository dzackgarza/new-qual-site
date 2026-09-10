---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS1-P5
kind: problem
title: Diagonal of the torus is a retract but not a deformation retract
classification:
  areas:
  - topology
  topics:
  - Retracts
  - Homotopy
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
(May 2016) Let $X=S^1\times S^1$, also thought of as the standard quotient of the unit square $[0,1]\times[0,1]$, and let $A=\{(x,x):x\in S^1\}$ be the diagonal of $X$.
Show that $A$ is a retract of $X$, but not a deformation retract of $X$.
:::

::: {.solution}
Write points of the torus as \((z,w)\in S^1\times S^1\). Define
\[
r:S^1\times S^1\longrightarrow A,
\qquad
r(z,w)=(z,z).
\]
This map is continuous and, for every \((z,z)\in A\),
\[
r(z,z)=(z,z).
\]
Hence \(r\) is a retraction of \(X\) onto \(A\).

Suppose \(A\) were a deformation retract of \(X\). Then the inclusion
\[
i:A\hookrightarrow X
\]
would be a homotopy equivalence and therefore induce an isomorphism on fundamental groups. But
\[
\pi_1(A)\cong\mathbb Z,
\qquad
\pi_1(X)\cong\mathbb Z^2,
\]
and, under these identifications, the diagonal inclusion induces
\[
i_*:\mathbb Z\to\mathbb Z^2,
\qquad
n\longmapsto(n,n),
\]
which is not surjective. This contradiction shows that \(A\) is not a deformation retract of \(X\).
:::
