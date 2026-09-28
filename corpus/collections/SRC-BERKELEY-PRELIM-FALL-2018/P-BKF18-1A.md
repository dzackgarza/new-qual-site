---
schema: qual/card@1
id: P-BKF18-1A
kind: problem
title: Integral identity for $x^{-x}$
classification:
  areas:
  - prelim
  topics:
  - Calculus
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Show that
\[
\int_0^1 x^{-x}\,dx=\sum_{n=1}^{\infty}n^{-n}.
\]
:::

::: {.solution}
Write $x ^ { - x } = \mathrm { e } ^ { - x \log x }$ , Taylor expand the exponential, and integrate term by term.
:::
