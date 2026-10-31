---
schema: qual/card@1
id: E-HK-UBFI
kind: problem
title: Consistency and solutions of a three-equation system
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
  note: Checked against Hoffman--Kunze, Section 1.4, Exercise 4.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Consider the system of equations

$$
\begin{aligned}
x_1 - x_2 + 2x_3 &= 1\\
2x_1 + 2x_3 &= 1\\
x_1 - 3x_2 + 4x_3 &= 2.
\end{aligned}
$$

Does this system have a solution?
If so, describe explicitly all solutions.
:::

::: {.solution}
The system is consistent and has the one-parameter family of solutions
$$
(x_1,x_2,x_3)
=\left(\frac12-t,-\frac12+t,t\right),
\qquad t\in F.
$$

::: pf

::: pf-step
Row reduction of the augmented matrix gives
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
2&0&2&1\\
1&-3&4&2
\end{array}
\right]
\sim
\left[
\begin{array}{ccc|c}
1&0&1&1/2\\
0&1&-1&-1/2\\
0&0&0&0
\end{array}
\right].
$$

::: pf-proof
This is ordinary Gaussian elimination; in particular no row of the form
$[0\ 0\ 0\mid c]$ with $c\ne0$ occurs, so the system is consistent.
:::

:::

::: pf-step
The displayed family is exactly the solution set.

::: pf-proof
The reduced equations are
$$
x_1+x_3=\frac12,
\qquad
x_2-x_3=-\frac12.
$$
Set the free variable $x_3=t$ and solve for $x_1,x_2$.
:::

:::

:::

:::
