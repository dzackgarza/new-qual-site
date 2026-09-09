---
schema: qual/card@1
id: P-E7PIY
kind: problem
title: Fundamental theorem of symmetric polynomials
classification:
  areas:
  - algebra
  topics:
  - Symmetric Functions
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

::: problem
State the fundamental theorem of symmetric polynomials.
:::


::: {.solution}
Let $R$ be a commutative ring and let
\[
e_1,\dots,e_n
\]
denote the elementary symmetric polynomials in $R[x_1,\dots,x_n]$.

The fundamental theorem of symmetric polynomials says that every symmetric polynomial
\[
f\in R[x_1,\dots,x_n]^{S_n}
\]
can be written uniquely in the form
\[
f=F(e_1,\dots,e_n)
\]
for some polynomial
\[
F\in R[t_1,\dots,t_n].
\]
Equivalently,
\[
R[x_1,\dots,x_n]^{S_n}=R[e_1,\dots,e_n],
\]
and the elementary symmetric polynomials are algebraically independent over $R$.
:::
