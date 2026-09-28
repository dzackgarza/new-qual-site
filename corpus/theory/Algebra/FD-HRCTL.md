---
schema: qual/card@1
id: FD-HRCTL
kind: definition
title: Normalizer $N_G(S)$ of a subset
prompts:
- What is the normalizer $N_G(S)$?
classification:
  areas:
  - algebra
  topics:
  - Centralizers and Normalizers
  - Subgroups
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group and $S\subseteq G$ a subset, and for $g\in G$ write $gSg^{-1}\coloneqq\theset{gsg^{-1} \st s\in S}$.
The \dfn{normalizer} of $S$ in $G$ is
$$
N_G(S) \coloneqq \theset{g\in G \st gSg^{-1} = S}.
$$
:::
