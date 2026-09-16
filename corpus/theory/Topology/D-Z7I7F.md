---
schema: qual/card@1
id: D-Z7I7F
kind: definition
title: Homotopic maps
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces, $I = [0,1]$, and $f, g\colon X\to Y$ continuous maps.
The maps $f$ and $g$ are \dfn{homotopic}, written $f\homotopic g$, if there is a continuous map $H\colon X\cross I \to Y$ with $H(x, 0) = f(x)$ and $H(x, 1) = g(x)$ for all $x\in X$.
Two [[D-J6XOC|paths]] $\gamma, \eta\colon I\to X$ with $\gamma(0) = \eta(0)$ and $\gamma(1) = \eta(1)$ are \dfn{homotopic rel endpoints} if there is a continuous map $H\colon I\cross I\to X$ with $H(s, 0) = \gamma(s)$, $H(s, 1) = \eta(s)$, $H(0,t) = \gamma(0)$, and $H(1,t) = \gamma(1)$ for all $s, t\in I$.
:::

::: {.proposition}
Homotopy is an equivalence relation on the set of continuous maps $X\to Y$, and homotopy rel endpoints is an equivalence relation on the set of paths in $X$ with given endpoints.
:::

::: {.remark}
The [[D-EBNUE|fundamental group]] $\pi_1(X, x_0)$ is the set of classes of loops at $x_0$ under homotopy rel endpoints.
:::

::: {.concept}
[@Hat02]; [@Mun00].
:::
