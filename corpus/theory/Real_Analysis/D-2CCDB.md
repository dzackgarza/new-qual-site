---
schema: qual/card@1
id: D-2CCDB
kind: definition
title: Equicontinuity and uniform equicontinuity
prompts:
- What must hold uniformly over the family for $\mcf$ to be equicontinuous at $x_0$?
- What does it mean for a family $\mcf$ to be equicontinuous at $x_0$?
- What is equicontinuity? Uniform equicontinuity?
classification:
  areas:
  - real-analysis
  topics:
  - Equicontinuity
  - Function Spaces
  - Metric Spaces
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, let $x_0\in X$, and let $\mcf\subseteq C(X)$ be a family of [[D-AEAAD|continuous]] functions $X\to\CC$.
The family $\mcf$ is \dfn{equicontinuous at $x_0$} if
$$
\forall \varepsilon > 0 \quad \exists \text{ an open set } U \ni x_0 \quad \forall x\in U \quad \forall f\in \mcf: \quad \abs{f(x) - f(x_0)} < \varepsilon.
$$

Now let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces and let $\mcf$ be a family of functions $X\to Y$.

- The family $\mcf$ is \dfn{equicontinuous at $x_0\in X$} if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x), f(x_0)) < \varepsilon$ for all $f\in\mcf$ and all $x\in X$ with $d_X(x, x_0) < \delta$.

- The family $\mcf$ is \dfn{uniformly equicontinuous} if for every $\varepsilon > 0$ there exists $\delta > 0$ such that $d_Y(f(x_1), f(x_2)) < \varepsilon$ for all $f\in\mcf$ and all $x_1, x_2\in X$ with $d_X(x_1, x_2) < \delta$.
:::

::: {.remark}
For a metric space $X$ and $Y=\CC$, the two definitions of equicontinuity at $x_0$ agree, since the balls about $x_0$ form a neighborhood base.
In equicontinuity at $x_0$ the number $\delta$ depends on $\varepsilon$ and $x_0$ but not on $f\in\mcf$; in uniform equicontinuity one $\delta$ depending only on $\varepsilon$ serves every $f\in\mcf$ and every pair of points of $X$.
:::
