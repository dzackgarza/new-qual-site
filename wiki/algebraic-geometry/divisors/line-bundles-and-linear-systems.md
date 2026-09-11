---
title: Line Bundles and Linear Systems
order: 2
topics:
- Invertible Sheaves
- Linear Systems
- Base Locus
---

# Line Bundles and Linear Systems

A divisor is only useful once it has been turned into a sheaf, and the sheaf is only useful once its sections have been counted.
This page is the passage between the three languages an examiner moves through without warning: divisors, invertible sheaves, and maps to projective space.

[[D-DIVOD]]

[[PR-DIVLB]]

The dictionary to have memorised in both directions: a divisor gives a line bundle with a rational section, and a line bundle with a chosen nonzero section gives an effective divisor, its zero locus.
Linear equivalence on the divisor side is isomorphism on the sheaf side, because changing the section by a rational function changes the divisor by a principal one.

## From sections to a map

[[D-DIVLINSYS]]

[[T-DIVMAPPN]]

The whole construction is one idea: evaluate a basis of sections at a point and read the values as homogeneous coordinates.
Base points are where that fails to define anything, and the separation conditions are where it fails to be injective or immersive.

This is also where the questions become computational.
Asking whether $D$ embeds $X$ becomes asking for $h^0(\OO(D))$ and for how it drops when points are imposed, and on a curve those are Riemann--Roch calculations.
