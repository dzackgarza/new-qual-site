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
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter II, section 1,
    exercise 1.5, printed page 66 (PDF page 81 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "Show that a morphism of sheaves
    is an isomorphism if and only if it is both injective and surjective." The
    card states exactly this. The proof was checked: injective plus surjective
    is exactness of 0 -> F -> G -> 0, which by exercise 1.2 is exactness on
    stalks, hence every phi_P is an isomorphism; conversely an isomorphism on
    stalks gives injectivity on sections and local liftability of sections of
    G, and the lifts agree on overlaps by injectivity, so they glue and the
    sectionwise inverses are compatible with restriction.
---


::: {.problem}
Show that a morphism of sheaves is an isomorphism if and only if it is both injective and surjective.
:::

::: {.solution}
Let $\phi: \mcf \to \mcg$ be a morphism of sheaves.
Being injective and surjective says exactly that the sequence
$$
0 \to \mcf \mapsvia{\phi} \mcg \to 0
$$
is exact as a sequence of sheaves.
By the stalkwise criterion for exactness, this holds if and only if
$$
0 \to \mcf_P \mapsvia{\phi_P} \mcg_P \to 0
$$
is exact for every $P$, that is, if and only if every $\phi_P$ is an isomorphism of abelian groups.

It remains to see that a morphism of sheaves which is an isomorphism on all stalks is an isomorphism.
Injectivity on stalks makes $\phi$ injective on sections, and surjectivity on stalks lets one lift any section of $\mcg$ locally and then glue the lifts, which are unique by the injectivity just established.
The resulting inverse maps on sections are compatible with restriction and define an inverse morphism $\inverseof{\phi}$.
:::
