---
schema: qual/card@1
id: P-BKS03-3B
kind: problem
title: An entire function bounded below in real part is constant
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: problem
Let $f$ be entire and suppose
\[
\operatorname{Re}f(z)\ge-2
\]
for all $z\in\mathbb C$.
Show that $f$ is constant.
:::

::: {.solution}
The function $g ( z ) = e ^ { - f ( z ) }$ is entire, and $| g ( z ) | = e ^ { - \mathrm { R e } f ( z ) } \leq e ^ { 2 }$ . Liouville’s Theorem implies that g is constant, say $g ( z ) = c$ . Clearly $c \neq 0$ . Then f maps the connected set C into the discrete set of all logarithms of c, so $f$ is constant.
:::
