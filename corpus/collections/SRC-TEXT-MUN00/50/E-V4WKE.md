---
schema: qual/card@1
id: E-V4WKE
kind: problem
title: The long line is normal but not metrizable
classification:
  areas:
  - topology
  topics:
  - Manifolds
  - Order Topology
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
    Checked against Munkres, Topology (2000), supplementary Exercise 5 of §50, printed p. 317, with the
    construction of the long line in the exercises of §24 and Theorem 32.4's method for the normality of an
    ordered space. Locally 1-euclidean: each point of the long line has a neighbourhood order-isomorphic to an
    open interval of R. Normal: the long line is a linear continuum, and a linear continuum in its order
    topology is normal. Not metrizable: a metrizable, connected, locally euclidean space has each component an
    m-manifold and so a countable basis, by the last supplementary exercise, while the long line has no
    countable basis. Nothing needed correction.
---

::: {.exercise}

Show that the long line ([[E-PQHZN]]) is locally 1-euclidean and satisfies (iv) but not (iii) of Exercise 2.
:::

::: {.solution}
Let $L$ be the long line of [[E-PQHZN]]. By [[E-PQHZN]], every point of $L$ has a neighborhood homeomorphic to an open interval in $\RR$, so $L$ is locally $1$-euclidean.

As a linearly ordered space in its order topology, $L$ is a linear continuum; every linear continuum is normal. Hence $L$ satisfies condition (iv) of [[E-OYPV7]].

It is not metrizable. If it were metrizable, then because it is connected and locally $1$-euclidean, [[E-LI4O5]] would make its unique component a $1$-manifold with a countable basis. But by [[E-PQHZN]] the long line has no countable basis. Therefore condition (iii) fails. Thus $L$ satisfies (iv) but not (iii).
:::
