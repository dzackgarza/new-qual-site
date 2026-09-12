---
schema: qual/card@1
id: E-AMD-HO6G56UF
kind: problem
title: Commuting diagonalizable matrices are simultaneously diagonalizable
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Matrices
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $A,B$ are diagonalizable and $[A, B] = 0$, then $A$ and $B$ are simultaneously diagonalizable.
:::

::: {.solution}
Let
\[
V=\bigoplus_\lambda E_A(\lambda)
\]
be the eigenspace decomposition for the diagonalizable operator $A$.

Because $AB=BA$, each $A$-eigenspace is $B$-stable: if $v\in E_A(\lambda)$, then
\[
A(Bv)=B(Av)=\lambda Bv.
\]
Thus $B$ restricts to an operator on every $E_A(\lambda)$.

Since $B$ is diagonalizable, its minimal polynomial splits into distinct linear factors. The minimal polynomial of each restriction $B|_{E_A(\lambda)}$ divides the minimal polynomial of $B$, hence also splits into distinct linear factors. Therefore each restriction is diagonalizable.

Choose a basis of $B$-eigenvectors inside each $E_A(\lambda)$. The union of these bases is a basis of $V$ consisting of common eigenvectors of $A$ and $B$. Hence $A$ and $B$ are simultaneously diagonalizable.
:::
