---
schema: qual/card@1
id: P-AGH326COLIMINJECTIVE
kind: problem
title: Direct limits of injective sheaves on a noetherian space are injective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cohomology
  - Injective Sheaves
  - Noetherian Spaces
relations: []
review: draft
---

::: problem
Let $X$ be a noetherian topological space, and let $\ts{\mci_\alpha}_{\alpha \in A}$ be a direct system of injective sheaves of abelian groups on $X$.
Then $\colim_\alpha \mci_\alpha$ is also injective.

Hints: First show that a sheaf $\mci$ is injective if and only if for every open set $U \subseteq X$, and for every subsheaf $\mcr \subseteq \ZZ_U$, and for every map $f: \mcr \to \mci$, there exists an extension of $f$ to a map $\ZZ_U \to \mci$.
Secondly, show that any such sheaf $\mcr$ is finitely generated, so any map $\mcr \to \colim_\alpha \mci_\alpha$ factors through one of the $\mci_\alpha$.
:::
