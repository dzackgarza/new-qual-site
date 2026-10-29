---
schema: qual/card@1
id: P-J4TFN
kind: problem
title: Eigenvalues of a linear map preserving a nondegenerate alternating form are
  closed under inversion
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
Let $V$ be a finite-dimensional vector space over a field $F$, and let $\omega: V \times V \to F$ be a nondegenerate alternating bilinear form on $V$.
Suppose $T: V \to V$ is a linear transformation that preserves $\omega$, i.e.
$$\omega(T(u), T(v)) = \omega(u, v) \quad \text{for all } u, v \in V.$$
Prove that if $\lambda \in F$ (or in an algebraic closure $\bar{F}$) is an eigenvalue of $T$, then $\lambda \ne 0$ and $\lambda^{-1} = 1/\lambda$ is also an eigenvalue of $T$ (with the same algebraic and geometric multiplicity).
:::

::: {.solution}
Choose a basis of $V$, and let $J$ and $M$ be the matrices of $\omega$ and $T$.

::: pf

::: {.pf-step #invertible}

$M^TJM=J$, $J$ and $M$ are invertible, and $0$ is not an eigenvalue of $T$.

::: pf-proof

Nondegeneracy of $\omega$ means that $J$ is invertible, and preservation of $\omega$ is the identity $M^TJM=J$. Taking determinants, $\det(M)^2\det J=\det J\ne0$, so $\det M\ne0$.

:::

:::

::: {.pf-step #similar}

$M$ is similar to $M^{-1}$.

::: pf-proof

By step [](#invertible){.pf-ref}, $M^{-1}=J^{-1}M^TJ$, so $M^{-1}$ is similar to $M^T$, and every square matrix is similar to its transpose.

:::

:::

::: pf-step

If $\lambda$ is an eigenvalue of $T$, then $\lambda\ne0$ and $\lambda^{-1}$ is an eigenvalue of $T$ with the same algebraic and geometric multiplicity.

::: pf-proof

Over $\bar F$, the Jordan form of $M^{-1}$ is obtained from that of $M$ by replacing each block $J_k(\lambda)$ with a block $J_k(\lambda^{-1})$, since $J_k(\lambda)^{-1}$ has the single eigenvalue $\lambda^{-1}$ and a one-dimensional eigenspace. By step [](#similar){.pf-ref}, $M$ and $M^{-1}$ have the same Jordan form, so the blocks of $M$ for $\lambda$ and for $\lambda^{-1}$ have the same sizes. The algebraic multiplicity is the sum of these sizes and the geometric multiplicity is their number.

:::

:::

:::

:::
