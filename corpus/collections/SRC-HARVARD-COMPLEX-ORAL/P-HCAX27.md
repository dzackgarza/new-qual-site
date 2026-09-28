---
schema: qual/card@1
id: P-HCAX27
kind: problem
title: Riemann hypothesis
classification:
  areas:
  - complex-analysis
  topics:
  - Riemann Zeta Function
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.problem}
State the Riemann hypothesis.
:::

::: {.solution}
The Riemann zeta function $\zeta$ is the meromorphic continuation to $\CC$ of
$\sum_{n\ge1}n^{-s}$ $(\operatorname{Re}s>1)$; it is holomorphic except for a
simple pole at $s=1$. The functional equation gives zeros at
$s=-2,-4,-6,\ldots$, the trivial zeros. Every other zero lies in the critical
strip $0<\operatorname{Re}s<1$.

The Riemann hypothesis states: every zero of $\zeta$ with
$0<\operatorname{Re}s<1$ satisfies $\operatorname{Re}s=\tfrac12$.
:::
