---
schema: qual/card@1
id: P-UCLAB09F-08
kind: problem
title: Matrix exponentials solve constant-coefficient systems
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
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
For $A\in M_n(\mathbb R)$ define
\[
e^A:=\sum_{k=0}^\infty \frac{A^k}{k!}.
\]
Let $v_0\in\mathbb R^n$.
Prove that
\[
v(t)=e^{At}v_0
\]
solves
\[
v'(t)=Av(t),\qquad v(0)=v_0.
\]
Explain precisely which theorems from calculus you use and why they apply.
:::
