---
schema: qual/card@1
id: P-UCLAB10F-12
kind: problem
title: Differentiate an integral over a moving disk
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 12. Let
\[
D(t)=\{(x,y)\in\mathbb R^2:x^2+y^2\le r(t)^2\},
\]
where $r:\mathbb R\to\mathbb R$ is continuously differentiable. For a given smooth nonnegative function $u:\mathbb R^2\times\mathbb R\to\mathbb R$, express
\[
\frac{d}{dt}\left(\int_{D(t)}u(x,t)\,dx\right)
-
\int_{D(t)}u_t(x,t)\,dx
\]
in terms of a surface integral. You may use standard calculus theorems without proof.
:::
