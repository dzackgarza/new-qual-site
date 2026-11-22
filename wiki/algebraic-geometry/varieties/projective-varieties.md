---
title: Projective varieties
order: 8
topics:
- Projective Varieties
- Homogeneous Ideals
- Nullstellensatz
---

# Projective varieties

Projective space is affine space with the points at infinity put back, and a projective variety is an irreducible closed subset of it ([[D-CP2MH]]); the algebra that describes one is the algebra of homogeneous forms, which is the coordinate ring of the affine cone over the variety [@Har77, Exercise I.2.10].

## Homogeneous ideals and the projective Nullstellensatz

[[D-CP2MH]]

A homogeneous ideal need not cut out anything: $V(J)$ is empty exactly when $\sqrt J$ contains the irrelevant ideal $S_+$, so $V(S_+)=\emptyset$ although $S_+$ is a proper radical ideal [@Har77, Exercise I.2.2], and the correspondence is between closed subsets and homogeneous radical ideals *other than* $S_+$ [@Har77, Exercise I.2.4].
The values of a form are not functions on $\PP^n$ — only its zero set is — so the ring of regular functions on projective space is the constants, and the homogeneous forms are sections of line bundles rather than functions ([[PR-EFW6B]]).

## The standard affine cover

[[D-VARQAP]]

Each chart $U_i=\theset{x_i\neq0}$ is an affine space, and a projective variety is covered by its intersections with them, each cut out by the dehomogenisations of the homogeneous ideal.
Everything local — smoothness, dimension, the local rings — is therefore affine-local and can be checked chart by chart.
The passage back is the projective closure, and a generating set no longer suffices: homogenising generators of $I(Z)$ can produce a strictly larger closed set, and one homogenises the whole ideal ([[D-VARQAP]]).

## The homogeneous coordinate ring

For a closed subset $X\subseteq\PP^n$ with homogeneous ideal $I(X)\subseteq S=k[x_0,\ldots,x_n]$, the homogeneous coordinate ring is $S(X)=S/I(X)$, graded by degree ([[D-L6ERW]]).

$S(X)$ is the coordinate ring of the affine cone $C(X)\subseteq\AA^{n+1}$ over $X$ [@Har77, Exercise I.2.10], and it is not an invariant of the variety: the same $\PP^1$ embedded by $\OO(1)$ has $S=k[x,y]$, and embedded by $\OO(2)$ has the Veronese subring $k[x^2,xy,y^2]$.
What is invariant is the Hilbert function of $S(X)$ in large degree, which is a polynomial — the Hilbert polynomial — whose degree and leading coefficient are the dimension and the degree of $X$ ([[D-L6ERW]]).
For a curve, the constant term of the Hilbert polynomial is $1-p_a$, so the arithmetic genus is read off the coordinate ring rather than off the variety.

## Embeddings: Segre and Veronese

[[PR-VA4S3]]

The product of projective spaces is projective through the Segre embedding, whose image is the closed subscheme cut out by the $2\times2$ minors ([[PR-VA4S3]]).
For $m=n=1$ the single minor is $z_{00}z_{11}-z_{01}z_{10}=0$, so the image of $\PP^1\times\PP^1$ is the smooth quadric surface in $\PP^3$, and the product of two projective varieties is projective because the Segre image of the product of their ambient spaces is projective and $\sigma(X\times_kY)$ is closed in it ([[PR-VA4S3]]).
The Veronese embedding $v_d\colon\PP^n\to\PP^N$, $N=\binom{n+d}{n}-1$, sends a point to the tuple of all degree-$d$ monomials in its coordinates; it is a closed immersion, and its image is the $d$-uple embedding whose coordinate ring is the $d$-th Veronese subring of $k[x_0,\ldots,x_n]$.
A projective variety is a closed subset of some $\PP^N$, and the choice of $N$ and of the embedding is exactly the choice of a very ample line bundle on it ([[T-DIVMAPPN]]).

## How projective varieties sit among the others

[[D-VARCOMP]]

Every projective variety is complete, and completeness is the property shared with proper schemes; the two are not the same, and a complete variety that admits no projective embedding exists ([[algebraic-geometry/varieties/affine-or-projective|affine or projective]]).
Over $\CC$ completeness is compactness; coherent cohomology on a projective variety is finite-dimensional ([[T-CARTSERRE]]), and intersection numbers are degrees of cycles ([[D-VARDEG]]).
