---
schema: qual/card@1
id: FE-VARSEGREPROD
kind: example
title: The product of two projective spaces is projective and not affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Varieties
  - Affine Varieties
  - Segre Embedding
relations:
- kind: uses
  target: PR-VA4S3
review: draft
prompts:
- Is $\PP^1\times\PP^1$ affine?
- Why can a projective variety of positive dimension not be affine?
---

::: {.example}
Let $k$ be an algebraically closed field.
The Segre embedding exhibits $\PP^1_k\times_k\PP^1_k$ as a closed subvariety of $\PP^3_k$, so it is projective ([[PR-VA4S3]]).
An affine variety isomorphic to a projective variety consists of a single point [@Har77, Exercise I.3], so $\PP^1\times\PP^1$ is not affine.
Equivalently, it contains the complete curve $\PP^1\times\set{p}$, which no affine variety of positive dimension does ([[D-VARCOMP]]).
:::
