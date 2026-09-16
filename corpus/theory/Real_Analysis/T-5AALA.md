---
schema: qual/card@1
id: T-5AALA
kind: theorem
title: Parseval's theorem for orthonormal families
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - L²
  - Bases
relations: []
review: draft
---

::: {.theorem}
Let $\mch$ be a [[D-7QQUO|Hilbert space]] and let $(u_n)_{n\in A}$ be a family in $\mch$, indexed by a set $A$, with $\inner{u_n}{u_m}=0$ for $n\neq m$ and $\norm{u_n}=1$ for all $n$.
For each $x\in\mch$ only countably many $\inner{x}{u_n}$ are nonzero ([[T-4CDKK]]), and sums over $A$ below are taken over those indices.
The following are equivalent:

1. (Completeness) If $x\in\mch$ and $\inner{x}{u_n}=0$ for all $n\in A$, then $x=0$.

2. (Parseval's identity) For every $x\in\mch$,
$$
\sum_{n\in A} \abs{ \inner{x}{u_n} }^2 = \norm{x}^2 .
$$

3. (Expansion) For every $x\in\mch$,
$$
x = \sum_{n\in A} \inner{x}{u_n}u_n ,
$$
with the series converging in norm in any enumeration of its nonzero terms; and if $x=\sum_{n\in A}c_nu_n$ for scalars $c_n$, only countably many nonzero, then $c_n=\inner{x}{u_n}$ for all $n$.
:::
