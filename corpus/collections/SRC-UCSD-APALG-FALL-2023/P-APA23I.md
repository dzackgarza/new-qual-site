---
schema: qual/card@1
id: P-APA23I
kind: problem
title: Trace of exterior powers of a normal operator and characteristic polynomial coefficients
classification:
  areas:
  - applied-algebra
  topics:
  - Linear Algebra
  - Multilinear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the exterior-power trace and characteristic-polynomial coefficient formulas.
---

::: {.problem}
Let $H$ be an $n$-dimensional Hilbert space and $A \colon H \to H$ a normal linear transformation.

(a) Derive a formula for the trace of the degree $d$ exterior power $A^{\wedge d}$ as a function of the eigenvalues of $A$.

(b) Express the coefficients of the characteristic polynomial of $A$ in terms of traces of exterior powers of $A$.
:::

::: {.solution}

**Goal:** Derive the formula for $\operatorname{tr}(A^{\wedge d})$ in terms of the eigenvalues of a normal operator $A$, and express the characteristic polynomial coefficients via traces of exterior powers.

::: pf

::: pf-step
Part (a): Spectral decomposition and basis of the exterior power $\bigwedge^d H$.

::: pf-proof
*Proof:*

::: pf-step
By the Spectral Theorem for normal operators on a finite-dimensional complex Hilbert space $H$, there exists an orthonormal basis $\{v_1, v_2, \dots, v_n\}$ of $H$ consisting of eigenvectors of $A$:
$$A v_j = \lambda_j v_j \quad \text{for } j = 1, \dots, n.$$
:::

::: pf-step
The $d$-th exterior power $\bigwedge^d H$ has dimension $\binom{n}{d}$, with an orthonormal basis given by the wedge products
$$\{v_I = v_{i_1} \wedge v_{i_2} \wedge \cdots \wedge v_{i_d} : 1 \le i_1 < i_2 < \cdots < i_d \le n\}.$$
:::

::: pf-step
By definition of the induced linear transformation $A^{\wedge d}: \bigwedge^d H \to \bigwedge^d H$:
$$A^{\wedge d}(v_{i_1} \wedge \cdots \wedge v_{i_d}) = (A v_{i_1}) \wedge \cdots \wedge (A v_{i_d}) = (\lambda_{i_1} v_{i_1}) \wedge \cdots \wedge (\lambda_{i_d} v_{i_d}) = \left(\prod_{k=1}^d \lambda_{i_k}\right) v_{i_1} \wedge \cdots \wedge v_{i_d}.$$
:::

::: pf-step
Thus every basis vector $v_I$ is an eigenvector of $A^{\wedge d}$ with eigenvalue $\prod_{k=1}^d \lambda_{i_k}$.
:::

:::

:::

::: {.pf-step #trace-formula-for-wedge-power}
Part (a): Trace formula for $A^{\wedge d}$.

::: pf-proof
*Proof:*

::: pf-step
The trace of an operator is the sum of its eigenvalues (the diagonal entries with respect to any orthonormal basis):
$$\operatorname{tr}\left(A^{\wedge d}\right) = \sum_{1 \le i_1 < i_2 < \cdots < i_d \le n} \lambda_{i_1} \lambda_{i_2} \cdots \lambda_{i_d} = e_d(\lambda_1, \dots, \lambda_n),$$
where $e_d(\lambda_1, \dots, \lambda_n)$ is the $d$-th elementary symmetric polynomial in the eigenvalues of $A$.
:::

:::

:::

::: pf-step
Part (b): Expressing characteristic polynomial coefficients via traces of exterior powers.

::: pf-proof
*Proof:*

::: pf-step
The characteristic polynomial of $A$ is defined by $p_A(t) = \det(tI - A)$.
:::

::: pf-step
Factoring $p_A(t)$ through its eigenvalues:
$$p_A(t) = \prod_{j=1}^n (t - \lambda_j) = \sum_{d=0}^n (-1)^d e_d(\lambda_1, \dots, \lambda_n) t^{n-d}.$$
:::

::: pf-step
Substituting $e_d(\lambda_1, \dots, \lambda_n) = \operatorname{tr}(A^{\wedge d})$ from step [](#trace-formula-for-wedge-power){.pf-ref} yields:
$$p_A(t) = \sum_{d=0}^n (-1)^d \operatorname{tr}\left(A^{\wedge d}\right) t^{n-d} = t^n - \operatorname{tr}(A) t^{n-1} + \operatorname{tr}\left(A^{\wedge 2}\right) t^{n-2} - \cdots + (-1)^n \operatorname{tr}\left(A^{\wedge n}\right),$$
with the standard convention $\operatorname{tr}(A^{\wedge 0}) = 1$ and $\operatorname{tr}(A^{\wedge n}) = \det(A)$.
:::

:::

:::

::: pf-step
Conclusion:

::: pf-proof
*Proof:*

$\operatorname{tr}(A^{\wedge d}) = e_d(\lambda_1, \dots, \lambda_n)$, and the coefficient of $t^{n-d}$ in $\det(tI - A)$ is $(-1)^d \operatorname{tr}(A^{\wedge d})$.
:::

:::

:::

:::
