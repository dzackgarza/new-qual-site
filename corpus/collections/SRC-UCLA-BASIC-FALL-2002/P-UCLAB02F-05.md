---
schema: qual/card@1
id: P-UCLAB02F-05
kind: problem
title: Optimal Lipschitz bound from bounded partial derivatives
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Suppose $f:\mathbb R^2\to\mathbb R$ has partial derivatives at every point and both partial derivatives are bounded in absolute value by $A>0$.

(a) Show that there is an $M>0$ such that
\[
|f(x,y)-f(x_1,y_1)|
\le M\sqrt{(x-x_1)^2+(y-y_1)^2}
\]
for all $(x,y),(x_1,y_1)\in\mathbb R^2$.

(b) What is the smallest value of $M$, in terms of $A$, for which this always works?

(c) Give an example for which that value of $M$ makes the inequality an equality.
:::
