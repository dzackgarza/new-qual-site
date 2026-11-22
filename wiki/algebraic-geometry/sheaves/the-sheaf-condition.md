---
title: The sheaf condition
order: 1
topics:
- Sheaves
- Presheaves
- Sheafification
---

# The sheaf condition

A presheaf is a contravariant functor from the open subsets of $X$ to abelian groups, and it is a sheaf when both axioms hold: sections over an open set are determined by their restrictions to the members of any open cover (locality), and a family of sections over a cover that agrees on the overlaps comes from a section of the whole (gluing) ([[D-RCCFY]]).

[[D-RCCFY]]

## The two axioms are independent

A nonzero section can be locally zero, and local sections that agree on overlaps can fail to glue, so neither axiom follows from the other ([[FE-AM5Z8]]).
On a disconnected space the constant presheaf fails gluing, the quotient of the continuous functions by the bounded ones has a nonzero class that restricts to zero on every bounded interval, and the tensor presheaf has chartwise sections that agree on the overlap and do not glue ([[FE-AM5Z8]]).

[[FE-AM5Z8]]

## Stalks

The stalk at a point is the colimit of the sections over its neighbourhoods, and a germ is a section on a neighbourhood taken modulo agreement on a smaller one ([[D-0QSI0]]).
For sheaves the local information is complete: a morphism of sheaves is an isomorphism exactly when every induced map of stalks is ([[PR-C9ZEK]]).

[[D-0QSI0]]

[[D-COMMACAT]]

## Sheafification

Every presheaf admits a morphism to a sheaf, universal among morphisms from it to sheaves, and that morphism is an isomorphism on every stalk ([[T-3VX80]]).
Being universal, the sheaf is the sheafification, and it repairs a failure of either axiom ([[T-3VX80]], [[FE-AM5Z8]]).

[[T-3VX80]]

[[D-A7LCT]]

## Sheafification as a space over $X$

Sheafification can be described without the axiom: turn each stalk into a point over the point it came from, topologise the disjoint union so that every germ has a neighbourhood of germs of one section, and the continuous sections of the resulting local homeomorphism are the sheaf ([[D-VJFAP]]).

[[D-VJFAP]]

On a noetherian space the presheaf colimit of a directed system of sheaves is already a sheaf, and global sections commute with the colimit ([[PR-IP6ZG]]); global sections do not commute with directed colimits in general, and the discrete space $\NN$ is the witness, where $\bigoplus_n\ZZ\to\prod_n\ZZ$ is injective and not surjective ([[FE-SHFCOLIMGAMMA]]).

[[PR-IP6ZG]]
