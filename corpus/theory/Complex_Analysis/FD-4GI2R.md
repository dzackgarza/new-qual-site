---
schema: qual/card@1
id: FD-4GI2R
kind: definition
title: Equicontinuity
prompts:
- What does it mean for a family of functions to be equicontinuous?
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
The family $\{f_n\}$ is \dfn{equicontinuous} on $S$ if for every $\varepsilon>0$ there exists $\delta>0$, depending only on $\varepsilon$, such that for all $x,y\in S$,
$$
\abs{x-y}<\delta\implies\abs{f_n(x)-f_n(y)}<\varepsilon\qquad\text{for all } n\ge1.
$$
:::
