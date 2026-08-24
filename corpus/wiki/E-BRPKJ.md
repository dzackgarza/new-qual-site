---
schema: qual/card@1
id: E-BRPKJ
kind: exercise
title: Where a proof about closures of unions fails
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
---

::: {.exercise title="Munkres §17.7"}

Criticize the following "proof" that $\overline{\bigcup A_\alpha} \subset \bigcup \overline{A}_\alpha$: if $\ts{A_\alpha}$ is a collection of sets in $X$ and if $x \in \overline{\bigcup A_\alpha}$, then every neighborhood $U$ of $x$ intersects $\bigcup A_\alpha$.
Thus $U$ must intersect some $A_\alpha$, so that $x$ must belong to the closure of some $A_\alpha$.
Therefore, $x \in \bigcup \overline{A}_\alpha$.
:::
