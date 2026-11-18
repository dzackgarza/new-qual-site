---
title: Morphisms of sheaves
order: 4
topics:
- Sheaves
- Sheaf Hom
- Exact Sequences
---

# Morphisms of sheaves

A morphism of sheaves is a morphism of presheaves that happens to respect the gluing, and the two constructions one wants from it — the kernel and the cokernel — do not behave alike.
The kernel of a map of sheaves is a subsheaf of the source and needs no repair; the cokernel is not a sheaf at all until it is sheafified, and that asymmetry is the first place the geometry enters the algebra.
This page fixes the definitions, records the stalk criterion that decides injectivity and surjectivity, and warns where a morphism that is onto as a map of sheaves is not onto on sections.

## Kernels, images, and cokernels

[[D-A7LCT]]

The reason the kernel is a sheaf and the cokernel is not is the direction of the quantifiers: a section is in the kernel when its image is zero, which is a property preserved by restriction, while a section is in the image only when it is locally in the image, which is a property not preserved by the presheaf cokernel's restriction maps.
Sheafifying the presheaf image and the presheaf cokernel gives the image and cokernel sheaves, and with those the $\OO_X$-modules form an abelian category in which the first isomorphism theorem holds ([[D-DEFABCAT]]).

## Stalks decide

[[PR-C9ZEK]]

A morphism is a monomorphism exactly when it is injective on every stalk, and an epimorphism exactly when it is surjective on every stalk, but a morphism that is onto on stalks need not be onto on global sections.
The standard instance is $\exp\colon\OO_X\to\OO_X^\times$ on $X=\CC\sm\theset{0}$: surjective on stalks, not surjective on $\OO_X(X)$, and the obstruction to a global logarithm is a class in $H^1(X,\ZZ)$ ([[FE-DNTT6]]).
That gap is what the long exact sequence of cohomology measures, and it is the reason this chapter is written before the one on cohomology.

## The sheaf of homomorphisms

[[D-MODOX]]

The presheaf $U\mapsto\Hom_{\OO_U}(\mcf_I,\mcg_I)$ of homomorphisms between the restrictions is already a sheaf, and this is where it differs from the tensor presheaf: a homomorphism is a rule on the sections of each open set, and two such functions that agree after restriction to every member of a cover agree everywhere, because the sections they are applied to glue ([[PR-C9ZEK]]).
So $\sheafhom(\mcf,\mcg)$ exists with no sheafification, its sections over $U$ are the homomorphisms over $U$, and $\sheafhom(\OO_X,\mcg)\cong\mcg$.

## The espace étalé

[[D-VJFAP]]

Sheafification can be described without the axiom: turn each stalk into a point over the point it came from, topologise the disjoint union so that every germ has a neighbourhood of germs of one section, and the continuous sections of the resulting local homeomorphism are the sheaf.
In that description a morphism of sheaves is a continuous map of the étale spaces over $X$, and injective, surjective, and bijective on stalks become injective, surjective, and bijective on the étale spaces — which is the geometric form of the stalk criterion above.

## Where a morphism that is onto fails to split

A surjection of sheaves of $\OO_X$-modules need not be a surjection on sections over any fixed open set, so the sequences that look split locally are not split globally.
The measure of the failure is $\Ext^1$: an extension of $\OO_X$-modules that is locally split but not globally split is a class in $\Ext^1(\mcg,\mcf)$, and in degree one that is the same as a class in $H^1(X,\sheafhom(\mcg,\mcf))$.
