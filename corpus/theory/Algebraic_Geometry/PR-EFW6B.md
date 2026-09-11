---
schema: qual/card@1
id: PR-EFW6B
kind: proposition
title: Regular functions on a projective variety are constant
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Regular Functions
  - Affine Schemes
relations:
- kind: uses
  target: D-CP2MH
review: draft
prompts:
- What are the global regular functions on a projective variety?
- Why is $\PP^n$ not affine?
---

::: {.proposition}
Let $X$ be a connected projective variety over $k = \bar{k}$.
Then $\OO_X(X) = k$.
:::

::: {.remark}
This is the algebraic shadow of the maximum principle, and it is the fastest separator of the two categories.
An affine variety is determined by its ring of global functions and has as many of them as it has coordinates; a projective one has only the constants, so it can be affine only if it is a point.
In particular $\PP^n$ is not affine for $n \geq 1$.

The same statement is the reason a morphism from a projective variety to an affine one is constant on each connected component, which is how one usually shows some proposed map cannot exist.
:::
