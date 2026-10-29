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

::: {.problem}
To which classes of operators does the classical Spectral Theorem for real symmetric matrices generalize? State the key theorems.
:::

::: {.solution}
::: pf

::: pf-step
Finite-dimensional complex inner product spaces: a matrix is unitarily diagonalizable if and only if it is normal; Hermitian matrices are the self-adjoint case and have real eigenvalues.

::: pf-proof
This is the spectral theorem for normal matrices; the real symmetric case is the self-adjoint case over $\RR$.
:::

:::

::: pf-step
Compact operators: a compact self-adjoint operator on a Hilbert space has an orthonormal basis of eigenvectors, made of eigenvectors for the nonzero eigenvalues together with an orthonormal basis of the kernel.
Its nonzero eigenvalues are real, have finite multiplicity, and can accumulate only at $0$.
The same holds for compact normal operators, with complex eigenvalues.

::: pf-proof
This is the spectral theorem for compact self-adjoint, and compact normal, operators.
:::

:::

::: pf-step
Bounded self-adjoint and normal operators: for a bounded self-adjoint operator $T$ there is a unique projection-valued measure $E$ on $\sigma(T)\subset\RR$ with
$$
T=\int_{\sigma(T)}\lambda\,dE(\lambda),
$$
and the same holds for bounded normal operators with $\sigma(T)\subset\CC$.

::: pf-proof
This is the spectral theorem in projection-valued-measure form; equivalent forms are the continuous functional calculus $f\mapsto f(T)$ and the unitary equivalence of $T$ to a multiplication operator on an $L^2$ space.
:::

:::

::: pf-step
Unbounded self-adjoint operators: a densely defined self-adjoint operator $T$ has the same representation $T=\int\lambda\,dE(\lambda)$, with domain the set of $x$ with $\int\abs{\lambda}^2\,d\inner{E(\lambda)x}{x}<\infty$.

::: pf-proof
This is the spectral theorem for unbounded self-adjoint operators.
:::

:::

:::

:::

::: {.remark}
In infinite dimensions the eigenbasis becomes a spectral measure: a normal operator has an orthonormal basis of eigenvectors exactly when its spectral measure is purely atomic, and this holds automatically for compact normal operators.
:::
