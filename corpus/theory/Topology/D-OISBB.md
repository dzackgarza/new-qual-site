---
schema: qual/card@1
id: D-OISBB
kind: definition
title: Path lifting property
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $p\colon E\to B$ be a continuous map and $I=[0,1]$.
The map $p$ has the \dfn{path lifting property} if for every [[D-J6XOC|path]] $\gamma\colon I\to B$ and every $e_0\in p\inv(\gamma(0))$ there is a path $\tilde\gamma\colon I\to E$ with $p\circ\tilde\gamma=\gamma$ and $\tilde\gamma(0)=e_0$.
:::

::: {.remark}
Identifying $\pt\times I$ with $I$, this is the [[D-HOCNK|homotopy lifting property]] of $p$ with respect to the one-point space $Y=\pt$.
:::

::: {.proposition}
Let $p\colon\tilde X\to X$ be a [[D-ANO2D|covering space]].
For every path $\gamma\colon I\to X$ and every $\tilde x_0\in p\inv(\gamma(0))$ there is a unique path $\tilde\gamma\colon I\to\tilde X$ with $p\circ\tilde\gamma=\gamma$ and $\tilde\gamma(0)=\tilde x_0$ [@Hat02, Prop. 1.30].
:::
