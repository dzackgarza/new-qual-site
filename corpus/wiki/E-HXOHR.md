---
schema: qual/card@1
id: E-HXOHR
kind: exercise
title: "Let $X$ be a compact space and let $A$ be a closed subspace."
classification:
  areas:
  - topology
  topics:
  - compactness
relations: []
review: draft
solved: true
---

Let $X$ be a compact space and let $A$ be a closed subspace.
Show that $A$ is compact.

::: {.solution}
::: {.concept}
:::
Let $X$ be compact, $A\subset X$ closed, and $\theset{U_\alpha} \covers A$ be an open cover.
By definition of the subspace topology, each $U_\alpha = V_\alpha \intersect A$ for some open $V_\alpha \subset X$, and $A\subset \union_\alpha V_\alpha$.
Since $A$ is closed in $X$, $X\setminus A$ is open.
Then $\theset{V_\alpha}\union \theset{X\setminus A}\covers X$ is an open cover, since every point is either in $A$ or $X\setminus A$.
By compactness of $X$, there is a finite subcover $\theset{U_j \suchthat j\leq N}\union \theset{X\setminus A}$ Then $\qty{\theset{U_j} \union \theset{X\setminus A}} \intersect A \definedas \theset{V_j}$ is a finite cover of $A$.
:::
