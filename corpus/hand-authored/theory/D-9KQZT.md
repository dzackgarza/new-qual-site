---
schema: qual/card@1
id: D-9KQZT
kind: definition
title: Homeomorphism
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Continuity
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X, Y$ be topological spaces and $f: X\to Y$ a bijection.
Then $f$ is a **homeomorphism** iff both $f$ and $f\inv$ are continuous, equivalently iff $f$ is a continuous open bijection, equivalently iff
\[
U \subseteq X \text{ open} \iff f(U)\subseteq Y \text{ open}
.\]
Such an $f$ is a bijection on points and on open sets at once, so every property of $X$ expressed in terms of its topology transfers to $Y$; write $X\cong Y$.
An injective $f: X\to Y$ that is a homeomorphism onto $f(X)$ with the subspace topology is an **embedding**.
:::

::: {.concept}
See Munkres, §18.
:::
