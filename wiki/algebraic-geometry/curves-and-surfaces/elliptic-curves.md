---
title: Elliptic curves
order: 4
topics:
- Elliptic Curves
- j-Invariant
- Group Schemes
---

# Elliptic curves

For an elliptic curve $(E,p_0)$ over an algebraically closed field, $p\mapsto\OO_E(p-p_0)$ is a bijection $E\to\Pic^0(E)$.

[[PR-CRVGRP]]

The group law on $E$ is the group structure of $\Pic^0(E)$ transported along this bijection, which Riemann--Roch supplies.
On the plane cubic model given by $\abs{3p_0}$, $p+q+r=0$ exactly when $p+q+r\sim3p_0$, that is, when $p,q,r$ are the intersection of $E$ with a line; this is the chord-and-tangent construction.

Addition and inversion are morphisms, so $E$ is a group scheme.
For $n\neq0$, $[n]$ is a nonconstant morphism of smooth projective curves, hence finite, of degree $n^2$.

## Classification

[[T-CRVJINV]]

In the proof, $\abs{2p_0}$ gives a degree-two map $E\to\PP^1$, Riemann--Hurwitz gives four branch points, a Möbius transformation moves them to $0,1,\lambda,\infty$, and $j$ is the rational function of $\lambda$ invariant under the $S_3$-action permuting $\{0,1,\lambda\}$.

$\AA^1$ is a coarse moduli space: its $k$-points are the isomorphism classes of elliptic curves.
It is not a fine moduli space.
For $\operatorname{char}k\neq2$, the family $ty^2=x^3-x$ over $\Spec k[t,t^{-1}]$ has every geometric fibre isomorphic to $y^2=x^3-x$, but it is not isomorphic to the constant family, since the isomorphism $y\mapsto\sqrt t\,y$ is defined only after adjoining $\sqrt t$.
The automorphism $-1$ of every elliptic curve permits this twist.

The automorphism counts $2$, $4$, and $6$ apply away from characteristics $2$ and $3$.
In characteristic $3$ the conditions $j = 0$ and $j = 1728$ describe one curve, whose automorphism group is noncommutative of order $12$; in characteristic $2$ the same curve has noncommutative automorphism group of order $24$.

Over $\CC$, elliptic curves are also classified by lattices up to homothety: [[algebraic-geometry/curves-and-surfaces/elliptic-curves-over-c|elliptic curves over $\CC$]].

## Characteristic $p$

[[D-CRVHASSE]]

The group scheme $E[p]$ always has order $p^2$, while its geometric points number $p$ in the ordinary case and $1$ in the supersingular case.

[[T-CRVHASSE]]

The coefficient criterion comes from the ideal sequence of a plane cubic: $H^1(\OO_E)\cong H^2(\PP^2,\OO(-3))$ is the line spanned by the Čech class $\tfrac{1}{xyz}$, and Frobenius sends it to $f^{p-1}/(xyz)^p$, whose image in that line is the coefficient of $(xyz)^{p-1}$ in $f^{p-1}$ times $\tfrac1{xyz}$.
For the Legendre family this coefficient is, up to a nonzero constant, the Hasse polynomial $h_p(\lambda)$.

[[FE-CRVSSPRIMES]]

For a curve over $\QQ$ with complex multiplication by an order in $K$, a prime of good reduction is supersingular exactly when it does not split in $K$ (Deuring), a set of density $\tfrac{1}{2}$.
Without complex multiplication the supersingular primes have density $0$ and are infinite in number (Elkies).
For $y^2=x^3-x$, with complex multiplication by $\ZZ[i]$, the supersingular primes are the $p\equiv3\bmod4$, the odd primes inert in $\ZZ[i]$.

## Rational points

[[T-CRVMORDELL]]

$E(k_0)$ is a subgroup of $E(k)$ because $p_0\in E(k_0)$ and the chord-and-tangent construction has coefficients in $k_0$.
Finite generation of $E(\QQ)$ follows from weak Mordell--Weil, the finiteness of $E(\QQ)/2E(\QQ)$, together with a height argument.
By Mazur's theorem $E(\QQ)_{\mathrm{tors}}$ is one of fifteen groups; no general algorithm for computing the rank $r$ is known.

## Families of elliptic curves

[[D-ELLSCH]]

## Twists

[[D-VARTWIST]]
