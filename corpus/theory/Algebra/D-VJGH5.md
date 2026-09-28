---
schema: qual/card@1
id: D-VJGH5
kind: definition
title: Index of a subgroup
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group and $H\leq G$ a [[D-IQ4OX|subgroup]].
The \dfn{index} of $H$ in $G$, written $[G:H]$, is the cardinality of the set $G/H=\theset{gH \st g\in G}$ of left cosets of $H$.
:::

::: {.remark}
The map $gH\mapsto Hg^{-1}$ is a well-defined bijection from left cosets to right cosets, since $g_1H=g_2H$ if and only if $g_2^{-1}g_1\in H$ if and only if $Hg_1^{-1}=Hg_2^{-1}$.
So $[G:H]$ is also the number of right cosets of $H$.
:::
