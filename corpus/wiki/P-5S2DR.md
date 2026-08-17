---
schema: qual/card@1
id: P-5S2DR
kind: problem
title: "Show that $\\alpha z e^z = 1$ where $\\abs{\\alpha} > e$ has exactly one\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
relations: []
review: draft
solved: true
---

::: {.exercise title="?"}
Show that $\alpha z e^z = 1$ where $\abs{\alpha} > e$ has exactly one solution in $\DD$.
:::

::: {.solution}
\envlist

- Set $f(z) = \alpha z$ and $g(z) = e^{-z}$.

- Estimate at $\abs{z} =1$ we have $\abs{g} =\abs{e^{-z}} = e^{-\Re(z)} \leq e^1 < \abs{\alpha} = \abs{f(z)}$

- $f$ has one zero at $z_0 = 0$, thus so does $f+g$.
:::
