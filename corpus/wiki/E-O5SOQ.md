---
schema: qual/card@1
id: E-O5SOQ
kind: exercise
title: "Suppose $f$ is entire and for every $z$,"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Suppose $f$ is entire and for every $z$,
\[
\abs{f(z)}\leq \abs{\sin(z)}
.\]
Characterize all possibilities for $f$.

 

:::

:::{.solution}
Write $g(z) \da f(z) / \sin(z)$, which is meromorphic with singularities at the zeros of $\sin(z)$ and bounded by 1.
By boundedness, these singularities are removable, so $g$ extends to a bounded entire and thus constant function.
So $f(z) = c\sin(z)$ where $\abs{c} \leq 1$.
:::

