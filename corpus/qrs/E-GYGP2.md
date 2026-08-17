---
schema: qual/card@1
id: E-GYGP2
kind: exercise
title: "Show that if $H < G$ is a proper subgroup, then $\\Union_{g\\in G} gHg\\inv \\subset G$ is a proper\u2026"
classification:
  areas:
  - algebra
  topics:
  - conjugacy
  - centralizers-and-normalizers
  - cosets-and-lagrange
relations: []
review: draft
solved: true
---
:::{.exercise title="?"}
Show that if $H < G$ is a proper subgroup, then $\Union_{g\in G} gHg\inv \subset G$ is a proper subset.

> Hint: consider the intersection and count.
> Try Orbit-stabilizer?

:::

:::{.solution}
Strategy: bound the cardinality.
All conjugates of $H$ have the same cardinality, say $\# H = m$.
Suppose there are $n$ distinct conjugates of $H$.
Then they intersect only at the identity, so count their elements:
\[
\# \Union_{g\in G} gHg\inv = 1 + n(m-1)
.\]
Use that $n = [G: N_G(H)]$ by Orbit-Stabilizer, and $N_G(H) \leq G \implies n \leq n' \da [G:H]$.
Now note $n'm = \# H[G:H] = \# G$ by Lagrange:
\[
\# \Union_{g\in G} gHg\inv 
&= 1 + n(m-1) \\
&\leq 1 + n'(m-1) \\
&= 1 + n'm -n' \\
&= 1 + \# G - n' \\
&= \# G - (n' - 1) \\
&< \# G && \iff n' \da [G:H] > 1
.\]
:::
