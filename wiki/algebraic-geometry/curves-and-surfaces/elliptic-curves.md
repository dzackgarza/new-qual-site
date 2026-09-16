---
title: Elliptic curves
order: 4
topics:
- Elliptic Curves
- j-Invariant
- Group Schemes
---

# Elliptic curves

Genus $1$ is the only genus where the classification is finished, and the reason is that the curve is its own Jacobian.

[[PR-CRVGRP]]

The group law is not extra structure laid on top of the curve.
It is linear equivalence, transported along a Riemann--Roch bijection, and the chord-and-tangent construction is that equivalence written in the coordinates of the plane cubic model.

Asked whether an elliptic curve is a group scheme, the answer is yes and the proof is that addition and inversion are morphisms, which is what makes $[n]$ a finite morphism with computable kernel.

## Classification

[[T-CRVJINV]]

The construction chains together the tools from the rest of the chapter: $\abs{2p_0}$ gives the degree-two map, Riemann--Hurwitz counts four branch points, a Möbius transformation normalizes three of them, and $j$ is the symmetric function killing the residual $S_3$-ambiguity.

The word *coarse* carries weight.
Points of $\AA^1$ are isomorphism classes, but there are nontrivial families with all fibres isomorphic, so no fine moduli space exists — the automorphisms $\pm 1$ present on every elliptic curve are what obstruct it.

The automorphism count is the follow-up, and the trap is stopping at $2$, $4$, $6$.
Those are the counts away from characteristics $2$ and $3$.
In characteristic $3$ the conditions $j = 0$ and $j = 1728$ describe one curve, which has $12$ automorphisms; in characteristic $2$ the same curve has $24$, and in both cases the group is noncommutative rather than cyclic.

Over $\CC$ the same classification is available a second time, through lattices and elliptic functions; that half is [[algebraic-geometry/curves-and-surfaces/elliptic-curves-over-c|its own page]].

## Characteristic $p$

[[D-CRVHASSE]]

The invariant is the vanishing of a single scalar, and it is exactly what decides which of the two possible $p$-torsion group schemes $E[p]$ is.
Answering "how many $p$-torsion points" with $p^2$ is the error the question is built around: the scheme always has order $p^2$, but an ordinary curve has $p$ points and a supersingular one has none.

[[T-CRVHASSE]]

The criterion is a monomial computation and can be reconstructed from the ideal sequence of a plane cubic: $H^1(\OO_E) \cong H^2(\PP^2, \OO(-3))$, a line spanned by $\tfrac{1}{xyz}$, and Frobenius multiplies by $f^{p-1}$.
For the Legendre family this becomes the Hasse polynomial, which is what one actually evaluates.

[[FE-CRVSSPRIMES]]

Fixing the curve and varying $p$ is the question that ties this chapter to the previous one.
With complex multiplication the answer is a congruence and the density is $\tfrac{1}{2}$; without it the supersingular primes are sparse.
For $y^2 = x^3 - x$ the computation is short enough to do on the board, and it lands on $p \equiv 3 \bmod 4$, which is exactly the condition that $p$ stays prime in $\ZZ[i]$.

## Rational points

[[T-CRVMORDELL]]

The subgroup claim is the part that needs the base point to be rational; finite generation is the part with content, and it is a descent plus a height.
Torsion is classified and the rank is not, which is where to stop.

## Families of elliptic curves

[[D-ELLSCH]]
