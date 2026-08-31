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

::: solution
**Goal:** Prove that the minimal polynomial $q(x) \in k[x]$ of an endomorphism $\phi \in \operatorname{End}_k(E)$ on an $n$-dimensional vector space $E$ has degree at most $n$.

<1>1. Characteristic polynomial and the Cayley–Hamilton Theorem:
    *Proof:*
    <2>1. Choose an ordered basis $\mathcal{B}$ for $E$ over $k$, and let $A = [\phi]_\mathcal{B} \in M_n(k)$ be the matrix representing $\phi$.
    <2>2. The characteristic polynomial of $\phi$ is defined by $p(x) = \det(x I_n - A) \in k[x]$.
    <2>3. By properties of the determinant, $p(x)$ is a monic polynomial of degree $\deg p = n = \dim_k E$.
    <2>4. By the Cayley–Hamilton Theorem, $p(A) = 0$ in $M_n(k)$, which implies $p(\phi) = 0$ in $\operatorname{End}_k(E)$.

<1>2. Divisibility by the minimal polynomial:
    *Proof:*
    <2>1. The minimal polynomial $q(x) \in k[x]$ of $\phi$ is the unique monic generator of the evaluation ideal $I = \{f \in k[x] : f(\phi) = 0\} \subseteq k[x]$.
    <2>2. Since $p(\phi) = 0$, $p(x) \in I = (q(x))$, so $q(x)$ divides $p(x)$ in $k[x]$.
    <2>3. Since $p(x) \neq 0$ and $q(x) \mid p(x)$, the degree of $q$ is bounded by the degree of $p$:
    $$\deg q \le \deg p = n.$$

<1>3. Conclusion:
    *Proof:*
    The degree of the minimal polynomial $q$ satisfies $\deg q \le \dim_k E = n$.
:::
