---
schema: qual/card@1
id: FD-ST7TD
kind: definition
title: Uniform Continuity
classification:
  areas:
  - real-analysis
  topics:
  - Uniform Continuity
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
For $f: (X, d_1) \to (Y, d_2)$, for every $\varepsilon > 0$ there exists $\delta(\varepsilon) > 0$ such that for every $x,y\in X$, $$x\in B_\delta(y) \implies f(x) \in B_\varepsilon(f(y)).$$

> Slogan: continuity, but $\delta$ can be chosen independent of $x$.
:::
