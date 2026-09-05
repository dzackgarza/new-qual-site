---
schema: qual/card@1
id: P-H42KM
kind: problem
title: Fundamental group of the mapping cone of a $k$-fold cover $S^1\to S^1$
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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 7 of the official UGA Spring 2019 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Replaced the incomplete argument and Z/mZ typo with the mapping-cone CW description and the van Kampen presentation <a | a^k>.
---

::: problem
For topological spaces $X,Y$, the mapping cone $C(f)$ of a map
\[
f:X\longrightarrow Y
\]
is defined as
\[
C(f)
=
\bigl((X\times[0,1])\amalg Y\bigr)/\sim,
\]
where
\[
(x,0)\sim(x',0)
\qquad\text{for all }x,x'\in X,
\]
and
\[
(x,1)\sim f(x).
\]
Let
\[
\phi_k:S^1\longrightarrow S^1
\]
be a $k$-fold covering.
Find
\[
\pi_1(C(\phi_k)).
\]
:::

::: {.solution}
Assume $k\ge1$, as in the usual meaning of a $k$-fold covering.

<1>1. The mapping cone $C(\phi_k)$ is obtained from the target circle by attaching one $2$-cell by the degree-$k$ map $\phi_k$:
\[
C(\phi_k)\cong S^1\cup_{\phi_k}D^2.
\]
::: {.proof}
The quotient
\[
(S^1\times[0,1])/(S^1\times\{0\})
\]
is the cone on $S^1$, hence is homeomorphic to $D^2$.
Its boundary is the copy
\[
S^1\times\{1\},
\]
and the remaining mapping-cone identification glues that boundary to the target circle by
\[
(x,1)\longmapsto\phi_k(x).
\]
Thus the mapping cone is exactly the displayed adjunction space.
:::

<1>2. If $a$ denotes the standard generator of the target circle, attaching the $2$-cell imposes the relation
\[
a^k=1
\]
on the fundamental group.
::: {.proof}
Before attaching the $2$-cell, the $1$-skeleton is $S^1$, so
\[
\pi_1(S^1)\cong\langle a\rangle\cong\ZZ.
\]
A $k$-fold covering
\[
\phi_k:S^1\to S^1
\]
induces multiplication by $k$ on fundamental groups; equivalently, its attaching loop represents $a^k$.
By the Seifert--van Kampen theorem for attaching a $2$-cell, the fundamental group of the resulting space is the quotient by the normal closure of that attaching element:
\[
\pi_1(C(\phi_k))
\cong
\langle a\mid a^k=1\rangle.
\]
:::

<1>3. Therefore
\[
\boxed{
\pi_1(C(\phi_k))\cong\ZZ/k\ZZ.
}
\]
::: {.proof}
The group with one generator $a$ and the single relation $a^k=1$ is the cyclic group of order $k$, namely $\ZZ/k\ZZ$.
For $k=1$ this is the trivial group, as the formula also indicates.
:::
:::
