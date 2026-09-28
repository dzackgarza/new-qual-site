---
schema: qual/card@1
id: P-UCLAB02F-06
kind: problem
title: A regular level set contains a nonconstant local curve
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2002 PDF.
---

::: {.problem}
Suppose $F:\mathbb R^3\to\mathbb R^2$ is continuously differentiable.
Suppose that for some $v_0\in\mathbb R^3$ and $x_0\in\mathbb R^2$,
\[
F(v_0)=x_0
\]
and the derivative
\[
F'(v_0):\mathbb R^3\to\mathbb R^2
\]
is onto.
Show that there are $\varepsilon>0$ and a continuously differentiable function
\[
\gamma:(-\varepsilon,\varepsilon)\to\mathbb R^3
\]
such that
\[
\gamma'(0)\ne0
\]
and
\[
F(\gamma(t))=x_0
\qquad\text{for every }t\in(-\varepsilon,\varepsilon).
\]
:::
