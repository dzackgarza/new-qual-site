---
schema: qual/card@1
id: D-K43GA
kind: definition
title: Contractible space
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
A topological space $X$ is \dfn{contractible} if $\id_X$ is [[D-MGRZP|nullhomotopic]]: there is a point $x_0\in X$ such that $\id_X$ is [[D-Z7I7F|homotopic]] to the constant map $c\colon X\to X$, $c(x) = x_0$.
:::

::: {.proposition}
A topological space $X$ is contractible if and only if $X$ is [[D-HFR32|homotopy equivalent]] to a one-point space $\ts{x_0}$, that is, there are continuous maps $f\colon X\to\ts{x_0}$ and $g\colon\ts{x_0}\to X$ with $f\circ g = \id_{\ts{x_0}}$ and $g\circ f\simeq\id_X$.
:::

::: {.concept}
See [@Hat02, p. 4].
:::
