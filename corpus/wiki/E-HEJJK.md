---
schema: qual/card@1
id: E-HEJJK
kind: exercise
title: "Entire functions missing a disc"
classification:
  areas:
  - complex-analysis
  topics:
  - liouville-s-theorem
  - entire-functions
  - removable-singularities
relations: []
review: draft
---
:::{.exercise title="Entire functions missing a disc"}
Show that if $f$ is entire and there exists a disc $\DD_r(a)$ not intersecting $f(\CC)$, then $f$ must be constant.

:::

:::{.solution}
Write $a\not\in f(\CC)$, and replace $f$ with $f(z) - a$ so that $f(a) = 0$ and there is some $\DD_R(0)$ not intersecting $f(\CC)$.
Then $f(z) \in \DD_R^c$ for all $z\in \CC$, so $\abs{f(z)} > R$ for all $z$.
Defining $G(z) \da {1\over f(z)}$ yields $\abs{G(z)} < R\inv$ for all $z$, making $G$ bounded.
The singularity of $G$ at $z=0$ is thus removable, so $G$ extends to an entire function by Riemann's removable singularity theorem.
By Liouville, $G$ is constant, so $f$ is constant.
:::
