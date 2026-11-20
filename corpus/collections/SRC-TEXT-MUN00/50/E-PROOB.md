---
schema: qual/card@1
id: E-PROOB
kind: problem
title: Manifolds have dimension at most m
classification:
  areas:
  - topology
  topics:
  - Dimension
  - Manifolds
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution was located; the sets searched are listed in the COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00.
    Checked against Munkres, Topology (2000), §50 Exercise 9, printed p. 316, with Theorem 50.6 (compact
    subspaces of R^N have dimension at most N), Theorem 50.1 and Corollary 50.3 for the finite union of the
    pieces of a compact set, and the preceding exercise (the card of Exercise 50.8) for the passage from the
    compact subspaces to the manifold, which is sigma-compact because it is locally compact and second
    countable. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 9 (printed p. 316).
    Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the ten GitHub repositories of Munkres
    solutions listed in COMPLAINTS.md stop before §36, and the AoPS post *Topology by Munkres Chapter 8 | Day
    18* (https://artofproblemsolving.com/community/c3401823h3647630) answers §50 with its formulas lost. The
    card reduces the manifold to the sigma-compact theorem [[E-MVB8P]] through the dimension bound on its
    compact subspaces, and that bound is the step the exercise is for: a compact set is covered by finitely
    many coordinate patches, each piece is a closed subspace of $\RR^m$ under its chart, and the finite union
    of closed pieces keeps the dimension. Nothing needed correction.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct in
    outline. Added: the reason a second-countable locally compact space is sigma-compact, and
    the local compactness of a manifold, which the card asserted; the shrinking step that
    produces compact K_i = K ∩ closure(V_i) each inside one chart domain, where the card said
    only 'shrink them'; the closedness of phi(K_i) in R^m that the closed-subspace corollary
    needs; and the attribution of each of the three ingredients to a card or a named result of
    §50 — the closed-subspace corollary to [[E-PYCIE]], the sigma-compact theorem to
    [[E-MVB8P]], and the finite closed-union theorem to §50 of the book. No statement was
    changed. Not claimed: a retained solution set; the collection's provenance is the Munkres
    textbook, whose text is not retained in this repository, so page references are limited to
    the two the corpus already records (printed pp. 305 and 315).
---

::: {.exercise}

Corollary.
Every $m$-manifold has topological dimension at most $m$.
:::

::: {.solution}
Throughout $M$ is an $m$-manifold in Munkres's sense — a second-countable Hausdorff space each point of which has a neighbourhood homeomorphic to an open subset of $\RR^{m}$ — and dimension is the covering dimension of Munkres, *Topology* (2000), §50, whose definitions of order and of topological dimension are on printed p. 305: a family refines another when each of its members lies in a member of the other, an open cover has order at most $m$ when no point lies in more than $m$ of its members, and $\dim X \le n$ when every open cover of $X$ has an open refinement of order at most $n+1$. The exercise is §50 Exercise 9.

::: pf

::: {.pf-step #sigmacompact}
$M$ is locally compact and $\sigma$-compact.

::: pf-proof
Each point has a neighbourhood homeomorphic to an open subset of $\RR^{m}$, and such a neighbourhood contains the homeomorphic image of a closed ball about the point, which is compact; so $M$ is locally compact. A second-countable locally compact space is $\sigma$-compact: the countable base yields a countable family of open sets with compact closures covering $M$, because each point has a base element with compact closure about it, and the closures of countably many compact sets have compact union in a countable union, so $M$ is a countable union of compact subspaces. $M$ is Hausdorff by hypothesis.

:::

:::

::: {.pf-step #cover}
For every compact $K \subseteq M$ there are compact sets $K_{1},\ldots,K_{r}$ with $K = K_{1} \cup \cdots \cup K_{r}$, each $K_{i}$ contained in the domain of a chart.

::: pf-proof
For $x \in K$ choose a chart $(U_{x},\varphi_{x})$ at $x$ and an open $V_{x}$ with $x \in V_{x} \subseteq \overline{V_{x}} \subseteq U_{x}$ and $\overline{V_{x}}$ compact, possible by local compactness inside the chart domain. The sets $V_{x}$ cover the compact $K$, so finitely many $V_{x_{1}},\ldots,V_{x_{r}}$ do; put $K_{i} \coloneqq K \cap \overline{V_{x_{i}}}$. Each $K_{i}$ is closed in the compact $K$, hence compact, and is contained in $U_{x_{i}}$; and $K = \bigcup_{i}K_{i}$ because the $V_{x_{i}}$ cover $K$.

:::

:::

::: {.pf-step #pieces}
$\dim K_{i} \le m$ for each $i$.

::: pf-proof
The chart $\varphi_{x_{i}}$ carries $K_{i}$ homeomorphically onto $\varphi_{x_{i}}(K_{i})$, a compact hence closed subspace of $\RR^{m}$. Dimension is a topological invariant, so $\dim K_{i} = \dim\varphi_{x_{i}}(K_{i})$, and a closed subspace of $\RR^{m}$ has dimension at most $m$, which is the corollary [[E-PYCIE]] of §50, resting on $\dim\RR^{m} = m$ and on monotonicity of dimension for closed subspaces.

:::

:::

::: {.pf-step #finite-union}
$\dim K \le m$ for every compact $K \subseteq M$.

::: pf-proof
The finite closed-union theorem for covering dimension, in §50 of the book, says that a space which is the union of finitely many closed subspaces of dimension at most $m$ has dimension at most $m$. The $K_{i}$ of step [](#cover){.pf-ref} are closed in $K$, and $K$ is the union of the finitely many of them, so the theorem applies with the bounds of step [](#pieces){.pf-ref}.

:::

:::

::: pf-step
$\dim M \le \boxed{m}$.

::: pf-proof
Step [](#sigmacompact){.pf-ref} puts $M$ among the $\sigma$-compact Hausdorff spaces, and step [](#finite-union){.pf-ref} gives the bound $m$ for every compact subspace of $M$; the $\sigma$-compact theorem [[E-MVB8P]], which is §50 Exercise 8, then gives $\dim M \le m$.

:::

:::

:::
:::
