---
schema: qual/card@1
id: P-TOP-WORKSHOP-2020-WS5-P5
kind: problem
title: Sphere with antipodal poles identified is homotopy equivalent to $S^1\vee S^2$
classification:
  areas:
  - topology
  topics:
  - Homotopy
  - Covering Spaces
  - Surfaces
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
(May 2013) Let $X$ be the space obtained from the $2$-sphere $S^2$ by identifying the north and south poles (i.e.\ by identifying two diametrically opposite points).

(a) Show that $X$ is homotopy equivalent to $S^1\vee S^2$.

(b) Describe all connected covering spaces of $X$.
:::

::: {.solution}
(a) Identifying two distinct points in a path-connected CW complex adds a circle up to homotopy. Applying this to the north and south poles of \(S^2\) gives
\[
X\simeq S^2\vee S^1.
\]
One can see this directly by choosing a CW decomposition with the two poles as vertices; after the identification and collapse of a maximal tree, one \(1\)-cell remains from the identification while the \(2\)-sphere remains as a sphere summand.

Thus
\[
\pi_1(X)\cong\mathbb Z.
\]

(b) Connected covers correspond to subgroups of \(\mathbb Z\), namely \(n\mathbb Z\) for \(n\ge1\) and the trivial subgroup. The universal cover is a bi-infinite chain of spheres
\[
\cdots\cup S^2_{-1}\cup S^2_0\cup S^2_1\cup\cdots
\]
with the north pole of \(S^2_i\) identified with the south pole of \(S^2_{i+1}\). The generator of the deck group shifts the chain by one sphere.

For \(n\ge1\), quotienting by the subgroup \(n\mathbb Z\) produces an \(n\)-sheeted cover: a cyclic necklace of \(n\) spheres, with successive north and south poles identified cyclically. The trivial subgroup gives the infinite chain. These are all connected covering spaces up to equivalence.
:::
