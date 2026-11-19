---
schema: qual/card@1
id: D-VARMORPH
kind: definition
title: Morphisms of varieties
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Varieties
  - Regular Maps
relations:
- kind: uses
  target: D-VARREG
- kind: related-to
  target: T-SK599
review: draft
prompts:
- What is a morphism of varieties?
- When is a map of sets between varieties a morphism?
- How is a morphism to an affine variety determined by regular functions?
---

::: {.definition title="morphism of varieties"}
Let $k$ be an algebraically closed field and let $X$ and $Y$ be varieties over $k$.
A \dfn{morphism} $\varphi\colon X\to Y$ is a continuous map such that for every open $U\subseteq Y$ and every regular function $f\in\OO_Y(U)$, the composite $f\circ\varphi$ is a regular function on $\varphi^{-1}(U)$ [@Har77, §I.3, p. 15].
An \dfn{isomorphism} of varieties is a morphism with a two-sided inverse, and composition of morphisms is a morphism [@Har77, §I.3, p. 16].
:::

::: {.lemma title="Morphisms to affine space"}
Let $X$ be a variety and $Y\subseteq\AA^n$ an affine variety.
A map of sets $\psi\colon X\to Y$ is a morphism if and only if each $x_i\circ\psi$ is a regular function on $X$ [@Har77, Lemma I.3.6, p. 20].
A morphism between quasi-projective varieties is therefore given locally by polynomials, homogeneous of the same degree in the projective coordinates, with no common zero ([[D-VARREG]]).
:::

::: {.remark}
Two morphisms $f,g\colon X\to Y$ that agree on a nonempty open subset of an irreducible variety agree everywhere: the agreement locus is closed when $Y$ is separated, and it contains a nonempty open subset of an irreducible space.
:::
