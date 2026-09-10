---
schema: qual/card@1
id: P-MZIFW
kind: problem
title: Operators to which the spectral theorem for symmetric matrices generalizes
classification:
  areas:
  - algebra
  topics:
  - Diagonalization
  - Inner Product Spaces
  - Functional Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: openai-gpt-5.6-sol
  date: 2026-09-09
---

::: problem
To which classes of operators does the classical Spectral Theorem for real symmetric matrices generalize? State the key theorems.
:::

::: {.solution}
The finite-dimensional spectral theorem extends in several standard directions.

- Over $\mathbb C$, a matrix is unitarily diagonalizable iff it is normal. Hermitian matrices are the self-adjoint special case and have real eigenvalues.
- A compact self-adjoint operator on a Hilbert space has an orthonormal basis consisting of eigenvectors after adjoining a basis of its kernel; its nonzero eigenvalues are real, have finite multiplicity, and can accumulate only at $0$. The analogous statement holds for compact normal operators with complex eigenvalues.
- For a bounded self-adjoint operator $T$, there is a unique projection-valued spectral measure $E$ on $\sigma(T)\subset\mathbb R$ such that
\[
T=\int_{\sigma(T)}\lambda\,dE(\lambda).
\]
Equivalently, one obtains the continuous functional calculus $f\mapsto f(T)$; multiplication-operator models follow from the spectral theorem with the appropriate multiplicity data.
- Densely defined unbounded self-adjoint operators have the corresponding projection-valued-measure theorem, with the domain characterized by square-integrability of $\lambda$ against the spectral measure.

Thus the eigenbasis theorem for symmetric matrices becomes, in infinite dimensions, a spectral decomposition; only compact normal operators retain a purely discrete eigenvector description in general.
:::
