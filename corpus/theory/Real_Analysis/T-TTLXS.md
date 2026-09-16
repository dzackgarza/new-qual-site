---
schema: qual/card@1
id: T-TTLXS
kind: theorem
title: Closed graph theorem
classification:
  areas:
  - real-analysis
  topics:
  - Functional Analysis
  - Continuity
relations: []
review: draft
---

::: {.theorem}
Let $X$ and $Y$ be [[D-BG455|Banach spaces]] over the same field $\RR$ or $\CC$, and let $T\colon X\to Y$ be a linear map whose graph
$$
\Gamma(T)\coloneqq\theset{(x,Tx)\suchthat x\in X}\subseteq X\times Y
$$
is closed in $X\times Y$ with the product topology.
Then $T$ is bounded: there exists $C\geq0$ with $\norm{Tx}_Y\leq C\norm{x}_X$ for all $x\in X$.
:::
