---
schema: qual/card@1
id: P-PRACT20-W4-13
kind: problem
title: Properties of the square of a real $2\times2$ matrix
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Matrices
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Let $A$ be a $2 \times 2$ real matrix.
Which of the following are necessarily true?

(a) All entries of $A^{2}$ are non-negative.

(b) The determinant of $A^{2}$ is non-negative.

(c) If $A$ has two distinct eigenvalues, then $A^{2}$ has two distinct eigenvalues.
:::

::: {.solution}
Only (b) is necessarily true.

(a) False:

$$
A=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\implies A^2=\begin{pmatrix}1&-2\\0&1\end{pmatrix},
$$

which has a negative entry.

(b) True, since the determinant is multiplicative:

$$
\det(A^2)=\det(A)^2\geq0.
$$

(c) False: $A=\begin{pmatrix}-1&0\\0&1\end{pmatrix}$ has the distinct eigenvalues $\pm1$, but $A^2=I$ has the single eigenvalue $1$.
:::
