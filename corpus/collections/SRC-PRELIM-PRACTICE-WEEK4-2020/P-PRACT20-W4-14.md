---
schema: qual/card@1
id: P-PRACT20-W4-14
kind: problem
title: Eigenvalues and eigenvectors of the $3\times3$ matrix with zero diagonal and ones elsewhere
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Find the eigenvalues and eigenvectors of $M = { \left( \begin{array} { l } { 0 \ 1 \ 1 } \\ { 1 \ 0 \ 1 } \\ { 1 \ 1 \ 0 } \end{array} \right) }$
:::

::: {.solution}
We see

$$
\operatorname* { d e t } ( M - \lambda I ) = { \left| \begin{array} { l l l } { - \lambda } & { 1 } & { 1 } \\ { 1 } & { - \lambda } & { 1 } \\ { 1 } & { 1 } & { - \lambda } \end{array} \right| } = - \lambda ( \lambda ^ { 2 } - 1 ) - ( - \lambda - 1 ) + ( 1 + \lambda )
$$

where we used co-factor expansion across the top row.
We can factor (1 + λ) from all terms:

$$
\operatorname * { d e t } ( M - \lambda I ) = ( 1 + \lambda ) ( - \lambda ( \lambda - 1 ) + 2 ) = - ( 1 + \lambda ) ^ { 2 } ( \lambda - 2 ) .
$$

Thus the eigenvalues are $\lambda _ { 1 } = 2$ with multiplicity 1 and $\lambda _ { 2 } = - 1$ with multiplicity 2. We look for an eigenvector $v _ { 1 } = ( x , y , z ) ^ { t }$ corresponding to $\lambda _ { 1 } = 2$ . We see $( M - 2 I ) v _ { 1 } = 0$ implies

$$
\begin{array} { r } { - 2 x + y + z = 0 } \\ { x - 2 y + z = 0 } \\ { x + y - 2 z = 0 . } \end{array}
$$

Adding 3x to the first equation, $3 y$ to the second and $3 z$ to the third shows that $x = y = z$ thus an eigenvector corresponding to $\lambda _ { 1 } = 2$ is a scalar multiple of $v _ { 1 } = ( 1 , 1 , 1 ) ^ { t }$ .

Eigenvectors $\boldsymbol { v } = ( x , y , z )$ corresponding to $\lambda _ { 2 } = - 1$ satisfy $x + y + z = 0$ . All such vectors are linear combinations of $v _ { 2 } = ( 1 , 0 , - 1 ) ^ { t }$ and $v _ { 3 } = ( 1 , - 1 , 0 ) ^ { t }$
:::
