---
schema: qual/card@1
id: D-VARCOMP
kind: definition
title: Complete varieties, and how completeness sits against projectivity
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
A variety $X$ over $k$ is \dfn{complete}, equivalently **proper**, if the structure morphism $X \to \Spec k$ is proper: separated and universally closed.
Finite type is automatic for varieties, so only the two substantive conditions are being asserted.
:::

::: {.proposition title="What completeness buys"}
If $X$ is complete then $\OO_X(X) = k$, the image of $X$ under any morphism is closed, and any morphism from $X$ to an affine variety is constant.
Every projective variety is complete; over $\CC$, completeness is compactness in the Euclidean topology.
:::

::: {.remark}
The standard non-example is $\AA^1$, and the witness must be a base change, not a closed-map check on $\AA^1$ itself: the projection $\AA^1 \times \AA^1 \to \AA^1$ sends the closed hyperbola $V(xy-1)$ to $\AA^1 \sm \ts{0}$, which is not closed.
Producing this on demand is the usual follow-up to the definition.

The converse of "projective implies complete" is false, and knowing that is the point of having a separate word: Nagata and Hironaka produced complete non-projective varieties, all of dimension at least three, since a complete curve or normal complete surface is projective.
The function-count consequence $\OO_X(X) = k$ is the same argument that appears for projective varieties, run one level up.
:::
