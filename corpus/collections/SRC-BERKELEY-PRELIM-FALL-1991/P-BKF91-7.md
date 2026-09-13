---
schema: qual/card@1
id: P-BKF91-7
kind: problem
title: Exponential norm bound for a time-dependent linear system
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Consider
\[
x'(t)=A(t)x(t),
\]
where $A$ is a smooth real $n\times n$ matrix-valued function. Assume that
\[
\langle A(t)y,y\rangle\le c\|y\|^2
\]
for all $y\in\mathbb R^n$ and all $t$, where $c\in\mathbb R$ is fixed. Prove that every solution satisfies
\[
\|x(t)\|\le e^{ct}\|x(0)\|
\qquad(t>0).
\]
:::
