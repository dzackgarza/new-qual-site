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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section VII.4,
    exercise 4, book page 365, read from the page image: "If q is the minimal
    polynomial of a linear transformation φ : E → E, with dim_K E = n, then
    deg q ≤ n." The card states exactly this. The proof was checked: the
    characteristic polynomial det(xI_n − A) is monic of degree n, Cayley-Hamilton
    gives p(φ) = 0, and the minimal polynomial generates the ideal of polynomials
    annihilating φ, so q | p and deg q ≤ n. Cayley-Hamilton is Theorem 5.3, later
    in the same chapter, and is available as a theorem; within section 4 the same
    bound also follows from q being an invariant factor whose product with the
    others is p. Complete; no defect.
---

::: {.problem}
Show that if $q$ is the minimal polynomial of a linear transformation $\phi: E\to E$ with $\dim_k E = n$ then $\deg q \leq n$.
:::

::: {.solution}
Choose an ordered basis of $E$, let $A \in M_n(k)$ be the matrix of $\phi$, and let $p(x) = \det(x I_n - A) \in k[x]$ be the characteristic polynomial.

::: pf

::: {.pf-step #s1}

$p$ is monic of degree $n$ and $p(\phi) = 0$.

::: pf-proof

Expanding the determinant, the only term of degree $n$ in $x$ is the product of the diagonal entries, so $p$ is monic of degree $n$. By the Cayley--Hamilton theorem $p(A) = 0$, hence $p(\phi) = 0$.

:::

:::

::: pf-qed

The minimal polynomial $q$ is the monic generator of the ideal $\{f \in k[x] \st f(\phi) = 0\}$. By step [](#s1){.pf-ref}, $p$ lies in this ideal, so $q \mid p$. Since $p \neq 0$, $\deg q \le \deg p = n$.

:::

:::

:::
