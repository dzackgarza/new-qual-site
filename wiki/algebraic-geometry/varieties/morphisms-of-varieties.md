---
title: Morphisms of varieties
order: 9
topics:
- Morphisms
- Coordinate Rings
- Segre Embedding
- Veronese Embedding
---

# Morphisms of varieties

A morphism of varieties is a continuous map pulling regular functions back to regular functions ([[D-VARMORPH]]); for affine varieties these are the maps of coordinate rings in the opposite direction ([[T-SK599]]).

## Morphisms of varieties

[[D-VARMORPH]]

The image of a morphism need be neither open nor closed, and the two pathologies are the subject of [[algebraic-geometry/varieties/affine-or-projective|affine or projective]] and of the scheme-theoretic treatment of images.

## Affine varieties are finitely generated domains

[[T-SK599]]

Over an algebraically closed field, $X\mapsto A(X)$ is an anti-equivalence between affine varieties over $k$ and finitely generated $k$-algebras that are domains, and the inverse sends $A$ to $\Spec A$ with its maximal spectrum.
Three consequences are used constantly: a morphism $X\to Y$ of affine varieties is the same as a $k$-algebra map $A(Y)\to A(X)$; a closed immersion is a surjection of coordinate rings; and a point of $X$ is a maximal ideal, so the fibre over a point is computed by tensoring with $k$.
The equivalence is not an equivalence with all finitely generated rings: a non-domain such as $k[x,y]/(xy)$ has no variety attached, and the two components it describes are recorded in the ideal rather than in a single irreducible space ([[FE-VARDISJUNION]]).

## Embeddings into projective space

[[PR-VA4S3]]

The Segre embedding turns a product of projective spaces into a projective variety, and it is the reason $\PP^m\times\PP^n$ is allowed at all: the product of two varieties is a variety, but the product of two projective ones need not come with an embedding, and the Segre map supplies one whose image is defined by the vanishing of the two-by-two minors of a matrix of coordinates.

[[FE-VARVERONESE]]

The Veronese is the standard example of a variety that is isomorphic to $\PP^n$ and embedded so that its homogeneous coordinate ring is not $k[x_0,\ldots,x_n]$: the embedding, not the variety, decides the ring, and what the ring retains is the Hilbert function ([[algebraic-geometry/varieties/projective-varieties|projective varieties]]).
Both constructions are written as maps given by sections of a line bundle, which is the general recipe: a base-point-free linear system on $X$ gives a morphism to projective space, and it is a closed immersion exactly when the linear system separates points and tangent vectors ([[T-DIVMAPPN]]).
