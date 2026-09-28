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
A morphism $f : X \to Y$ is \dfn{separated} if the diagonal
$$
\Delta_{X/Y} : X \to \fiberprod{X}{Y}{X}
$$
is a closed immersion.
It is \dfn{quasi-separated} if $\Delta_{X/Y}$ is quasicompact, equivalently if for every affine open $V \subseteq Y$ the scheme $f^{-1}(V)$ is quasi-separated in the sense below.
:::

::: {.definition title="Quasicompact and quasi-separated"}
A scheme $X$ is \dfn{quasicompact} if every open cover of $X$ has a finite subcover, and a morphism $f: X \to Y$ is \dfn{quasicompact} if $f^{-1}(V)$ is quasicompact for every affine open $V \subseteq Y$.
A scheme $X$ is \dfn{quasi-separated} if the intersection of any two quasicompact open subsets of $X$ is quasicompact, equivalently if the intersection of any two affine open subsets is quasicompact; this is quasi-separatedness of $X \to \Spec \ZZ$.
:::

::: {.remark}
A topological space $X$ is Hausdorff if and only if the diagonal is closed in $X\times X$ with the product topology.
An irreducible variety of positive dimension is not Hausdorff in the Zariski topology, since any two nonempty open subsets meet; and the underlying space of $\fiberprod{X}{Y}{X}$ is in general not the product space.
Separatedness asks that the diagonal be closed in the fibre product of schemes: $\AA^1_k$ is separated over $k$, while the line $X$ with a doubled origin is not, since the closure of the diagonal in $X\times_kX$ contains the point $(0_1,0_2)$ for the two origins $0_1\ne0_2$.

Every separated morphism is quasi-separated, and every morphism from a Noetherian scheme is quasi-separated.
Gluing two copies of $\Spec k[x_1,x_2,\ldots]$ along the complement of the origin gives a scheme that is not quasi-separated: the intersection of the two affine copies is not quasicompact.
:::
