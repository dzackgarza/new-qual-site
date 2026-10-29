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
If $X$ is an integral complete variety over $k$, then $\Gamma(X,\OO_X)$ is a finite field extension of $k$.
In particular, if $k$ is algebraically closed, then $\Gamma(X,\OO_X)=k$ and every morphism from $X$ to an affine $k$-variety is constant.
The image of $X$ under any morphism to a $k$-variety is closed.
Every projective variety is complete; over $\CC$, completeness is compactness in the Euclidean topology.
:::

::: {.remark}
$\AA^1$ is not complete, although $\AA^1\to\Spec k$ is a closed map: after base change, the projection $\AA^1 \times \AA^1 \to \AA^1$ sends the closed hyperbola $V(xy-1)$ to $\AA^1 \sm \theset{0}$, which is not closed.

The converse of "projective implies complete" is false.
Complete curves and smooth complete surfaces are projective, so a smooth complete non-projective variety has dimension at least three; Hironaka constructed one of dimension three.
Nagata constructed complete non-projective surfaces, which are therefore singular.
:::
