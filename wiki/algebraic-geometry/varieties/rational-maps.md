---
title: Rational maps
order: 10
topics:
- Rational Maps
- Birational Geometry
- Function Field
---

# Rational maps

A rational map is a morphism that is allowed to be undefined on a closed subset, and on an irreducible variety the loss is smaller than it looks: the map is determined by its values on any nonempty open set, so a rational map is a rule given by rational functions.
That makes the function field the main invariant of a variety — two varieties are birational exactly when their function fields agree — and the rest of the chapter is the study of what a birational class contains and which quantities are constant on it.

## Rational and dominant maps

[[D-VARREG]]

A rational map need not be definable at every point: on $\PP^2$ the rule $\thevector{x:y:z}\mapsto\thevector{x:y}$ is undefined exactly at $\thevector{0:0:1}$, and it is a morphism on the complement.
The indeterminacy locus is small in a precise sense: a rational map from a normal variety to a projective variety fails to be defined only in codimension at least two, which is why a rational map from a curve of dimension one to a projective variety is always a morphism ([[T-CRVMINMOD]]).
A rational map is dominant when its image is dense, and dominance is the condition under which it pulls functions back: a dominant map $X\dashrightarrow Y$ induces an injection $k(Y)\hookrightarrow k(X)$.

## Rational maps to projective space

For an irreducible variety $X$ with function field $k(X)$, a dominant rational map $X\dashrightarrow\PP^n$ is the same thing as an $(n+1)$-tuple $(f_0:\cdots:f_n)$ of rational functions not all zero, modulo multiplication by a single element of $k(X)^\times$.
The tuple may be chosen with no common factor, since it is taken modulo $k(X)^\times$, and then the indeterminacy locus is the common zero locus of $f_0,\ldots,f_n$ inside the largest open set on which all of them are regular functions.
So a rational map to projective space is a linear system on $X$ with no requirement that it be base-point-free, and the morphisms correspond exactly to the base-point-free ones ([[algebraic-geometry/divisors/line-bundles-and-linear-systems|line bundles and linear systems]]).

## Birational equivalence

Two varieties are \dfn{birational} when there are dominant rational maps between them that are inverse after restriction to open sets, and this is the same as an isomorphism $k(X)\cong k(Y)$ of fields over $k$.
Hence the birational classes of varieties over $k$ correspond to the finitely generated field extensions of $k$ of finite transcendence degree, and a variety is called a model of its function field: the geometric object chosen to represent the field.
The correspondence is not an equivalence of categories — a birational map is only a morphism on an open set — but it is exact enough that a question invariant under birational equivalence can be asked of the field alone.

## Models of one function field

[[T-CRVMINMOD]]

In dimension one the model is unique: each function field of transcendence degree one has exactly one smooth projective curve, its closed points are the discrete valuation rings of the field containing $k$, and birational maps between smooth projective curves are isomorphisms.
From dimension two onwards this fails, and how it fails is the subject of the minimal model programme: blowing up a point of a smooth projective surface produces another smooth projective surface, birational and not isomorphic, so a birational class has many smooth projective members ([[algebraic-geometry/varieties/blowups|blowups]]).
What survives is the function field, together with the invariants extracted from it.

## Birational invariants

[[T-BIRINV]]

The plurigenera $\dim H^0(X,\omega_X^{\tensor m})$ and the irregularity $h^1(X,\OO_X)$ are birational invariants, which is why they can be read off a resolution or a smooth model rather than only off the variety in front of us.
The general mechanism is that a birational map is an isomorphism in codimension one, so a differential form defined off a closed subset extends across it.
The canonical class is instead controlled by the map's own discrepancy: a birational morphism changes $K$ only along its exceptional locus, and the maps that change it by nothing are the crepant ones ([[D-VARCREPANT]]).
So a computation on a convenient model answers the question for the whole birational class, which is how the classification of surfaces is organised ([[algebraic-geometry/curves-and-surfaces/blowups-and-the-classification-of-surfaces|blowups and the classification of surfaces]]).

## Factorising a birational map

[[T-SRFZMT]]

Zariski's main theorem makes birational projective morphisms to a normal target rigid: they have connected fibres, and one that is quasi-finite is an isomorphism.
The reason a blowup is not an isomorphism is exactly the positive-dimensional fibre it creates, and the reason a birational map between surfaces factors into blowups and contractions is the loop that statement closes.
A subfield question of the same shape is Lüroth's theorem: a finitely generated subfield of $k(t)$ of transcendence degree one is of the form $k(u)$, so every curve dominated by $\PP^1$ is rational ([[T-IV2LUROTH]]).
