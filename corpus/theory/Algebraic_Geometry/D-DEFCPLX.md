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
- When are two morphisms of complexes homotopic, and what do homotopic morphisms induce on cohomology?
---

::: {.definition title="complex"}
In an abelian category $\mca$, a \dfn{complex} $A^\bullet$ is a family of objects $A^i$, $i \in \ZZ$, with maps $\delta^i: A^i \to A^{i+1}$ such that $\delta^{i+1}\circ \delta^i = 0$ for all $i$; equivalently $\im \delta^i \subseteq \ker \delta^{i+1}$.
Its cohomology is $h^i(A^\bullet) \definedas \ker \delta^i / \im \delta^{i-1}$.

A \dfn{morphism of complexes} $f: A^\bullet \to B^\bullet$ is a family $f^i: A^i \to B^i$ commuting with the differentials, $\delta^i \circ f^i = f^{i+1}\circ \delta^i$.
:::

::: {.definition title="homotopic"}
Morphisms of complexes $f, g: A^\bullet \to B^\bullet$ are \dfn{homotopic}, written $f \sim g$, if there are maps $h^i: A^i \to B^{i-1}$ with
$$
f^i - g^i = \delta^{i-1}h^i + h^{i+1}\delta^i
$$
for all $i$.
:::

::: {.proposition}
Homotopic morphisms of complexes induce the same map $h^i(A^\bullet) \to h^i(B^\bullet)$ on cohomology.
:::

::: {.remark}
Any two injective resolutions $I^\bullet$, $J^\bullet$ of an object $A$ are homotopy equivalent through morphisms lifting $\id_A$.
An additive functor $F$ carries this homotopy equivalence to a homotopy equivalence $F(I^\bullet)\simeq F(J^\bullet)$, so $h^i(F(I^\bullet))\cong h^i(F(J^\bullet))$ and $R^iF(A)$ is independent of the injective resolution up to canonical isomorphism.
:::
