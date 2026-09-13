---
schema: qual/card@1
id: P-BKF98-5
kind: problem
title: A homogeneous function with bilinear polarization is a quadratic form
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $f:\mathbb R^n\to\mathbb R$ satisfy:

1. The function
\[
g(x,y)=f(x+y)-f(x)-f(y)
\]
is bilinear.

2. For every $x\in\mathbb R^n$ and $t\in\mathbb R$,
\[
f(tx)=t^2f(x).
\]

Show that there is a linear transformation $A:\mathbb R^n\to\mathbb R^n$ such that
\[
f(x)=\langle x,Ax\rangle
\]
for the usual inner product.
:::
