---
schema: qual/card@1
id: FD-2XUJ5
kind: definition
title: Locally homeomorphic
prompts:
- What does it mean for $X$ to be locally homeomorphic to $Y$?
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
$X$ is *locally homeomorphic* to $Y$ iff every $x\in X$ admits a neighborhood $U_x$ that is homeomorphic to an open subset of $Y$.

Note that $X$ being locally homeomorphic to $Y$ does *not* imply that there exists a local homeomorphism, which needs to be a single map.

Counterexample: $S^2$ locally homeomorphic to $\RR^2$, but there is no single local homeomorphism $f:S^2 \to \RR$.
:::
