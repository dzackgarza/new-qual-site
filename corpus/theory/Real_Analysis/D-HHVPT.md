---
schema: qual/card@1
id: D-HHVPT
kind: definition
title: Continuity and uniform continuity
classification:
  areas:
  - real-analysis
  topics:
  - Continuity
  - Uniform Continuity
relations: []
review: draft
---

::: {.definition}
Let $X\subseteq\RR$ and let $f\colon X\to \RR$.

- The function $f$ is \dfn{continuous} on $X$ if
$$
\forall x_0\in X \quad \forall \varepsilon>0 \quad \exists \delta=\delta(\varepsilon, x_0)>0 \quad \forall y\in X: \quad \abs{x_0 - y} < \delta \implies \abs{f(x_0) - f(y)} < \varepsilon.
$$

- The function $f$ is \dfn{uniformly continuous} on $X$ if
$$
\forall \varepsilon>0 \quad \exists \delta=\delta(\varepsilon)>0 \quad \forall x, y \in X: \quad \abs{x - y} < \delta \implies \abs{f(x) - f(y)} < \varepsilon.
$$
:::

::: {.remark}
Substituting $y = x_0 + h$, the two conditions read
$$
\begin{aligned}
&\forall x_0\in X \quad \forall \varepsilon>0 \quad \exists \delta(\varepsilon, x_0)>0 \quad \forall h \text{ with } x_0+h\in X: && \abs{h} < \delta \implies \abs{f(x_0) - f(x_0 + h)} < \varepsilon, \\
&\forall \varepsilon>0 \quad \exists \delta(\varepsilon)>0 \quad \forall x\in X \quad \forall h \text{ with } x+h\in X: && \abs{h} < \delta \implies \abs{f(x) - f(x + h)} < \varepsilon.
\end{aligned}
$$
In the first, $\delta$ may depend on the point $x_0$; in the second, one $\delta$ serves every point of $X$.
:::
