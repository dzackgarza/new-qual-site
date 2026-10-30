---
schema: qual/card@1
id: P-BKS07-2A
kind: problem
title: Jordan form and Jordan basis of a $3\times 3$ matrix with eigenvalues $-1,1,1$
classification:
  areas: [prelim]
  topics:
  - Linear Algebra
relations: []
review: draft
---

::: {.problem}
Find a matrix $U$ such that $U^{-1} A U = J$ is in Jordan canonical form, where
$$
A = \begin{pmatrix} 0 & -3 & 5 \\ -1 & -6 & 11 \\ 0 & -4 & 7 \end{pmatrix}.
$$
:::

::: {.solution}

One answer is
$$
U=\begin{pmatrix}1&1&1\\2&3&1\\1&2&1\end{pmatrix},
\qquad
J=\begin{pmatrix}-1&0&0\\0&1&1\\0&0&1\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1}

The characteristic polynomial of $A$ is $\det(\lambda I-A)=(\lambda-1)^2(\lambda+1)$.

::: pf-proof

Expanding $\det(A-\lambda I)$ along the first column gives
$$
-\lambda\bigl((-6-\lambda)(7-\lambda)+44\bigr)+\bigl(-3(7-\lambda)+20\bigr)=-\lambda^3+\lambda^2+\lambda-1,
$$
which is $-(\lambda-1)^2(\lambda+1)$.

:::

:::

::: {.pf-step #s2}

Let $u_1=(1,2,1)^T$, $u_2=(1,3,2)^T$ and $u_3=(1,1,1)^T$. Then $Au_1=-u_1$, $Au_2=u_2$ and $Au_3=u_3+u_2$.

::: pf-proof

Direct multiplication gives $Au_1=(-1,-2,-1)^T$, $Au_2=(1,3,2)^T$ and $Au_3=(2,4,3)^T$.

:::

:::

::: {.pf-step #s3}

The matrix $U$ with columns $u_1,u_2,u_3$ is invertible.

::: pf-proof

Expanding along the first row, $\det U=1\cdot(3-2)-1\cdot(2-1)+1\cdot(4-3)=1$.

:::

:::

::: pf-qed

By step [](#s2){.pf-ref}, $AU=UJ$, and by step [](#s3){.pf-ref}, $U^{-1}AU=J$. The matrix $J$ is in Jordan canonical form, with a block of size $1$ for $-1$ and a block of size $2$ for $1$, in agreement with step [](#s1){.pf-ref}.

:::

:::

:::
