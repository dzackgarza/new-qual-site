---
schema: qual/card@1
id: P-UCLAB16S-04
kind: problem
title: Limit of a Volterra-type recursion
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
Given continuous functions $\alpha:[0,1]\to\mathbb R$ and $\beta:[0,1]\to[0,1)$, define $f_n:[0,1]\to\mathbb R$ recursively by
\[
f_{n+1}(x)=\alpha(x)+\int_0^x \beta(t)f_n(t)\,dt,
\qquad f_0(x)=0.
\]
Prove that for each $x\in[0,1]$ the limit
\[
f(x):=\lim_{n\to\infty}f_n(x)
\]
exists and compute its value.
:::
