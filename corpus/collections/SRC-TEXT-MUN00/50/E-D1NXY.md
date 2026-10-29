---
schema: qual/card@1
id: E-D1NXY
kind: problem
title: The line is a manifold that is not compact
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

Show that $\RR$ is locally 1-euclidean and satisfies (ii) but not (i) of Exercise 2.
:::

::: {.solution}
The usual line \(\RR\) is locally \(1\)-euclidean since every point has an open interval neighborhood homeomorphic to an open interval of \(\RR\). It is Hausdorff and has the countable basis of intervals with rational endpoints, so it is a \(1\)-manifold; thus it satisfies condition (ii) of [[E-OYPV7]].

It is not compact: the open cover
\[
\{(-n,n):n\in\ZZ_+\}
\]
has no finite subcover. Hence condition (i) fails. Therefore \(\RR\) is locally \(1\)-euclidean and satisfies (ii) but not (i).
:::
