---
schema: qual/card@1
id: D-DEFABCAT
kind: definition
title: Abelian categories
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Abelian Categories
  - Homological Algebra
relations: []
review: draft
prompts:
- What is an abelian category?
- Which axiom gives the first isomorphism theorem, and which gives the image factorisation?
- Name an additive category that is not abelian.
---

::: {.definition title="abelian category"}
An \dfn{abelian category} is a category $\mca$ such that

(i) for all objects $A, B$, $\Hom(A, B)$ is an abelian group;

(ii) composition distributes: $f \circ (g+h) = (f\circ g) + (f \circ h)$ and $(f+g)\circ h = (f \circ h) + (g\circ h)$;

(iii) biproducts $A \oplus B$ exist, hence so do all finite sums;

(iv) for every $f: A \to B$, $\ker f$ and $\coker f$ exist;

(v) every monomorphism is the kernel of its cokernel, and every epimorphism is the cokernel of its kernel;

(vi) every morphism $f: A \to B$ factors as $f = g \circ h$ with $h$ an epimorphism and $g$ a monomorphism, so that $f$ surjects onto its image, which injects into the target.
:::

::: {.remark}
Axioms (i)--(iii) say that $\mca$ is additive.
Axiom (v) is the first isomorphism theorem in categorical form: with (iv), it makes the canonical map $\coim f\to\im f$ an isomorphism for every $f$, so a morphism that is both a monomorphism and an epimorphism is an isomorphism.
The additive category of topological abelian groups has kernels and cokernels but is not abelian: the identity map from $\RR$ with the discrete topology to $\RR$ with the Euclidean topology is a monomorphism and an epimorphism but not an isomorphism.

Examples include $\Ab$, $\mods{A}$ for a ring $A$, and $\mods{\OO_X}$ on a ringed space.
Sheaves of abelian groups on a space form an abelian category, whose cokernel is the sheafification of the presheaf cokernel ([[D-A7LCT]]).
The functor $\Gamma(X,\wait)$ preserves kernels but not cokernels: on $X=\CC\sm\ts{0}$, $\exp\colon\OO_X\to\OO_X^\times$ is an epimorphism of sheaves, and $z\in\OO_X^\times(X)$ is not the image of any section of $\OO_X$ over $X$.
:::
