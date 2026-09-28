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
- What is a locally small category?
- Define the Yoneda embedding $h \colon \mathsf{C} \to \operatorname{Fun}(\mathsf{C}^{\mathrm{op}}, \mathsf{Set})$ and show that it is fully faithful.
- If a functor $\mathsf{C} \to \mathsf{Set}$ is representable, show that the representing object is unique up to unique isomorphism.
- Describe initial and terminal objects as limits, and decide whether a product is a limit or a colimit.
---

::: {.definition title="full, faithful, fully faithful"}
A covariant functor $F: \mca \to \mcb$ is \dfn{faithful} if for all objects $A, A'$ the induced map
$$
\Mor_{\mca}(A, A') \to \Mor_{\mcb}(F(A), F(A'))
$$
is injective, \dfn{full} if that map is surjective, and \dfn{fully faithful} if it is bijective.

A subcategory $\mca'$ of $\mca$ is a \dfn{full subcategory} if its inclusion functor is full, that is, $\Mor_{\mca'}(A,A')=\Mor_{\mca}(A,A')$ for all objects $A,A'$ of $\mca'$.
:::

::: {.remark}
The forgetful functor from groups to sets is faithful and not full, since not every map of underlying sets is a homomorphism.

A fully faithful functor reflects isomorphisms, and it is an equivalence of categories if and only if it is essentially surjective.
Examples: $\Spec$ is fully faithful from the opposite of the category of rings to schemes, with essential image the affine schemes; and $M\mapsto\widetilde M$ is an equivalence $\mods{A}\simeq\QCoh(\Spec A)$.
:::
