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
A covariant functor $F: \mca \to \mcb$ between abelian categories is **additive** if the induced map
\[
\Hom_{\mca}(A, A') \to \Hom_{\mcb}(F(A), F(A'))
\]
is a homomorphism of abelian groups, that is, $F(f+g) = F(f) + F(g)$ for all $f, g \in \Hom(A,A')$.
:::

::: {.remark}
Additivity is the minimum hypothesis under which $F$ carries a complex to a complex: it is what gives
$F(\delta^{i+1}) \circ F(\delta^i) = F(\delta^{i+1}\circ \delta^i) = F(0) = 0$.
Without it there is nothing to take cohomology of, so every statement about derived functors, $\delta$-functors, and the FHHF theorem silently assumes it.
An additive functor also automatically preserves finite biproducts.
:::
