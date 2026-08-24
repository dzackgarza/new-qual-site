---
schema: qual/card@1
id: E-5ZG7B
kind: exercise
title: $\mathbb{R}/\mathbb{Q}$ has the indiscrete topology
classification:
  areas:
  - topology
  topics:
  - Quotient Spaces
  - Point-Set Topology
relations: []
review: draft
---

::: {.problem title="?"}
Show that $\RR/\QQ$ has the indiscrete topology.
:::

::: {.solution}
\envlist

- Let $U \subset \RR/\QQ$ be open and nonempty, show $U = \RR/\QQ$.

- Let $[x] \in U$, then $x \in \pi\inv(U) \definedas V \subset\RR$ is open.

- Then $V$ contains an interval $(a, b)$

- Every $y\in V$ satisfies $y+q \in V$ for all $q\in \QQ$, since $y+q-y \in \QQ \implies [y+q] = [y]$.

- So $(a-q, b+q) \in V$ for all $q\in \QQ$.

- So $\union_{q\in \QQ}(a-q, b+q) \in V \implies \RR \subset V$.

- So $\pi(V) = \RR/\QQ = U$, and thus the only open sets are the entire space and the empty set.
:::
