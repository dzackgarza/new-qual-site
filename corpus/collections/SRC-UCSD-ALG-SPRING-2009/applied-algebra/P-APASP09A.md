---
schema: qual/card@1
id: P-APASP09A
kind: problem
title: "Schur Decomposition Theorem and characterization of normal matrices"
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Proved Schur decomposition by induction on dimension and derived the spectral theorem for normal matrices by showing a normal upper-triangular matrix is diagonal.
---

::: problem
(a) State and prove the Schur Decomposition Theorem.

(b) Use Schur to prove that a square matrix $A$ has an orthonormal basis of eigenvectors if and only if $A^H A = AA^H$.
:::

::: {.solution}
**Part (a).**

<1>1. For every $A\in\mathbb C^{n\times n}$ there is a unitary matrix $Q$ such that
\[
Q^HAQ=T
\]
is upper triangular.
::: {.proof}
We argue by induction on $n$.
For $n=1$ the assertion is immediate.
Assume $n>1$.
Since the characteristic polynomial of $A$ splits over $\mathbb C$, choose an eigenvalue $\lambda$ and a unit eigenvector $q_1$ with
\[
Aq_1=\lambda q_1.
\]
Extend $q_1$ to an orthonormal basis $q_1,\ldots,q_n$ of $\mathbb C^n$, and let
\[
Q_1=(q_1\ \cdots\ q_n).
\]
Then $Q_1$ is unitary and, because the first column of $Q_1^HAQ_1$ is $\lambda e_1$, it has block form
\[
Q_1^HAQ_1=
\begin{pmatrix}
\lambda & *\\
0 & B
\end{pmatrix}
\]
for some $(n-1)\times(n-1)$ matrix $B$.
By the induction hypothesis there is a unitary $U$ such that $U^HBU$ is upper triangular.
Set
\[
Q=Q_1
\begin{pmatrix}
1&0\\0&U
\end{pmatrix}.
\]
Then $Q$ is unitary and
\[
Q^HAQ=
\begin{pmatrix}
\lambda & *\\
0 & U^HBU
\end{pmatrix}
\]
is upper triangular.
:::

<1>2. The diagonal entries of the Schur triangular matrix are the eigenvalues of $A$, counted with algebraic multiplicity.
::: {.proof}
Unitary similarity preserves the characteristic polynomial.
For an upper-triangular matrix $T$, the characteristic polynomial is
\[
\det(tI-T)=\prod_{j=1}^n(t-t_{jj}),
\]
so its diagonal entries are precisely its eigenvalues with multiplicity.
:::

Thus <1>1 and <1>2 are the Schur Decomposition Theorem.

**Part (b).**

<1>3. If $A$ has an orthonormal basis of eigenvectors, then $A$ is normal:
\[
A^HA=AA^H.
\]
::: {.proof}
Let $Q$ be the unitary matrix whose columns are an orthonormal eigenbasis.
Then
\[
Q^HAQ=D
\]
is diagonal, so
\[
A=QDQ^H,
\qquad
A^H=QD^HQ^H.
\]
Because diagonal matrices commute with their adjoints,
\[
A^HA=QD^HDQ^H=QDD^HQ^H=AA^H.
\]
:::

<1>4. Every normal upper-triangular complex matrix is diagonal.
::: {.proof}
Let $T=(t_{ij})$ be upper triangular and normal.
Comparing the $(1,1)$ entries of $TT^H$ and $T^HT$ gives
\[
\sum_{j=1}^n|t_{1j}|^2=|t_{11}|^2,
\]
because the first column of an upper-triangular matrix has only the entry $t_{11}$.
Hence
\[
t_{1j}=0\qquad(j>1).
\]
Thus
\[
T=
\begin{pmatrix}
t_{11}&0\\0&T_1
\end{pmatrix}.
\]
Normality of $T$ implies normality of $T_1$.
Induction on the size of the matrix now shows that $T_1$ is diagonal, hence so is $T$.
:::

<1>5. If $A$ is normal, then $A$ has an orthonormal basis of eigenvectors.
::: {.proof}
By Schur decomposition, choose a unitary $Q$ such that
\[
T=Q^HAQ
\]
is upper triangular.
Normality is preserved by unitary similarity, so $T$ is normal.
By <1>4, $T$ is diagonal.
Therefore
\[
A=QTQ^H
\]
is unitarily diagonalizable, and the columns of $Q$ form an orthonormal eigenbasis of $A$.
:::

<1>6. Consequently, a complex square matrix has an orthonormal basis of eigenvectors if and only if it is normal.
::: {.proof}
Combine <1>3 and <1>5.
:::
:::
