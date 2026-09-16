---
schema: qual/card@1
id: FD-ST7TD
kind: definition
title: Uniform continuity
prompts:
- 'What does it mean for $f: (X, d_1) \to (Y, d_2)$ to be uniformly continuous?'
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
Let $(X, d_1)$ and $(Y, d_2)$ be metric spaces.
A function $f\colon X \to Y$ is \dfn{uniformly continuous} if for every $\varepsilon > 0$ there exists $\delta=\delta(\varepsilon) > 0$ such that for all $x,y\in X$,
$$
x\in B_\delta(y) \implies f(x) \in B_\varepsilon(f(y)).
$$
:::

::: {.remark}
In the $\varepsilon$-$\delta$ formulation of [[D-HHVPT|continuity]], $\delta$ may depend on the point $y$; uniform continuity requires one $\delta$ for all $y\in X$.
:::
