---
schema: qual/card@1
id: D-3JJJN
kind: definition
title: Left and right splittings of a short exact sequence
classification:
  areas:
  - algebra
  topics:
  - Exact Sequences
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a ring, and let
$$
\xi\colon 0 \to A \mapsvia{d_1} B \mapsvia{d_2} C \to 0
$$
be a short [[D-BJYH3|exact sequence]] of $R$-modules.
A \dfn{right splitting} of $\xi$ is an $R$-linear map $s\colon C\to B$ with $d_2 \circ s = \id_{C}$.
A \dfn{left splitting} of $\xi$ is an $R$-linear map $t\colon B\to A$ with $t \circ d_1 = \id_A$.
:::
