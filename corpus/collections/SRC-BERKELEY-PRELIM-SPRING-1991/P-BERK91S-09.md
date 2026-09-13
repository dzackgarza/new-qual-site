---
schema: qual/card@1
id: P-BERK91S-09
kind: problem
title: Iterating a strict norm decrease on the unit ball converges to the origin
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Let
\[
B_n=\{x\in\mathbb R^n:\|x\|<1\}
\]
and let $f:B_n\to B_n$ be continuous. Suppose
\[
\|f(x)\|<\|x\|
\]
for every nonzero $x\in B_n$. For nonzero $x_0\in B_n$, define
\[
x_k=f(x_{k-1}).
\]
Prove that
\[
x_k\to0.
\]
:::
