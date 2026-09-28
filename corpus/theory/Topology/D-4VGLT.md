---
schema: qual/card@1
id: D-4VGLT
kind: definition
title: Tor functors
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Modules
relations: []
review: draft
---

::: {.definition}
Let $R$ be a commutative ring, let $B$ be an $R$-module, and let $n\geq 0$.
The functor $\Tor_n^R(\wait, B)$ is the $n$th [[D-6B77N|left derived functor]] of $\wait\tensor_R B$:
$$
\Tor_n^R(A, B) \coloneqq L_n(\wait\tensor_R B)(A) = H_n(P_\bullet\tensor_R B)
,$$
where $P_\bullet \to A$ is a [[D-PKIY7|projective resolution]] of the $R$-module $A$.
:::

::: {.concept}
[@DF04].
:::
