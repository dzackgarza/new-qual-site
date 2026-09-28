---
schema: qual/card@1
id: P-UCLAB07S-07
kind: problem
title: Quadratic convergence of Newton iteration near a simple root
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
  note: Checked against Problem 7 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $f\colon\mathbb R\to\mathbb R$ be twice continuously differentiable with uniformly bounded second derivative and a simple root $x^*$, so $f(x^*)=0$ and $f'(x^*)\ne0$.
For Newton iteration
\[
x_n=F(x_{n-1}),\qquad F(x)=x-\frac{f(x)}{f'(x)},
\]
prove that if $x_0$ is sufficiently close to $x^*$, then there is a constant $C$ such that
\[
|x_n-x^*|\le C|x_{n-1}-x^*|^2
\]
for all $n$.
:::
