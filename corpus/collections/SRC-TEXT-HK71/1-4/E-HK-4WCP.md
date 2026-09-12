---
schema: qual/card@1
id: E-HK-4WCP
kind: problem
title: Row-reducing a $3 \times 2$ matrix over $\CC$
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
  note: Checked against Hoffman--Kunze, Section 1.4, Exercise 2.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Find a row-reduced echelon matrix which is row-equivalent to

$$
A = \left[ \begin{array}{c c} 1 & - i \\ 2 & 2 \\ i & 1 + i \end{array} \right].
$$

What are the solutions of $AX = 0$ ?
:::

::: solution
Row reduction gives
\[
\begin{bmatrix}
1&-i\\
2&2\\
i&1+i
\end{bmatrix}
\sim
\begin{bmatrix}
1&0\\
0&1\\
0&0
\end{bmatrix}.
\]

<1>1. The displayed matrix is a row-reduced echelon matrix row-equivalent to
$A$.
::: proof
Subtract $2R_1$ from $R_2$ and $iR_1$ from $R_3$. This gives
\[
\begin{bmatrix}
1&-i\\
0&2+2i\\
0&i
\end{bmatrix}.
\]
The second column contains a nonzero pivot below the first. Scaling that row to
make the pivot $1$, clearing the second column above and below it, yields the
displayed RREF.
:::

<1>2. The only solution of $AX=0$ is $X=0$.
::: proof
Row operations preserve the homogeneous solution set, and the reduced system
is $x_1=0$, $x_2=0$.
:::
:::
