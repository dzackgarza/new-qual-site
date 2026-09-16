---
schema: qual/card@1
id: P-AGH310SUBVARIETY
kind: problem
title: Subvarieties and the restriction of a morphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Subvarieties
  - Morphisms
  - Locally Closed Sets
relations: []
review: draft
---

::: {.problem}
A subset of a topological space is **locally closed** if it is an open subset of its closure, equivalently if it is the intersection of an open set with a closed set.

If $X$ is a quasi-affine or quasi-projective variety and $Y \subseteq X$ is an irreducible locally closed subset, then $Y$ is itself quasi-affine, respectively quasi-projective, by virtue of being a locally closed subset of the same affine or projective space.
This is the **induced structure** on $Y$, and $Y$ is called a **subvariety** of $X$.

Now let $\phi: X \to Y$ be a morphism, and let $X' \subseteq X$ and $Y' \subseteq Y$ be irreducible locally closed subsets with $\phi(X') \subseteq Y'$.
Show that $\ro{\phi}{X'} : X' \to Y'$ is a morphism.
:::
