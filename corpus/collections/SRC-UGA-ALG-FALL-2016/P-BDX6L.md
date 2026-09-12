---
schema: qual/card@1
id: P-BDX6L
kind: problem
title: Commuting diagonalizable matrices are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-11
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-11
---

::: problem
Let $A, B$ be two $n\times n$ matrices with the property that $AB = BA$.
Suppose that $A$ and $B$ are diagonalizable.
Prove that $A$ and $B$ are *simultaneously* diagonalizable.
:::

::: {.solution}
<1>1. Let
\[
V=\mathbb C^n=\bigoplus_{\lambda}E_\lambda(A)
\]
be the eigenspace decomposition for $A$.
Each eigenspace $E_\lambda(A)$ is invariant under $B$.
::: {.proof}
Because $A$ is diagonalizable, the direct-sum decomposition by eigenspaces holds.
If $v\in E_\lambda(A)$, then
\[
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv,
\]
using $AB=BA$. Hence $Bv\in E_\lambda(A)$.
:::

<1>2. For every eigenvalue $\lambda$ of $A$, the restriction
\[
B_\lambda:=B|_{E_\lambda(A)}
\]
is diagonalizable.
::: {.proof}
Since $B$ is diagonalizable over $\mathbb C$, its minimal polynomial is a product of distinct linear factors:
\[
\mu_B(t)=\prod_{j=1}^r(t-\beta_j).
\]
Because $E_\lambda(A)$ is $B$-invariant, the restriction $B_\lambda$ is well-defined, and every polynomial annihilating $B$ also annihilates $B_\lambda$. Hence
\[
\mu_{B_\lambda}(t)\mid \mu_B(t).
\]
Therefore $\mu_{B_\lambda}$ also has no repeated root, so $B_\lambda$ is diagonalizable.
:::

<1>3. Each eigenspace $E_\lambda(A)$ has a basis consisting of common eigenvectors of $A$ and $B$.
::: {.proof}
By <1>2, choose a basis of $E_\lambda(A)$ consisting of eigenvectors of $B_\lambda$.
Every vector in this basis is automatically an eigenvector of $A$ with eigenvalue $\lambda$, since it lies in $E_\lambda(A)$. Thus every basis vector is an eigenvector for both matrices.
:::

<1>4. Taking the union of these bases over all eigenvalues $\lambda$ gives a basis of $\mathbb C^n$ in which both $A$ and $B$ are diagonal.
::: {.proof}
The eigenspaces of $A$ form the direct sum
\[
\mathbb C^n=\bigoplus_\lambda E_\lambda(A).
\]
Therefore the union of the bases from <1>3 is a basis of $\mathbb C^n$.
Each basis vector is a common eigenvector, so the matrices of both $A$ and $B$ in this basis are diagonal.
Hence $A$ and $B$ are simultaneously diagonalizable.
:::
:::
