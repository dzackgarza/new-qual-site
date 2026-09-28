---
schema: qual/card@1
id: P-UCLAB13F-05
kind: problem
title: Monotonicity of the gradient implies convexity
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Fall 2013.
---

::: {.problem}
A function $f:\mathbb R^d\to\mathbb R$ is convex if
\[
f(tx+(1-t)y)\le tf(x)+(1-t)f(y)
\]
for all $x,y\in\mathbb R^d$ and $0\le t\le1$.

Assume that $f$ is continuously differentiable and
\[
(\nabla f(x)-\nabla f(y))\cdot(x-y)\ge0
\]
for all $x,y\in\mathbb R^d$. Prove that $f$ is convex.
:::
