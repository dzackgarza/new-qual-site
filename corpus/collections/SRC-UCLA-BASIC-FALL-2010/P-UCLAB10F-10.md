---
schema: qual/card@1
id: P-UCLAB10F-10
kind: problem
title: Euler polygonal approximations for a Lipschitz ODE
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 10. Suppose $f:\mathbb R\to\mathbb R$ is bounded and Lipschitz continuous.
For $k\in\mathbb N$, define $x_k:[0,1]\to\mathbb R$ by $x_k(0)=0$ and
\[
x_k(t)=x_k(n2^{-k})+(t-n2^{-k})f(x_k(n2^{-k}))
\]
whenever
\[
n2^{-k}<t\le(n+1)2^{-k},\qquad n\in\mathbb N.
\]
Explain why $x_k$ converges uniformly, as $k\to\infty$, to a solution $x:[0,1]\to\mathbb R$ of
\[
x'(t)=f(x(t)),\qquad x(0)=0.
\]
:::
