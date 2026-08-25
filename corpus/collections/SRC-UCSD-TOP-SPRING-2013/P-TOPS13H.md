---
schema: qual/card@1
id: P-TOPS13H
kind: problem
title: "Mayer-Vietoris exact sequence for the double mapping cylinder"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Exact Sequences
  - Mapping Cylinder
relations: []
review: draft
---

::: problem
Let $X$, $Y$ and $Z$ be spaces, and let $f : X \to Y$, $g : X \to Z$ be continuous maps.
Define the double mapping cylinder $D$ to be the quotient of the disjoint union of $X \times [0, 1]$, $Y$ and $Z$ via the equivalence relation $(x, 0) \sim f(x)$, $(x, 1) \sim g(x)$.
Show there is an exact sequence
$$
\cdots \to H_q(X) \to H_q(Y) \oplus H_q(Z) \to H_q(D) \to H_{q-1}(X) \to \cdots.
$$
:::
