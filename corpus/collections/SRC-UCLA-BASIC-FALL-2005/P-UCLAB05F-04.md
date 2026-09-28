---
schema: qual/card@1
id: P-UCLAB05F-04
kind: problem
title: Arc length bound for a strictly concave graph
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 of the official UCLA Basic Examination, September 2005 PDF.
---

::: {.problem}
Suppose $F:[0,1]\to[0,1]$ is a $C^2$ function with
\[
F(0)=F(1)=0
\qquad\text{and}\qquad
F''(x)<0
\]
for all $x\in[0,1]$.
Prove that the arc length of the curve
\[
\{(x,F(x)):x\in[0,1]\}
\]
is less than $3$.

Suggestion: in the arc-length formula, use
\[
\sqrt{a^2+b^2}<|a|+|b|.
\]
:::
