---
schema: qual/card@1
id: E-HK-RTYK
kind: problem
title: Row-reducing a matrix over $\CC$
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
    Read as a second reader against the retained text; the statement matches Hoffman and
    Kunze Exercise 1.3.4, printed p. 11. The displayed R was verified by an independent
    route: the third row of A is -2i times the first minus the second, so A has rank 2;
    the null space of A is spanned by (1-i, 1, 1+i), which scaled by 1/(1+i) is (-i,
    (1-i)/2, 1), exactly the null vector of R; and R has leading 1s in columns 1 and 2,
    each the only nonzero entry of its column, with the zero row last, so it is row-
    reduced. No defect found; nothing was changed.
---

::: {.exercise}
Find a row-reduced matrix which is row-equivalent to

$$
A = \left[ \begin{array}{c c c} i & - (1 + i) & 0 \\ 1 & - 2 & 1 \\ 1 & 2 i & - 1 \end{array} \right].
$$
:::

::: {.solution}
A row-reduced matrix row-equivalent to $A$ is
$$
R=\begin{bmatrix}
1&0&i\\
0&1&\dfrac{-1+i}{2}\\
0&0&0
\end{bmatrix}.
$$

::: pf

::: pf-step
Row reduction of $A$ yields $R$.

::: pf-proof
Applying elementary row operations to
$$
A=\begin{bmatrix}
i&-(1+i)&0\\
1&-2&1\\
1&2i&-1
\end{bmatrix}
$$
gives the reduced row-echelon form
$$
\operatorname{rref}(A)
=\begin{bmatrix}
1&0&i\\
0&1&(-1+i)/2\\
0&0&0
\end{bmatrix}.
$$
Each step in Gaussian elimination is an elementary row operation, so this
matrix is row-equivalent to $A$.
:::

:::

::: pf-step
The displayed matrix is row-reduced.

::: pf-proof
Its two nonzero rows have leading entries $1$ in columns $1$ and $2$, each
pivot is the only nonzero entry in its column, the second pivot lies to the
right of the first, and the zero row is last.
:::

:::

:::

:::
