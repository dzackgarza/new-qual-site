---
schema: qual/card@1
id: P-UGAP09F-07
kind: problem
title: Diagonalize a $2\times2$ Hermitian complex matrix
classification:
  areas: [prelim]
  topics:
  - Diagonalization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let
$$
A=\begin{pmatrix}
2&1+i\\
1-i&3
\end{pmatrix}.
$$
Find an invertible complex matrix $P$ for which $P^{-1}AP$ is diagonal.
:::

::: {.solution}

::: pf

::: pf-step

The eigenvalues of $A$ are $1$ and $4$.


::: pf-proof

The characteristic polynomial is
$$
\begin{aligned}
\det(A-\lambda I)
&=(2-\lambda)(3-\lambda)-(1+i)(1-i)\\
&=(2-\lambda)(3-\lambda)-2\\
&=\lambda^2-5\lambda+4\\
&=(\lambda-1)(\lambda-4).
\end{aligned}
$$
Thus the eigenvalues are $1$ and $4$.

:::

:::

::: {.pf-step #s1-2}

Eigenvectors for the eigenvalues $1$ and $4$ are respectively
$$
v_1=\begin{pmatrix}-(1+i)\\1\end{pmatrix},
\qquad
v_4=\begin{pmatrix}1\\1-i\end{pmatrix}.
$$


::: pf-proof

For $\lambda=1$, the equation $(A-I)v=0$ includes
$$
x+(1+i)y=0,
$$
so $y=1$ gives $v_1$. For $\lambda=4$, the equation $(A-4I)v=0$ includes
$$
-2x+(1+i)y=0.
$$
Taking $y=1-i$ gives $(1+i)(1-i)=2$, hence $x=1$, which gives $v_4$.

:::

:::

::: {.pf-step #s1-3}

The matrix
$$
\boxed{
P=\begin{pmatrix}
-(1+i)&1\\
1&1-i
\end{pmatrix}
}
$$
is invertible and satisfies
$$
\boxed{P^{-1}AP=\begin{pmatrix}1&0\\0&4\end{pmatrix}}.
$$


::: pf-proof

The columns of $P$ are the eigenvectors from step [](#s1-2){.pf-ref}, so
$$
AP=P\begin{pmatrix}1&0\\0&4\end{pmatrix}.
$$
Moreover,
$$
\det P=(-(1+i))(1-i)-1=-2-1=-3\ne0,
$$
so $P$ is invertible. Multiplying the displayed relation on the left by $P^{-1}$ gives the claimed diagonalization.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} provides the required invertible matrix and diagonal form.

:::

:::

:::
