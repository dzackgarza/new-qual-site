---
schema: qual/card@1
id: P-BKS00-6
kind: problem
title: Resolvents as low-degree polynomials in a matrix
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $A$ be an $n\times n$ complex matrix whose minimal polynomial $\mu$ has degree $k$.

1. If $\lambda\in\mathbb C$ is not an eigenvalue of $A$, prove that there is a polynomial $p_\lambda$ of degree at most $k-1$ such that
   \[
   p_\lambda(A)=(A-\lambda I)^{-1}.
   \]
2. Let $\lambda_1,\ldots,\lambda_k$ be distinct complex numbers, none of them an eigenvalue of $A$. Prove that there exist $c_1,\ldots,c_k\in\mathbb C$ such that
   \[
   \sum_{j=1}^k c_j(A-\lambda_jI)^{-1}=I.
   \]
:::
