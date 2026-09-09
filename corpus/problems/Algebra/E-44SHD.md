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
- event: source-checked
  by: OpenAI
  date: 2026-09-09
  note: Checked against the UCR qualifying-algebra linear algebra problem list.
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
p(\lambda)=\det(A+\lambda B)\in k[\lambda].
\]
Then \(p\) is not the zero polynomial.
::: {.proof}
Because \(B\) is invertible,
\[
A+\lambda B=B(B^{-1}A+\lambda I),
\]
so
\[
p(\lambda)=\det(B)\det(B^{-1}A+\lambda I).
\]
If \(A,B\in M_n(k)\), then the second factor is monic of degree \(n\) in \(\lambda\). Since \(\det(B)\neq0\), \(p\) has degree \(n\) and is therefore nonzero.
:::

<1>2. The matrix \(A+\lambda B\) is singular for only finitely many \(\lambda\in k\).
::: {.proof}
A square matrix over a field is singular exactly when its determinant is zero. By <1>1, \(p\) is a nonzero polynomial of degree \(n\), so it has at most \(n\) roots in \(k\). Thus only finitely many \(\lambda\) satisfy \(\det(A+\lambda B)=0\).
:::

<1>3. Hence \(A+\lambda B\) is invertible for all but finitely many \(\lambda\in k\).
::: {.proof}
This is the complement of the finite exceptional set from <1>2.
:::
:::
