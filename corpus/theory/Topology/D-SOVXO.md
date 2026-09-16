---
schema: qual/card@1
id: D-SOVXO
kind: definition
title: Homotopy
classification:
  areas:
  - topology
  topics:
  - Homotopy
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces, let $I=[0,1]$, and let $f,g\colon X\to Y$ be [[D-AEAAD|continuous maps]].
A \dfn{homotopy} from $f$ to $g$ is a continuous map $F\colon X\times I\to Y$ with
$$
F(x,0)=f(x)\quad\text{and}\quad F(x,1)=g(x)\qquad\text{for all }x\in X.
$$
If a homotopy from $f$ to $g$ exists, $f$ and $g$ are \dfn{homotopic}, written $f\simeq g$ [@Hat02, p. 3].
:::

::: {.proposition}
Homotopy is an equivalence relation on the set $C(X,Y)$ of continuous maps $X\to Y$ [@Hat02, p. 3].
The set of equivalence classes is denoted $[X,Y]\coloneqq C(X,Y)/{\simeq}$.
:::
