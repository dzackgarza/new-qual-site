---
schema: qual/card@1
id: P-DRL6B
kind: problem
title: Diagonalizable iff the space is a direct sum of eigenspaces
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Linear Algebra
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
Let $V$ be a finite-dimensional vector space over a field $K$, and let $T: V \to V$ be a linear operator.
Show that $T$ is diagonalizable if and only if $V$ is the direct sum of its eigenspaces:
$$V = \bigoplus_{i=1}^k E_{\lambda_i}(T) = \bigoplus_{i=1}^k \ker(T - \lambda_i I)$$
where $\lambda_1, \dots, \lambda_k \in K$ are the distinct eigenvalues of $T$.
:::

::: {.solution}
For each eigenvalue $\lambda$ of $T$, write
\[
E_\lambda=\ker(T-\lambda I).
\]
Eigenspaces for distinct eigenvalues are linearly independent: if
\[
v_1+\cdots+v_r=0,\qquad v_i\in E_{\lambda_i},
\]
with the $\lambda_i$ distinct, then applying
\[
\prod_{j\ne i}(T-\lambda_jI)
\]
gives
\[
\left(\prod_{j\ne i}(\lambda_i-\lambda_j)\right)v_i=0,
\]
so $v_i=0$. Hence the sum of the eigenspaces is always direct.

If $T$ is diagonalizable, $V$ has a basis of eigenvectors. Every basis vector lies in one of the eigenspaces, so the eigenspaces span $V$. Therefore
\[
V=\bigoplus_\lambda E_\lambda.
\]

Conversely, suppose
\[
V=\bigoplus_\lambda E_\lambda.
\]
Choose a basis of each eigenspace and take their union. Because the sum is direct and equals $V$, this union is a basis of $V$, and every one of its vectors is an eigenvector of $T$. Thus the matrix of $T$ in this basis is diagonal, so $T$ is diagonalizable.

Equivalently,
\[
T\text{ is diagonalizable}
\iff
\sum_\lambda \dim E_\lambda=\dim V.
\]
:::
