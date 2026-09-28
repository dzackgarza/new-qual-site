---
title: Elliptic curves over $\CC$
order: 5
topics:
- Elliptic Curves
- Elliptic Functions
- Complex Multiplication
---

# Elliptic curves over $\CC$

Over $\CC$ the classification of genus $1$ is available twice, and the two answers are the same answer stated in two languages.
The algebraic route produces the Legendre model and $j$ as a rational function of $\lambda$.
The analytic route produces a lattice, and everything after that is a computation with series.

## The functions

[[D-CRVWEIER]]

Two facts drive the whole construction and both are consequences of compactness: residues of an elliptic function sum to zero on the torus, so nothing has a single simple pole, and a holomorphic elliptic function is constant.
The first says $\wp$ is the smallest thing that can exist; the second turns every identity into a cancellation of principal parts.

## From a lattice to a cubic

[[T-CRVUNIF]]

The map $z \mapsto (\wp(z), \wp'(z))$ lands in the cubic because of the differential equation, and is bijective by degree counting: $\wp$ has degree $2$ and is even, $\wp'$ is odd and breaks the tie.

Abel's theorem on the torus identifies the analytic and algebraic group laws, so the uniformization $\CC/\Lambda \to E$ is a group isomorphism rather than merely a bijection.
The torsion reading is immediate: $E[n] = \tfrac{1}{n}\Lambda/\Lambda \cong (\ZZ/n)^2$.

## The modular function

[[T-CRVMODJ]]

The normalisation must be fixed because conventions for $J$ and $j$ differ by the factor $1728$.
The invariance is a weight count --- $g_2^3$ and $\Delta$ both scale by $\alpha^{-12}$ --- and the restriction to $\SL_2(\ZZ)$ rather than $\GL_2(\ZZ)$ comes from the formula for $\Im\qty{\tfrac{a\tau+b}{c\tau+d}}$, which is the usual place to slip.

Uniqueness of a representative in the fundamental region upgrades invariance into a moduli statement, and the two points where the region folds onto itself are the two curves with extra automorphisms.

## Complex multiplication

[[T-CRVCM]]

The endomorphism ring is realized inside $\CC$ as the scalars preserving the lattice.
It is therefore either $\ZZ$ or an order in an imaginary quadratic field, and the order need not be maximal; $\tau=2i$ gives conductor $2$.

[[T-CRVCMCFT]]

Nine counts imaginary quadratic fields of class number one; thirteen counts imaginary quadratic *orders*, and endomorphism rings range over orders.
The four extra ones have discriminant $-12$, $-16$, $-27$, and $-28$.

A non-algebraic-integer $j$ cannot be the $j$-invariant of a CM elliptic curve.
