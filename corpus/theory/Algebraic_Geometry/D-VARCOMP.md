---
schema: qual/card@1
id: D-VARCOMP
kind: definition
title: Complete varieties and projectivity
classification:
  areas:
  - algebraic-geometry
  topics:
  - Complete Varieties
  - Proper Morphisms
  - Projective Varieties
relations:
- kind: uses
  target: D-8XX95
review: draft
prompts:
- What is a complete variety?
- What is a proper variety?
- Give an example of a non-proper variety.
---

::: {.definition title="Complete"}
A variety $X$ over $k$ is \dfn{complete}, equivalently \dfn{proper}, if the structure morphism $X \to \Spec k$ is proper: separated, of finite type, and universally closed.
:::

::: {.proposition title="Consequences of completeness"}
Let $k$ be algebraically closed and $X$ a complete variety over $k$.
Then $\OO_X(X) = k$, the image of $X$ under any morphism of varieties is closed, and any morphism from $X$ to an affine variety is constant.
Every projective variety is complete; over $\CC$, a variety is complete if and only if it is compact in the Euclidean topology.
:::

::: {.remark}
$\AA^1$ is not complete, although $\AA^1\to\Spec k$ is a closed map: after base change, the projection $\AA^1 \times \AA^1 \to \AA^1$ sends the closed hyperbola $V(xy-1)$ to $\AA^1 \sm \ts{0}$, which is not closed.

Complete varieties need not be projective: Hironaka constructed a nonsingular complete threefold that is not projective.
Every complete curve and every nonsingular complete surface is projective, while there are complete normal surfaces that are not projective.
:::
