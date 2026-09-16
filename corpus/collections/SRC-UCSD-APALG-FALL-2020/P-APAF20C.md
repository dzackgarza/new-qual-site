---
schema: qual/card@1
id: P-APAF20C
kind: problem
title: Positive-definite square-root conjugation and diagonalizability of a product
classification:
  areas:
  - applied-algebra
  topics:
  - Positive Definite Matrices
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $V$ be a finite-dimensional inner product space and $\alpha,\beta\colon V\to V$ two positive definite self-adjoint linear maps.
We write $\alpha^{1/2}$ to denote the unique positive definite square-root of $\alpha$; you may assume without proof that this exists.

(a) Give an example to show that $\alpha\circ\beta\colon V\to V$ need not be a positive definite self-adjoint linear map.

(b) Prove that $\alpha^{1/2}\circ\beta\circ\alpha^{1/2}\colon V\to V$ is a positive definite self-adjoint linear map.

(c) Prove that $\alpha\circ\beta$ is diagonalizable and that all its eigenvalues are positive and real.

[Hint: use the previous part.]
:::

::: {.solution}
<1>1. The product of two positive definite self-adjoint maps need not be self-adjoint.
::: {.proof}
Take $V=\mathbb R^2$ with its standard inner product and
\[
\alpha=
\begin{pmatrix}
2&0\\
0&1
\end{pmatrix},
\qquad
\beta=
\begin{pmatrix}
2&1\\
1&2
\end{pmatrix}.
\]
Both matrices are symmetric. The eigenvalues of $\alpha$ are $2,1$, and the eigenvalues of $\beta$ are $3,1$, so both are positive definite.
However
\[
\alpha\beta=
\begin{pmatrix}
4&2\\
1&2
\end{pmatrix},
\]
which is not symmetric. Hence $\alpha\circ\beta$ need not be self-adjoint, and therefore need not be a positive definite self-adjoint map in the sense of the problem.
:::

<1>2. The map
\[
\gamma:=\alpha^{1/2}\beta\alpha^{1/2}
\]
is self-adjoint.
::: {.proof}
Because $\alpha^{1/2}$ and $\beta$ are self-adjoint,
\[
\gamma^*
=(\alpha^{1/2}\beta\alpha^{1/2})^*
=\alpha^{1/2}\beta\alpha^{1/2}
=\gamma.
\]
:::

<1>3. The map $\gamma$ is positive definite.
::: {.proof}
Let $0\ne v\in V$. Since $\alpha^{1/2}$ is positive definite, it is invertible, so
\[
w:=\alpha^{1/2}v\ne0.
\]
Then
\[
\langle\gamma v,v\rangle
=\langle\alpha^{1/2}\beta\alpha^{1/2}v,v\rangle
=\langle\beta w,w\rangle.
\]
Because $\beta$ is positive definite and $w\ne0$, the last quantity is positive. Hence $\gamma$ is positive definite.
:::

<1>4. The maps $\alpha\beta$ and $\gamma$ are similar:
\[
\alpha\beta
=\alpha^{1/2}\gamma\alpha^{-1/2}.
\]
::: {.proof}
Since $\alpha^{1/2}$ is invertible,
\[
\alpha^{1/2}\gamma\alpha^{-1/2}
=\alpha^{1/2}(\alpha^{1/2}\beta\alpha^{1/2})\alpha^{-1/2}
=\alpha\beta.
\]
:::

<1>5. Therefore $\alpha\beta$ is diagonalizable and all of its eigenvalues are positive real numbers.
::: {.proof}
By <1>2 and <1>3, $\gamma$ is positive definite and self-adjoint. The spectral theorem therefore gives an orthonormal eigenbasis for $\gamma$, and every eigenvalue $\lambda$ of $\gamma$ satisfies
\[
\lambda\|v\|^2=\langle\gamma v,v\rangle>0
\]
for a corresponding nonzero eigenvector $v$. Thus every eigenvalue of $\gamma$ is real and positive, and $\gamma$ is diagonalizable.

By <1>4, $\alpha\beta$ is similar to $\gamma$. Similar matrices have the same eigenvalues and diagonalizability. Hence $\alpha\beta$ is diagonalizable and all of its eigenvalues are positive real numbers.
:::
:::
