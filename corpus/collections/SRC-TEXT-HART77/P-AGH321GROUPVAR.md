---
schema: qual/card@1
id: P-AGH321GROUPVAR
kind: problem
title: Group varieties $\GG_a$ and $\GG_m$, and the group structure on $\Hom(X,G)$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Group Varieties
  - Morphisms
  - Regular Functions
relations: []
review: draft
---

::: {.problem}
A **group variety** consists of a variety $Y$ together with a morphism $\mu: Y \times Y \to Y$ such that the set of points of $Y$ with the operation given by $\mu$ is a group, and such that the inverse map $y \mapsto y\inv$ is also a morphism $Y \to Y$.

1. The **additive group** $\GG_a$ is the variety $\AA^1$ with the morphism $\mu: \AA^1 \times \AA^1 \to \AA^1$ defined by $\mu(a,b) = a+b$.
   Show that it is a group variety.

2. The **multiplicative group** $\GG_m$ is the variety $\AA^1 \sm \ts{0}$ with the morphism $\mu(a,b) = ab$.
   Show that it is a group variety.

3. If $G$ is a group variety and $X$ is any variety, show that the set $\Hom(X, G)$ has a natural group structure.

4. For any variety $X$, show that $\Hom(X, \GG_a)$ is isomorphic to $\mco(X)$ as a group under addition.

5. For any variety $X$, show that $\Hom(X, \GG_m)$ is isomorphic to the group of units in $\mco(X)$, under multiplication.
:::
