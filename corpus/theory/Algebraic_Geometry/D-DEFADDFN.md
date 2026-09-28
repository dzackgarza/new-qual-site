---
schema: qual/card@1
id: D-DEFADDFN
kind: definition
title: Additive functors
classification:
  areas:
  - algebraic-geometry
  topics:
  - Category Theory
  - Homological Algebra
relations:
- kind: uses
  target: D-DEFABCAT
review: draft
prompts:
- What is an additive functor?
- Why is additivity a prerequisite for defining derived functors?
---

::: {.definition title="additive functor"}
A covariant functor $F: \mca \to \mcb$ between abelian categories is \dfn{additive} if the induced map
$$
\Hom_{\mca}(A, A') \to \Hom_{\mcb}(F(A), F(A'))
$$
is a homomorphism of abelian groups, that is, $F(f+g) = F(f) + F(g)$ for all $f, g \in \Hom(A,A')$.
:::

::: {.remark}
An additive functor sends zero morphisms to zero morphisms, so it carries a complex to a complex: $F(\delta^{i+1}) \circ F(\delta^i) = F(\delta^{i+1}\circ \delta^i) = F(0) = 0$.
If $f-g=\delta h+h\delta$ is a homotopy of morphisms of complexes, then additivity gives $F(f)-F(g)=F(\delta)F(h)+F(h)F(\delta)$, so $F$ carries homotopic morphisms to homotopic morphisms.
Since any two injective resolutions of an object are homotopy equivalent, $R^iF$ is well defined up to canonical isomorphism for additive $F$.
An additive functor also preserves finite biproducts.
:::
