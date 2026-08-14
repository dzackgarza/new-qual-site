---
schema: qual/card@1
id: P-BUD7S
kind: problem
title: "Suppose $A, B \\subseteq \\RR^n$ are disjoint and compact. Prove that there exist $a\\in A, b\\in B$\u2026"
classification:
  areas:
  - complex-analysis
  topics:
  - compactness
  - metric-spaces
  - euclidean-spaces
relations: []
review: draft
---
:::{.problem title="?"}
Suppose $A, B \subseteq \RR^n$ are disjoint and compact.
Prove that there exist $a\in A, b\in B$ such that
\[  
\norm{a - b} = \inf\theset{\norm{x-y} \suchthat x\in A,\, y\in B}
.\]
:::

:::{.solution}
Define a function
\[
d: A \cross B &\to \RR \\
(x, y) &\mapsto \norm{x- y}
.\]
Then $d$ is a continuous function on a compact topological space (where the product is compact by Tychonoff), and the extreme value theorem applies: $d$ attains its min/max for some pair $(a, b)$ in its domain.

> Note that disjointness just guarantees that $\norm{a-b}>0$, since $\norm{a-b} = 0 \implies a=b$ and $A \intersect B = \emptyset$.

:::

