---
schema: qual/card@1
id: P-UCLAB01F-06
kind: problem
title: Direct local surjectivity from an identity derivative
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Suppose $F:\mathbb R^2\to\mathbb R^2$ is continuously differentiable, satisfies
\[
F(0,0)=(0,0),
\]
and has Jacobian matrix equal to the identity at $(0,0)$.
Outline a direct proof that there exists $\delta>0$ such that whenever
\[
a^2+b^2<\delta,
\]
there is a point $(x,y)\in\mathbb R^2$ with
\[
F(x,y)=(a,b).
\]

Do not merely restate the Inverse Function Theorem: the requested argument is part of its proof.
You may use without proof basic estimates expressing that the change in $F$ is approximated by its differential.
:::
