---
schema: qual/card@1
id: P-CDRT6
kind: problem
title: Diagonalizable does not imply distinct eigenvalues
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Eigenvalues and Eigenvectors
  - Counterexamples
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
- Does diagonalizable imply distinct eigenvalues?
:::


::: {.solution}
No. For example, the identity matrix
\[
I_2=\begin{pmatrix}1&0\\0&1\end{pmatrix}
\]
is already diagonal, hence diagonalizable, but it has only one eigenvalue, namely $1$, with algebraic multiplicity $2$.

More generally, a diagonalizable matrix may have repeated diagonal entries. Diagonalizability means that the vector space has a basis of eigenvectors; it does not require the corresponding eigenvalues to be distinct.
:::
