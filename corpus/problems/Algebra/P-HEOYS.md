---
schema: qual/card@1
id: P-HEOYS
kind: problem
title: Colorings of a tetrahedron with $C$ colors up to symmetry
classification:
  areas:
  - algebra
  topics:
  - Burnside's Lemma
  - Group Actions
  - Permutations
relations: []
review: draft
---

::: {.problem}

Let a regular tetrahedron be colored with $C$ available colors.

(a) Count colorings of its four vertices (equivalently, its four faces) up to the full symmetry group.

(b) Count colorings of its six edges up to the full symmetry group.

(c) How do the answers change if only orientation-preserving rotational symmetries are allowed?

:::

::: {.solution}

The full symmetry group of a tetrahedron is $S_4$, of order $24$, acting naturally on the four vertices; the rotational subgroup is $A_4$, of order $12$. By Burnside's lemma, the number of colorings up to a group $\Gamma$ is the average over $\gamma\in\Gamma$ of $C^{k(\gamma)}$, where $k(\gamma)$ is the number of cycles of $\gamma$ on the colored objects.

::: pf

::: pf-step

(a) There are $\boxed{\frac{C^4+6C^3+11C^2+6C}{24}}=\binom{C+3}{4}$ vertex colorings, and as many face colorings, up to $S_4$.

::: pf-proof

The cycle types of $S_4$ on the vertices are $1^4$, $2\,1^2$, $2^2$, $3\,1$, $4$, with multiplicities $1,6,3,8,6$ and cycle counts $4,3,2,2,1$. Burnside's lemma gives
$$
\frac{C^4+6C^3+3C^2+8C^2+6C}{24}
=
\frac{C^4+6C^3+11C^2+6C}{24}
=\binom{C+3}{4}.
$$
Sending each face to its opposite vertex is an $S_4$-equivariant bijection, so face colorings give the same count.

:::

:::

::: pf-step

(b) There are $\boxed{\frac{C^6+9C^4+14C^2}{24}}$ edge colorings up to $S_4$.

::: pf-proof

Identify the six edges with the two-element subsets of $\{1,2,3,4\}$. The five cycle types above have respectively $6,4,4,2,2$ cycles on the edge set. Burnside's lemma gives
$$
\frac{C^6+6C^4+3C^4+8C^2+6C^2}{24}=\frac{C^6+9C^4+14C^2}{24}.
$$

:::

:::

::: pf-step

(c) Up to rotations, there are $\boxed{\frac{C^4+11C^2}{12}}$ vertex (or face) colorings and $\boxed{\frac{C^6+3C^4+8C^2}{12}}$ edge colorings.

::: pf-proof

The group $A_4$ consists of the identity, three double transpositions, and eight $3$-cycles. On the vertices these have $4,2,2$ cycles, and on the edges $6,4,2$ cycles. Burnside's lemma gives
$$
\frac{C^4+3C^2+8C^2}{12}=\frac{C^4+11C^2}{12},
\qquad
\frac{C^6+3C^4+8C^2}{12}.
$$

:::

:::

:::

:::
