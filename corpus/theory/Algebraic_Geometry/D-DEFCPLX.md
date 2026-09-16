---
schema: qual/card@1
id: D-DEFCPLX
kind: definition
title: Complexes, morphisms of complexes, and chain homotopy
classification:
  areas:
  - algebraic-geometry
  topics:
  - Homological Algebra
  - Complexes
relations:
- kind: uses
  target: D-DEFABCAT
review: draft
prompts:
- What is a complex in an abelian category, and what is a morphism of complexes?
- When are two morphisms of complexes homotopic, and why does that matter?
---

::: {.definition title="complex"}
In an abelian category $\mca$, a \dfn{complex} $A^\bullet$ is a family of objects $A^i$, $i \in \ZZ$, with maps $\delta^i: A^i \to A^{i+1}$ such that $\delta^{i+1}\circ \delta^i = 0$ for all $i$; equivalently $\im \delta^i \subseteq \ker \delta^{i+1}$.
Its cohomology is $h^i(A^\bullet) \da \ker \delta^i / \im \delta^{i-1}$.

A **morphism of complexes** $f: A^\bullet \to B^\bullet$ is a family $f^i: A^i \to B^i$ commuting with the differentials, $\delta^i \circ f^i = f^{i+1}\circ \delta^i$.
:::

::: {.definition title="homotopic"}
Morphisms of complexes $f, g: A^\bullet \to B^\bullet$ are \dfn{homotopic}, written $f \sim g$, if there are maps $h^i: A^i \to B^{i-1}$ with
\[
f^i - g^i = \delta^{i-1}h^i + h^{i+1}\delta^i
\]
for all $i$.
:::

::: {.remark}
Homotopic maps induce the same map $h^i(A^\bullet) \to h^i(B^\bullet)$ on cohomology.
This is the whole reason derived functors are well defined: two injective resolutions of $A$ are only homotopy equivalent, never equal, so $R^iF(A)$ is independent of the resolution exactly because cohomology cannot see a homotopy.
:::
