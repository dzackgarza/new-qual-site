---
schema: qual/card@1
id: P-BERK81S-16
kind: problem
title: A continuous-kernel integral operator sends $L^2$-Cauchy sequences to uniformly convergent sequences
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f_n:[0,1]\to\mathbb R$ be continuous and suppose
\[
\int_0^1\bigl(f_n(x)-f_m(x)\bigr)^2\,dx\to0
\qquad(n,m\to\infty).
\]
Let $K:[0,1]\times[0,1]\to\mathbb R$ be continuous, and define
\[
g_n(x)=\int_0^1K(x,y)f_n(y)\,dy.
\]
Prove that $\{g_n\}$ converges uniformly on $[0,1]$.
:::
