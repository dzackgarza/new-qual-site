---
schema: qual/card@1
id: P-BKS03-1A
kind: problem
title: Scalar matrices characterized by universal eigenvectors
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $k$ be a field and $A\in M_n(k)$.
Prove that the following are equivalent:

(a) $A$ is a scalar multiple of the identity.

(b) Every nonzero vector in $k^n$ is an eigenvector of $A$.
:::

::: {.solution}
Obviously (a) implies (b). If (b) holds, then in particular, the standard basis vectors $e _ { j }$ are eigenvectors of A, so A is diagonal, say with entries $A _ { i i } = \lambda _ { i }$ . If $\lambda _ { i } \neq \lambda _ { j }$ , then $A ( e _ { i } + e _ { j } ) = \lambda _ { i } e _ { i } + \lambda _ { j } e _ { j }$ is not a scalar multiple of $e _ { i } + e _ { j }$ This contradicts the hypothesis that $e _ { i } + e _ { j }$ is an eigenvector of A. Hence the diagonal entries $\lambda _ { i }$ are all equal and we have (a).
:::
