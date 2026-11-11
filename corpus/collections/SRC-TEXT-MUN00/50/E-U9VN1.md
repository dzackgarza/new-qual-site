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
