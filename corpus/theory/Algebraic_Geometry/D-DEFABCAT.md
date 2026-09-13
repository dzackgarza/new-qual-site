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
An abelian category is a category $\mca$ such that

(i) for all objects $A, B$, $\Hom(A, B)$ is an abelian group;

(ii) composition distributes: $f \circ (g+h) = (f\circ g) + (f \circ h)$ and $(f+g)\circ h = (f \circ h) + (g\circ h)$;

(iii) biproducts $A \oplus B$ exist, hence so do all finite sums;

(iv) for every $f: A \to B$, $\ker f$ and $\coker f$ exist;

(v) every monomorphism is the kernel of its cokernel, and every epimorphism is the cokernel of its kernel;

(vi) every morphism $f: A \to B$ factors as $f = g \circ h$ with $h$ an epimorphism and $g$ a monomorphism, so that $f$ surjects onto its image, which injects into the target.
:::

::: {.remark}
Axioms (i)--(iii) are the additive axioms; (iv)--(vi) are what make homological algebra possible.
Axiom (v) is the first isomorphism theorem in categorical form, and it is exactly what fails in the additive categories that are not abelian: filtered vector spaces and topological abelian groups both have kernels and cokernels, but a map there can be both mono and epi without being an isomorphism.

The examples that matter for this exam are $\Ab$, $\mods{A}$ for a ring $A$, and $\mods{\OO_X}$ on a ringed space.
Sheaves of abelian groups on a space form an abelian category, but the cokernel there is the *sheafified* presheaf cokernel.
That single sheafification is why global sections is only left exact, and hence why sheaf cohomology exists at all.
:::
