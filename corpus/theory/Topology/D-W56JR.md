---
schema: qual/card@1
id: D-W56JR
kind: definition
title: Paracompact space
classification:
  areas:
  - topology
  topics:
  - Paracompactness
  - Compactness
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
A **refinement** of an open cover $\mcu \covers X$ is an open cover $\mcv\covers X$ such that for every $V_\beta \in \mcv$, there exists a $U_\alpha \in \mcu$ such that $V_\beta \subseteq U_\alpha$ -- setting $\mcv \leq \mcu$ iff $\mcv$ refines $\mcu$ yields a preorder on all open covers of $X$.

A topological space $X$ is **paracompact** iff every open cover $\mcu\covers X$ admits an locally finite *refinement* -- a division into (potentially more) open subsets $\mcv \covers X$ such that each $x\in X$ is contained in only finitely many $V_\beta$.
:::
