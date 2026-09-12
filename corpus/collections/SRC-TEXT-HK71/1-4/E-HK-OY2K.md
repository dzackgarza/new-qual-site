---
schema: qual/card@1
id: E-HK-OY2K
kind: problem
title: Solving a system of four equations in five unknowns
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
Find all solutions of

$$
\begin{array}{r l} 2 x _ {1} - 3 x _ {2} - 7 x _ {3} + 5 x _ {4} + 2 x _ {5} = & - 2 \\ x _ {1} - 2 x _ {2} - 4 x _ {3} + 3 x _ {4} + & x _ {5} = - 2 \\ 2 x _ {1} \qquad - 4 x _ {3} + 2 x _ {4} + & x _ {5} = 3 \\ x _ {1} - 5 x _ {2} - 7 x _ {3} + 6 x _ {4} + 2 x _ {5} = & - 7. \end{array}
$$
:::

::: solution
All solutions are
\[
(x_1,x_2,x_3,x_4,x_5)
=(1+2s-t,\ 2-s+t,\ s,\ t,\ 1),
\qquad s,t\in F.
\]

<1>1. Row reduction of the augmented matrix yields
\[
\left[
\begin{array}{ccccc|c}
1&0&-2&1&0&1\\
0&1&1&-1&0&2\\
0&0&0&0&1&1\\
0&0&0&0&0&0
\end{array}
\right].
\]
::: proof
Applying Gaussian elimination to the coefficient matrix together with the
right-hand side gives the displayed reduced row-echelon augmented matrix.
:::

<1>2. The displayed family is exactly the solution set.
::: proof
The reduced system is
\[
x_1-2x_3+x_4=1,
\qquad
x_2+x_3-x_4=2,
\qquad
x_5=1.
\]
Set the free variables $x_3=s$ and $x_4=t$. Then
\[
x_1=1+2s-t,
\qquad
x_2=2-s+t,
\qquad
x_5=1,
\]
which gives precisely the stated solutions.
:::
:::
