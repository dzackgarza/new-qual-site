---
schema: qual/card@1
id: D-WGYSB
kind: definition
title: Continuity and uniform continuity in metric spaces
prompts:
- 'What does it mean for $f\colon (X, d_X) \to (Y, d_Y)$ to be uniformly continuous?'
classification:
  areas:
  - topology
  - real-analysis
  topics:
  - Uniform Continuity
  - Metric Spaces
  - Continuity
relations: []
review: draft
---

::: {.definition}
Let $(X, d_X)$ and $(Y, d_Y)$ be metric spaces and let $f\colon X\to Y$.

- The map $f$ is \dfn{continuous} if for every $x_0\in X$ and every $\varepsilon>0$ there exists $\delta=\delta(\varepsilon,x_0)>0$ such that for all $y\in X$,
$$
d_X(x_0, y) < \delta \implies d_Y(f(x_0), f(y)) < \varepsilon.
$$

- The map $f$ is \dfn{uniformly continuous} if for every $\varepsilon > 0$ there exists $\delta=\delta(\varepsilon) > 0$ such that for all $x_1, x_2\in X$,
$$
d_X(x_1, x_2) < \delta \implies d_Y(f(x_1), f(x_2)) < \varepsilon.
$$
:::

::: {.remark title="Variations"}
For $X\subseteq\RR$ and $Y=\RR$, substituting $y = x_0 + h$ the two conditions read
$$
\begin{aligned}
&\forall x_0\in X \quad \forall \varepsilon>0 \quad \exists \delta(\varepsilon, x_0)>0 \quad \forall h \text{ with } x_0+h\in X: && \abs{h} < \delta \implies \abs{f(x_0) - f(x_0 + h)} < \varepsilon, \\
&\forall \varepsilon>0 \quad \exists \delta(\varepsilon)>0 \quad \forall x\in X \quad \forall h \text{ with } x+h\in X: && \abs{h} < \delta \implies \abs{f(x) - f(x + h)} < \varepsilon.
\end{aligned}
$$
In the first, $\delta$ may depend on the point $x_0$; in the second, one $\delta$ serves every point of $X$.
:::
