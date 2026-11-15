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
---

::: {.exercise}

Corollary.
Every $m$-manifold can be imbedded in $\RR^{2m+1}$ as a closed subspace.
:::

::: {.solution}
An $m$-manifold $M$ is locally compact Hausdorff and second-countable, and every compact subspace of $M$ has dimension at most $m$, as shown in the proof of [[E-PROOB]]. By [[E-26ELV]], a locally compact Hausdorff space with a countable basis, all of whose compact subspaces have dimension at most $m$, embeds as a closed subspace of $\RR^{2m+1}$. Therefore there is an embedding
$$
M\hookrightarrow\RR^{2m+1}
$$
whose image is closed.
:::
