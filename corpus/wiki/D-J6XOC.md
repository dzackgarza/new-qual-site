---
schema: qual/card@1
id: D-J6XOC
kind: definition
title: "Path"
classification:
  areas:
  - topology
  topics:
  - connectedness
  - fundamental-group
relations: []
review: draft
---

::: {.definition title="Path"}
A **path** in $X$ is a continuous map $\gamma: I \da [0,1] \to X$; it is a path *from* $\gamma(0)$ *to* $\gamma(1)$, and a **loop** iff $\gamma(0) = \gamma(1)$.
When $\gamma(1) = \eta(0)$ the two paths concatenate:
\[
(\gamma\cdot \eta)(s) \da
\begin{cases}
\gamma(2s) & 0\leq s \leq 1/2, \\
\eta(2s-1) & 1/2 \leq s \leq 1.
\end{cases}
\]
:::

::: {.concept}
See Hatcher, §1.1, p. 25; Munkres, §51.
:::
