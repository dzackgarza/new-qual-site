---
schema: qual/card@1
id: E-AMD-FAT34AQV
kind: problem
title: Diagonalizable versus distinct eigenvalues
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09

---

::: {.exercise}
Does diagonalizable imply distinct eigenvalues?
:::

::: {.solution}
No. For $n\ge2$, the identity matrix
\[
I_n
\]
is already diagonal, hence diagonalizable, but its characteristic polynomial is
\[
\chi_{I_n}(x)=(x-1)^n.
\]
Thus it has only the single eigenvalue $1$, with algebraic multiplicity $n$.

An $n\times n$ matrix with $n$ distinct eigenvalues is diagonalizable, since eigenvectors for distinct eigenvalues are linearly independent; $I_n$ shows that the converse fails.
:::
