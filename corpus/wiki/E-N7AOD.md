---
schema: qual/card@1
id: E-N7AOD
kind: exercise
title: The fundamental group of a topological group is abelian
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Topological Groups
relations: []
review: draft
solved: false
---

Let $G$ be a topological group with operation $\cdot$ and identity element $x_0$. Let $\Omega(G, x_0)$ denote the set of all loops in $G$ based at $x_0$. If $f, g \in \Omega(G, x_0)$, let us define a loop $f \otimes g$ by the rule

$$
(f \otimes g)(s) = f(s) \cdot g(s).
$$

(a) Show that this operation makes the set $\Omega(G, x_0)$ into a group.

(b) Show that this operation induces a group operation $\otimes$ on $\pi_1(G, x_0)$.

(c) Show that the two group operations $*$ and $\otimes$ on $\pi_1(G, x_0)$ are the same. [Hint: Compute $(f * e_{x_0}) \otimes (e_{x_0} * g)$.]

(d) Show that $\pi_1(G, x_0)$ is abelian.

::: {.remark}
Munkres, *Topology*, §52 Exercise 7.
:::
