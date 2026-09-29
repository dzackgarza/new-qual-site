---
schema: qual/card@1
id: P-APAS04A
kind: problem
title: 'Schur decomposition theorem'
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
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
State and prove the Schur Decomposition Theorem.
:::

::: {.solution}

::: pf

::: pf-step

**Schur Decomposition Theorem.** For every matrix $A\in M_n(\mathbb C)$, there exists a unitary matrix $U\in U(n)$ such that
\[
U^*AU=T
\]
is upper triangular. The diagonal entries of $T$ are the eigenvalues of $A$, counted with algebraic multiplicity.

::: pf-proof

We prove the triangularization statement by induction on $n$.

:::

:::

::: pf-step

The theorem holds for $n=1$.

::: pf-proof

Every $1\times1$ matrix is already upper triangular, and the identity matrix is unitary.

:::

:::

::: pf-step

Assume $n>1$. Since the characteristic polynomial of $A$ splits over $\mathbb C$, choose an eigenvalue $\lambda$ and a unit eigenvector $v_1$ such that
\[
Av_1=\lambda v_1.
\]
Extend $v_1$ to an orthonormal basis
\[
v_1,v_2,\ldots,v_n
\]
of $\mathbb C^n$, and let
\[
U_1=[v_1\ v_2\ \cdots\ v_n].
\]
Then $U_1$ is unitary and
\[
U_1^*AU_1=
\begin{pmatrix}
\lambda & *\\
0 & B
\end{pmatrix}
\]
for some $B\in M_{n-1}(\mathbb C)$.

::: pf-proof

The columns of $U_1$ form an orthonormal basis, so $U_1$ is unitary.
The first column of $U_1^*AU_1$ is the coordinate vector of $Av_1=\lambda v_1$ in this basis, namely
\[
(\lambda,0,\ldots,0)^T.
\]
Thus every entry below the $(1,1)$ entry in the first column is zero, giving the displayed block form.

:::

:::

::: {.pf-step #s4}

By the induction hypothesis, there exists a unitary matrix $W\in U(n-1)$ such that
\[
W^*BW=T_0
\]
is upper triangular.

::: pf-proof

The matrix $B$ is an arbitrary complex $(n-1)\times(n-1)$ matrix, so the induction hypothesis applies to it.

:::

:::

::: pf-step

Put
\[
D=
\begin{pmatrix}
1&0\\
0&W
\end{pmatrix}
\qquad\text{and}\qquad
U=U_1D.
\]
Then $U$ is unitary and
\[
U^*AU
=
\begin{pmatrix}
\lambda&*\\
0&T_0
\end{pmatrix},
\]
which is upper triangular.

::: pf-proof

Both $U_1$ and $D$ are unitary, hence so is their product $U$. Moreover
\[
U^*AU
=D^*U_1^*AU_1D
=
\begin{pmatrix}
1&0\\
0&W^*
\end{pmatrix}
\begin{pmatrix}
\lambda&*\\
0&B
\end{pmatrix}
\begin{pmatrix}
1&0\\
0&W
\end{pmatrix}
=
\begin{pmatrix}
\lambda&*\\
0&W^*BW
\end{pmatrix}.
\]
By step [](#s4){.pf-ref}, the lower-right block is upper triangular, so the whole matrix is upper triangular.

:::

:::

::: pf-step

The diagonal entries of $T=U^*AU$ are the eigenvalues of $A$, counted with algebraic multiplicity.

::: pf-proof

Because $T$ is similar to $A$, they have the same characteristic polynomial. Since $T$ is upper triangular,
\[
\det(tI-T)=\prod_{j=1}^n(t-t_{jj}).
\]
Thus the roots of the characteristic polynomial, with multiplicity, are exactly the diagonal entries $t_{11},\ldots,t_{nn}$.

:::

:::

:::

:::
