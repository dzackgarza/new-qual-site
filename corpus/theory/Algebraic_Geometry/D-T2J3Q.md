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
- Why is the diagonal the right condition rather than the Hausdorff axiom?
---

::: {.definition title="Separated"}
A morphism $f : X \to Y$ is \dfn{separated} if the diagonal
\[
\Delta_{X/Y} : X \to \fiberprod{X}{Y}{X}
\]
is a closed immersion.
It is **quasi-separated** if $\Delta_{X/Y}$ is quasicompact, equivalently if for every affine open $V \subseteq Y$ the scheme $f^{-1}(V)$ is quasi-separated in the sense below.
:::

::: {.definition title="Quasicompact and quasi-separated"}
A scheme $X$ is **quasicompact** if every open cover of $X$ has a finite subcover, and a morphism $f: X \to Y$ is **quasicompact** if $f^{-1}(V)$ is quasicompact for every affine open $V \subseteq Y$.
A scheme $X$ is **quasi-separated** if the intersection of any two quasicompact open subsets of $X$ is quasicompact, equivalently if the intersection of any two affine open subsets is quasicompact; this is quasi-separatedness of $X \to \Spec \ZZ$.
:::

::: {.remark}
The Hausdorff axiom is not available, because the Zariski topology is never Hausdorff for a positive-dimensional variety: any two nonempty opens meet.
What survives is the equivalent formulation for topological spaces — $X$ is Hausdorff exactly when the diagonal is closed in $X \times X$ — once the product is taken in the right category.
That is the whole content of the definition, and it is the answer to why the definition looks the way it does: the *statement* of Hausdorffness transfers even though the *proof technique* does not, provided $X \times X$ means the fibre product of schemes and not the topological product.

Quasi-separatedness is the same move applied one notch weaker, and it is a finiteness condition rather than a geometric one.
Every separated morphism is quasi-separated, every morphism of Noetherian schemes is quasi-separated, and it is only for non-Noetherian schemes that one has to say so.
:::
