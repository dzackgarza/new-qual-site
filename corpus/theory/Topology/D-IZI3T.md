---
schema: qual/card@1
id: D-IZI3T
kind: definition
title: Homotopy class
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
The \dfn{homotopy class} $[f]$ of a continuous map $f\colon X\to Y$ is its equivalence class under the relation $\simeq$ of being [[D-Z7I7F|homotopic]].
The set of homotopy classes of continuous maps $X\to Y$ is
$$
[X, Y]\coloneqq\Hom_{\Top}(X, Y)/\simeq.
$$
:::

::: {.proposition}
If $f, g\colon X\to Y$ are homotopic, then $f_* = g_*\colon H_n(X)\to H_n(Y)$ for every $n$.
:::

::: {.remark}
For a based space $(Y, y_0)$ and $n\geq 1$, the [[D-EUX36|homotopy group]] $\pi_n(Y, y_0)$ is the set $[(S^n, s_0), (Y, y_0)]$ of homotopy classes of based maps under homotopies fixing the basepoint.
:::

::: {.concept}
See [@Hat02, p. 3 and Theorem 2.10].
:::
