---
schema: qual/card@1
id: E-AY5GK
kind: exercise
title: Topologically complete spaces
subtitle: Munkres §43.6
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
---

::: {.exercise}

A space $X$ is said to be topologically complete if there exists a metric for the topology of $X$ relative to which $X$ is complete.

(a) Show that a closed subspace of a topologically complete space is topologically complete.

(b) Show that a countable product of topologically complete spaces is topologically complete (in the product topology).

(c) Show that an open subspace of a topologically complete space is topologically complete.
[Hint: If $U \subset X$ and $X$ is complete under the metric $d$, define $\phi: U \to \mathbb{R}$ by the equation

$$
\phi(x) = 1/d(x, X - U).
$$

Imbed $U$ in $X \times \mathbb{R}$ by setting $f(x) = x \times \phi(x)$.]

(d) Show that if $A$ is a $G_\delta$ set in a topologically complete space, then $A$ is topologically complete.
[Hint: Let $A$ be the intersection of the open sets $U_n$, for $n \in \mathbb{Z}_+$. Consider the diagonal imbedding $f(a) = (a, a, \ldots)$ of $A$ into $\prod U_n$.] Conclude that the irrationals are topologically complete.
:::
