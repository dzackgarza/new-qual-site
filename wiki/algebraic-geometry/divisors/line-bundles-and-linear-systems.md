---
title: Line Bundles and Linear Systems
order: 2
topics:
- Invertible Sheaves
- Linear Systems
- Base Locus
---

# Line Bundles and Linear Systems

Divisors, invertible sheaves, and maps to projective space are three linked descriptions of the same linear-system data.

[[D-DIVOD]]

[[PR-DIVLB]]

The dictionary works in both directions: a divisor gives a line bundle with a rational section, and a line bundle with a chosen nonzero section gives an effective divisor, its zero locus.
Linear equivalence on the divisor side is isomorphism on the sheaf side, because changing the section by a rational function changes the divisor by a principal one.

## From sections to a map

[[D-DIVLINSYS]]

[[T-DIVMAPPN]]

The whole construction is one idea: evaluate a basis of sections at a point and read the values as homogeneous coordinates.
Base points are where that fails to define anything, and the separation conditions are where it fails to be injective or immersive.

The construction is computational: whether $D$ embeds $X$ depends on $h^0(\OO(D))$ and on how it drops when points are imposed, and on a curve those are Riemann--Roch calculations.
