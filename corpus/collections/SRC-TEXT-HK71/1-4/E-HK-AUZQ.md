---
schema: qual/card@1
id: E-HK-AUZQ
kind: problem
title: Column space characterization for a $4 \times 4$ matrix
classification:
  areas:
  - algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hoffman--Kunze, Section 1.4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Let

$$
A = \left[ \begin{array}{c c c c} 3 & - 6 & 2 & - 1 \\ - 2 & 4 & 1 & 3 \\ 0 & 0 & 1 & 1 \\ 1 & - 2 & 1 & 0 \end{array} \right].
$$

For which $(y_{1}, y_{2}, y_{3}, y_{4})$ does the system of equations AX = Y have a solution?
:::

::: solution
The system $AX=Y$ is solvable exactly for those
$Y=(y_1,y_2,y_3,y_4)^t$ satisfying
\[
2y_1+3y_2-7y_3=0,
\qquad
3y_1+y_2-7y_4=0.
\]

<1>1. Every vector in the column space of $A$ satisfies the two displayed
relations.
::: proof
The vectors
\[
u=(-2,-3,7,0)^t,
\qquad
v=(-3,-1,0,7)^t
\]
satisfy
\[
u^tA=0,
\qquad
v^tA=0.
\]
Hence if $Y=AX$, then
\[
u^tY=u^tAX=0,
\qquad
v^tY=v^tAX=0,
\]
which are exactly the stated equations.
:::

<1>2. The two relations are also sufficient.
::: proof
Row reduction shows $\operatorname{rank}A=2$. Therefore the left nullspace
\[
\ker(A^t)
\]
has dimension $4-2=2$. The two vectors $u,v$ in <1>1 are linearly independent,
so they form a basis of this left nullspace.

The column space is the annihilator of the left nullspace. Consequently a vector
$Y$ lies in the column space of $A$ exactly when $u^tY=v^tY=0$, namely exactly
when the two displayed relations hold.
:::
:::
