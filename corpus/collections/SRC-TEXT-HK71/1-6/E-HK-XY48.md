---
schema: qual/card@1
id: E-HK-XY48
kind: problem
title: Inverse of a $4 \times 4$ upper-triangular matrix
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
  note: Checked against Hoffman--Kunze Exercise 1.6.5.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}
Discover whether

$$
A = \left[ \begin{array}{c c c c} 1 & 2 & 3 & 4 \\ 0 & 2 & 3 & 4 \\ 0 & 0 & 3 & 4 \\ 0 & 0 & 0 & 4 \end{array} \right]
$$

is invertible, and find $A^{-1}$ if it exists.
:::


::: solution
All diagonal entries are nonzero, so $A$ is invertible. Direct multiplication verifies that
\[
A^{-1}=
\begin{bmatrix}
1&-1&0&0\\
0&\frac12&-\frac12&0\\
0&0&\frac13&-\frac13\\
0&0&0&\frac14
\end{bmatrix}.
\]
Indeed, multiplying $A$ by this matrix gives $I_4$: each diagonal product is $1$, while the successive superdiagonal cancellations are
\[
-1+2\cdot\frac12=0,
\qquad
2\left(-\frac12\right)+3\left(\frac13\right)=0,
\qquad
3\left(-\frac13\right)+4\left(\frac14\right)=0,
\]
and the remaining upper entries cancel similarly. Hence the displayed matrix is $A^{-1}$.
:::
