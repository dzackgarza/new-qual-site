---
schema: qual/card@1
id: P-BERK97S-03
kind: problem
title: A weighted average of an integrable nonnegative function tends to zero
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
---

::: {.problem}
Let $f:[0,\infty)\to[0,\infty)$ be continuous and suppose
\[
\int_0^\infty f(x)\,dx<\infty.
\]
Prove that
\[
\lim_{n\to\infty}\int_0^n\frac{x f(x)}{n}\,dx=0.
\]
:::
