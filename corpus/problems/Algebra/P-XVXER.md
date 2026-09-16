---
schema: qual/card@1
id: P-XVXER
kind: problem
title: Unit quaternions and $\mathrm{SO}(3)$
classification:
  areas:
  - algebra
  topics:
  - Groups
  - Geometry
  - Matrix Groups
relations: []
review: draft
---

::: {.problem}
Describe the group of unit quaternions topologically and explain its relationship with $\SO(3)$.
:::

::: {.solution}
Write the quaternion algebra as
\[
\HH=\{a+bi+cj+dk:a,b,c,d\in\RR\}.
\]
The norm is
\[
|q|^2=a^2+b^2+c^2+d^2.
\]
Hence the unit quaternions
\[
\{q\in\HH:|q|=1\}
\]
form the unit sphere
\[
S^3\subset\RR^4.
\]
Under quaternion multiplication this is a Lie group, isomorphic to
\[
\SU(2).
\]

Let $\operatorname{Im}\HH\cong\RR^3$ be the purely imaginary quaternions. For a unit quaternion $q$, define
\[
\rho(q)(v)=qvq^{-1},
\qquad v\in\operatorname{Im}\HH.
\]
Conjugation preserves the quaternion norm and fixes the real axis, so $\rho(q)$ restricts to an orientation-preserving orthogonal transformation of $\operatorname{Im}\HH$. Thus
\[
\rho:S^3\to\SO(3)
\]
is a group homomorphism.

Every rotation of $\RR^3$ is obtained in this way, so $\rho$ is surjective. Its kernel consists of the unit quaternions commuting with every imaginary quaternion, namely the real unit quaternions
\[
\{\pm1\}.
\]
Therefore
\[
\SO(3)\cong S^3/\{\pm1\},
\]
and
\[
S^3\cong\SU(2)\longrightarrow\SO(3)
\]
is a double covering map.
:::
