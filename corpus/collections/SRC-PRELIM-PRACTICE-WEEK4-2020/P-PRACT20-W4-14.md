---
schema: qual/card@1
id: P-PRACT20-W4-14
kind: problem
title: Eigenvalues and eigenvectors of the $3\times3$ matrix with zero diagonal and ones elsewhere
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
  - Eigenvalues and Eigenvectors
relations: []
review: draft
---

::: {.problem}
Find the eigenvalues and eigenvectors of $M=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$.
:::

::: {.solution}
We see

$$
\det(M-\lambda I)=\begin{vmatrix}-\lambda&1&1\\1&-\lambda&1\\1&1&-\lambda\end{vmatrix}=-\lambda(\lambda^2-1)-(-\lambda-1)+(1+\lambda),
$$

by cofactor expansion along the top row.
Factoring $1+\lambda$ from all terms:

$$
\det(M-\lambda I)=(1+\lambda)\bigl(-\lambda(\lambda-1)+2\bigr)=-(1+\lambda)^2(\lambda-2).
$$

Thus the eigenvalues are $\lambda_1=2$ with multiplicity 1 and $\lambda_2=-1$ with multiplicity 2. An eigenvector $v_1=(x,y,z)^t$ for $\lambda_1=2$ satisfies $(M-2I)v_1=0$:

$$
\begin{aligned}
-2x+y+z&=0,\\
x-2y+z&=0,\\
x+y-2z&=0.
\end{aligned}
$$

Each equation says that one coordinate equals the mean of the three, so $x=y=z$, and the eigenvectors for $\lambda_1=2$ are the nonzero multiples of $v_1=(1,1,1)^t$.

The eigenvectors $v=(x,y,z)^t$ for $\lambda_2=-1$ are the nonzero solutions of $(M+I)v=0$, that is, of $x+y+z=0$. They are the nonzero linear combinations of $v_2=(1,0,-1)^t$ and $v_3=(1,-1,0)^t$.
:::
