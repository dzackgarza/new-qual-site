---
schema: qual/card@1
id: P-APA22B
kind: problem
title: Unitary maps have singular values $1$; Frobenius and operator norms force diagonalizability
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Norms
  - Diagonalization
relations: []
review: draft
---

::: problem
Let $V$ be a finite-dimensional inner product space and write $n = \dim V$.
For the purposes of this question, the definition of a linear map $\phi \colon V \to V$ being unitary is that $\phi$ is invertible and $\phi^{-1} = \phi^*$ (where $\phi^*$ is the adjoint of $\phi$).

(a) Let $\phi \colon V \to V$ be a linear map, and write $\sigma_1, \ldots, \sigma_n$ for its singular values.
Prove that $\phi \colon V \to V$ is unitary if and only if $\sigma_i = 1$ for all $1 \leq i \leq n$.

Now let $W = \mathbb{C}^{100}$, considered as an inner product space with its usual inner product (i.e., dot product).

(b) Suppose $\psi \colon W \to W$ is a linear map such that (a) $\|\psi\|_{\mathrm{Frob}} = 30$, and (b) $\|\psi\|_{\mathrm{op}} \leq 3$, where $\|\psi\|_{\mathrm{op}}$ denotes the operator norm with respect to the usual $\ell^2$-norm on $W$.
Using (a), or otherwise, prove that $\psi$ is diagonalizable.
:::


::: solution
(a) The singular values of $\phi$ are the square roots of the eigenvalues of the positive semidefinite operator $\phi^*\phi$.

If $\phi$ is unitary, then
\[
\phi^*\phi=\phi^{-1}\phi=I,
\]
so every eigenvalue of $\phi^*\phi$ is $1$, and hence every singular value of $\phi$ is $1$.

Conversely, if every singular value is $1$, then every eigenvalue of the Hermitian operator $\phi^*\phi$ is $1$. By the spectral theorem,
\[
\phi^*\phi=I.
\]
Thus $\phi$ is injective, hence invertible in finite dimension, and multiplying by $\phi^{-1}$ gives
\[
\phi^*=\phi^{-1}.
\]
Therefore $\phi$ is unitary.

(b) Let $\sigma_1,\ldots,\sigma_{100}$ be the singular values of $\psi$. The operator norm is the largest singular value, so
\[
0\le \sigma_i\le3
\qquad(1\le i\le100).
\]
On the other hand,
\[
\|\psi\|_{\mathrm{Frob}}^2=\sum_{i=1}^{100}\sigma_i^2=30^2=900.
\]
Since there are $100$ summands and each satisfies $\sigma_i^2\le9$, equality with $900=100\cdot9$ forces
\[
\sigma_1=\cdots=\sigma_{100}=3.
\]
Hence the singular values of $U:=\frac13\psi$ are all $1$. By part (a), $U$ is unitary. By the spectral theorem for unitary operators, there is a unitary matrix $Q$ such that $Q^*UQ$ is diagonal. Therefore
\[
Q^*\psi Q=3Q^*UQ
\]
is diagonal as well. Thus $\psi$ is diagonalizable.
:::
