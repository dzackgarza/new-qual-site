---
schema: qual/card@1
id: P-PRACT20-W4-16
kind: problem
title: "Week 4: Differential Equations & Linear Algebra, problem 16"
classification:
  areas:
  - applied-algebra
  topics: []
relations: []
review: draft
---

::: {.problem}
Find the rank of the $n \times n$ matrix with entries which simply count up from 1 to $n ^ { 2 }$ in increasing order.
For example, if $n = 3$ , we are considering the matrix $\left( \begin{array} { l l l } { 1 } & { \hat { 2 } } & { 3 } \\ { 4 } & { 5 } & { 6 } \\ { 7 } & { 8 } & { 9 } \end{array} \right)$
:::

::: {.solution}
Call the matrix A. Then the $i , j$ entry of A is given by $A _ { i , j } = ( i - 1 ) n + j$ for $i , j = 1 , \ldots , n$ Now fixing $i > 2$ , we have

$$
\begin{array} { r l } & { A _ { i , j } = ( i - 1 ) n + j } \\ & { \quad \quad = ( i - 1 ) n + ( ( i - 1 ) - ( i - 2 ) ) j } \\ & { \quad \quad = ( i - 1 ) ( n + j ) - ( i - 2 ) j } \\ & { \quad \quad = ( i - 1 ) A _ { 2 , j } - ( i - 2 ) A _ { 1 , j } , \quad \mathrm { ~ f o r ~ a l l ~ } j = 1 , \dots , n . } \end{array}
$$

This shows that any row $A _ { i }$ for $i > 2$ can be written as a linear combination of the first two rows.
The first two rows are linearly independent, so the matrix has rank 2 regardless of n. [Note: to see that the first two rows are linearly independent, you can consider the principle $2 \times 2$ submatrix: $\left( { \begin{array} { c } { 1 } \\ { n { + } 1 } \end{array} } { \begin{array} { c } { 2 } \\ { n { + } 2 } \end{array} } \right)$ . This matrix has determinant −n and is this invertible.]
:::
