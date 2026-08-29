---
schema: qual/card@1
id: E-4NU4A
kind: exercise
title: Injective continuous maps from compact spaces to Hausdorff spaces are embeddings
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Hausdorff Spaces
  - Homeomorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: exercise
Show that an injective continuous map from a compact space to a Hausdorff space is an embedding (a homeomorphism onto its image).
:::

::: solution
**Goal:** Prove that if $f: X \to Y$ is a continuous injection from a compact topological space $X$ into a Hausdorff topological space $Y$, then $f$ is a topological embedding (i.e. a homeomorphism from $X$ onto its subspace image $f(X)$).

<1>1. Bijectivity and continuity of the corestriction: *Proof:* <2>1. The map $f: X \to f(X)$ is surjective onto its image by construction.
<2>2. Since $f: X \to Y$ is injective, $f: X \to f(X)$ is a bijection.
<2>3. Since $f: X \to Y$ is continuous, the corestriction $f: X \to f(X)$ is continuous with respect to the subspace topology on $f(X) \subseteq Y$.

<1>2. Closedness of the map: For any closed subset $C \subseteq X$, its image $f(C)$ is closed in $Y$ (and hence closed in the subspace $f(X)$). *Proof:* <2>1. Let $C$ be a closed subset of $X$.
<2>2. Since $X$ is compact and $C$ is a closed subspace of $X$, $C$ is compact.
<2>3. Because continuous maps preserve compactness, $f(C)$ is a compact subset of $Y$.
<2>4. Since $Y$ is a Hausdorff space, every compact subset of $Y$ is closed in $Y$.
<2>5. Thus $f(C)$ is closed in $Y$, and consequently $f(C) = f(C) \cap f(X)$ is closed in the subspace topology of $f(X)$.

<1>3. Continuity of the inverse and embedding conclusion: *Proof:* <2>1. The inverse map $f^{-1}: f(X) \to X$ satisfies $(f^{-1})^{-1}(C) = f(C)$ for every closed subset $C \subseteq X$.
<2>2. By <1>2, $(f^{-1})^{-1}(C)$ is closed in $f(X)$ whenever $C$ is closed in $X$, which proves that $f^{-1}: f(X) \to X$ is continuous.
<2>3. Because $f: X \to f(X)$ is a continuous bijection with a continuous inverse, it is a homeomorphism.
<2>4. Therefore, $f: X \to Y$ is a topological embedding.
Q.E.D.
:::
