---
schema: qual/card@1
id: D-HOCNK
kind: definition
title: Homotopy lifting property
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
relations: []
review: draft
---

::: {.definition}
Let $p\colon E\to B$ be a continuous map and $Y$ a topological space.
The map $p$ has the \dfn{homotopy lifting property} with respect to $Y$ if for every [[D-Z7I7F|homotopy]] $g_t\colon Y\to B$, $t\in[0,1]$, and every continuous $\tilde g_0\colon Y\to E$ with $p\circ\tilde g_0 = g_0$, there is a homotopy $\tilde g_t\colon Y\to E$ starting at $\tilde g_0$ with $p\circ\tilde g_t = g_t$ for all $t$.
The map $p$ is a \dfn{fibration} if it has the homotopy lifting property with respect to every space $Y$.
:::

::: {.proposition}
A [[D-ANO2D|covering space]] $p\colon\tilde X\to X$ has the homotopy lifting property with respect to every space $Y$, and the lifted homotopy $\tilde g_t$ starting at a given $\tilde g_0$ is unique.
:::

::: {.concept}
See [@Hat02, p. 60, Proposition 1.30, and p. 375].
:::
