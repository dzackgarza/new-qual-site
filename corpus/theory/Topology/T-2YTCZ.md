---
schema: qual/card@1
id: T-2YTCZ
kind: theorem
title: Maps into a convex set are homotopic
slogan: 'Convex targets make any two maps homotopic by straight-line interpolation.'
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.theorem}
Let $X$ be a topological space and $C\subseteq\RR^n$ a convex subset.
Any two continuous maps $f, g\colon X\to C$ are homotopic, via the linear homotopy $F(x,t) = (1-t)f(x) + t\,g(x)$, which lies in $C$ by convexity; for paths this is [@Hat02].
:::
