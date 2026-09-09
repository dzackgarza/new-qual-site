---
schema: qual/card@1
id: E-HK-CG7N
kind: problem
title: Solving $AX = 0$ by row reduction
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
  note: Checked against Hoffman--Kunze, Section 1.3.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
If

$$
A = \left[ \begin{array}{c c c} 3 & - 1 & 2 \\ 2 & 1 & 1 \\ 1 & - 3 & 0 \end{array} \right]
$$

find all solutions of AX = 0 by row-reducing A.
:::

::: solution
Row-reduce $A$:
\[
\begin{bmatrix}
3&-1&2\\
2&1&1\\
1&-3&0
\end{bmatrix}
\sim
\begin{bmatrix}
1&-3&0\\
0&7&1\\
0&8&2
\end{bmatrix}
\sim
\begin{bmatrix}
1&-3&0\\
0&7&1\\
0&0&6
\end{bmatrix}.
\]

<1>1. The matrix has a pivot in every column.
::: proof
The displayed echelon form has three nonzero pivots; equivalently its reduced
row-echelon form is $I_3$.
:::

<1>2. The only solution of $AX=0$ is
\[
X=\begin{bmatrix}0\\0\\0\end{bmatrix}.
\]
::: proof
Row operations preserve the solution set of a homogeneous system. Since the
reduced system is $I_3X=0$, all three coordinates vanish.
:::
:::
