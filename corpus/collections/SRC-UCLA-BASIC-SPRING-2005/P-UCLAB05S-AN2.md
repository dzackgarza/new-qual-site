---
schema: qual/card@1
id: P-UCLAB05S-AN2
kind: problem
title: Accumulation points in the binary sequence space
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Analysis Problem 2 of the official UCLA Basic Exam, May 2005 PDF.
---

::: {.problem}
Let $X$ be the set of all infinite sequences $(\sigma_n)_{n=1}^{\infty}$ of $0$'s and $1$'s, endowed with the metric
\[
\operatorname{dist}\bigl((\sigma_n),(\sigma_n')\bigr)
=\sum_{n=1}^{\infty}\frac{|\sigma_n-\sigma_n'|}{2^n}.
\]
Give a direct proof that every infinite subset of $X$ has an accumulation point.
:::
