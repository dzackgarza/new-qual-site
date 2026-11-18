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

A morphism of varieties is a map that is regular, and the whole content of the affine theory is that such maps are the same thing as maps of coordinate rings in the opposite direction.
That contravariant equivalence is the reason a geometric question about affine varieties can be answered by a ring computation, and the reason the catalogue of constructions in this chapter is a catalogue of graded algebras.
Projective varieties are not affine, so their morphisms are the ones given by linear systems — and the Segre and Veronese embeddings are the two constructions that produce them from nothing.

## Morphisms of varieties

::: {.definition title="Morphism of varieties"}
Let $X$ and $Y$ be varieties over an algebraically closed field $k$.
A \dfn{morphism} $f\colon X\to Y$ is a continuous map together with a map of sheaves of $k$-algebras $f^\sharp\colon\OO_Y\to f_*\OO_X$ making $X$ and $Y$ locally ringed spaces over $k$.
A \dfn{regular map} from an open $U\subseteq X$ to $Y$ is a morphism $U\to Y$.
:::

Concretely, a morphism between quasi-projective varieties is given locally by polynomials, homogeneous of the same degree in the projective coordinates, with no common zero ([[D-VARREG]]).
Two morphisms $f,g\colon X\to Y$ that agree on a nonempty open subset of an irreducible variety agree everywhere: the set where they agree is closed when $Y$ is separated, and it contains a nonempty open subset of an irreducible space, hence is all of $X$.
The image of a morphism need be neither open nor closed, and the two pathologies are the subject of [[algebraic-geometry/varieties/affine-or-projective|affine or projective]] and of the scheme-theoretic treatment of images.

## Affine varieties are finitely generated domains

[[T-SK599]]

Over an algebraically closed field, $X\mapsto A(X)$ is an anti-equivalence between affine varieties over $k$ and finitely generated $k$-algebras that are domains, and the inverse sends $A$ to $\Spec A$ with its maximal spectrum.
Three consequences are used constantly: a morphism $X\to Y$ of affine varieties is the same as a $k$-algebra map $A(Y)\to A(X)$; a closed immersion is a surjection of coordinate rings; and a point of $X$ is a maximal ideal, so the fibre over a point is computed by tensoring with $k$.
The equivalence is not an equivalence with all finitely generated rings: a non-domain such as $k[x,y]/(xy)$ has no variety attached, and the two components it describes are recorded in the ideal rather than in a single irreducible space ([[FE-VARDISJUNION]]).

## Embeddings into projective space

[[PR-VA4S3]]

The Segre embedding turns a product of projective spaces into a projective variety, and it is the reason $\PP^m\times\PP^n$ is allowed at all: the product of two varieties is a variety, but the product of two projective ones need not come with an embedding, and the Segre map supplies one whose image is defined by the vanishing of the two-by-two minors of a matrix of coordinates.

::: {.example title="The Veronese embedding"}
For $d\ge1$, the map
$$
v_d\colon\PP^n\longrightarrow\PP^N,\qquad
\thevector{x_0:\cdots:x_n}\longmapsto\thevector{x_0^d:x_0^{d-1}x_1:\cdots:x_n^d},
$$
with $N=\binom{n+d}{n}-1$, is a closed immersion, the \dfn{$d$-uple embedding}.
Its image is the set of points whose coordinate vector is the tuple of degree-$d$ monomials in some point, which is the vanishing locus of the quadratic relations among those monomials, and the coordinate ring of the image is the $d$-th Veronese subring $k[x_0,\ldots,x_n]^{(d)}$.
:::

The Veronese is the standard example of a variety that is isomorphic to $\PP^n$ and embedded so that its homogeneous coordinate ring is not $k[x_0,\ldots,x_n]$: the embedding, not the variety, decides the ring, and what the ring retains is the Hilbert function ([[algebraic-geometry/varieties/projective-varieties|projective varieties]]).
Both constructions are written as maps given by sections of a line bundle, which is the general recipe: a base-point-free linear system on $X$ gives a morphism to projective space, and it is a closed immersion exactly when the linear system separates points and tangent vectors ([[T-DIVMAPPN]]).
