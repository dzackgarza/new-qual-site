---
title: The fan dictionary
order: 1
topics:
- Toric Varieties
- Fans
- Orbits
---

# The fan dictionary

[[D-Q7Q2N]]

## The convex geometry underneath

[[PR-FULSEP]]

[[PR-FULFACET]]

[[PR-FULFACEDUAL]]

A polyhedral cone $\sigma$ is both finitely generated and an intersection of finitely many closed half-spaces, $\sigma^{\vee\vee}=\sigma$, and $\tau\mapsto\sigma^\vee\cap\tau^\perp$ is an inclusion-reversing bijection from the faces of $\sigma$ to the faces of $\sigma^\vee$.
The orbit-cone correspondence uses this bijection.

## How the affine charts glue

[[PR-FULLOC]]

[[PR-O8V3I]]

[[PR-D2F15]]

## Orbit closures are toric too

[[D-FULSTAR]]

The closure of the orbit $O(\tau)$ is the toric variety of the star fan $\Star(\tau)$ in $N/\operatorname{span}(\tau\cap N)$.
In particular each boundary divisor $D_\rho=X_{\Star(\rho)}$ is a toric variety of dimension $\dim X_\Sigma-1$, which permits induction on dimension.

## Standard examples from fans

| Geometric feature | Fan that supplies it |
| --- | --- |
| a normal variety that is not smooth | cone on $(0,1)$, $(d,-1)$ for $d \geq 2$ |
| a Weil divisor that is not Cartier | the same, $d = 2$: the quadric cone $V(xy - z^2)$ |
| a class group with torsion | the same: $\Cl = \ZZ/d$ |
| a resolution, explicitly | subdivide by inserting the missing lattice rays |
| a proper variety that is not projective | a complete fan that admits no strictly convex support function |

The first four entries are computations on a two-dimensional fan.
Every complete toric surface is projective, so the last entry needs a fan of dimension at least $3$.
