---
schema: qual/card@1
id: P-IR6HQ
kind: problem
title: Degree of the minimal polynomial is bounded by the dimension
classification:
  areas:
  - algebra
  topics:
  - Minimal and Characteristic Polynomials
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: {.problem}
Show that if $q$ is the minimal polynomial of a linear transformation $\phi: E\to E$ with $\dim_k E = n$ then $\deg q \leq n$.
:::

::: {.solution}
Choose an ordered basis of $E$, let $A \in M_n(k)$ be the matrix of $\phi$, and let $p(x) = \det(x I_n - A) \in k[x]$ be the characteristic polynomial.

<1>1. $p$ is monic of degree $n$ and $p(\phi) = 0$.

::: {.proof}
Expanding the determinant, the only term of degree $n$ in $x$ is the product of the diagonal entries, so $p$ is monic of degree $n$. By the Cayley--Hamilton theorem $p(A) = 0$, hence $p(\phi) = 0$.
:::

<1>2. Q.E.D.

::: {.proof}
The minimal polynomial $q$ is the monic generator of the ideal $\{f \in k[x] : f(\phi) = 0\}$. By step <1>1, $p$ lies in this ideal, so $q \mid p$. Since $p \neq 0$, $\deg q \le \deg p = n$.
:::
:::
