---
schema: qual/card@1
id: D-5LJUX
kind: definition
title: Dimension of a variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Dimension
  - Varieties
relations:
- kind: uses
  target: D-9DIKB
review: draft
prompts:
- What is the dimension of a variety?
- How does dimension relate to the function field?
- How does dimension relate to Krull dimension of the coordinate ring?
---

::: {.definition title="Dimension"}
The **dimension** of a topological space is the supremum of the lengths $n$ of chains
\[
Z_0 \subsetneq Z_1 \subsetneq \cdots \subsetneq Z_n
\]
of irreducible closed subsets.
:::

::: {.proposition}
For an affine variety $X$ over $k = \bar{k}$,
\[
\dim X = \krulldim k[X] = \trdeg_k k(X) .
\]
:::

::: {.remark}
The dimension of $V(f) \subseteq \AA^n$ for $f$ nonconstant is $n-1$ because one algebraic relation drops the transcendence degree by one.

The equality with Krull dimension relates the topological definition to dimension theory of rings.
The identification with transcendence degree is where algebraic closure is used, and it fails without it.
:::
