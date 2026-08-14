---
schema: qual/card@1
id: P-QE3QK
kind: problem
title: "There is no simple group of order 148"
classification:
  areas:
  - algebra
  topics:
  - sylow-theory
  - simple-groups
  - normal-subgroups
relations: []
review: draft
---

By definition, $G$ is simple iff its only normal subgroups are $1$ and $G$, so we will show that if $\abs G = 148$ then it contains a proper nontrivial normal subgroup.

Noting that $148 = p^2 q$ where $p=2, q = 37$, Sylow gives $n_{37} \divides 4$ and $n_{37} \equiv 1 \mod 37$.
The divisors of $4$ are $1, 2, 4$, and neither $2$ nor $4$ is congruent to $1$ modulo $37$, so $n_{37} = 1$.
So $G$ has a normal Sylow $37\dash$subgroup, which is proper and nontrivial, and we are done.

The Sylow $2\dash$subgroup does not settle this on its own: $n_2 \divides 37$ and $n_2$ is odd, and both $1$ and $37$ satisfy that.
