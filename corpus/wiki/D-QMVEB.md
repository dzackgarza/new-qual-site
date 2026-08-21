---
schema: qual/card@1
id: D-QMVEB
kind: definition
title: Normal Core of a subgroup
classification:
  areas:
  - algebra
  topics:
  - Normal Subgroups
  - Subgroups
  - Group Actions
relations: []
review: draft
---

:::{.definition title="Normal Core of a subgroup"}
The largest normal subgroup of $G$ contained in $H$:
\[
H_G = \Intersect_{g\in G} gHg^{-1} = \gens{ N: N \normal G ~\&~ N \leq H} = \ker \psi
.\]
where
\[
\psi: G &\to \Aut(G/H) \\
g &\mapsto (xH\mapsto gxH)
\]
:::
