---
schema: qual/card@1
id: E-HK-PNK2
kind: problem
title: Non-row-equivalent matrices
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
    Exercise 1.3.5, printed p. 11. The two determinants were recomputed: A is lower triangular
    with det A = 2(-1)3 = -6, so rank 3; and det B expands to 1(0*5+3) - 1(-10+1) + 2(-6) = 3 +
    9 - 12 = 0, with the minor on rows 1-2 and columns 1-2 equal to 2, so rank 2. Elementary row
    operations preserve rank, so the matrices are not row-equivalent. The step that asserted det
    B = 0 now carries the expansion; no other step changed.
---

::: {.exercise}
Prove that the following two matrices are not row-equivalent:

$$
\left[ \begin{array}{c c c} 2 & 0 & 0 \\ a & - 1 & 0 \\ b & c & 3 \end{array} \right], \qquad \left[ \begin{array}{c c c} 1 & 1 & 2 \\ - 2 & 0 & - 1 \\ 1 & 3 & 5 \end{array} \right].
$$
:::

::: {.solution}
Let
$$
A=\begin{bmatrix}2&0&0\\a&-1&0\\b&c&3\end{bmatrix},
\qquad
B=\begin{bmatrix}1&1&2\\-2&0&-1\\1&3&5\end{bmatrix}.
$$

::: pf

::: {.pf-step #a-has-rank-3}
The matrix $A$ has rank $3$.

::: pf-proof
$A$ is lower triangular and
$$
\det A=2(-1)3=-6\ne0.
$$
Hence $A$ is invertible and has rank $3$.
:::

:::

::: {.pf-step #b-has-rank-2}
The matrix $B$ has rank $2$.

::: pf-proof
Expanding along the first row,
$$
\det B=1\,(0\cdot5-(-1)\cdot3)-1\,((-2)\cdot5-(-1)\cdot1)+2\,((-2)\cdot3-0\cdot1)=3+9-12=0,
$$
so its rank is at most $2$. The minor formed by the first two rows and first two
columns is
$$
\det\begin{bmatrix}1&1\\-2&0\end{bmatrix}=2\ne0,
$$
so its rank is at least $2$.
:::

:::

::: pf-step
Therefore $A$ and $B$ are not row-equivalent.

::: pf-proof
Elementary row operations preserve rank, whereas steps [](#a-has-rank-3){.pf-ref} and [](#b-has-rank-2){.pf-ref} give different
ranks.
:::

:::

:::

:::
