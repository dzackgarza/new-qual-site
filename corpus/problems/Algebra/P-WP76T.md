---
schema: qual/card@1
id: P-WP76T
kind: problem
title: Maximal subgroups of a $p$-group have index $p$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Subgroups
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
- Show that every maximal subgroup of a $p\dash$group has index $p$.
:::

::: {.solution}
Let $G$ be a finite $p$-group and let $M<G$ be maximal.

First, every proper subgroup of a finite $p$-group is properly contained in its normalizer. Indeed, let $M$ act by left multiplication on $G/M$. The number of fixed cosets is congruent to
\[
[G:M]\equiv0\pmod p.
\]
The fixed cosets are exactly the cosets $gM$ with $g\in N_G(M)$, so their number is
\[
[N_G(M):M].
\]
Since the coset $M$ is fixed, this positive number is divisible by $p$, hence is at least $p$. Thus
\[
M<N_G(M).
\]

By maximality, $N_G(M)=G$, so $M\trianglelefteq G$. Then $G/M$ is a nontrivial finite $p$-group with no proper nontrivial subgroup. Hence it has prime order, necessarily $p$. Therefore
\[
\boxed{[G:M]=p}.
\]
:::
