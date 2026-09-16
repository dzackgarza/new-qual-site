---
schema: qual/card@1
id: D-2MJRE
kind: definition
title: Nowhere dense sets
classification:
  areas:
  - real-analysis
  topics:
  - Density
  - Closure
relations: []
review: draft
---

::: {.definition}
Let $X$ be a topological space.
A subset $S\subseteq X$ is \dfn{nowhere dense} in $X$ if its [[D-ASXW6|closure]] $\overline{S}$ has empty interior, that is, no nonempty open subset of $X$ is contained in $\overline{S}$.
:::

::: {.remark}
Equivalently, every nonempty open set $U\subseteq X$ contains a nonempty open set $V$ with $V\cap S=\emptyset$, so $S$ is not [[D-KJBAK|dense]] in any nonempty open subset of $X$.
Indeed, if $\overline{S}$ has empty interior then $V\coloneqq U\setminus\overline{S}$ is nonempty and open; conversely, a nonempty open $W\subseteq\overline{S}$ contains no nonempty open set disjoint from $S$.
For $X=\RR$, $S$ is nowhere dense if and only if every open interval contains an open subinterval disjoint from $S$.
:::
