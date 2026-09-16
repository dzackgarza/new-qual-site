---
schema: qual/card@1
id: D-T5Q3V
kind: definition
title: Loop space
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Function Spaces
  - Fundamental Group
relations: []
review: draft
---

::: {.definition}
Let $(X,x_0)$ be a based space and $s_0\in S^1$ a basepoint.
The \dfn{loop space} of $X$ is the set
$$
\Omega X\coloneqq\ts{\gamma\colon S^1\to X \st \gamma\text{ continuous},\ \gamma(s_0)=x_0}
$$
with the compact-open topology, based at the constant loop at $x_0$ [@Hat02, p. 395].
:::

::: {.proposition}
Let $(X,x_0)$ and $(Y,y_0)$ be based spaces, and write $[-,-]_*$ for based homotopy classes of based maps and $\Sigma$ for reduced suspension.

(a) $\pi_n(\Omega X)\cong\pi_{n+1}(X,x_0)$ for all $n\geq0$.

(b) There is a bijection $[\Sigma X,Y]_*\cong[X,\Omega Y]_*$, natural in $X$ and $Y$.

[@Hat02, p. 395]
:::
