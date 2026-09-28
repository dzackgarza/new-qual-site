---
schema: qual/card@1
id: D-GDXFZ
kind: definition
title: Proper map
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuity
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
A [[D-AEAAD|continuous]] map $f\colon X\to Y$ is \dfn{proper} if $f\inv(K)$ is [[D-EILKJ|compact]] for every compact $K\subseteq Y$.
:::

::: {.proposition}
Let $f\colon X\to Y$ be a continuous map.

(a) If $Y$ is Hausdorff and [[D-5EOQZ|locally compact]], then $f$ is proper if and only if $f$ is a [[D-METXE|closed map]] and $f\inv(\ts{y})$ is compact for every $y\in Y$.

(b) If $X$ is Hausdorff and $Y$ is Hausdorff and locally compact, then $f$ is proper if and only if $f$ is universally closed: for every topological space $Z$, the map $f\times\id_Z\colon X\times Z\to Y\times Z$ is a closed map.

(c) If $X$ is a metric space, then $f$ is proper if and only if for every sequence $(x_k)_{k\geq1}$ in $X$ such that each compact subset of $X$ contains $x_k$ for only finitely many $k$, each compact subset of $Y$ contains $f(x_k)$ for only finitely many $k$.
:::

::: {.concept}
[@Lee12].
:::
