---
schema: qual/card@1
id: D-XRHTV
kind: definition
title: Topology via open and closed sets
classification:
  areas:
  - topology
  topics:
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ be a set.
A \dfn{topology} on $X$ is a collection $\tau$ of subsets of $X$, the \dfn{open sets}, such that $\emptyset, X\in\tau$, $\tau$ is closed under arbitrary unions, and $\tau$ is closed under finite intersections.
A subset $F\subseteq X$ is \dfn{closed} if $X\sm F\in\tau$.
:::

::: {.proposition}
A collection $\mathcal F$ of subsets of a set $X$ is the collection of closed sets of a topology on $X$ if and only if $\emptyset, X\in\mathcal F$, $\mathcal F$ is closed under arbitrary intersections, and $\mathcal F$ is closed under finite unions.
:::

::: {.example}
An intersection of infinitely many open sets need not be open: in $\RR$, $\Intersect_{n\geq 1} (-1/n, 1/n) = \ts{0}$, which is closed and not open.
:::
