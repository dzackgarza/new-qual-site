---
schema: qual/card@1
id: E-AMD-2MKY6V2W
kind: exercise
title: Does diagonalizable imply invertible? The converse?
classification:
  areas:
  - algebra
  topics:
  - diagonalization
  - matrices
  - counterexamples
relations: []
review: draft
solved: true
---

::: {.exercise}
Does diagonalizable imply invertible?
The converse?
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Neither property implies the other in general.

**(1) Does diagonalizable imply invertible? NO.**
- **Counterexample:** The zero matrix $A = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$ (or any projection matrix like $\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$) is already diagonal (hence diagonalizable), but has $\det(A) = 0$, so it is not invertible.
- A diagonalizable matrix is invertible if and only if all of its eigenvalues are non-zero.

**(2) Does invertible imply diagonalizable? NO.**
- **Counterexample:** Consider the non-zero shear / unipotent Jordan block:
  $$
  B = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}.
  $$
  - **Invertibility:** $\det(B) = 1 \cdot 1 - 1 \cdot 0 = 1 \neq 0$, so $B$ is invertible (with $B^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$).
  - **Non-diagonalizability:** The characteristic polynomial is $\operatorname{char}_B(\lambda) = (\lambda - 1)^2$, so the only eigenvalue is $\lambda = 1$ with algebraic multiplicity 2.
    The eigenspace is $\ker(B - I) = \ker \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} = \operatorname{span}\left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix} \right\}$, which has geometric multiplicity 1.
    Since the geometric multiplicity ($1$) is strictly less than the algebraic multiplicity ($2$), $B$ is not diagonalizable.
:::
