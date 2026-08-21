---
schema: qual/card@1
id: P-AMD-D4G4SW2S
kind: problem
title: 'Given: $H \subseteq G, P \in \text{Syl}_p(G)$'
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Conjugacy
  - Subgroups
relations: []
review: draft
solved: false
---

::: {.problem}
Given: $H \subseteq G, P \in \text{Syl}_p(G)$

Show: $\exists g \in G \ni gPg^{-1} \cap H \in \text{Syl}_p(H)$

> The intersection with $H$ is needed.
> $gPg^{-1}$ has the full $p\dash$part of $\abs G$ as its order and need not be contained in $H$ at all, so it is a Sylow $p\dash$subgroup of $H$ only in the case $\abs H$ and $\abs G$ share that $p\dash$part.

Given: $H \normal G$

Show: $P\cap H \in \text{Syl}_p(H)$

Given: $P  \normal G$

Show: $P \cap H \in \text{Syl}_p(H)$ and $|\text{Syl}_p(H)| = 1$
:::
