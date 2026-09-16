---
schema: qual/card@1
id: P-AGHOPENDENSE
kind: problem
title: Opens are dense in an irreducible space, and closures stay irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Irreducibility
  - Zariski Topology
relations:
- kind: uses
  target: D-9DIKB
review: draft
---

::: {.problem}
Any nonempty open subset of an irreducible topological space is dense and irreducible.
If $Y$ is a subset of a topological space $X$ which is irreducible in its induced topology, then the closure $\bar{Y}$ is also irreducible.
:::

::: {.solution}
**Density.** Let $U \subseteq X$ be open and nonempty with $X$ irreducible, and suppose $\cl_X(U) \neq X$.
Then
\[
X = (X \sm U) \union \cl_X(U)
\]
writes $X$ as a union of two proper closed subsets, contradicting irreducibility.

**Closures.** Suppose $Y$ is irreducible and write $\cl_X(Y) = A \union B$ with $A, B$ closed in $X$.
Intersecting with $Y$ gives $Y = (A \intersect Y) \union (B \intersect Y)$, so by irreducibility $Y \subseteq A \intersect Y \subseteq A$ after relabelling.
Then $\cl_X(Y) \subseteq \cl_X(A) = A$, so the decomposition was trivial and $\cl_X(Y)$ is irreducible.
:::

::: {.remark}
Irreducible is strictly stronger than connected: connected forbids a decomposition into two proper *disjoint* closed sets, irreducible forbids it without disjointness.
$V(xy)$ is connected and reducible.
:::
