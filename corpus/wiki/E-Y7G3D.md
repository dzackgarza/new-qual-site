---
schema: qual/card@1
id: E-Y7G3D
kind: exercise
title: "Suppose that $g$ is entire and satisfies the functional equation $g(1-\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Suppose that $g$ is entire and satisfies the functional equation $g(1-z) = 1-g(z)$.
Show that $g(\CC) = \CC$.

#complex/exercise/completed

:::

:::{.solution}
By Picard, $g$ omits at most one value $a$.
Note that $a\neq 1/2$, since $g(a) = g(1/2) = g(1-1/2) = 1-g(1/2) = 1-g(a)$, so $2g(a) = 1$ and $g(a) = 1/2$.
Noting that $1-a\neq a$ for any $a$ other than $1/2$, we have that $w\da 1-a\in g(\CC)$.
Then $g(w) \da g(1-a) = 1-g(a) = 1 - w = 1-(1-a) = a$, so $a\in g(\CC)$ and $g$ omits no values.
:::
