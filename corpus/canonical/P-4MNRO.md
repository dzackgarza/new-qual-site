---
schema: qual/card@1
id: P-4MNRO
kind: problem
title: Jordan form of $\begin{pmatrix}0&1&-2\\1&1&-3\\1&2&-4\end{pmatrix}$
classification:
  areas:
  - algebra
  topics:
  - jordan-canonical-form
  - eigenvalues-and-eigenvectors
  - matrices
relations: []
review: draft
solved: true
---

::: problem
Let

$$
A=\left[\begin{array}{lll}{0} & {1} & {-2} \\ {1} & {1} & {-3} \\ {1} & {2} & {-4}\end{array}\right] \in M_{3}(\mathbb{C})
$$

(a) Find the Jordan canonical form J of A.

(b) Find an invertible matrix $P$ such that $P\inv AP = J$.

> You should not need to compute $P\inv$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**(a) Characteristic polynomial and Jordan form:**

Compute $\det(\lambda I - A)$:
$$
\det\begin{pmatrix} \lambda & -1 & 2 \\ -1 & \lambda-1 & 3 \\ -1 & -2 & \lambda+4 \end{pmatrix}
= \lambda [(\lambda-1)(\lambda+4) + 6] + 1 [-(\lambda+4) + 3] + 2 [2 + (\lambda-1)]
$$
$$
= \lambda (\lambda^2 + 3\lambda + 2) + 1(-\lambda - 1) + 2(\lambda + 1)
= (\lambda+1) [\lambda(\lambda+2) - 1 + 2] = (\lambda+1)(\lambda^2 + 2\lambda + 1) = (\lambda+1)^3.
$$
Thus the only eigenvalue is $\lambda = -1$ with algebraic multiplicity 3.

Compute $A - (-1)I = A + I$:
$$
A + I = \begin{pmatrix} 1 & 1 & -2 \\ 1 & 2 & -3 \\ 1 & 2 & -3 \end{pmatrix}.
$$
Row-reducing $A+I$:
$$
\begin{pmatrix} 1 & 1 & -2 \\ 0 & 1 & -1 \\ 0 & 0 & 0 \end{pmatrix} \implies \rank(A+I) = 2.
$$
The geometric multiplicity of $\lambda = -1$ is $\nullity(A+I) = 3 - 2 = 1$.
Since there is only 1 Jordan block for $\lambda = -1$, the Jordan canonical form is a single $3 \times 3$ block:
$$
J = \begin{pmatrix} -1 & 1 & 0 \\ 0 & -1 & 1 \\ 0 & 0 & -1 \end{pmatrix}.
$$

**(b) Finding the change-of-basis matrix $P$:**

We seek a generalized eigenvector chain $(v_1, v_2, v_3)$ such that:
$$
(A+I)v_3 = v_2, \quad (A+I)v_2 = v_1, \quad (A+I)v_1 = 0 \quad (\text{with } v_1 \neq 0).
$$
Compute $(A+I)^2$:
$$
(A+I)^2 = \begin{pmatrix} 1 & 1 & -2 \\ 1 & 2 & -3 \\ 1 & 2 & -3 \end{pmatrix}\begin{pmatrix} 1 & 1 & -2 \\ 1 & 2 & -3 \\ 1 & 2 & -3 \end{pmatrix} = \begin{pmatrix} 0 & -1 & 1 \\ 0 & -1 & 1 \\ 0 & -1 & 1 \end{pmatrix}.
$$
We choose $v_3$ such that $(A+I)^2 v_3 \neq 0$.
Choose $v_3 = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.
Then:
$$
v_2 = (A+I)v_3 = \begin{pmatrix} -2 \\ -3 \\ -3 \end{pmatrix},
$$
$$
v_1 = (A+I)v_2 = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}.
$$
Check: $(A+I)v_1 = \begin{pmatrix} 1 & 1 & -2 \\ 1 & 2 & -3 \\ 1 & 2 & -3 \end{pmatrix} \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix}$.

Thus the columns of $P = [v_1 \mid v_2 \mid v_3]$ give:
$$
P = \begin{pmatrix} 1 & -2 & 0 \\ 1 & -3 & 0 \\ 1 & -3 & 1 \end{pmatrix}.
$$
Since $\det(P) = 1(-3) - (-2)(1) = -1 \neq 0$, $P$ is invertible and satisfies $P^{-1}AP = J$.
:::
