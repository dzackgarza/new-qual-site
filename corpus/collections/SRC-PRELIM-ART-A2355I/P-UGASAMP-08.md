---
schema: qual/card@1
id: P-UGASAMP-08
kind: problem
title: Diagonalization of $\begin{pmatrix}2&1\\1&2\end{pmatrix}$
classification:
  areas: [prelim]
  topics:
  - Diagonalization
  - Eigenvalues
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Diagonalize the matrix
$$
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
$$
:::

::: {.solution}

Let
$$
A=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
$$

::: pf

::: pf-step

The characteristic polynomial of $A$ is
$$
\chi_A(\lambda)=(\lambda-3)(\lambda-1).
$$


::: pf-proof

One has
$$
\det(A-\lambda I)
=
\det
\begin{pmatrix}
2-\lambda&1\\
1&2-\lambda
\end{pmatrix}
=(2-\lambda)^2-1.
$$
Factoring gives
$$
(2-\lambda)^2-1
=(1-\lambda)(3-\lambda)
=(\lambda-1)(\lambda-3).
$$

:::

:::

::: {.pf-step #s1-2}

An eigenvector for $\lambda=3$ is
$$
v_3=
\begin{pmatrix}
1\\
1
\end{pmatrix},
$$
and an eigenvector for $\lambda=1$ is
$$
v_1=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$


::: pf-proof

Direct multiplication gives
$$
A
\begin{pmatrix}
1\\
1
\end{pmatrix}
=
\begin{pmatrix}
3\\
3
\end{pmatrix}
=
3
\begin{pmatrix}
1\\
1
\end{pmatrix},
$$
and
$$
A
\begin{pmatrix}
1\\
-1
\end{pmatrix}
=
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
$$

:::

:::

::: pf-step

The matrix
$$
P=
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}
$$
is invertible, with
$$
P^{-1}
=
\frac12
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix}.
$$


::: pf-proof

The determinant is
$$
\det P=-2\ne0,
$$
so $P$ is invertible. Moreover
$$
P^2=
\begin{pmatrix}
2&0\\
0&2
\end{pmatrix}
=2I,
$$
which gives the displayed formula for $P^{-1}$.

:::

:::

::: {.pf-step #s1-4}

A diagonalization of $A$ is
$$
\boxed{
P^{-1}AP=
\begin{pmatrix}
3&0\\
0&1
\end{pmatrix}.}
$$


::: pf-proof

The columns of $P$ are the eigenvectors $v_3$ and $v_1$ from step [](#s1-2){.pf-ref}. Therefore
$$
AP
=
P
\begin{pmatrix}
3&0\\
0&1
\end{pmatrix}.
$$
Multiplying on the left by $P^{-1}$ yields the claimed diagonalization.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested diagonal form and change-of-basis matrix.

:::

:::

:::
