---
schema: qual/card@1
id: P-UCLAB07S-01
kind: problem
title: Normal equations for full-column-rank least squares
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $A$ be a real $m\times n$ matrix with $m>n$ and linearly independent columns, and let $b\in\mathbb R^m$.
Show that the vector $x^*\in\mathbb R^n$ minimizing
\[
g(x)=\|Ax-b\|_2^2
\]
is the solution of the normal equations
\[
A^TAx=A^Tb.
\]
:::
