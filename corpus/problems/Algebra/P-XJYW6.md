---
schema: qual/card@1
id: P-XJYW6
kind: problem
title: Eigenspaces of commuting matrices
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Diagonalization
  - Matrices
relations: []
review: draft
---

::: problem
Let $A$ and $B$ be commuting linear operators on a finite-dimensional vector space. What can be said about their eigenspaces? When can they be simultaneously diagonalized?
:::

::: solution
Suppose
\[
AB=BA.
\]
Let $E_\lambda(A)=\ker(A-\lambda I)$ be an eigenspace of $A$. If $v\in E_\lambda(A)$, then
\[
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv.
\]
Hence
\[
B(E_\lambda(A))\subseteq E_\lambda(A).
\]
Thus every eigenspace of $A$ is $B$-invariant. By symmetry, every eigenspace of $B$ is $A$-invariant.

If, in addition, both $A$ and $B$ are diagonalizable over the base field, then they are simultaneously diagonalizable. Indeed,
\[
V=\bigoplus_\lambda E_\lambda(A),
\]
and each $E_\lambda(A)$ is $B$-invariant. The restriction of a diagonalizable operator to an invariant subspace is diagonalizable, so each $E_\lambda(A)$ has a basis of $B$-eigenvectors. Combining these bases gives a basis of simultaneous eigenvectors for $A$ and $B$.
:::
