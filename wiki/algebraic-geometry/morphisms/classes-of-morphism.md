---
title: Classes of morphism
order: 3
topics:
- Immersions
- Finite Type Morphisms
- Projective Morphisms
---

# Classes of morphism

The definitions on this page are short, and the useful content is the ordering between them and the example separating each adjacent pair.
State the chain and the counterexamples together.

## Immersions

[[D-MORIMM]]

Immersions are where the scheme structure first does work that the topology cannot: a homeomorphism onto a closed subset need not be a closed immersion, because the scheme structure on the subset carries nilpotents that the topology cannot see.

## Affine, finite, and finite type

[[D-MORAFF]]

[[D-MORFT]]

[[D-MORFIN]]

Finite against finite type is a one-line distinction that is asked directly: finitely generated as a module against as an algebra, with $\AA^1_k \to \Spec k$ separating them.

[[D-MORQF]]

[[FE-MORHYP]]

[[PR-MORFINCHAR]]

## Projective

[[D-MORPROJ]]

The chain to carry is
\[
\text{closed immersion} \implies \text{finite} \implies \text{projective} \implies \text{proper} \implies \text{universally closed} ,
\]
together with the fact that finite type sits underneath all of it and is implied by each.
Every arrow has a standard counterexample to its converse, and the two worth having on hand are $\PP^1_k \to \Spec k$, projective and not finite, and the hyperbola projection, quasi-finite and not proper.

## Base change

[[D-MORFIB]]

[[PR-MORBC]]

Stability under base change is what turns a property of a morphism into a property of its fibres, and it is why properness is defined with the word *universally* in it rather than by closedness alone.
