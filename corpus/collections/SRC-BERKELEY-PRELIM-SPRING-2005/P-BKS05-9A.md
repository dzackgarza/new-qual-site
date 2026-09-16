---
schema: qual/card@1
id: P-BKS05-9A
kind: problem
title: Principal value of $\iint f(x,y)/(x+iy)^3\,dx\,dy$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
---

::: {.problem}
Let $f \colon  { \mathbb { R } } ^ { 2 } \to  { \mathbb { R } }$ be an infinitely differentiable function that is zero outside some bounded subset of $\mathbb { R } ^ { 2 }$ . Prove that

$$
\operatorname * { l i m } _ { \epsilon \to 0 } \int \int _ { x ^ { 2 } + y ^ { 2 } \geq \epsilon ^ { 2 } } { \frac { f ( x , y ) } { ( x + i y ) ^ { 3 } } } d x d y
$$

exists.
:::
