---
schema: qual/card@1
id: D-Z2V7T
kind: definition
title: Exact functor
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Category Theory
relations:
- kind: variant-of
  target: D-S7L6M
review: draft
---

::: {.definition}
Let $\mathcal A$ and $\mathcal B$ be abelian categories and $T\colon\mathcal A\to\mathcal B$ an additive functor.
The functor $T$ is \dfn{right exact} if for every [[D-SIUWU|short exact sequence]] $0 \to A \to B \to C \to 0$ in $\mathcal A$ the sequence
$$
TA \to TB \to TC \to 0
$$
is [[D-STPAM|exact]], and \dfn{left exact} if for every such sequence
$$
0 \to TA \to TB \to TC
$$
is exact.
The functor $T$ is \dfn{exact} if it is both left exact and right exact, that is, if for every short exact sequence $0 \to A \to B \to C \to 0$ in $\mathcal A$ the sequence
$$
0 \to TA \to TB \to TC \to 0
$$
is exact.
:::
