---
schema: qual/card@1
id: P-APA17B
kind: problem
title: Simultaneous orthogonal diagonalization of commuting real symmetric matrices
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Diagonalization
relations: []
review: draft
---

::: problem
Let $A, B \in \mathbb{R}^{n \times n}$ be two real symmetric matrices.
If $AB = BA$, show that there exists an orthogonal matrix $Q \in \mathbb{R}^{n \times n}$ such that $Q^T AQ$ and $Q^T BQ$ are both diagonal.
:::

::: solution
Because \(A\) is real symmetric, the spectral theorem gives an orthogonal decomposition
\[
\mathbb R^n=\bigoplus_{\lambda}E_\lambda,
\qquad
E_\lambda=\ker(A-\lambda I),
\]
into eigenspaces of \(A\).

Since \(AB=BA\), every eigenspace \(E_\lambda\) is invariant under \(B\). Indeed, if \(v\in E_\lambda\), then
\[
A(Bv)=B(Av)=B(\lambda v)=\lambda Bv,
\]
so \(Bv\in E_\lambda\).

The restriction
\[
B|_{E_\lambda}:E_\lambda\to E_\lambda
\]
is again symmetric with respect to the Euclidean inner product, because for \(u,v\in E_\lambda\),
\[
\langle B u,v\rangle=\langle u,Bv\rangle.
\]
Hence the spectral theorem applied on each \(E_\lambda\) gives an orthonormal basis of \(E_\lambda\) consisting of eigenvectors of \(B\).

Taking the union of these orthonormal bases over all eigenvalues \(\lambda\) gives an orthonormal basis of \(\mathbb R^n\) consisting of vectors that are simultaneously eigenvectors of both \(A\) and \(B\). Let \(Q\) be the orthogonal matrix whose columns are these common eigenvectors. Then both
\[
Q^TAQ
\quad\text{and}\quad
Q^TBQ
\]
are diagonal.
:::
