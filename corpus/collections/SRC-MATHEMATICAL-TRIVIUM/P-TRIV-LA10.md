---
schema: qual/card@1
id: P-TRIV-LA10
kind: problem
title: Eigenvalues and eigenvectors of the cyclic shift matrix
classification:
  areas: [prelim]
  topics:
  - Eigenvalues and Eigenvectors
  - Permutation Matrices
  - Roots of Unity
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 10, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Calculate the eigenvalues and the eigenvectors of the matrix

$$
A = \begin{bmatrix} 0 & 0 & 0 & \dots & 0 & 1 \\ 1 & 0 & 0 & \dots & 0 & 0 \\ 0 & 1 & 0 & \dots & 0 & 0 \\ \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & 0 & \dots & 1 & 0 \end{bmatrix}. \tag{3}
$$
:::

::: {.solution}

For
$$
v=
\begin{pmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{pmatrix},
$$
one has
$$
Av=
\begin{pmatrix}
x_n\\
x_1\\
x_2\\
\vdots\\
x_{n-1}
\end{pmatrix}.
$$

::: pf

::: {.pf-step #s1-1}

If $Av=\lambda v$ with $v\neq0$, then
$$
\lambda^n=1.
$$


::: pf-proof

The eigenvalue equation gives
$$
x_n=\lambda x_1
$$
and
$$
x_{j-1}=\lambda x_j,
\qquad
j=2,\ldots,n.
$$
Thus
$$
x_j=\lambda^{-(j-1)}x_1.
$$
Substituting $j=n$ into the first equation gives
$$
\lambda^{-(n-1)}x_1
=
\lambda x_1.
$$
An eigenvalue of the invertible shift matrix cannot be zero, and a nonzero
eigenvector must have $x_1\neq0$ by the recurrence. Hence
$$
\lambda^n=1.
$$

:::

:::

::: {.pf-step #s1-2}

The eigenvalues are
$$
\boxed{
\lambda_k
=
e^{2\pi i k/n},
\qquad
k=0,1,\ldots,n-1.
}
$$


::: pf-proof

Step [](#s1-1){.pf-ref} shows that every eigenvalue is an $n$th root of unity. Conversely,
for every $n$th root of unity the vector constructed in step [](#s1-3){.pf-ref} is a
nonzero eigenvector, so every such root occurs.

:::

:::

::: {.pf-step #s1-3}

For an eigenvalue $\lambda$ with $\lambda^n=1$, an eigenvector is
$$
\boxed{
v_\lambda
=
\begin{pmatrix}
1\\
\lambda^{-1}\\
\lambda^{-2}\\
\vdots\\
\lambda^{-(n-1)}
\end{pmatrix}.
}
$$


::: pf-proof

Applying $A$ gives
$$
Av_\lambda
=
\begin{pmatrix}
\lambda^{-(n-1)}\\
1\\
\lambda^{-1}\\
\vdots\\
\lambda^{-(n-2)}
\end{pmatrix}.
$$
Since $\lambda^n=1$,
$$
\lambda^{-(n-1)}=\lambda.
$$
Therefore
$$
Av_\lambda
=
\lambda v_\lambda.
$$

:::

:::

::: {.pf-step #s1-4}

For $\lambda_k=e^{2\pi i k/n}$, the corresponding eigenspace is
one-dimensional and is spanned by $v_{\lambda_k}$.


::: pf-proof

The recurrence in step [](#s1-1){.pf-ref} determines every coordinate of an eigenvector from
$x_1$. Hence every eigenvector for a fixed $\lambda_k$ is a scalar multiple of
$v_{\lambda_k}$.

:::

:::

::: pf-qed

Steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} give all eigenvalues and eigenvectors.

:::

:::

:::
