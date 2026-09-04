---
schema: qual/card@1
id: P-WB56B
kind: problem
title: An uncountable $E\subset[0,1]$ meets both $(-\infty,t)$ and $(t,\infty)$ in
  uncountable sets
classification:
  areas:
  - complex-analysis
  topics:
  - Point-Set Topology
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Show that if $E \subset [0, 1]$ is uncountable, then there exists some $t \in (0, 1)$ such that both $E \cap (-\infty, t)$ and $E \cap (t, \infty)$ are uncountable.
:::

::: solution
For each $n\ge1$, partition $[0,1]$ into the $2^n$ dyadic intervals of length $2^{-n}$, taking them half-open except for the last endpoint.
Since $E$ is uncountable and the partition is finite, at least one interval at every level meets $E$ in an uncountable set.

Suppose that at every level there were exactly one such interval, say $I_n$.
The dyadic partitions refine one another, so
\[
I_1\supset I_2\supset I_3\supset\cdots,
\qquad |I_n|=2^{-n}.
\]
Their closures therefore have a unique common point $x$.

At level $n$, every dyadic interval other than $I_n$ meets $E$ countably.
Hence
\[
E\setminus I_n
\]
is countable, being a finite union of countable sets.
Moreover, every $y\neq x$ is outside $I_n$ for all sufficiently large $n$, so
\[
E\setminus\{x\}
\subseteq \bigcup_{n=1}^\infty(E\setminus I_n).
\]
The right-hand side is countable.
This would make $E$ countable, a contradiction.

Thus at some dyadic level there are two distinct intervals $I$ and $J$ whose intersections with $E$ are uncountable.
Order them so that $I$ lies to the left of $J$, and choose $t$ between them; if they are adjacent, take their common endpoint.
Removing at most that endpoint from either interval does not change uncountability.
Therefore
\[
E\cap(-\infty,t)
\quad\text{and}\quad
E\cap(t,\infty)
\]
are both uncountable.
Since the two intervals are distinct subintervals of $[0,1]$, such a separating $t$ lies in $(0,1)$.
:::
