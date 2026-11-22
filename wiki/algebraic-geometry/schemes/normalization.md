---
title: Normal schemes and normalization
order: 8
topics:
- Normalization
- Normal Schemes
- Integral Extensions
---

# Normal schemes and normalization

Normality is the weakest of the smoothness conditions, and it is the one that survives the operations of the chapter: it is local, it is checked on local rings, and every integral scheme has a best normal scheme mapping to it.
The construction of that best scheme is the normalization; on a curve it is the map that removes the singularities, and a smooth projective curve is its own normalization ([[T-CRVMINMOD]]).

## Normality

[[D-QJ5M9]]

A regular local ring is normal and the converse fails from dimension two onwards, so normality is a genuinely weaker condition than smoothness: the cone over a smooth conic is normal and singular at its vertex.
The criterion that makes it usable is local on the scheme and local in codimension: a noetherian scheme is normal exactly when it is regular in codimension one and satisfies the depth condition $S_2$ [@Har77, Theorem II.8.22A], so a normal variety can be singular only along a closed subset of codimension at least two, and a normal curve is a nonsingular curve.
In dimension one that collapse is total: a noetherian local domain of dimension one is normal exactly when it is a discrete valuation ring, so normality and regularity are the same condition on a curve.

## Integral extensions

[[D-DEFINTEG]]

The integral closure of $A$ in its fraction field is the largest integral extension inside that field, and it is a finite $A$-algebra when $A$ is a finitely generated algebra over a field [@Har77, Theorem I.3.9A] ([[D-DEFINTEG]]).
That finiteness is what makes the geometric statement useful: for an integral extension $B\subseteq A$, lying over and going up hold, so $\Spec A\to\Spec B$ is surjective and closed with zero-dimensional fibres [@AM18, Theorems 5.10 and 5.11].

## Integrally closed domains

[[D-DEFINTCL]]

## Rational functions on a non-integral scheme

[[D-DEFTOTQ]]

Divisors were defined through rational functions, and a rational function is a section of the sheaf of total quotient rings rather than of a constant field as soon as the scheme is not integral.
That sheaf is also what the normalization is glued from: the integral closure of an affine ring inside its fraction field is intrinsic, so the affine normalizations patch over an affine cover, and the morphism they produce is independent of the cover.

## Normalization

[[D-SCHNORM]]

## Normalization of curves

On a curve nothing is lost, because normal and regular agree there: the normalization of an integral curve is its nonsingular model, and for a projective curve it is the unique smooth projective curve with the same function field ([[T-CRVMINMOD]]).
That uniqueness makes the function field a complete invariant of a smooth projective curve ([[T-CRVMINMOD]]).
The failure of the singular curve to be normal is also visible in its Picard group: comparison with the normalization computes $\Pic$ of a nodal and of a cuspidal cubic ([[FE-ADOKK]]), and the quotient is the local unit group at the singular point.

A different face of the same condition appears in toric geometry, where the semigroup of a cone is saturated exactly when the affine toric variety is normal, so the normalization of an affine toric variety is the toric variety of the saturation ([[D-FULSAT]]).
