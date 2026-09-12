---
schema: qual/card@1
id: E-HK-A9AS
kind: problem
title: Column space characterization for a $3 \times 3$ matrix
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
  note: Checked against Hoffman--Kunze, Section 1.4, Exercise 8.
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
A = \left[ \begin{array}{c c c} 3 & - 1 & 2 \\ 2 & 1 & 1 \\ 1 & - 3 & 0 \end{array} \right].
$$

For which triples $(y_{1}, y_{2}, y_{3})$ does the system $AX = Y$ have a solution?
:::

::: solution
The system $AX=Y$ has a solution for every triple
\[
(y_1,y_2,y_3)\in F^3.
\]

<1>1. The coefficient matrix $A$ is invertible.
::: proof
Its determinant is
\[
\det\begin{bmatrix}
3&-1&2\\
2&1&1\\
1&-3&0
\end{bmatrix}=-6\ne0.
\]
:::

<1>2. Hence $AX=Y$ is solvable for every $Y\in F^3$.
::: proof
By <1>1, $A^{-1}$ exists. For arbitrary
$Y=(y_1,y_2,y_3)^t$, take
\[
X=A^{-1}Y.
\]
Then $AX=Y$. In fact the solution is unique.
:::
:::
