---
schema: qual/card@1
id: P-UCLAB08S-01
kind: problem
title: Fixed points and contraction iteration
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
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $g\in C([a,b])$ satisfy $a\le g(x)\le b$ for all $x\in[a,b]$.

<1>1. Prove that $g$ has a fixed point $p\in[a,b]$.

<1>2. Suppose there is $\gamma<1$ such that
\[
|g(x)-g(y)|\le \gamma|x-y|
\]
for all $x,y\in[a,b]$. Prove that the fixed point is unique and that, for every $x_0\in[a,b]$, the iteration $x_{n+1}=g(x_n)$ converges to $p$.
:::
