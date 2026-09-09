---
schema: qual/card@1
id: P-Q6PDD
kind: problem
title: Eigenvalues of a Hermitian matrix are real, and $A=PDP^{-1}$ with orthogonal
  columns
classification:
  areas:
  - algebra
  topics:
  - Eigenvalues and Eigenvectors
  - Inner Product Spaces
  - Diagonalization
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Show that the eigenvalues of a Hermitian matrix $A$ are real and that $A = PDP\inv$ where $P$ is an invertible matrix with orthogonal columns.
:::


::: {.solution}
<1>1. Every eigenvalue of \(A\) is real.
::: {.proof}
Let \(Av=\lambda v\) with \(v\neq0\). Since \(A\) is Hermitian,
\[
\langle Av,v\rangle=\langle v,Av\rangle.
\]
The left side is \(\lambda\langle v,v\rangle\), while the right side is \(\overline{\lambda}\langle v,v\rangle\). Since \(\langle v,v\rangle>0\), one gets \(\lambda=\overline{\lambda}\), so \(\lambda\in\mathbb R\).
:::

<1>2. If \(v\) and \(w\) are eigenvectors for distinct eigenvalues \(\lambda\neq\mu\), then \(v\perp w\).
::: {.proof}
By Hermitian symmetry,
\[
\lambda\langle v,w\rangle
=\langle Av,w\rangle
=\langle v,Aw\rangle
=\mu\langle v,w\rangle,
\]
where \(\lambda,\mu\in\mathbb R\) by <1>1. Thus \((\lambda-\mu)\langle v,w\rangle=0\), and \(\langle v,w\rangle=0\).
:::

<1>3. The space \(\mathbb C^n\) has an orthogonal basis of eigenvectors of \(A\).
::: {.proof}
Proceed by induction on \(n\). The case \(n=1\) is immediate. Since the characteristic polynomial splits over \(\mathbb C\), choose an eigenvector \(v\neq0\) with eigenvalue \(\lambda\). Let
\[
W=v^\perp.
\]
For \(w\in W\),
\[
\langle Aw,v\rangle=\langle w,Av\rangle
=\lambda\langle w,v\rangle=0,
\]
so \(Aw\in W\). Hence \(W\) is \(A\)-invariant, and the restriction \(A|_W\) is again Hermitian. By induction, \(W\) has an orthogonal basis of eigenvectors of \(A|_W\). Adjoining \(v\) gives an orthogonal eigenbasis of \(\mathbb C^n\).
:::

<1>4. If \(P\) is the matrix whose columns are the orthogonal eigenbasis from <1>3, and \(D\) is the diagonal matrix of the corresponding eigenvalues, then
\[
A=PDP^{-1}.
\]
::: {.proof}
The eigenvector equations for the columns of \(P\) are exactly
\[
AP=PD.
\]
Since the columns form a basis, \(P\) is invertible, and right-multiplication by \(P^{-1}\) gives \(A=PDP^{-1}\). If the eigenvectors are normalized, \(P\) is unitary and \(P^{-1}=P^*\).
:::
:::
