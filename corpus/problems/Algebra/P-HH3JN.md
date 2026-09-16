---
schema: qual/card@1
id: P-HH3JN
kind: problem
title: Spectral theorem for real symmetric matrices
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Inner Product Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Prove that every real symmetric matrix $A \in M_n(\mathbb{R})$ has **real eigenvalues** and can be **orthogonally diagonalized**: there exists an orthogonal matrix $Q \in O(n)$ such that $Q^T A Q = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ (The Real Spectral Theorem).
:::

::: {.solution}
Let $A=A^T\in M_n(\mathbb R)$. Regard $A$ as a complex matrix. If $Av=\lambda v$ with $v\ne0$, then
\[
v^*Av=\lambda v^*v.
\]
Because $A^*=A$, the scalar $v^*Av$ is real:
\[
\overline{v^*Av}=v^*A^*v=v^*Av.
\]
Since $v^*v>0$, it follows that $\lambda=\overline\lambda$, hence every eigenvalue is real.

We prove orthogonal diagonalizability by induction on $n$. The case $n=1$ is immediate. For $n>1$, choose a unit eigenvector $u_1\in\mathbb R^n$ with $Au_1=\lambda_1u_1$. Let
\[
W=u_1^\perp.
\]
For $w\in W$,
\[
\langle Aw,u_1\rangle
=\langle w,A u_1\rangle
=\lambda_1\langle w,u_1\rangle=0,
\]
so $W$ is $A$-invariant. The restriction $A|_W$ is again symmetric. By induction, $W$ has an orthonormal basis $u_2,\dots,u_n$ of eigenvectors of $A$.

Thus $u_1,\dots,u_n$ is an orthonormal eigenbasis of $\mathbb R^n$. If
\[
Q=[u_1\ \cdots\ u_n],
\]
then $Q^TQ=I$ and
\[
Q^TAQ=\operatorname{diag}(\lambda_1,\dots,\lambda_n).
\]
Hence every real symmetric matrix has real eigenvalues and is orthogonally diagonalizable.
:::
