---
schema: qual/card@1
id: D-T2J3Q
kind: definition
title: Separated and quasi-separated morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Separated Morphisms
  - Quasi-separated Morphisms
  - Diagonal
relations:
- kind: uses
  target: D-AN662
review: draft
prompts:
- Define separated morphism.
- What does quasi-separated mean?
- How is closedness of the diagonal related to the Hausdorff property?
---

::: {.definition title="Separated"}
A morphism $f\colon X \to Y$ is \dfn{separated} if the diagonal
$$
\Delta_{X/Y} : X \to \fiberprod{X}{Y}{X}
$$
is a closed immersion.
It is \dfn{quasi-separated} if $\Delta_{X/Y}$ is quasicompact, equivalently if for every affine open $V \subseteq Y$ the scheme $f^{-1}(V)$ is quasi-separated in the sense below.
:::

::: {.definition title="Quasicompact and quasi-separated"}
A scheme $X$ is \dfn{quasicompact} if every open cover of $X$ has a finite subcover, and a morphism $f\colon X \to Y$ is \dfn{quasicompact} if $f^{-1}(V)$ is quasicompact for every affine open $V \subseteq Y$.
A scheme $X$ is \dfn{quasi-separated} if the intersection of any two quasicompact open subsets of $X$ is quasicompact, equivalently if the intersection of any two affine open subsets is quasicompact; this is quasi-separatedness of $X \to \Spec \ZZ$.
:::

::: {.remark}
The Hausdorff axiom is not available, because the Zariski topology is never Hausdorff for a positive-dimensional variety: in an irreducible component of positive dimension, any two nonempty opens meet.
What survives is the equivalent formulation for topological spaces — $X$ is Hausdorff exactly when the diagonal is closed in $X \times X$ — once the product is taken in the right category.
Separatedness transfers this closed-diagonal criterion to schemes, with $X\times_YX$ the fibre product in schemes rather than the topological product.

Quasi-separatedness replaces the closed-diagonal condition by quasicompactness of the diagonal.
Every separated morphism is quasi-separated, every morphism of Noetherian schemes is quasi-separated, and it is only for non-Noetherian schemes that one has to say so.
:::
