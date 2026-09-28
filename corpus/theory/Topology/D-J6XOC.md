---
schema: qual/card@1
id: D-J6XOC
kind: definition
title: Path
classification:
  areas:
  - topology
  topics:
  - Connectedness
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space and $I\coloneqq[0,1]$.
A \dfn{path} in $X$ is a [[D-AEAAD|continuous]] map $\gamma\colon I\to X$; it is a path from $\gamma(0)$ to $\gamma(1)$.
A path $\gamma$ is a \dfn{loop} if $\gamma(0) = \gamma(1)$, and then it is a loop based at $\gamma(0)$.
For paths $\gamma, \eta\colon I\to X$ with $\gamma(1) = \eta(0)$, the \dfn{concatenation} $\gamma\cdot\eta\colon I\to X$ is the path
$$
(\gamma\cdot\eta)(s)\coloneqq
\begin{cases}
\gamma(2s) & 0\leq s\leq 1/2, \\
\eta(2s-1) & 1/2\leq s\leq 1.
\end{cases}
$$
:::

::: {.concept}
See [@Hat02] and [@Mun00].
:::
