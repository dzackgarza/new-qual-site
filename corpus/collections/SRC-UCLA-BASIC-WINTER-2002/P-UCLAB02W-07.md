---
schema: qual/card@1
id: P-UCLAB02W-07
kind: problem
title: A nonsingular planar map covering the open unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
Suppose $F:\mathbb R^2\to\mathbb R^2$ is differentiable everywhere, its derivative matrix is continuous everywhere, and its Jacobian determinant is everywhere nonzero.
Assume also that
\[
\|F(x,y)\|\geq1
\quad\text{whenever}\quad
\|(x,y)\|=1,
\]
and that
\[
F(0,0)=(0,0).
\]
Prove that
\[
F\bigl(\{(x,y):x^2+y^2<1\}\bigr)
\supseteq
\{(x,y):x^2+y^2<1\}.
\]

Hint: if $U=\{(x,y):x^2+y^2<1\}$, prove that $F(U)\cap U$ is open and closed in $U$.
:::
