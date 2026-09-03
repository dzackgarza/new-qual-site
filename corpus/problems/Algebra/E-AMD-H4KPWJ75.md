---
schema: qual/card@1
id: E-AMD-H4KPWJ75
kind: problem
title: The minimal polynomial divides the characteristic polynomial
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
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Prove that the minimal polynomial divides the characteristic polynomial.
:::

::: solution
**Goal:** Prove that for any matrix $A \in M_n(F)$ (or linear operator on a finite-dimensional vector space), the minimal polynomial $m_A(t)$ divides the characteristic polynomial $\chi_A(t) = \det(t I_n - A)$.

<1>1. Annihilation via Cayley-Hamilton Theorem:
    *Proof:*
    <2>1. Let $\chi_A(t) = \det(t I_n - A) \in F[t]$ be the characteristic polynomial of $A$.
    <2>2. By the Cayley-Hamilton Theorem, substituting $A$ into $\chi_A(t)$ gives the zero matrix:
        $$\chi_A(A) = 0.$$

<1>2. Division algorithm in $F[t]$:
    *Proof:*
    <2>1. By definition, the minimal polynomial $m_A(t)$ is the monic polynomial of least degree in $F[t]$ such that $m_A(A) = 0$.
    <2>2. Applying the polynomial division algorithm in the Euclidean domain $F[t]$ to divide $\chi_A(t)$ by $m_A(t)$:
        $$\chi_A(t) = q(t) m_A(t) + r(t),$$
        where $q(t), r(t) \in F[t]$ and either $r(t) = 0$ or $\deg(r) < \deg(m_A)$.

<1>3. Evaluation at $A$ and minimality contradiction:
    *Proof:*
    <2>1. Evaluating both sides of the division identity at the matrix $A$:
        $$\chi_A(A) = q(A) m_A(A) + r(A).$$
    <2>2. Substituting $\chi_A(A) = 0$ and $m_A(A) = 0$ yields:
        $$0 = q(A) \cdot 0 + r(A) = r(A).$$
    <2>3. If $r(t) \neq 0$, then $r(t)$ would be a non-zero polynomial annihilating $A$ with $\deg(r) < \deg(m_A)$, directly contradicting the minimality of $\deg(m_A)$.
    <2>4. Therefore, the remainder must be identically zero: $r(t) = 0$.

<1>4. Conclusion:
    $\chi_A(t) = q(t) m_A(t)$, so $m_A(t) \mid \chi_A(t)$ in $F[t]$. Q.E.D.
:::
