---
title: The fan dictionary
order: 1
topics:
- Toric Varieties
- Fans
- Orbits
---

# The fan dictionary

Toric geometry converts many geometric questions into finite computations with cones, fans, and lattice points.

[[D-Q7Q2N]]

## The convex geometry underneath

The dual cone is central to the construction; the following three facts control how generator and inequality descriptions pass between a cone and its dual.

[[PR-FULSEP]]

[[PR-FULFACET]]

[[PR-FULFACEDUAL]]

Together these say that a cone may be presented by generators or by inequalities, that either presentation recovers the other through duality, and that duality reverses the face poset.
The dual-cone computation uses separation and facet descriptions, while the orbit-cone correspondence uses the order-reversing correspondence of faces.

## How the affine charts glue

[[PR-FULLOC]]

[[PR-O8V3I]]

[[PR-D2F15]]

## Orbit closures are toric too

[[D-FULSTAR]]

The orbit-cone correspondence lists the orbits; the star fan identifies each closure as a toric variety in its own right.
That is what makes induction on dimension available: a statement about $X_\Sigma$ can be tested on the boundary divisors $D_\rho = X_{\Star(\rho)}$, which are toric varieties one dimension down.

## Standard examples from fans

| Geometric feature | Fan that supplies it |
| --- | --- |
| a normal variety that is not smooth | cone on $(0,1)$, $(d,-1)$ for $d \geq 2$ |
| a Weil divisor that is not Cartier | the same, $d = 2$: the quadric cone $V(xy - z^2)$ |
| a class group with torsion | the same: $\Cl = \ZZ/d$ |
| a resolution, explicitly | subdivide by inserting the missing lattice rays |
| a proper variety that is not projective | a complete fan that admits no strictly convex support function |

Each entry is checked by a computation on a two-dimensional fan.

The dictionary applies only to toric varieties; a statement about general varieties requires an argument beyond the fan combinatorics.
