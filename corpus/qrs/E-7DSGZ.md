---
schema: qual/card@1
id: E-7DSGZ
kind: exercise
title: "Show that an injective continuous map from a compact space\u2026"
classification:
  areas:
  - topology
  topics:
  - compactness
  - hausdorff-spaces
  - homeomorphisms
relations: []
review: draft
solved: true
---

::: exercise
Show that an injective continuous map from a compact space to a Hausdorff space is an embedding (a homeomorphism onto its image).
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that an injective continuous map $f: X \to Y$ from a compact space $X$ to a Hausdorff space $Y$ is an embedding: a homeomorphism onto its image.

<1>1. $f: X \to f(X)$ is a continuous bijection.
Proof: $f$ is injective by hypothesis, so viewed as a map onto its image it is bijective; continuity is inherited.

<1>2. $f(X)$ is Hausdorff.
Proof: Subspaces of Hausdorff spaces are Hausdorff, and $Y$ is Hausdorff.

<1>3. $f$ maps closed sets to closed sets (in $f(X)$). <2>1. Let $C \subseteq X$ be closed; then $C$ is compact.
Proof: Closed subsets of compact spaces are compact.
<2>2. $f(C)$ is compact in $Y$.
Proof: Continuous images of compact sets are compact.
<2>3. $f(C)$ is closed in $Y$, hence closed in $f(X)$.
Proof: Compact subsets of Hausdorff spaces are closed; and closed in $Y$ implies closed in the subspace $f(X)$.

<1>4. $f^{-1}: f(X) \to X$ is continuous.
Proof: A bijective map is a homeomorphism iff it is a closed map (equivalently: $f^{-1}$ is continuous iff for every closed $C \subseteq X$, $(f^{-1})^{-1}(C) = f(C)$ is closed in $f(X)$), and <1>3 gives closedness.

<1>5. Q.E.D. Proof: <1>1 and <1>4 show $f: X \to f(X)$ is a homeomorphism, i.e. $f$ is an embedding.
:::
