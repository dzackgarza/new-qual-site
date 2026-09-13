---
schema: qual/card@1
id: P-UCLAB08F-10
kind: problem
title: Norm inequality for vector-valued integrals
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
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
For $v=(v_1,\ldots,v_n)\in\mathbb R^n$, let
\[
\|v\|=\left(\sum_{j=1}^n|v_j|^2\right)^{1/2}.
\]
If $f=(f_1,\ldots,f_n)\colon[a,b]\to\mathbb R^n$ is continuous, define
\[
\int_a^b f(t)\,dt
=\left(\int_a^b f_1(t)\,dt,\ldots,\int_a^b f_n(t)\,dt\right).
\]
Prove that
\[
\left\|\int_a^b f(t)\,dt\right\|\le \int_a^b\|f(t)\|\,dt.
\]
:::
