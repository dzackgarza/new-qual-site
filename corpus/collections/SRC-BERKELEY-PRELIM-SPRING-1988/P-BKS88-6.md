---
schema: qual/card@1
id: P-BKS88-6
kind: problem
title: Real matrices satisfying $A^2+2A+5I=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
Prove or disprove: There is a real $n\times n$ matrix $A$ such that

$$
A^2+2A+5I=0
$$

if and only if $n$ is even.
:::

::: {.solution}
::: pf

::: pf-step
If a real $n\times n$ matrix $A$ satisfies $A^2+2A+5I=0$, then $n$ is even.

::: pf-proof
The equation is equivalent to
$$
(A+I)^2=-4I.
$$
Taking determinants gives
$$
\det(A+I)^2=\det(-4I)=(-4)^n.
$$
The left-hand side is the square of a real number and is nonzero because the right-hand side is nonzero. Hence it is positive. Therefore $(-4)^n>0$, which is possible only when $n$ is even.
:::

:::

::: pf-step
For every even $n$, there is a real $n\times n$ matrix satisfying $A^2+2A+5I=0$.

::: pf-proof
Write $n=2m$ and let
$$
J_0:=
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix},
\qquad
B:=-I_2+2J_0=
\begin{pmatrix}
-1&-2\\
2&-1
\end{pmatrix}.
$$
Since $J_0^2=-I_2$,
$$
(B+I_2)^2=(2J_0)^2=-4I_2,
$$
and hence $B^2+2B+5I_2=0$. Let $A$ be the block-diagonal matrix with $m$ copies of $B$. The same polynomial identity holds on each block, so
$$
A^2+2A+5I_n=0.
$$
:::

:::

:::

:::
