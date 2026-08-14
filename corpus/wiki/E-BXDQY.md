---
schema: qual/card@1
id: E-BXDQY
kind: exercise
title: "Rudin 10.3"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - removable-singularities
  - entire-functions
relations: []
review: draft
---
:::{.exercise title="Rudin 10.3"}
Suppose $\abs{f(z)}\leq \abs{g(z)}$ for all $z$.
What conclusion can you draw?

:::

:::{.solution}
Write $h(z) \da f(z)/g(z)$, then $\abs{f}\leq 1$ is bounded.
Provided the zeros of $g$ do not have a limit point, the singularities of $h$ are isolated and thus removable.
By Riemann's removable singularity theorem, $h$ extends to an entire function.
By continuity, $\abs{h(z)}\leq 1$ on $\CC$ and is thus bounded.
By Liouville $h$ is constant, making $f = cg$ for some $c$.
:::

