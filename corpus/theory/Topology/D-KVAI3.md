---
schema: qual/card@1
id: D-KVAI3
kind: definition
title: Homotopy extension property
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Cell Complexes
  - Retracts
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space, $A\subseteq X$ a subspace, and $I = [0,1]$.
The pair $(X, A)$ has the \dfn{homotopy extension property} if for every space $Y$, every continuous map $f_0\colon X\to Y$, and every [[D-SOVXO|homotopy]] $g_t\colon A\to Y$ with $g_0 = f_0|_A$, there is a homotopy $f_t\colon X\to Y$ starting at $f_0$ with $f_t|_A = g_t$ for all $t\in I$.
Equivalently, every pair of continuous maps $X\times\ts{0}\to Y$ and $A\times I\to Y$ that agree on $A\times\ts{0}$ extends to a continuous map $X\times I\to Y$.
:::

::: {.proposition}
If $A$ is closed in $X$, then $(X, A)$ has the homotopy extension property if and only if $X\times\ts{0}\cup A\times I$ is a [[D-6FSWY|retract]] of $X\times I$.
:::

::: {.proposition}
Every CW pair $(X, A)$ has the homotopy extension property.
:::

::: {.concept}
See [@Hat02, p. 14, and Proposition 0.16, p. 15].
:::
