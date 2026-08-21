---
schema: qual/card@1
id: D-JDDCP
kind: definition
title: Free Product
classification:
  areas:
  - topology
  topics:
  - Groups
  - van Kampen
relations: []
review: draft
---

::: {.definition title="Free Product"}
For a family of groups $\ts{G_\alpha}$, the **free product** $\ast_\alpha G_\alpha$ consists of reduced words $g_1 g_2 \cdots g_k$ with each $g_i \in G_\alpha \sm \ts{1}$ for some $\alpha$ and consecutive letters in different factors, multiplied by concatenation followed by reduction.
It is the coproduct in $\Grp$: homomorphisms $\varphi_\alpha: G_\alpha \to H$ extend to a unique $\varphi: \ast_\alpha G_\alpha \to H$.
A free group on a set $S$ is $\ast_{s\in S}\ZZ$.
:::

::: {.concept}
See Hatcher, §1.2, p. 41.
:::
