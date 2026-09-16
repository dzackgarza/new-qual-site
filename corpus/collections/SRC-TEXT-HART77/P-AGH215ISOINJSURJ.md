---
schema: qual/card@1
id: P-AGH215ISOINJSURJ
kind: problem
title: A morphism of sheaves is an isomorphism exactly when it is injective and surjective
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves
  - Exact Sequences
  - Stalks
relations: []
review: draft
---

::: {.problem}
Show that a morphism of sheaves is an isomorphism if and only if it is both injective and surjective.
:::

::: {.solution}
Let $\phi: \mcf \to \mcg$ be a morphism of sheaves.
Being injective and surjective says exactly that the sequence
\[
0 \to \mcf \mapsvia{\phi} \mcg \to 0
\]
is exact as a sequence of sheaves.
By the stalkwise criterion for exactness, this holds if and only if
\[
0 \to \mcf_P \mapsvia{\phi_P} \mcg_P \to 0
\]
is exact for every $P$, that is, if and only if every $\phi_P$ is an isomorphism of abelian groups.

It remains to see that a morphism of sheaves which is an isomorphism on all stalks is an isomorphism.
This is standard: injectivity on stalks makes $\phi$ injective on sections, and surjectivity on stalks lets one lift any section of $\mcg$ locally and then glue the lifts, which are unique by the injectivity just established.
The resulting inverse maps on sections are compatible with restriction and define an inverse morphism $\phi\inv$.
:::
