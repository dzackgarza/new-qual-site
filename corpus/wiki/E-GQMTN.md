---
schema: qual/card@1
id: E-GQMTN
kind: exercise
title: "Find all entire functions $f$ satisfying"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - counterexamples
relations: []
review: draft
solved: true
---
:::{.exercise title="?"}
Find all entire functions $f$ satisfying
\[
\abs{f(z)} \geq \abs{z} + 1 &&\forall z\in \CC
.\]

:::

:::{.solution}
The inequality implies $f$ has no zeros, so $g(z) \da 1/f(z)$ is entire.
Moreover it is bounded on $\CC$, since
\[
\abs{g(z)} \leq {1\over \abs{z} + 1} \leq 1
,\]
so $g\equiv c$ is constant by Liouville.
This means $f\equiv c$ is constant, but $\lim_{z\to \infty}g(z) = 0$ forces $c=\infty$, so there are no such entire functions.
:::

