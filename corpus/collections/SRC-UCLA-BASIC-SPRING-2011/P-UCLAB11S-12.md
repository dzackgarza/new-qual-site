---
schema: qual/card@1
id: P-UCLAB11S-12
kind: problem
title: Contraction mapping iteration for the equation f prime equals f
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Spring 2011.
---

::: {.problem}
Let $0<c<1$ and let $M=C([0,c])$ with the uniform metric
\[
d(f,g)=\sup_{0\le t\le c}|f(t)-g(t)|.
\]
Define
\[
(Tf)(x)=1+\int_0^x f(t)\,dt.
\]
Recall that every contraction of a complete metric space has a unique fixed point.

<1>1. Use this fixed-point theorem to obtain the solution of
\[
f'(t)=f(t),\qquad f(0)=1,
\]
carefully explaining why the theorem applies.
<1>2. Determine the successive approximations $T(0),T^2(0),T^3(0),\ldots$.
:::
