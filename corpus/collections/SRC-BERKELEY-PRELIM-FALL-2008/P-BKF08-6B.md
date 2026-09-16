---
schema: qual/card@1
id: P-BKF08-6B
kind: problem
title: The identity $\int_0^1 x^{-x}\,dx=\sum_{n\ge1} n^{-n}$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 6B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
---

::: {.problem}
Show that
\[
\int_0^1\frac{1}{x^x}\,dx=\sum_{n=1}^{\infty}\frac1{n^n}.
\]

*Hint.* Write $x^x$ in terms of the exponential and logarithm functions, and evaluate $\int_0^1x^s\log(x)^n\,dx$.
:::
