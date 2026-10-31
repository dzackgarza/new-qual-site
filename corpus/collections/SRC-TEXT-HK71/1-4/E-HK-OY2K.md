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
\begin{aligned}
2x_1 - 3x_2 - 7x_3 + 5x_4 + 2x_5 &= -2\\
x_1 - 2x_2 - 4x_3 + 3x_4 + x_5 &= -2\\
2x_1 - 4x_3 + 2x_4 + x_5 &= 3\\
x_1 - 5x_2 - 7x_3 + 6x_4 + 2x_5 &= -7.
\end{aligned}
$$
:::

::: {.solution}
All solutions are
$$
(x_1,x_2,x_3,x_4,x_5)
=(1+2s-t,\ 2-s+t,\ s,\ t,\ 1),
\qquad s,t\in F.
$$

::: pf

::: pf-step
Row reduction of the augmented matrix yields
$$
\left[
\begin{array}{ccccc|c}
1&0&-2&1&0&1\\
0&1&1&-1&0&2\\
0&0&0&0&1&1\\
0&0&0&0&0&0
\end{array}
\right].
$$

::: pf-proof
Applying Gaussian elimination to the coefficient matrix together with the
right-hand side gives the displayed reduced row-echelon augmented matrix.
:::

:::

::: pf-step
The displayed family is exactly the solution set.

::: pf-proof
The reduced system is
$$
x_1-2x_3+x_4=1,
\qquad
x_2+x_3-x_4=2,
\qquad
x_5=1.
$$
Set the free variables $x_3=s$ and $x_4=t$. Then
$$
x_1=1+2s-t,
\qquad
x_2=2-s+t,
\qquad
x_5=1,
$$
which gives precisely the stated solutions.
:::

:::

:::

:::
