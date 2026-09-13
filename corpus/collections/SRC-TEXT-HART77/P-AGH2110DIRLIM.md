---
schema: qual/card@1
id: P-AGH2110DIRLIM
kind: problem
title: Direct limits of sheaves are the sheafification of the sectionwise limit
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Direct Limits
  - Universal Properties
relations: []
review: draft
---

::: problem
Let $\ts{\mcf_i}$ be a direct system of sheaves and morphisms on $X$.
Define the direct limit of the system, denoted $\varinjlim \mcf_i$, to be the sheaf associated to the presheaf $U \mapsto \varinjlim \mcf_i(U)$.

Show that this is a direct limit in the category of sheaves on $X$: given a sheaf $\mcg$ and a collection of morphisms $\mcf_i \to \mcg$ compatible with the maps of the direct system, there exists a unique map $\varinjlim \mcf_i \to \mcg$ such that for each $i$ the original map $\mcf_i \to \mcg$ is the composite $\mcf_i \to \varinjlim \mcf_i \to \mcg$.
:::
