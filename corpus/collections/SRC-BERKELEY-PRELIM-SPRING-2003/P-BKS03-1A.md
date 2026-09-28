---
schema: qual/card@1
id: P-BKS03-1A
kind: problem
title: A matrix for which every nonzero vector is an eigenvector is scalar
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
Obviously (a) implies (b). If (b) holds, then in particular, the standard basis vectors $e_j$ are eigenvectors of $A$, so $A$ is diagonal, say with entries $A_{ii}=\lambda_i$. If $\lambda_i\neq\lambda_j$, then $A(e_i+e_j)=\lambda_ie_i+\lambda_je_j$ is not a scalar multiple of $e_i+e_j$. This contradicts the hypothesis that $e_i+e_j$ is an eigenvector of $A$. Hence the diagonal entries $\lambda_i$ are all equal and we have (a).
:::
