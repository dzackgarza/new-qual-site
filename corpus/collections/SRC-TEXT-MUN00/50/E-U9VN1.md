---
schema: qual/card@1
id: E-U9VN1
kind: problem
title: Every $m$-manifold imbeds as a closed subspace of $\RR^{2m+1}$
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
    Checked against Munkres, Topology (2000), §50 Exercise 7, printed p. 316, with the preceding exercise (the
    card of Exercise 50.6) and the argument of Exercise 50.9 for the dimension of the compact subspaces of a
    manifold. A manifold is locally compact Hausdorff and second countable by definition, so the imbedding
    theorem of Exercise 50.6 applies once its compact subspaces are known to have dimension at most m, which is
    what Exercise 50.9 supplies. Nothing needed correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). Nothing located proves Munkres §50 Exercise 7 (printed p. 316);
    it is a corollary of the theorem of Exercise 6 and of the dimension bound of Exercise 9, both of which the
    card cites as [[E-26ELV]] and [[E-PROOB]]. Murayama's selection has no Chapter 8, dbFin has no chapter-8
    page, the ten GitHub repositories of Munkres solutions listed in COMPLAINTS.md stop before §36, and the AoPS
    post *Topology by Munkres Chapter 8 | Day 18* (https://artofproblemsolving.com/community/c3401823h3647630)
    answers §50 with its formulas lost. The Stack Exchange question 3082048 on imbedding theorems for
    non-second-countable manifolds, returned by the query "Prüfer manifold", is about a different question and
    does not treat this corollary. Nothing needed correction.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, and the card now says on its face that the argument is
    its own, no retained set proving the corollary. Each citation checked against the thing
    it names: the definition of an m-manifold on printed p. 225 (Hausdorff, countable basis,
    locally m-euclidean), which supplies two of the three hypotheses outright; the theorem
    of §50 Exercise 6 on printed p. 315, which is what the card E-26ELV states; and §50
    Exercise 7 on printed p. 316, the corollary itself, with Exercise 9, the dimension bound,
    on the same page. The claim that every compact subspace of M has dimension at most m was
    checked against the card E-PROOB, whose solution does establish it -- finitely many
    coordinate neighbourhoods, closed subspaces of R^m, finite closed-union theorem -- and
    then applies the sigma-compact theorem; the step here records that argument rather than
    only the reference, since it is the hypothesis the imbedding theorem needs. Local
    compactness of M is now derived from the chart by taking a compact closed ball
    (Theorem 27.3, printed p. 173). No repair to the statement.
---

::: {.exercise}

Corollary.
Every $m$-manifold can be imbedded in $\RR^{2m+1}$ as a closed subspace.
:::

::: {.solution}
The argument is the card's own: no retained set proves this corollary, as the audit records. It combines two cards of this section, and the corollary in the book is printed immediately after them: Munkres §50 Exercise 7 (printed p. 316), the theorem of Exercise 6 (printed p. 315) on a locally compact Hausdorff space with a countable basis whose compact subspaces have dimension at most $m$, and the corollary of Exercise 9 (printed p. 316) that an $m$-manifold has dimension at most $m$.

Throughout, $M$ is an $m$-manifold: a Hausdorff space with a countable basis in which every point has a neighbourhood homeomorphic with an open subset of $\RR^m$ (§36, printed p. 225).

::: pf

::: {.pf-step #hypotheses}
$M$ is locally compact Hausdorff with a countable basis.

::: pf-proof
Hausdorff and second countable are part of the definition of an $m$-manifold (printed p. 225). For local compactness, let $x\in M$ and let $U$ be a neighbourhood of $x$ homeomorphic with an open subset of $\RR^m$; inside $U$, and hence inside the corresponding open subset of $\RR^m$, choose a closed ball of positive radius about $x$, which is compact (Theorem 27.3, printed p. 173) and is a neighbourhood of $x$ inside $U$. So every point has a compact neighbourhood.
:::

:::

::: {.pf-step #dimension}
Every compact subspace of $M$ has topological dimension at most $m$.

::: pf-proof
This is what the proof of [[E-PROOB]] establishes, and it is the hypothesis the theorem of step [](#imbedding){.pf-ref} needs, so it is repeated here: a compact $K\subset M$ is covered by finitely many coordinate neighbourhoods, inside a chart each piece is a closed subspace of $\RR^m$ and so has dimension at most $m$, and a finite union of closed subsets of dimension at most $m$ has dimension at most $m$.
:::

:::

::: {.pf-step #imbedding}
$M$ is homeomorphic to a closed subspace of $\RR^{2m+1}$.

::: pf-proof
The theorem of §50 Exercise 6, [[E-26ELV]] (printed p. 315), states that a locally compact Hausdorff space with a countable basis, every compact subspace of which has dimension at most $m$, is homeomorphic to a closed subspace of $\RR^{2m+1}$. Step [](#hypotheses){.pf-ref} gives the first two hypotheses and step [](#dimension){.pf-ref} the third one, so there is a homeomorphism of $M$ onto a closed subspace of $\RR^{2m+1}$, which is the statement of the corollary printed as §50 Exercise 7 (printed p. 316).
:::

:::

:::
:::
