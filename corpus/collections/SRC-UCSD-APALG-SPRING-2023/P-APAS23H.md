---
schema: qual/card@1
id: P-APAS23H
kind: problem
title: 'Invariant inner products for the unipotent $\mathbb{Z}$-representation on $\mathbb{C}^2$'
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
  - Inner Product Spaces
relations: []
review: draft
---

::: problem
Let $G = \mathbb{Z}$ be the group of integers under addition.
The group homomorphism $\rho \colon G \to \mathrm{GL}_2(\mathbb{C})$ given by
\[
\rho(n) = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}
\]
gives $\mathbb{C}^2$ the structure of a $G$-module.
Does $\mathbb{C}^2$ admit a $G$-invariant inner product?
:::

::: solution
No.

If such a $G$-invariant inner product existed, then the operator representing the generator $1\in\mathbb Z$,
\[
T=\rho(1)=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\]
would preserve that inner product. Thus $T$ would be unitary with respect to that positive-definite Hermitian form.

Every unitary operator on a finite-dimensional complex inner-product space is diagonalizable: after choosing an orthonormal basis, its matrix is unitary and hence normal, so the spectral theorem applies.

But $T$ is a nontrivial Jordan block. Its only eigenvalue is $1$, and
\[
T-I=\begin{pmatrix}0&1\\0&0\end{pmatrix}\ne0,
\qquad
(T-I)^2=0.
\]
Therefore its minimal polynomial is $(t-1)^2$, so $T$ is not diagonalizable. This contradiction shows that no $G$-invariant inner product exists.

Hence
\[
\boxed{\mathbb C^2\text{ admits no }\mathbb Z\text{-invariant inner product for this representation}.}
\]
:::
