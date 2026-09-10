---
schema: qual/card@1
id: E-AMD-KCLZUB2B
kind: problem
title: A linear operator is diagonalizable iff $V$ is the direct sum of its eigenspaces
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
  date: 2026-08-29
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Reduced the equivalence to the eigenbasis/direct-sum argument.
---

::: {.exercise}
Show that a linear map $T:V\to V$ is diagonalizable if and only if
\[
V=\bigoplus_\lambda \ker(T-\lambda I),
\]
where the sum runs over the eigenvalues of $T$ in the base field.
:::

::: {.solution}
If $T$ is diagonalizable, choose a basis of eigenvectors and group the basis vectors according to their eigenvalues. The span of the vectors with eigenvalue $\lambda$ is exactly
\[
E_\lambda=\ker(T-\lambda I),
\]
and the basis partition shows
\[
V=\bigoplus_\lambda E_\lambda.
\]

Conversely, suppose
\[
V=\bigoplus_\lambda E_\lambda.
\]
Choose a basis of each eigenspace $E_\lambda$. The union of these bases is a basis of $V$, and every vector in it is an eigenvector of $T$. Hence the matrix of $T$ in this basis is diagonal.

Thus $T$ is diagonalizable exactly when $V$ is the direct sum of its eigenspaces.
:::
