---
schema: qual/card@1
id: FD-PLAEO
kind: definition
title: Composition series of a group
prompts:
- What is a composition series of a group $G$?
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Simple Groups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group.
A \dfn{composition series} of $G$ is a finite sequence of subgroups
$$
1=N_{0} \leq N_{1} \leq \cdots \leq N_{k-1} \leq N_{k}=G
$$
such that $N_i \normal N_{i+1}$ and $N_{i+1}/N_i$ is [[FD-2UWAQ|simple]] for $0\leq i<k$.
The quotients $N_{i+1}/N_i$ are the \dfn{composition factors} of the series.
:::
