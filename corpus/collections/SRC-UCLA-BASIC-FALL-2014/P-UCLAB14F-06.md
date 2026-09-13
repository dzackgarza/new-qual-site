---
schema: qual/card@1
id: P-UCLAB14F-06
kind: problem
title: Total variation of a $C^1$ function from uniform partitions
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
  note: Checked against Problem 6 of the retained UCLA Basic Examination, Fall 2014.
---

::: {.problem}
Problem 6. Let $f:[0,1]\to\mathbb R$ be a $C^1$ function. Prove that
\[
\lim_{n\to\infty}\sum_{k=0}^{n-1}
\left|f\!\left(\frac{k+1}{n}\right)-f\!\left(\frac{k}{n}\right)\right|
=
\int_0^1 |f'(t)|\,dt.
\]
:::
