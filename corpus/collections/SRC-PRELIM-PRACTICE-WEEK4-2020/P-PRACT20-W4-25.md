---
schema: qual/card@1
id: P-PRACT20-W4-25
kind: problem
title: Maximum number of ones in an invertible $0$--$1$ matrix
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Matrices
  - Determinants
relations: []
review: draft
---

::: {.problem}
Consider an $n \times n$ matrix in which each entry is either zero or one.
If the matrix is invertible, what is the maximum amount of ones in the matrix?
:::

::: {.solution}
The maximum amount of ones in the matrix is $n ^ { 2 } - n + 1$ . Indeed, we can think of starting with a matrix full of ones and removing entries and replacing them with zero.
If we have removed less than $n - 1$ entries, then two columns have remained untouched, meaning there are still two columns full of ones and the matrix is singular since its columns are linearly dependent.
Thus there can be a most $n ^ { 2 } - n + 1$ ones.

Now we exhibit a matrix that actually has this number of ones.
Define $A \in \mathbb { R } ^ { n \times n }$ by

$$
A = \left( \begin{array} { l l l l l l l } { 1 } & { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 0 } & { 1 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { 1 } & { 0 } & { 1 } & { 1 } & { \cdots } & { 1 } \\ { \vdots } & { \ddots } & { \ddots } & { \ddots } & & { \vdots } \\ & & { \ddots } & { \ddots } & { \ddots } & { \vdots } \\ { 1 } & { 1 } & { \cdots } & { 1 } & { 0 } & { 1 } \end{array} \right) .
$$

That is, A is full of ones except the first subdiagonal is zero.
Then A has $n ^ { 2 } - n + 1$ ones and A is invertible.
Indeed, if

$$
A x = 0
$$

then

$$
\begin{array} { c } { { x _ { 1 } + x _ { 2 } + \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad x _ { 2 } + \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad x _ { 1 } + \qquad \cdots + x _ { n - 1 } + x _ { n } = 0 , } } \\ { { \qquad \vdots } } \\ { { \qquad x _ { 1 } + x _ { 2 } + \cdots \qquad \quad + x _ { n } = 0 . } } \end{array}
$$

Subtracting the second equation from the first gives $x _ { 1 } = 0$ . Then subtracting the third from the first gives $x _ { 2 } = 0$ . Continuing this procedure, subtracting the $k ^ { \mathrm { t h } }$ equation from the first will give $x _ { k } = 0$ until the last equation simply reads $x _ { n } = 0$ . Thus $x = 0$ is the only solution to $A x = 0$ and so A is invertible.
(One can also show by induction on the dimension n that det $( A ) = 1$ , though this is a bit tricky).
:::
