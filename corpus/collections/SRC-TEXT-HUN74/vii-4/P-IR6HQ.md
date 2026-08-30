---
schema: qual/card@1
id: P-IR6HQ
kind: problem
title: Hungerford 7.4.4
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
**Goal:** Prove $\deg q\le n$ for the minimal polynomial of $\phi$.

<1> Apply Cayley--Hamilton.
    *Proof:*
    <2>1. Let $A$ be the matrix of $\phi$ in some basis of $E$.
    <2>2. The characteristic polynomial $\chi_A(t)$ has degree $n=\dim E$.
    <2>3. By the Cayley--Hamilton theorem, $\chi_A(\phi)=0$ (or $\chi_A(A)=0$).
    <2>4. The minimal polynomial $q$ is the monic polynomial of smallest degree that annihilates $\phi$.
    <2>5. Therefore $q$ divides $\chi_A$, so $\deg q\le\deg\chi_A=n$.

Authored by **Codex 5.3 Spark Extra High**.
:::
