---
schema: qual/card@1
id: P-UCLAB11F-02
kind: problem
title: Strong monotonicity of the gradient implies convexity
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2011.
---

::: {.problem}
Problem 2. A function $f:\mathbb R^n\to\mathbb R$ is called convex if
\[
f(\alpha x+(1-\alpha)y)\le \alpha f(x)+(1-\alpha)f(y)
\]
for all $x,y\in\mathbb R^n$ and $0\le\alpha\le1$.

Assume that $f$ is continuously differentiable and that for some constant $c>0$,
\[
(\nabla f(x)-\nabla f(y))\cdot(x-y)\ge c\,(x-y)\cdot(x-y)
\]
for all $x,y\in\mathbb R^n$. Show that $f$ is convex.
:::
