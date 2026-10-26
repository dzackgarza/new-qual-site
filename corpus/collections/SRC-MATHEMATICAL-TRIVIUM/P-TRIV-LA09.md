---
schema: qual/card@1
id: P-TRIV-LA09
kind: problem
title: Determinant of the all-ones matrix with zeros on the diagonal after the first entry
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate det A, if

$$
A = \left[ { \begin{array} { l l l l l } { 1 } & { 1 } & { 1 } & { \dots } & { 1 } \\ { 1 } & { 0 } & { 1 } & { \dots } & { 1 } \\ { 1 } & { 1 } & { 0 } & { \dots } & { 1 } \\ { \vdots } & { \vdots } & { \vdots } & { \ddots } & { \vdots } \\ { 1 } & { 1 } & { 1 } & { \dots } & { 0 } \end{array} } \right] .\tag{2}
$$
:::

Assume $A$ is $n\times n$.

::: pf

::: pf-step

For each
$$
i=2,\ldots,n,
$$
perform the row operation
$$
R_i\longleftarrow R_i-R_1.
$$


::: pf-proof

Adding a multiple of one row to another does not change the determinant.

:::

:::

::: pf-step

After the operations in step <1>1, the matrix becomes
$$
\begin{pmatrix}
1&1&1&\cdots&1\\
0&-1&0&\cdots&0\\
0&0&-1&\cdots&0\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
0&0&0&\cdots&-1
\end{pmatrix}.
$$


::: pf-proof

In row $i\geq2$, the first entry is
$$
1-1=0.
$$
At column $i$, the entry is
$$
0-1=-1.
$$
Every other entry in that row is
$$
1-1=0.
$$

:::

:::

::: pf-step

The transformed matrix has determinant
$$
1\cdot(-1)^{n-1}.
$$


::: pf-proof

The matrix in step <1>2 is upper triangular. The determinant of a triangular
matrix is the product of its diagonal entries.

:::

:::

::: pf-step

Therefore
$$
\boxed{\det A=(-1)^{n-1}}.
$$


::: pf-proof

The row operations in step <1>1 preserve the determinant, and step <1>3
computes the determinant of the resulting matrix.

:::

:::

::: pf-qed

Step <1>4 is the required value.

:::

:::
