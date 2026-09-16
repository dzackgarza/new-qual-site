---
schema: qual/card@1
id: FD-TGBYP
kind: definition
title: Equicontinuous families
prompts:
- What does it mean for a family $\mathcal{F}$ to be equicontinuous at $x_0$?
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
Let $(X,d_X)$ and $(Y,d_Y)$ be metric spaces, let $x_0\in X$, and let $\mathcal{F}$ be a family of functions $X\to Y$.

- The family $\mathcal{F}$ is \dfn{equicontinuous at $x_0$} if for every $\varepsilon > 0$ there exists $\delta=\delta(\varepsilon, x_0)>0$ such that for all $x\in X$ and all $f\in\mathcal{F}$,
$$
x\in B_\delta(x_0) \implies f(x) \in B_\varepsilon(f(x_0)).
$$

- The family $\mathcal{F}$ is \dfn{uniformly equicontinuous} if for every $\varepsilon>0$ there exists $\delta=\delta(\varepsilon)>0$ such that for all $x_1,x_2\in X$ and all $f\in\mathcal{F}$,
$$
x_1\in B_\delta(x_2) \implies f(x_1) \in B_\varepsilon(f(x_2)).
$$
:::
