---
schema: qual/card@1
id: E-LI4O5
kind: problem
title: Components of metrizable locally euclidean spaces are manifolds
classification:
  areas:
  - topology
  topics:
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
    Checked against Munkres, Topology (2000), supplementary Exercise 9 of §50, printed p. 318, with Theorem 25.4
    (the components of a locally path connected space are open), Theorem 30.2, Theorem 42.1 and the card of §41
    Exercise 10, which shows that a connected, locally compact, paracompact space is a countable union of compact
    subspaces. Points checked: a locally euclidean space is locally path connected, so components are open; the
    component is then locally m-euclidean and metrizable, hence Hausdorff, locally compact and paracompact; the
    countable cover by compact pieces yields a countable cover by second countable coordinate neighbourhoods,
    whose union of countable bases is a countable basis. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The Stack Exchange query "locally m-euclidean" returned 3942394,
    "Each component of metrizable locally euclidean space is a manifold", which is supplementary Exercise 9 of
    §50 (printed p. 318) verbatim and has no answer, the text kept at tmp/sources/mse-3942394-munkres-50-supp-9.md;
    the same query returned 4416020 and 2317193, on second countability and paracompactness, which are not this
    exercise. Nothing located proves it. Murayama's selection has no Chapter 8, dbFin has no chapter-8 page, the
    ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS post
    *Topology by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630)
    answers §50 with its formulas lost. The card's argument is its own: components of a locally euclidean space
    are open because it is locally path connected; the component is then a connected, locally compact,
    paracompact space, hence a countable union of compact pieces, which finitely many coordinate neighbourhoods
    cover, giving a countable basis. Nothing needed correction.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps. Citations added where the prose had none or by name
    only: the definition of an m-manifold (printed p. 225, a Hausdorff space with a
    countable basis, locally m-euclidean), §50 supplementary Exercise 9 (printed p. 318),
    Theorem 25.3 (printed p. 161) for components of a locally connected space being open,
    Theorem 27.3 (printed p. 173) for the compact closed ball inside a coordinate
    neighbourhood, and Theorem 41.4 (printed p. 257) in place of "Stone's theorem" for
    metrizable implying paracompact. The citation of E-GZX7B is now exact: that card
    records that the conclusion printed for Exercise 41.10, a countable basis, is false,
    and proves instead that each component is a countable union of compact subspaces, which
    is what is used here; the earlier prose attributed the exhaustion to the card without
    saying that the printed statement was replaced. Steps now written out that the prose
    asserted: that coordinate neighbourhoods give a basis of path-connected sets, so that X
    is locally path connected; that a closed ball inside a coordinate neighbourhood is a
    compact neighbourhood, so that C is locally compact; and that the union of countable
    bases of the members of a countable open cover is a countable basis, with the basis
    criterion verified at a point. No repair to the statement.
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that if $X$ is metrizable, then each component of $X$ is an $m$-manifold.
:::

::: {.solution}
The argument is the card's own: no retained set solves this exercise, as the audit and the COMPLAINTS.md entry for §43--§50 record. It rests on three book facts and on the compact exhaustion proved on [[E-GZX7B]].

Throughout, $X$ is metrizable and locally $m$-euclidean, and an $m$-manifold is a Hausdorff space with a countable basis in which every point has a neighbourhood homeomorphic with an open subset of $\RR^m$ (Munkres, *Topology* (2000), §36, printed p. 225). The exercise is supplementary Exercise 9 of §50, printed p. 318. Let $C$ be a component of $X$.

::: pf

::: {.pf-step #open}
$X$ is locally path connected, so $C$ is open in $X$.

::: pf-proof
Each $x\in X$ has a neighbourhood homeomorphic with an open subset of $\RR^m$, and $\RR^m$ is path connected, so $X$ has a basis of path-connected sets: every neighbourhood of $x$ contains such a set containing $x$. Hence $X$ is locally path connected, therefore locally connected, and the components of a locally connected space are open (Theorem 25.3, printed p. 161).
:::

:::

::: {.pf-step #properties}
$C$ is connected, locally $m$-euclidean, metrizable, Hausdorff, locally compact and paracompact.

::: pf-proof
$C$ is a component, hence connected. It is open in $X$ by step [](#open){.pf-ref}, so the subspace topology on $C$ inherits from $X$ a neighbourhood homeomorphic to an open subset of $\RR^m$ at each of its points, which is local $m$-euclidean; and a subspace of a metrizable space is metrizable, hence Hausdorff. For local compactness, a point $x\in C$ has a neighbourhood $U\subset C$ homeomorphic with an open subset of $\RR^m$; inside $U$ there is a set containing $x$ that is homeomorphic with a closed ball of positive radius, which is compact (Theorem 27.3, printed p. 173), and it is a neighbourhood of $x$ in $C$. Finally a metrizable space is paracompact (Theorem 41.4, printed p. 257).
:::

:::

::: {.pf-step #exhaustion}
$C$ is a countable union of compact subspaces.

::: pf-proof
$C$ is connected, Hausdorff, locally compact and paracompact by step [](#properties){.pf-ref}. [[E-GZX7B]], Exercise 10 of §41, proves that each component of such a space is a countable union of compact subspaces — the conclusion printed for that exercise, a countable basis, is false, and that card replaces it — and applied to the space $C$ itself it exhibits $C=\bigcup_n K_n$ with each $K_n$ compact.
:::

:::

::: {.pf-step #basis}
$C$ has a countable basis.

::: pf-proof

::: {.pf-step #cover-K}
Each $K_n$ is covered by finitely many open sets of $C$ that are homeomorphic with open subsets of $\RR^m$.

::: pf-proof
At each $x\in K_n$, local $m$-euclideaness of $C$ gives a neighbourhood of $x$ in $C$ homeomorphic with an open subset of $\RR^m$; these neighbourhoods cover the compact set $K_n$, so finitely many of them do.
:::

:::

::: {.pf-step #countable-cover}
The family $\mathcal{V}$ of all the sets so obtained, over all $n$, is a countable open cover of $C$ by second-countable subspaces.

::: pf-proof
It is a union over $n$ of the finite families of step [](#cover-K){.pf-ref}, hence countable, and the $K_n$ cover $C$, so it covers $C$. A space homeomorphic with an open subset of $\RR^m$ is second countable, because $\RR^m$ has a countable basis and a subspace of a second-countable space is second countable.
:::

:::

::: {.pf-step #union-basis}
The union of countable bases of the members of $\mathcal{V}$ is a countable basis for $C$.

::: pf-proof
Choose a countable basis $\mathcal{B}_V$ of each $V\in\mathcal{V}$; the union $\mathcal{B}$ over the countable family $\mathcal{V}$ is countable, and each of its members is open in $C$ because $V$ is open in $C$. It is a basis: if $x\in C$ and $O$ is an open neighbourhood of $x$, choose $V\in\mathcal{V}$ with $x\in V$, then $O\cap V$ is a neighbourhood of $x$ in $V$, so there is $B\in\mathcal{B}_V$ with $x\in B\subset O\cap V\subset O$.
:::

:::

:::

:::

::: {.pf-step}
$C$ is an $m$-manifold.

::: pf-proof
By step [](#properties){.pf-ref} $C$ is Hausdorff and locally $m$-euclidean, as a subspace of the locally $m$-euclidean space $X$; by step [](#basis){.pf-ref} it has a countable basis. Those three properties are the definition of an $m$-manifold (printed p. 225), so each component of $X$ is an $m$-manifold.
:::

:::

:::
:::
