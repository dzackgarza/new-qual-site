---
schema: qual/card@1
id: P-UCLAB09F-02
kind: problem
title: Contractions and a fixed point for a prescribed derivative
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2009.
---

::: {.problem}
<1>1. Let $(X,d)$ be a complete metric space.
A map $T\colon X\to X$ is a contraction if there is $0<\lambda<1$ such that
\[
d(Tx,Ty)\le \lambda d(x,y)
\]
for all $x,y\in X$.
Prove that every contraction has a fixed point.

<1>2. Using <1>1, show that if $f\colon\mathbb R\to\mathbb R$ is differentiable and
\[
f'(x)=e^{-x^2}-e^{-x^4},
\]
then there exists $\alpha\in\mathbb R$ such that $f(\alpha)=\alpha$.
:::
