---
schema: qual/card@1
id: P-UCLAB16S-01
kind: problem
title: Continuity along the diagonal under separate monotonicity
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $a<b$ be real numbers, and let
\[
f:[a,b]\times[a,b]\to\mathbb R
\]
satisfy:

1. for each $y\in[a,b]$, the map $x\mapsto f(x,y)$ is non-increasing and continuous on $[a,b]$;
2. for each $x\in[a,b]$, the map $y\mapsto f(x,y)$ is non-decreasing and continuous on $[a,b]$.

Prove that $g(x):=f(x,x)$ is continuous on $[a,b]$.
:::
