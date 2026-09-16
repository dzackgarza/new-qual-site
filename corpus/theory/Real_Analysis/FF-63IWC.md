---
schema: qual/card@1
id: FF-63IWC
kind: fact
title: Equicontinuity and uniform equicontinuity
prompts:
- What is equicontinuity? Uniform equicontinuity?
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Metric Spaces
relations: []
review: draft
---

::: {.fact}
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces, let $\mcf$ be a family of functions $X\to Y$, and let $x_0\in X$.

- $\mcf$ is [[FD-XVMEE|equicontinuous at $x_0$]] if and only if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x), f(x_0)) < \varepsilon$ for all $f\in\mcf$ and all $x\in X$ with $d_X(x, x_0) < \delta$.

- $\mcf$ is [[FD-XVMEE|uniformly equicontinuous]] if and only if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x_1), f(x_2)) < \varepsilon$ for all $f\in\mcf$ and all $x_1, x_2\in X$ with $d_X(x_1, x_2) < \delta$.
:::
