---
title: Rational maps
order: 10
topics:
- Rational Maps
- Birational Geometry
- Function Field
---

# Rational maps

[[D-VARBIRAT]]

Recall that a [[D-VARBIRAT|rational map]] is an equivalence class of morphisms on nonempty open subsets, so on an irreducible variety it is determined by its values on any nonempty open set.

## Rational maps and dominance

[[D-VARBIRAT]]

For the rule $\thevector{x:y:z}\mapsto\thevector{x:y}$ on $\PP^2$, the indeterminacy locus is the single point $\thevector{0:0:1}$.
The indeterminacy locus is small: a rational map from a normal variety to a projective variety is undefined only in codimension at least two [@Vak25, Exercise 15.3.B]: at a point of codimension one the local ring $\OO_{X,\eta}$ is a discrete valuation ring, so a tuple of rational functions can be cleared of denominators there. In particular a rational map from a nonsingular curve to a projective variety is a morphism ([[T-CRVMINMOD]]).
The [[D-VARBIRAT|dominant]] rational maps $X\dashrightarrow Y$ pull functions back along the inclusion $k(Y)\into k(X)$ of function fields.

## Rational maps to projective space

For an irreducible variety $X$ over $k$, a rational map $X\dashrightarrow\PP^n_k$ is the same thing as an $(n+1)$-tuple $(f_0:\cdots:f_n)$ of rational functions on $X$, not all zero, modulo multiplication by a single element of $k(X)^\times$: on a dense open $U$ on which the $f_i$ are regular and have no common zero they are global sections generating $\OO_U$, so they define a morphism $U\to\PP^n_k$ [@Har77, Theorem II.7.1], and two tuples define the same morphism on a dense open subset exactly when they differ by an element of $k(X)^\times$.
The tuple may be chosen with no common factor, and then the indeterminacy locus is the common zero locus of $f_0,\ldots,f_n$ in the largest open set on which all of them are regular.
A rational map to $\PP^n$ is a linear system on $X$ with no requirement that it be base-point-free, and the morphisms are the base-point-free linear systems ([[algebraic-geometry/divisors/line-bundles-and-linear-systems|line bundles and linear systems]]).

## Birational equivalence

Two varieties are birational when there is a birational map between them ([[D-VARBIRAT]]), and this is the same as an isomorphism $k(X)\cong k(Y)$ of fields over $k$ [@Har77, Corollary I.4.5].
So the birational classes of varieties over $k$ are the finitely generated field extensions of $k$ of finite transcendence degree, and a variety is a model of its function field.
Invariants of the field alone are therefore birational invariants, and a birational question may be asked of the field.

## Models of one function field

[[T-CRVMINMOD]]

In dimension one the model is unique: each function field of transcendence degree one has exactly one smooth projective curve, its closed points are the discrete valuation rings of the field containing $k$, and birational maps between smooth projective curves are isomorphisms ([[T-CRVMINMOD]]).
From dimension two onwards this fails: blowing up a point of a smooth projective surface produces another smooth projective surface that is birational and not isomorphic, so a birational class has many smooth projective members ([[algebraic-geometry/varieties/blowups|blowups]]).

## Birational invariants

[[T-BIRINV]]

The plurigenera $\dim H^0(X,\omega_X^{\tensor m})$ and the irregularity $h^1(X,\OO_X)$ are birational invariants, so they may be computed on any smooth projective model ([[T-BIRINV]]).
The indeterminacy locus of a birational map from a normal variety to a projective variety has codimension at least two, and a rational differential form on a nonsingular variety whose domain of definition misses a closed subset of codimension two extends across it: at a point of codimension at least two the local ring $\OO_{X,x}$ is an integrally closed noetherian domain, so a rational function regular at every height-one prime is regular there [@Har77, Proposition II.6.3A].
Across a divisor the extension can fail, and the failure is measured by the discrepancy: a birational morphism changes $K$ only along its exceptional locus, and the maps that change it by nothing are the crepant ones ([[D-VARCREPANT]]).

## Factorising a birational map

[[T-SRFZMT]]

Zariski's main theorem makes a birational projective morphism to a normal target rigid: it has connected fibres, and one that is quasi-finite is an isomorphism ([[T-SRFZMT]]).
A birational map between smooth projective surfaces factors into blowups and contractions ([[T-SRFZMT]]).
Lüroth's theorem is the same shape in dimension one: a finitely generated subfield of $k(t)$ of transcendence degree one is $k(u)$, so every curve dominated by $\PP^1$ is rational ([[T-IV2LUROTH]]).
