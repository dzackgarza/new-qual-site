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

::: {.problem}
2. Prove that if $A$ and $B$ are invertible matrices over a field $\boldsymbol{k}$, then $A+\lambda B$ is invertible for all but finitely many $\lambda \in \boldsymbol{k}$.
:::

::: {.solution}
<1>1. Suppose \(A,B\in M_n(k)\) are invertible.
For \(\lambda\in k\),
\[
A+\lambda B=B\bigl(B^{-1}A+\lambda I_n\bigr).
\]
::: {.proof}
Expanding the right-hand side gives \(BB^{-1}A+\lambda BI_n=A+\lambda B\).
:::

<1>2. Hence
\[
\det(A+\lambda B)=\det(B)\,p(\lambda),
\qquad
p(t):=\det(B^{-1}A+tI_n)\in k[t].
\]
::: {.proof}
Apply multiplicativity of the determinant to <1>1.
:::

<1>3. The polynomial \(p(t)\) is nonzero and has degree \(n\).
::: {.proof}
In the determinant expansion of \(B^{-1}A+tI_n\), the product of the \(t\)-terms on the diagonal contributes \(t^n\), and no other term has degree \(n\). Thus \(p(t)\) is monic of degree \(n\).
:::

<1>4. Therefore \(A+\lambda B\) is singular for at most \(n\) values of \(\lambda\in k\).
::: {.proof}
Because \(B\) is invertible, \(\det(B)\neq0\). Thus
\[
\det(A+\lambda B)=0
\quad\Longleftrightarrow\quad
p(\lambda)=0.
\]
A nonzero polynomial of degree \(n\) over a field has at most \(n\) roots.
:::

<1>5. Hence \(A+\lambda B\) is invertible for all but finitely many \(\lambda\in k\).
::: {.proof}
A square matrix over a field is invertible exactly when its determinant is nonzero, so the conclusion follows from <1>4.
:::
:::
