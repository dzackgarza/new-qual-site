---
schema: qual/card@1
id: E-4J6IB
kind: exercise
title: "When bounds imply removability"
classification:
  areas:
  - complex-analysis
  topics:
  - removable-singularities
  - singularities
relations: []
review: draft
solved: true
---
:::{.exercise title="When bounds imply removability"}
Suppose $f$ is holomorphic with $z_0 = 0$ an isolated singularity, and suppose there is some neighborhood of $0$ on which
\[
\abs{f(z)} \leq \abs{z}^{-{ 1\over 2}}
.\]
Show that $z_0$ is removable.

> Warning: Riemann's removable singularity theorem won't apply to $z^{1\over 2}f(z)$ since $z^{1\over 2}$ is highly singular at $z=0$.

:::

:::{.solution}
Using the inequality,
\[
\abs{(z-0)f(z)} \leq \abs{z}^{1\over 2}\convergesto{\abs{z}\to 0}0
,\]
so $z=0$ is removable by Riemann's removable singularity theorem.
:::
