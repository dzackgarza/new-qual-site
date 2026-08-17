---
schema: qual/card@1
id: E-W2CWJ
kind: exercise
title: "Removable singularity at infinity iff constant"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - removable-singularities
  - singularities
relations: []
review: draft
solved: true
---

::: {.exercise title="Removable singularity at infinity iff constant"}
Let $f$ be entire.
Show that $f$ has a removable singularity at $z_0 = \infty$ iff $f$ is constant.
:::

::: {.solution}
Suppose $f$ is not constant.
If $z=\infty$ is removable, $f$ is bounded in a neighborhood of $\infty$, say by $M_1$ on $\abs{z} > R$.
Now $\abs{z} \leq R$ is a closed and bounded set, thus compact, and since $f$ is continuous here it is bounded by the extreme value theorem, say by $M_2$.
Then $\abs{f(z)} \leq \max(M_1, M_2)$ on $\CC$ is entire and bounded, thus constant by Liouville, a contradiction.
$\contradiction$

Conversely, if $f$ is constant, $f$ is trivially bounded in every neighborhood of $\infty$, making it a removable singularity.
:::
