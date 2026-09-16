---
schema: qual/card@1
id: D-DEFFFF
kind: definition
title: Full, faithful, and fully faithful functors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Functors
relations: []
review: draft
prompts:
- Define full, faithful, and fully faithful for a functor.
- What extra condition upgrades a fully faithful functor to an equivalence of categories?
- Give a faithful functor that is not full.
---

::: {.definition title="full, faithful, fully faithful"}
A covariant functor $F: \mca \to \mcb$ is \dfn{faithful} if for all objects $A, A'$ the induced map
\[
\Mor_{\mca}(A, A') \to \Mor_{\mcb}(F(A), F(A'))
\]
is injective, **full** if that map is surjective, and **fully faithful** if it is bijective.

A subcategory $\mca'$ of $\mca$ is called **full** if its inclusion functor is full: it may have fewer objects, but it never loses morphisms between the objects it keeps.
:::

::: {.remark}
The forgetful functor from groups to sets is faithful and not full, since not every map of underlying sets is a homomorphism.

A fully faithful functor is an equivalence of categories exactly when it is additionally essentially surjective, and it then reflects isomorphisms.
That criterion is the one actually used: it is how one states that $\Spec$ is an anti-equivalence from rings to affine schemes, and how one recognises $\QCoh(\Spec A) \simeq \mods{A}$.
:::
