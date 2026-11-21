---
title: Elliptic curves over $\CC$
order: 8
topics:
- Elliptic Curves
- Lattices
- Complex Multiplication
---

# Elliptic curves over $\CC$

Over $\CC$ an elliptic curve is a complex torus: the quotient $\CC/\Lambda$ of the plane by a lattice $\Lambda=\ZZ\omega_1+\ZZ\omega_2$, and the analytic and algebraic descriptions agree.

## The functions

[[D-CRVWEIER]]

For a lattice $\Lambda\subseteq\CC$ the field of elliptic functions for $\Lambda$ is generated over $\CC$ by the Weierstrass function $\wp$ and its derivative $\wp'$ [@Har77, Theorem IV.4.12B].
The pair $(\wp,\wp')$ satisfies $\wp'^2=4\wp^3-g_2\wp-g_3$ with $g_2,g_3$ determined by $\Lambda$, so it defines a morphism $\CC/\Lambda\to\PP^2$ onto the plane cubic with that equation.

## From a lattice to a cubic

[[T-CRVUNIF]]

Two lattices give isomorphic elliptic curves exactly when one is a nonzero complex multiple of the other after a change of basis by $\GL_2(\ZZ)$, equivalently exactly when their values of the modular function $j$ agree [@Har77, Theorem IV.4.15B].
As an abstract group, an elliptic curve over $\CC$ is $\RR/\ZZ\times\RR/\ZZ$ [@Har77, Theorem IV.4.16].

## The modular function

[[T-CRVMODJ]]

## Complex multiplication

[[T-CRVCM]]

[[T-CRVCMCFT]]

An elliptic curve over $\CC$ has complex multiplication exactly when the corresponding $\tau$ lies in an imaginary quadratic field [@Har77, Theorem IV.4.19].
