---
schema: qual/card@1
id: E-U2X4C
kind: exercise
title: "Show that if $f$ is entire and $\\abs{f(z)} > 1$ for all $z$, then $f$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that if $f$ is entire and $\abs{f(z)} > 1$ for all $z$, then $f$ is constant.
:::

::: {.solution}
The inequality forces $f\neq 0$ anywhere, so $1/f$ is entire and bounded by 1. By Liouville, $1/f$ is constant, and thus so is $f$.
:::
