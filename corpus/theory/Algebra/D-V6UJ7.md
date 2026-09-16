---
schema: qual/card@1
id: D-V6UJ7
kind: definition
title: Group presentation
classification:
  areas:
  - algebra
  topics:
  - Group Presentations
  - Free Groups
  - Normal Subgroups
relations: []
review: draft
---

::: {.definition}
Let $S$ be a set, let $F[S]$ be the free group on $S$, and let $R\subseteq F[S]$ be a set of words in $S$.
The group \dfn{presented} by generators $S$ and relations $R$ is
$$
\gens{S \st R} \coloneqq F[S] / \cl_n(R),
$$
where $\cl_n(R)$ is the [[D-BPRD3|normal closure]] of $R$ in $F[S]$, the smallest [[D-EKE4Q|normal subgroup]] of $F[S]$ containing $R$.
A \dfn{presentation} of a group $G$ is an isomorphism $G\cong\gens{S \st R}$.
:::
