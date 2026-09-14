---
schema: qual/card@1
id: P-BKF85-7
kind: problem
title: Divergence to infinity for an autonomous ODE
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md; Flash drops the leading $0$ in the domain and garbles “as $t\to+\infty$,” both restored from the deterministic sentence structure.
---

::: {.problem}
Let $y(t)$ be a real-valued solution, defined for
\[
0<t<\infty,
\]
of
\[
\frac{dy}{dt}=e^{-y}-e^{-3y}+e^{-5y}.
\]
Show that
\[
y(t)\longrightarrow+\infty
\qquad\text{as }t\to+\infty.
\]
:::
