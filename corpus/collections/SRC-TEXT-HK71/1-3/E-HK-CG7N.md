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
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read as a second reader against the retained text; the statement matches Hoffman and Kunze
    Exercise 1.3.2, printed p. 10. The reduction was recomputed: after swapping the first and
    third rows, R2 - 2R1 = (0,7,1) and R3 - 3R1 = (0,8,2), and 7R3 - 8R2 = (0,0,6), so the
    echelon form has a pivot in each column and the reduced system is I3 X = 0; the only
    solution is X = 0. The determinant confirms it, det A = -6. The rendered solution now
    records the retained text and its locator. No proof step changed.
---

::: {.exercise}
If

$$
A = \left[ \begin{array}{c c c} 3 & - 1 & 2 \\ 2 & 1 & 1 \\ 1 & - 3 & 0 \end{array} \right]
$$

find all solutions of $AX = 0$ by row-reducing $A$.
:::

::: {.solution}
No retained solution set covers this exercise; the book's text is retained as `assets/attachments/Hoffman-Kunze-Linear-Algebra.pdf` (Hoffman and Kunze, *Linear Algebra*, 2nd ed., 1971), where it is §1.3 Exercise 2 on printed p. 10. The argument is the card's own.

Row-reduce $A$:
$$
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
$$

::: pf

::: pf-step
The matrix has a pivot in every column.

::: pf-proof
The displayed echelon form has three nonzero pivots; equivalently its reduced
row-echelon form is $I_3$.
:::

:::

::: pf-step
The only solution of $AX=0$ is
$$
X=\begin{bmatrix}0\\0\\0\end{bmatrix}.
$$

::: pf-proof
Row operations preserve the solution set of a homogeneous system. Since the
reduced system is $I_3X=0$, all three coordinates vanish.
:::

:::

:::

:::
