---
schema: qual/card@1
id: D-VARLOGRES
kind: definition
title: Log resolutions
classification:
  areas:
  - algebraic-geometry
  topics:
  - Resolution of Singularities
  - Normal Crossings
  - Blowups
relations:
- kind: uses
  target: D-VARNCROSS
- kind: uses
  target: D-VARBLOW
review: draft
prompts:
- What is a log resolution?
---

::: {.definition title="Log resolution"}
Let $X$ be a variety and $D \subseteq X$ a closed subset of codimension at least $1$, possibly empty.
A \dfn{log resolution} of the pair $(X, D)$ is a proper birational morphism $f \colon Y \to X$ such that $Y$ is smooth, the exceptional locus $\operatorname{Exc}(f)$ is a divisor, and $\operatorname{Exc}(f) \cup f^{-1}(D)$ is a simple normal crossing divisor.
:::

::: {.theorem title="Hironaka"}
Over a field of characteristic $0$, every pair $(X, D)$ has a log resolution, which can be taken to be a composite of blowups along smooth centres and an isomorphism over the open set where $X$ is smooth and $D$ is a simple normal crossing divisor.
:::

::: {.example}
For the cuspidal curve $D = V(y^2 - x^3) \subseteq \AA^2 = X$, one blowup at the origin makes the strict transform smooth but tangent to the exceptional curve $E_1$.
A second blowup leaves the strict transform and the two exceptional curves passing through one point, which is not a normal crossing.
A third blowup at that point gives a log resolution: the total transform is a simple normal crossing divisor.
:::
