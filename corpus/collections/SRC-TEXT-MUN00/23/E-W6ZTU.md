---
schema: qual/card@1
id: E-W6ZTU
kind: exercise
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
**Goal.** Show a discrete space is totally disconnected, and decide the converse.

<1>1. A discrete space is totally disconnected.
<2>1. In the discrete topology, every subset is open (and closed).
::: {.proof}
definition of the discrete topology.
:::
<2>2. A connected subspace with more than one point would be disconnected.
::: {.proof}
if $C \subseteq X$ has two distinct points $x, y$, then $\theset{x}$ and $C \sm \theset{x}$ are both open in $C$ (since every subset is open), nonempty, and disjoint, so $C$ is disconnected.
:::
<2>3. Hence the only connected subspaces are singletons (and the empty set).
::: {.proof}
<1>1.2.
:::
<2>4. Hence $X$ is totally disconnected.
::: {.proof}
definition.
:::

<1>2. The converse is false.
<2>1. Counterexample: $\QQ$ with the usual (subspace) topology.
::: {.proof}
$\QQ$ is totally disconnected (its only connected subspaces are singletons).
:::
<2>2. But $\QQ$ is not discrete.
::: {.proof}
no singleton $\theset{q}$ is open in $\QQ$ (every open set contains infinitely many rationals).
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 proves the forward direction; <1>2 shows the converse fails.
:::
:::
