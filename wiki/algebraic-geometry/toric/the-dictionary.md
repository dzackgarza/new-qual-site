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

A cone may be presented by generators or by inequalities, and either presentation recovers the other through duality, which reverses the face poset ([[PR-FULSEP]], [[PR-FULFACET]], [[PR-FULFACEDUAL]]).
The dual-cone computation uses separation and facet descriptions, while the orbit-cone correspondence uses the order-reversing correspondence of faces ([[PR-O8V3I]]).

## How the affine charts glue

[[PR-FULLOC]]

[[PR-O8V3I]]

[[PR-D2F15]]

## Orbit closures are toric too

[[D-FULSTAR]]

The closure of the orbit $O(\tau)$ is the toric variety of the star fan $\Star(\tau)$ in $N/\operatorname{span}(\tau\cap N)$ ([[D-FULSTAR]]).
In particular each boundary divisor $D_\rho=X_{\Star(\rho)}$ is a toric variety of dimension $\dim X_\Sigma-1$, which permits induction on dimension ([[D-FULSTAR]]).

## Standard examples from fans

| Geometric feature | Fan that supplies it |
| --- | --- |
| a normal variety that is not smooth | cone on $(0,1)$, $(d,-1)$ for $d \geq 2$ ([[FE-TORCD]]) |
| a Weil divisor that is not Cartier | the same, $d = 2$: the quadric cone $V(xy - z^2)$ ([[FE-TORCD]]) |
| a class group with torsion | the same: $\Cl = \ZZ/d$ ([[FE-TORCD]]) |
| a resolution, explicitly | subdivide by inserting the missing lattice rays ([[PR-D2F15]]) |
| a proper variety that is not projective | a complete fan that admits no strictly convex support function ([[PR-FULCRIT]]) |

The first four entries are computations on a two-dimensional fan ([[FE-TORCD]], [[PR-D2F15]]).
Every smooth complete surface is projective, so a smooth proper toric variety that is not projective has dimension at least three ([[D-VARCOMP]]); the last row is the fan criterion for projectivity ([[PR-FULCRIT]]).
