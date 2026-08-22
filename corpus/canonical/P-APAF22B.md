---
schema: qual/card@1
id: P-APAF22B
kind: problem
title: Schur eigenvalues versus singular values; equality implies normality
classification:
  areas:
  - applied-algebra
  topics:
  - Singular Values
  - Normal Operators
relations: []
review: draft
solved: false
---

::: problem
Let $V$ be a finite-dimensional complex inner product space of dimension $n$, and $\phi \colon V \to V$ a linear map. Suppose that $B$ is an orthonormal basis for $V$ such that the matrix
\[
A = \mathcal{M}(\phi, B, B)
=
\begin{pmatrix}
\lambda_1 & * & \cdots & * \\
0 & \lambda_2 & \cdots & * \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_n
\end{pmatrix}
\]
is upper-triangular, i.e., a Schur decomposition. Finally let $\sigma_1 \geq \cdots \geq \sigma_n$ denote the singular values of $\phi$, with multiplicity.

(a) By considering $\|\phi\|_{\mathrm{Frob}}$, or otherwise, prove that $\sum_{i=1}^{n} |\lambda_i|^2 \leq \sum_{i=1}^{n} \sigma_i^2$.

(b) Suppose now that $\sum_{i=1}^{n} |\lambda_i|^2 = \sum_{i=1}^{n} \sigma_i^2$. By considering $A$, or otherwise, prove that $\phi$ is normal.
:::
