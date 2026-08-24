---
schema: qual/card@1
id: E-ZCJZC
kind: exercise
title: The union of conjugates of a proper subgroup is a proper subset
classification:
  areas:
  - algebra
  topics:
  - Conjugacy
  - Centralizers and Normalizers
  - Cosets and Lagrange
relations: []
review: draft
---

:::{.exercise title="?"}
Show that if $H < G$ is a proper subgroup, then $\Union_{g\in G} gHg\inv \subset G$ is a proper subset.

> Hint: consider the intersection and count.
> Try Orbit-stabilizer?

:::

:::{.solution}
Strategy: bound the cardinality.
All conjugates of $H$ have the same cardinality, say $\size  H = m$.
Suppose there are $n$ distinct conjugates of $H$.
Then they intersect only at the identity, so count their elements:
\[
\size  \Union_{g\in G} gHg\inv = 1 + n(m-1)
.\]
Use that $n = [G: N_G(H)]$ by Orbit-Stabilizer, and $N_G(H) \leq G \implies n \leq n' \da [G:H]$.
Now note $n'm = \size  H[G:H] = \size  G$ by Lagrange:
\[
\size  \Union_{g\in G} gHg\inv 
&= 1 + n(m-1) \\
&\leq 1 + n'(m-1) \\
&= 1 + n'm -n' \\
&= 1 + \size  G - n' \\
&= \size  G - (n' - 1) \\
&< \size  G && \iff n' \da [G:H] > 1
.\]
:::

