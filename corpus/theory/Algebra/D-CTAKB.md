---
schema: qual/card@1
id: D-CTAKB
kind: definition
title: Character of a representation
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Representation Theory
  - Trace
relations: []
review: draft
---

::: {.definition}
Let $G$ be a group, let $k$ be a field, and let $M$ be a finite-dimensional representation of $G$ over $k$, that is, a finite-dimensional $k$-vector space with a linear action $G\actson M$.
For $g\in G$, let
$$
T_g\colon M \to M, \qquad m \mapsto g\actson m.
$$
The \dfn{character} of $M$ is the function $\chi_M\colon G\to k$, $\chi_M(g) \coloneqq \tr T_g$.
:::
