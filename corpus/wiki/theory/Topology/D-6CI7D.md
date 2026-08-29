---
schema: qual/card@1
id: D-6CI7D
kind: definition
title: Local Orientation
classification:
  areas:
  - topology
  topics:
  - Orientation
  - Manifolds
  - Homology
relations: []
review: draft
---

::: {.definition}
Let $M$ be an $n\dash$manifold and $x\in M$.
Excision and the local Euclidean structure give
\[
H_n(M, M\sm\ts{x}; \ZZ) \cong H_n(\RR^n, \RR^n \sm\ts{0}; \ZZ) \cong \ZZ
,\]
written $H_n(M \mid x)$.
A **local orientation of $M$ at $x$** is a choice of generator $\mu_x$ of this infinite cyclic group; there are exactly two.

An **orientation** of $M$ is a function $x \mapsto \mu_x$ choosing a local orientation at every point, subject to local consistency: every $x$ has a neighbourhood $\RR^n \subseteq M$ containing an open ball $B$ of finite radius about $x$ such that all $\mu_y$ for $y\in B$ are the images of a single generator $\mu_B$ of $H_n(M\mid B)$ under $H_n(M\mid B) \to H_n(M \mid y)$.
$M$ is **orientable** iff such a function exists.
:::

::: {.remark}
The local orientations assemble into the orientation double cover $\tilde M \to M$, whose points are the pairs $(x, \mu_x)$; $\tilde M$ is always orientable, and for $M$ connected, $M$ is orientable exactly when $\tilde M$ has two components.
:::

::: {.concept}
See Hatcher, §3.3, p. 234.
:::
