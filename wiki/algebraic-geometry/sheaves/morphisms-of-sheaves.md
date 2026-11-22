---
title: Morphisms of sheaves
order: 4
topics:
- Sheaves
- Sheaf Hom
- Exact Sequences
---

# Morphisms of sheaves

Kernels, images, and cokernels of a morphism of sheaves differ in whether they need sheafifying ([[D-A7LCT]]): the kernel of a map of sheaves is a subsheaf of the source and needs no repair, while the presheaf cokernel need not be a sheaf, so the cokernel in the category is its sheafification.

## Kernels, images, and cokernels

[[D-A7LCT]]

Sheafifying the presheaf image and the presheaf cokernel gives the image and cokernel sheaves, and with those the $\OO_X$-modules form an abelian category in which the first isomorphism theorem holds ([[D-DEFABCAT]]).

## Stalks decide

[[PR-C9ZEK]]

A morphism is a monomorphism exactly when it is injective on every stalk, and an epimorphism exactly when it is surjective on every stalk, but a morphism that is onto on stalks need not be onto on global sections.
The standard instance is $\exp\colon\OO_X\to\OO_X^\times$ on $X=\CC\sm\theset{0}$: surjective on stalks, not surjective on $\OO_X(X)$, and the obstruction to a global logarithm is a class in $H^1(X,\ZZ)$ ([[FE-DNTT6]]).
That gap is what the long exact sequence of cohomology measures ([[PR-COHLES]]).

## The sheaf of homomorphisms

[[D-MODOX]]

The presheaf $U\mapsto\Hom_{\OO_U}(\restrictionof{\mcf}{U},\restrictionof{\mcg}{U})$ of homomorphisms between the restrictions is already a sheaf, and this is where it differs from the tensor presheaf: a homomorphism is a rule on the sections of each open set, and two such rules that agree after restriction to every member of a cover agree everywhere, because the sections they are applied to glue ([[D-MODOX]]).
So $\sheafhom(\mcf,\mcg)$ exists with no sheafification, its sections over $U$ are the homomorphisms over $U$, and $\sheafhom(\OO_X,\mcg)\cong\mcg$.

## The espace étalé

[[D-VJFAP]]

Sheafification can be described without the axiom: turn each stalk into a point over the point it came from, topologise the disjoint union so that every germ has a neighbourhood of germs of one section, and the continuous sections of the resulting local homeomorphism are the sheaf.
In that description a morphism of sheaves is a continuous map of the étale spaces over $X$, and injective, surjective, and bijective on stalks become injective, surjective, and bijective on the étale spaces — which is the geometric form of [[PR-C9ZEK|the stalk criterion]].

## Where a morphism that is onto fails to split

A surjection of sheaves of $\OO_X$-modules is onto on every stalk and need not be onto on the sections over $X$: the [[FE-DNTT6|exponential]] is the example. On $X=\Spec A$ with $A$ noetherian, a surjection of quasicoherent sheaves is surjective on global sections ([[T-COHAFF]]).
Splitting is a separate condition, and it is what $\Ext^1$ measures: the extensions of $\mcf$ by $\mcg$ are in bijection with $\Ext^1(\mcg,\mcf)$, with the split extension as the zero class, so a surjection splits exactly when its class vanishes ([[D-DEFEXT]]).
