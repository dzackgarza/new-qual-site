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
---

::: {.exercise}

Show that the long line ([[E-PQHZN]]) is locally 1-euclidean and satisfies (iv) but not (iii) of Exercise 2.
:::

::: {.solution}
Let \(L\) be the long line of [[E-PQHZN]]. By [[E-PQHZN]], every point of \(L\) has a neighborhood homeomorphic to an open interval in \(\mathbb R\), so \(L\) is locally \(1\)-euclidean.

As a linearly ordered space in its order topology, \(L\) is a linear continuum; every linear continuum is normal. Hence \(L\) satisfies condition (iv) of [[E-OYPV7]].

It is not metrizable. If it were metrizable, then because it is connected and locally compact, [[E-LI4O5]] would give a countable basis on its unique component. But by [[E-PQHZN]] the long line has no countable basis (indeed no embedding into any \(\mathbb R^n\)). Therefore condition (iii) fails. Thus \(L\) satisfies (iv) but not (iii).
:::
