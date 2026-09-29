---
schema: qual/card@1
id: E-W6ZTU
kind: problem
title: Discrete spaces are totally disconnected
classification:
  areas:
  - topology
  topics:
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

A space is totally disconnected if its only connected subspaces are one-point sets.
Show that if $X$ has the discrete topology, then $X$ is totally disconnected.
Does the converse hold?
:::

::: {.solution}
::: pf

::: {.pf-step #discrete-totally-disconnected}
A discrete space $X$ is totally disconnected.

::: pf-proof
Let $C\subseteq X$ contain distinct points $x$ and $y$.
Every subset of $C$ is open in $C$, so $\theset{x}$ and $C\sm\theset{x}$ are disjoint nonempty open subsets of $C$ with union $C$, and $C$ is not connected.
:::

:::

::: {.pf-step #converse-fails}
The converse is false: $\QQ$ with the subspace topology from $\RR$ is totally disconnected but not discrete.

::: pf-proof
Let $C\subseteq\QQ$ contain rationals $p<q$, and choose an irrational $r$ with $p<r<q$.
Then $C\cap(-\infty,r)$ and $C\cap(r,\infty)$ are disjoint nonempty open subsets of $C$ with union $C$, so $C$ is not connected.
No singleton $\theset{q}$ is open in $\QQ$, since every open interval about $q$ contains other rationals.
:::

:::

::: pf-qed
Step [](#discrete-totally-disconnected){.pf-ref} proves the statement, and step [](#converse-fails){.pf-ref} answers the question about the converse.
:::

:::

:::
