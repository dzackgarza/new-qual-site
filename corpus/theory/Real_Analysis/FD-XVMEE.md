---
schema: qual/card@1
id: FD-XVMEE
kind: definition
title: Equicontinuous and uniformly equicontinuous families
prompts:
- What must hold uniformly over the family for $\mcf$ to be equicontinuous at $x_0$?
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Metric Spaces
relations:
- kind: variant-of
  target: FD-TGBYP
review: draft
---

::: {.definition}
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces, let $\mcf$ be a family of functions $X\to Y$, and let $x_0\in X$.

- The family $\mcf$ is \dfn{equicontinuous at $x_0$} if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x), f(x_0)) < \varepsilon$ for all $f\in\mcf$ and all $x\in X$ with $d_X(x, x_0) < \delta$.

- The family $\mcf$ is \dfn{uniformly equicontinuous} if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x_1), f(x_2)) < \varepsilon$ for all $f\in\mcf$ and all $x_1, x_2\in X$ with $d_X(x_1, x_2) < \delta$.
:::

::: {.remark}
In equicontinuity at $x_0$ the number $\delta$ depends on $\varepsilon$ and $x_0$ but not on $f\in\mcf$; in uniform equicontinuity one $\delta$ depending only on $\varepsilon$ serves every $f\in\mcf$ and every pair of points of $X$.
:::
