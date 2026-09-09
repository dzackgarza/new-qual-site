---
schema: qual/card@1
id: P-Q6PDD
kind: problem
title: Eigenvalues of a Hermitian matrix are real, and $A=PDP^{-1}$ with orthogonal columns
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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
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
<1>1. Every eigenvalue of a Hermitian matrix is real.
::: {.proof}
Let $Av=\lambda v$ with $v\ne0$. Since $A=A^*$,
\[
\lambda\langle v,v\rangle
=\langle Av,v\rangle
=\langle v,Av\rangle
=\overline\lambda\langle v,v\rangle.
\]
Because $\langle v,v\rangle>0$, one has $\lambda=\overline\lambda$, so $\lambda\in\mathbb R$.
:::

<1>2. If $v$ is an eigenvector with eigenvalue $\lambda$, then $v^\perp$ is $A$-invariant.
::: {.proof}
For $w\in v^\perp$,
\[
\langle Aw,v\rangle
=\langle w,A^*v\rangle
=\langle w,Av\rangle
=\lambda\langle w,v\rangle
=0.
\]
Hence $Aw\in v^\perp$.
:::

<1>3. Every Hermitian matrix admits an orthonormal basis of eigenvectors.
::: {.proof}
We argue by induction on the dimension. The result is trivial in dimension $1$. Over $\mathbb C$, the characteristic polynomial has a root, so $A$ has an eigenvector $v$; normalize it to have norm $1$. By <1>1 its eigenvalue is real. By <1>2, the orthogonal complement $v^\perp$ is $A$-invariant, and the restriction of $A$ to $v^\perp$ is again Hermitian. By induction, $v^\perp$ has an orthonormal basis of eigenvectors. Together with $v$, this gives an orthonormal eigenbasis of the whole space.
:::

<1>4. Let $v_1,\dots,v_n$ be such an orthonormal eigenbasis with eigenvalues $\lambda_1,\dots,\lambda_n\in\mathbb R$. Put
\[
P=[v_1\ \cdots\ v_n],
\qquad
D=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
\]
Then $P$ is invertible with orthogonal columns and
\[
A=PDP^{-1}.
\]
::: {.proof}
The columns form a basis, so $P$ is invertible; in fact $P$ is unitary because the columns are orthonormal. The eigenvector equations $Av_i=\lambda_i v_i$ combine to
\[
AP=PD,
\]
which is equivalent to $A=PDP^{-1}$.
:::
:::
