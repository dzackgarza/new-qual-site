---
title: Affine toric computations
order: 2
topics:
- Toric Varieties
- Cones
- Class Groups
---

# Affine toric computations

Everything affine in this subject is one procedure: dualise the cone, list the lattice points of the dual, read the relations among them.
The procedure is short enough to do at a board, which is why an examiner asks for it.

[[FE-TORDUAL]]

![A two-dimensional cone in $N$ with its dual cone shaded, ray generators marked](/assets/algebraic-geometry/toric/dual-cone-lattice-computation.png)

Two things are worth saying about the answer before moving on.
The number of generators of $S_\sigma$ is the embedding dimension, so a cone with four Hilbert basis elements gives a surface in $\AA^4$ and not in $\AA^3$.
The relations always assemble into the minors of a matrix, because a two-dimensional toric singularity is determinantal.

## When is the answer smooth

[[PR-TORSMAFF]]

The determinant of the ray generators decides everything in dimension two.
It is $1$ exactly when the cone is smooth, and in general it is the order of the local class group, so it is the first number to compute about a cone and the last one that is needed.

## The standard singular cone

[[FE-TORCD]]

![The quadric cone $V(y^2 - xz)$, the affine toric variety of the cone on $(0,1)$, $(2,-1)$](/assets/algebraic-geometry/toric/quadric-cone-surface-plot.png)

This single family answers three separate questions on a syllabus — a normal variety that is not smooth, a Weil divisor that is not Cartier, a class group with torsion — and it answers them with a determinant.

## Resolving it

[[FE-TORMINRES]]

![The lattice points of the convex hull of $\sigma \intersect N$, marked as the rays of the minimal resolution](/assets/algebraic-geometry/toric/minimal-resolution-by-convex-hull-of-cone.png)

The contrast with the general theory is the point of the chapter.
Resolution of singularities is a theorem with a long proof; here it is the convex hull of the lattice points in a cone, computed by inspection.
