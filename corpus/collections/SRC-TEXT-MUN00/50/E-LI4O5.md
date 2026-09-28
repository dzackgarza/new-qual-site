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
---

::: {.exercise}

Let $X$ be a space that is locally $m$-euclidean.
Show that if $X$ is metrizable, then each component of $X$ is an $m$-manifold.
:::

::: {.solution}
Let \(C\) be a component of the metrizable locally \(m\)-euclidean space \(X\).

A locally euclidean space is locally path connected, so its components are open. Hence \(C\) is itself locally \(m\)-euclidean and metrizable (therefore Hausdorff).

It remains to prove that \(C\) has a countable basis. The space \(C\) is locally compact, since every point has a neighborhood homeomorphic to \(\mathbb R^m\), and Hausdorff. It is metrizable, hence paracompact by Stone's theorem. A connected space is its own unique component, so by [[E-GZX7B]], applied to the locally compact paracompact Hausdorff space \(C\), the space \(C\) has a countable basis. Hence \(C\) is Hausdorff, second-countable, and locally \(m\)-euclidean: it is an \(m\)-manifold.
:::
