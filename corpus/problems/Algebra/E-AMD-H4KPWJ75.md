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
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Prove that the minimal polynomial divides the characteristic polynomial.
:::

::: {.solution}
Let $m_A(t)$ be the minimal polynomial and $\chi_A(t)$ the characteristic polynomial of $A$. By Cayley--Hamilton,
\[
\chi_A(A)=0.
\]
Divide $\chi_A$ by $m_A$ in $F[t]$:
\[
\chi_A=q\,m_A+r,\qquad \deg r<\deg m_A.
\]
Evaluating at $A$ gives
\[
0=\chi_A(A)=q(A)m_A(A)+r(A)=r(A).
\]
By minimality of $m_A$, no nonzero polynomial of smaller degree annihilates $A$. Hence $r=0$, and therefore
\[
\boxed{m_A\mid\chi_A}.
\]
:::
