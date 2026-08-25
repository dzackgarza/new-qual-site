---
schema: qual/card@1
id: E-A7HJX
kind: exercise
title: Kernels under surjective composites of homomorphisms
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
relations: []
review: draft
---

::: {.exercise title="Munkres §73.3"}

Lemma.
Let $f: G \to H$ and $g: H \to K$ be homomorphisms; assume $f$ is surjective.
If $x_0 \in G$, and if $\ker g$ is the least normal subgroup of $H$ containing $f(x_0)$, then $\ker(g \circ f)$ is the least normal subgroup $N$ of $G$ containing $\ker f$ and $x_0$.

Proof.
Show that $f(N)$ is normal; conclude that $\ker(g \circ f) = f^{-1}(\ker g) \subset f^{-1}f(N) = N$.
:::
