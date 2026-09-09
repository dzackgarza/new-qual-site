---
schema: qual/card@1
id: E-44SHD
kind: problem
title: $A+\lambda B$ is invertible for all but finitely many $\lambda$
classification:
  areas:
  - algebra
  topics:
  - Determinants
  - Matrices
  - Polynomials
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
2. Prove that if $A$ and $B$ are invertible matrices over a field $\boldsymbol{k}$, then $A+\lambda B$ is invertible for all but finitely many $\lambda \in \boldsymbol{k}$.
:::

::: {.solution}
<1>1. Define
\[
p(t)=\det(A+tB)\in \boldsymbol{k}[t].
\]
Then \(p(t)\) is a polynomial in \(t\).
::: {.proof}
Each entry of \(A+tB\) is affine-linear in \(t\), and the determinant is a polynomial expression in the matrix entries.
Hence \(\det(A+tB)\) is a polynomial in \(t\).
:::

<1>2. The polynomial \(p(t)\) is nonzero.
::: {.proof}
Evaluating at \(t=0\) gives
\[
p(0)=\det(A)\neq0
\]
because \(A\) is invertible.
Thus \(p\) cannot be the zero polynomial.
:::

<1>3. There are only finitely many \(\lambda\in\boldsymbol{k}\) such that \(p(\lambda)=0\).
::: {.proof}
A nonzero polynomial over a field has at most its degree many roots.
Therefore the root set of \(p\) in \(\boldsymbol{k}\) is finite.
:::

<1>4. For every \(\lambda\in\boldsymbol{k}\) outside that finite root set, the matrix \(A+\lambda B\) is invertible.
::: {.proof}
For such \(\lambda\), one has
\[
\det(A+\lambda B)=p(\lambda)\neq0.
\]
A square matrix over a field is invertible if and only if its determinant is nonzero.
:::
:::
