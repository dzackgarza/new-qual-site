---
schema: qual/card@1
id: P-TOPF10H
kind: problem
title: "Deck translation group of the hexagonal lattice covering the theta graph"
classification:
  areas:
  - topology
  topics:
  - Covering Spaces
  - Deck Transformations
  - Graphs
relations: []
review: draft
---

::: {.problem}
The infinite hexagonal lattice forms a covering space of the theta graph, as shown.
What is the group of deck translations (covering automorphisms) of the covering?
:::

::: {.solution}

::: pf

::: pf-step

Give the theta graph $\Theta$ its standard structure with two vertices and three oriented edges $e_1,e_2,e_3$ joining them. Then
$$
\pi_1(\Theta)\cong F_2,\qquad H_1(\Theta;\mathbb Z)\cong\mathbb Z^2.
$$

::: pf-proof

A connected graph with $E=3$ and $V=2$ has free fundamental group of rank $E-V+1=2$, and its abelianization is $\mathbb Z^2$.

:::

:::

::: pf-step

The infinite hexagonal lattice in the source is the covering corresponding to the commutator subgroup
$$[F_2,F_2]\triangleleft F_2.$$

::: pf-proof

Lift the three edge types of $\Theta$ to the three edge directions of the hexagonal lattice. Choosing two independent translation vectors of the lattice, traversing either vector changes the abelianized edge-count by one of the two standard generators of $H_1(\Theta)$. A closed path in the lattice has zero net translation exactly when its projected word has trivial abelianization. Hence the covering subgroup is the kernel of $F_2\to F_2^{\mathrm{ab}}\cong\mathbb Z^2$, namely $[F_2,F_2]$.

:::

:::

::: {.pf-step #s3}

Since this subgroup is normal, the covering is regular and its deck group is
$$
F_2/[F_2,F_2]\cong\mathbb Z^2.
$$

::: pf-proof

For a connected regular covering corresponding to a normal subgroup $H\triangleleft\pi_1(X)$, the deck group is $\pi_1(X)/H$.

:::

:::

::: pf-step

Geometrically these deck transformations are exactly the translations by the rank-two translation lattice of the hexagonal tiling. Thus
$$
\boxed{\operatorname{Deck}(\widetilde\Theta/\Theta)\cong\mathbb Z^2.}
$$

::: pf-proof

The two independent lattice translations preserve the covering projection and generate all translations of the hexagonal lattice; step [](#s3){.pf-ref} shows there are no additional deck transformations.

:::

:::

:::

:::
