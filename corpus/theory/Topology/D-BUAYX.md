---
schema: qual/card@1
id: D-BUAYX
kind: definition
title: Injective map
classification:
  areas:
  - topology
  topics:
  - Category Theory
relations: []
review: draft
---

::: {.definition}
Let $A$ and $B$ be sets.
A map $\iota\colon A\to B$ is \dfn{injective} if for all $x, y\in A$, $\iota(x) = \iota(y)$ implies $x = y$.
:::

::: {.remark}
If $A\neq\emptyset$, then $\iota\colon A\to B$ is injective if and only if it has a left inverse: a map $p\colon B\to A$ with $p\circ\iota = \id_A$.
The empty map $\emptyset\to B$ with $B\neq\emptyset$ is injective and has no left inverse.
For a continuous injective map of topological spaces, a left inverse need not be continuous: the inclusion $S^1\injects D^2$ has no continuous left inverse.
:::

::: {.concept}
[@DF04].
:::
