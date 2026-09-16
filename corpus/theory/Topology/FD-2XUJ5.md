---
schema: qual/card@1
id: FD-2XUJ5
kind: definition
title: Locally homeomorphic spaces
prompts:
- What does it mean for $X$ to be locally homeomorphic to $Y$?
classification:
  areas:
  - topology
  topics:
  - Homeomorphisms
  - Point-Set Topology
relations: []
review: draft
---

::: {.definition}
Let $X$ and $Y$ be topological spaces.
The space $X$ is \dfn{locally homeomorphic} to $Y$ if every $x\in X$ has an open [[D-JMRPA|neighborhood]] $U_x$ that is [[D-9KQZT|homeomorphic]] to an open subset of $Y$.
:::

::: {.remark}
If there is a [[FD-ONITX|local homeomorphism]] $f\colon X\to Y$, then $X$ is locally homeomorphic to $Y$; the converse fails.
:::

::: {.example}
The sphere $S^2$ is locally homeomorphic to $\RR^2$, by stereographic projection from each of two antipodal points, but there is no local homeomorphism $f\colon S^2 \to \RR^2$: the image $f(S^2)$ would be a nonempty subset of $\RR^2$ that is open, because local homeomorphisms are open maps, and closed, because it is compact, hence equal to the noncompact space $\RR^2$.
:::
