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

::: problem
Prove that the minimal polynomial of a square matrix divides its characteristic polynomial.
:::

::: {.solution}
Let $A\in M_n(F)$, let $m_A(x)$ be its minimal polynomial, and let $\chi_A(x)$ be its characteristic polynomial.

By the Cayley--Hamilton theorem,
\[
\chi_A(A)=0.
\]
By definition, $m_A$ is the monic polynomial of least positive degree annihilating $A$. Divide $\chi_A$ by $m_A$:
\[
\chi_A=q\,m_A+r,
\qquad \deg r<\deg m_A.
\]
Evaluating at $A$ gives
\[
0=\chi_A(A)=q(A)m_A(A)+r(A)=r(A).
\]
The minimality of $m_A$ forces $r=0$. Hence
\[
m_A\mid\chi_A.
\]
:::
