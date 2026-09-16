---
schema: qual/card@1
id: D-5Y4MC
kind: definition
title: Equicontinuous family
classification:
  areas:
  - complex-analysis
  topics:
  - Equicontinuity
  - Sequences of Functions
relations: []
review: draft
---

::: {.definition}
Let $S\subseteq\CC$ and let $(f_n)_{n\ge1}$ be a sequence of functions $f_n\colon S\to\CC$.
The family $\{f_n\}$ is \dfn{equicontinuous} on $S$ if for every $\varepsilon>0$ there exists $\delta>0$ such that
$$
\abs{f_n(x)-f_n(y)}<\varepsilon\qquad\text{for all } n\ge1 \text{ and all } x,y\in S \text{ with } \abs{x-y}<\delta.
$$
:::

::: {.remark}
The number $\delta$ depends only on $\varepsilon$, not on $n$, $x$, or $y$.
[@Rud76] states this definition for families of complex functions on a subset of a metric space.
:::
