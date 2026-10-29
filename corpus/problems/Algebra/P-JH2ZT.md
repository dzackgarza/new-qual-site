---
schema: qual/card@1
id: P-JH2ZT
kind: problem
title: Minimal polynomial divides the characteristic polynomial
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
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.problem}
Prove that the minimal polynomial of a square matrix divides its characteristic polynomial.
:::

::: {.solution}
Let $A\in M_n(F)$, with minimal polynomial $m_A$ and characteristic polynomial $\chi_A$. Divide with remainder: $\chi_A=q\,m_A+r$ with $r=0$ or $\deg r<\deg m_A$.

::: pf

::: {.pf-step #remainder}

$r(A)=0$.

::: pf-proof

By the Cayley--Hamilton theorem $\chi_A(A)=0$, and $m_A(A)=0$, so $r(A)=\chi_A(A)-q(A)m_A(A)=0$.

:::

:::

::: pf-step

$m_A\mid\chi_A$.

::: pf-proof

By step [](#remainder){.pf-ref}, $r$ annihilates $A$. A nonzero $r$ would, after scaling to be monic, be an annihilating polynomial of smaller degree than $m_A$. Hence $r=0$.

:::

:::

:::

:::
