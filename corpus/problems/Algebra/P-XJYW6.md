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

::: {.problem}
Let $A$ and $B$ be commuting linear operators on a finite-dimensional vector space. What can be said about their eigenspaces? When can they be simultaneously diagonalized?
:::

::: {.solution}
Suppose
$$
AB=BA.
$$
Let $E_\lambda(A)=\ker(A-\lambda I)$ be an eigenspace of $A$. If $v\in E_\lambda(A)$, then
$$
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv.
$$
Hence
$$
B(E_\lambda(A))\subseteq E_\lambda(A).
$$
Thus every eigenspace of $A$ is $B$-invariant. By symmetry, every eigenspace of $B$ is $A$-invariant.

Commuting $A$ and $B$ are simultaneously diagonalizable if and only if each is diagonalizable over the base field. A basis diagonalizing both diagonalizes each, which gives one direction. Conversely, suppose both are diagonalizable. Then
$$
V=\bigoplus_\lambda E_\lambda(A),
$$
and each $E_\lambda(A)$ is $B$-invariant. The minimal polynomial of $B|_{E_\lambda(A)}$ divides that of $B$, which is a product of distinct linear factors, so $B|_{E_\lambda(A)}$ is diagonalizable and each $E_\lambda(A)$ has a basis of $B$-eigenvectors. Combining these bases gives a basis of simultaneous eigenvectors for $A$ and $B$.
:::
