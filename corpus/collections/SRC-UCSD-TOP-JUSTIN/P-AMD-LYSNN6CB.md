---
schema: qual/card@1
id: P-AMD-LYSNN6CB
kind: problem
title: $X$ is contractible iff $\mathrm{id}_X$ is homotopic to a constant
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.problem}
Show that $X$ is homotopy-equivalent to a point $\iff$ $\text{id}_X \simeq g$ for some constant map $g$.
:::

::: {.solution}
<1>1. Suppose $X$ is homotopy-equivalent to a point. Then $\operatorname{id}_X$ is homotopic to a constant map.
::: {.proof}
Let $p:X\to\{*\}$ and $i:\{*\}\to X$ be homotopy inverses. Since $p\circ i=\operatorname{id}_{\{*\}}$ automatically, the other homotopy-inverse relation is
$$
i\circ p\simeq\operatorname{id}_X.
$$
But $i\circ p$ is the constant map with value $i(*)$.
:::

<1>2. Conversely, suppose $\operatorname{id}_X\simeq g$ for a constant map $g(x)=x_0$. Then $X$ is homotopy-equivalent to a point.
::: {.proof}
Let $p:X\to\{*\}$ be the unique map and let $i:\{*\}\to X$ send $*$ to $x_0$. Then
$$
p\circ i=\operatorname{id}_{\{*\}},
$$
while
$$
i\circ p=g\simeq\operatorname{id}_X.
$$
Hence $p$ and $i$ are homotopy inverses.
:::

<1>3. Thus
$$
\boxed{X\simeq *\iff \operatorname{id}_X\text{ is homotopic to a constant map}.}
$$
::: {.proof}
Combine <1>1 and <1>2.
:::
:::
