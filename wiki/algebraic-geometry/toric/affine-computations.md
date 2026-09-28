---
title: Affine toric computations
order: 2
topics:
- Toric Varieties
- Cones
- Class Groups
---

# Affine toric computations

Affine toric computations follow one procedure: dualise the cone, list the lattice points of the dual, and read the relations among them.

[[FE-TORDUAL]]

![A two-dimensional cone in $N$ with its dual cone shaded, ray generators marked](/assets/algebraic-geometry/toric/dual-cone-lattice-computation.png)

Two numerical consequences are immediate.
The number of generators of $S_\sigma$ is the embedding dimension, so a cone with four Hilbert basis elements gives a surface in $\AA^4$ and not in $\AA^3$.
The relations always assemble into the minors of a matrix, because a two-dimensional toric singularity is determinantal.

## When is the answer smooth

[[PR-TORSMAFF]]

[[PR-FULCOTAN]]

The two cards answer the same question from opposite ends.
One assumes a lattice basis and computes the variety; the other computes the tangent space first and shows a lattice basis was forced.
The cotangent-space computation explains the criterion because the embedding dimension at the fixed point can be counted from the picture.

The determinant of the ray generators decides everything in dimension two.
It is $1$ exactly when the cone is smooth, and in general it is the order of the local class group.

## The normality caveat, and how to repair it

[[D-FULSAT]]

A semigroup handed to you need not be the semigroup of a cone.
Saturation tests whether the semigroup already comes from the lattice points of its cone; passing to the saturation gives the normalization.

## The standard singular cone

[[FE-TORCD]]

![The quadric cone $V(y^2 - xz)$, the affine toric variety of the cone on $(0,1)$, $(2,-1)$](/assets/algebraic-geometry/toric/quadric-cone-surface-plot.png)

This single family supplies three standard examples: a normal variety that is not smooth, a Weil divisor that is not Cartier, and a class group with torsion.

[[FE-FULQUOT]]

The two presentations expose different invariants of the same variety.
The minors give the equations and the embedding; the quotient gives the singularity a name, its local class group, and the reason it is only an orbifold point.

## Resolving it

[[FE-TORMINRES]]

![The lattice points of the convex hull of $\sigma \intersect N$, marked as the rays of the minimal resolution](/assets/algebraic-geometry/toric/minimal-resolution-by-convex-hull-of-cone.png)

For toric surfaces, the minimal resolution is encoded by the convex hull of the lattice points in the cone.
