---
schema: qual/card@1
id: D-2CCDB
kind: definition
title: Equicontinuity at a point
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Function Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, let $x\in X$, and let $\mathcal F\subseteq C(X)$ be a family of [[D-AEAAD|continuous]] functions $X\to\CC$.
The family $\mathcal F$ is \dfn{equicontinuous at $x$} if
$$
\forall \varepsilon > 0 \quad \exists \text{ an open set } U \ni x \quad \forall y\in U \quad \forall f\in \mathcal{F}: \quad \abs{f(y) - f(x)} < \varepsilon.
$$
:::
