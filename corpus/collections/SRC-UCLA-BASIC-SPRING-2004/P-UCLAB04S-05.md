---
schema: qual/card@1
id: P-UCLAB04S-05
kind: problem
title: Differentiability and a mean-value bound for vector-valued maps
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Exam Spring 2004 PDF. The source uses $p,q$ in the estimate without explicitly naming them as the endpoints of the line segment $I$; that intended role is made explicit here.
---

::: {.problem}
Suppose $G\subset\mathbb R^n$ is open, $f:G\to\mathbb R^m$ is a function, and $x_0\in G$.

(a) Carefully define what is meant by the derivative
\[
f'(x_0):\mathbb R^n\to\mathbb R^m.
\]

(b) Let $I$ be the line segment from $p$ to $q$ contained in $G$, and suppose that $f$ is differentiable at every point of $I$.
Show that for some $c\in I$,
\[
\|f(q)-f(p)\|_2
\leq
\|f'(c)\|\,\|q-p\|_2.
\]

Hint: let $w$ be a unit vector such that
\[
\|f(q)-f(p)\|_2=(f(q)-f(p))\mathbin{\cdot}w.
\]
:::
