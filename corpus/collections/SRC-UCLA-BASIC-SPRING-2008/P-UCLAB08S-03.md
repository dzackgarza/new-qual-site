---
schema: qual/card@1
id: P-UCLAB08S-03
kind: problem
title: Error in the centered finite-difference approximation to a second derivative
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
  note: Checked against Problem 3 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Assume $f\in C^4([a,b])$ is real-valued.
Derive a formula for the approximation error $E(h)$ when
\[
f''(x)\sim \frac{f(x+h)-2f(x)+f(x-h)}{h^2},
\]
where $x,x+h,x-h\in(a,b)$.
:::
