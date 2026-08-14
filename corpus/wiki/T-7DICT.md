---
schema: qual/card@1
id: T-7DICT
kind: theorem
title: "Cantor's Intersection Theorem"
classification:
  areas:
  - topology
  topics:
  - compactness
relations: []
review: draft
---

::: {.theorem title="Cantor's Intersection Theorem"}
Let $X$ be compact and let $C_1 \supseteq C_2 \supseteq \cdots$ be a nested decreasing sequence of nonempty **closed** subsets of $X$.
Then $\Intersect_n C_n \neq \emptyset$.

Equivalently, taking each $C_n$ compact suffices when $X$ is Hausdorff, since a compact subset of a Hausdorff space is closed.
:::

::: {.remark}
Munkres, *Topology*, §26, Theorem 26.9 and the nested-sequence special case that follows it.

Closedness is what the argument uses, and dropping it is not harmless: give an infinite set the indiscrete topology, where every subset is compact, and take $C_n = \ts{n, n+1, \cdots}$. Each is nonempty and compact and the sequence decreases, but the intersection is empty.
:::
