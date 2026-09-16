---
schema: qual/card@1
id: T-YHH3M
kind: theorem
title: Schur's lemma
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Semisimplicity
relations: []
review: draft
---

::: {.theorem}
Let $G$ be a group, $k$ an algebraically closed field, and $M$ an irreducible representation of $G$ over $k$ with $\dim_k M < \infty$.
Then every $G$-equivariant endomorphism of $M$ is multiplication by a scalar, so the map
$$
k \mapsvia{\sim} \Endo_G(M),\qquad \lambda\mapsto \lambda\cdot\id_M,
$$
is an isomorphism.
:::

::: {.remark}
For an irreducible representation $M$ of $G$ over an arbitrary field $k$, every nonzero $G$-equivariant endomorphism of $M$ has $G$-stable kernel $0$ and image $M$, so $\Endo_G(M)$ is a division algebra over $k$.
:::

::: {.slogan}
Over an algebraically closed field, an irreducible finite-dimensional representation has only scalar equivariant endomorphisms.
:::
