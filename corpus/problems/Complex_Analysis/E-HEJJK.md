---
schema: qual/card@1
id: E-HEJJK
kind: problem
title: An entire function whose image misses a disk is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Removable Singularities
relations: []
review: draft
---

::: {.exercise}
Show that if $f$ is entire and there exists a disc $\DD_r(a)$ not intersecting $f(\CC)$, then $f$ must be constant.
:::

::: {.solution}
Let $g(z)\definedas f(z)-a$.
Then $\DD_r(0)$ does not intersect $g(\CC)$, so $\abs{g(z)} \geq r$ for all $z\in\CC$.
In particular $g$ has no zeros, so $G(z) \definedas {1\over g(z)}$ is entire, and $\abs{G(z)} \leq \inverseof{r}$ for all $z$.
By Liouville, $G$ is constant, so $g$ and hence $f$ are constant.
:::
