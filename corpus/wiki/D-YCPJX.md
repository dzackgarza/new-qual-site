---
schema: qual/card@1
id: D-YCPJX
kind: definition
title: "Orientation of a manifold"
classification:
  areas:
  - topology
  topics: []
relations: []
review: draft
---
:::{.definition title="Orientation of a manifold"}
A family of $\theset{\mu_{x}}_{x\in M}$ with local consistency: if $x,y \in U$ then $\mu_{x}, \mu_{y}$ are related via a propagation.

Formally, a function $$M^n \to \coprod_{x\in M} H(X \mid \theset{x})\\ x \mapsto \mu_{x}$$ such that $\forall x \exists N_{x}$ in which  $\forall y\in N_{x}$, the preimage of each $\mu_{y}$ under the map $H_{n}(M\mid N_{x}) \surjects H_{n}(M\mid y)$ is a single generator $\mu_{N_{x}}$.

TFAE:

- $M$ is orientable.
- The map $W: (M, x) \to \ZZ_{2}$ is trivial.
- $\tilde M_{o} = M \coprod \ZZ_{2}$ (two sheets).
- $\tilde M_{o}$ is disconnected
- The projection $\tilde M_{o} \to M$ admits a section.

:::
