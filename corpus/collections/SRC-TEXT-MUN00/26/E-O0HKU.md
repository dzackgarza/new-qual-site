---
schema: qual/card@1
id: E-O0HKU
kind: problem
title: Maps from compact to Hausdorff spaces are closed
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Continuous Functions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.exercise}

Show that if $f: X \to Y$ is continuous, where $X$ is compact and $Y$ is Hausdorff, then $f$ is a closed map (that is, $f$ carries closed sets to closed sets).
:::

::: {.solution}
Let $C$ be closed in $X$. Every open cover of $C$, together with the open set $X\setminus C$, covers compact $X$; hence $C$ is compact. Since $f$ is continuous, $f(C)$ is compact: an open cover of $f(C)$ pulls back to one of $C$, and a finite subcover pushes forward.

A compact subset of a Hausdorff space is closed. Indeed, for $y\notin f(C)$, separate $y$ from each point of $f(C)$ by disjoint open neighborhoods; compactness gives finitely many neighborhoods covering $f(C)$, and the intersection of the corresponding neighborhoods of $y$ misses $f(C)$. Thus $f(C)$ is closed in $Y$. Since $C$ was arbitrary, $f$ is a closed map.
:::
