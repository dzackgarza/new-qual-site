---
schema: qual/card@1
id: P-TRIV-LA03
kind: problem
title: Linear independence of $(1,2,3)$, $(1,3,5)$, $(5,13,15)$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find if the vectors ${ \left[ \begin{array} { l } { 1 } \\ { 2 } \\ { 3 } \end{array} \right] } , { \left[ \begin{array} { l } { 1 } \\ { 3 } \\ { 5 } \end{array} \right] } , { \left[ \begin{array} { l } { 5 } \\ { 1 3 } \\ { 1 5 } \end{array} \right] }$ are linear independent or not.
:::

::: {.solution}
Let
$$
M=
\begin{pmatrix}
1&1&5\\
2&3&13\\
3&5&15
\end{pmatrix},
$$
whose columns are the three given vectors.

<1>1. One has
$$
\det M=-6.
$$

::: {.proof}
Expanding along the first row,
$$
\begin{aligned}
\det M
&=(3\cdot15-13\cdot5)-(2\cdot15-13\cdot3)\\
&\qquad+5(2\cdot5-3\cdot3)\\
&=-20+9+5\\
&=-6.
\end{aligned}
$$
:::

<1>2. The matrix $M$ is invertible.

::: {.proof}
By step <1>1, $\det M\neq0$, so $M$ is invertible.
:::

<1>3. The three given vectors are linearly independent.

::: {.proof}
The columns of an invertible matrix are linearly independent. Since the given vectors are exactly the columns of $M$, step <1>2 proves the claim.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
