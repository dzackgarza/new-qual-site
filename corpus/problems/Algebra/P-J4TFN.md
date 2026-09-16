---
schema: qual/card@1
id: P-J4TFN
kind: problem
title: Eigenvalues of a linear map preserving a nondegenerate alternating form come
  in pairs $k,1/k$
classification:
  areas:
  - algebra
  topics:
  - Bilinear Forms
  - Eigenvalues and Eigenvectors
  - Matrix Groups
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
Let $V$ be a finite-dimensional vector space over a field $F$, and let $\omega: V \times V \to F$ be a **nondegenerate alternating bilinear form** on $V$.
Suppose $T: V \to V$ is a linear transformation that preserves $\omega$, i.e.
$$\omega(T(u), T(v)) = \omega(u, v) \quad \text{for all } u, v \in V.$$
Prove that if $\lambda \in F$ (or in an algebraic closure $\bar{F}$) is an eigenvalue of $T$, then $\lambda \ne 0$ and $\lambda^{-1} = 1/\lambda$ is also an eigenvalue of $T$ (with the same algebraic and geometric multiplicity).
:::

::: {.solution}
Choose a basis of $V$ and let $J$ be the matrix of $\omega$ and $M$ the matrix of $T$. Nondegeneracy of $\omega$ means that $J$ is invertible, and preservation of $\omega$ gives
\[
M^TJM=J.
\]
Hence $M$ is invertible, so $0$ is not an eigenvalue.

From the displayed identity,
\[
M^{-1}=J^{-1}M^TJ.
\]
Thus $M^{-1}$ is similar to $M^T$, and every matrix is similar to its transpose. Therefore
\[
M\sim M^{-1}.
\]

The eigenvalues of $M^{-1}$ are the reciprocals of the eigenvalues of $M$, with the same Jordan block sizes. Since $M$ and $M^{-1}$ are similar, the multiset of Jordan blocks of $M$ is invariant under
\[
\lambda\longmapsto\lambda^{-1}.
\]
Consequently, if $\lambda$ is an eigenvalue of $T$, then $\lambda\ne0$ and $\lambda^{-1}$ is also an eigenvalue, with the same algebraic multiplicity and the same geometric multiplicity.
:::
