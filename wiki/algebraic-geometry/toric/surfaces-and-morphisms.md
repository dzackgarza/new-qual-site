---
title: Toric surfaces and toric morphisms
order: 4
topics:
- Toric Varieties
- Surfaces
- Morphisms
---

# Toric surfaces and toric morphisms

Dimension two is where the dictionary is completely explicit: a smooth complete toric surface is a cyclically ordered list of lattice vectors, and every intersection number is one subtraction.

[[PR-TORMOR]]

![The fan of $\PP^2$ with each cone labelled by $\lim_{t \to 0} \lambda^u(t)$](/assets/algebraic-geometry/toric/one-parameter-subgroup-limits-in-fan-of-p2.png)

The completeness criterion is the cleanest illustration of what the fan is for.
Properness is a limit condition, one-parameter subgroups are lattice points, and "the limit exists" becomes "the point lies in a cone".

## The classification

[[T-TORSURF]]

[[FE-TORHIRZ]]

The three families are not independent.
$\FF_0 = \PP^1 \times \PP^1$ is the quadric surface, $\FF_1 = \Bl_1 \PP^2$, and every surface with five or more rays is obtained from one of these by inserting rays.

[[PR-FULKSQ]]

## Blowups

[[FE-TORBLOW]]

![A fan for $\PP^2$ under two blowups and a contraction, with the self-intersection numbers of the boundary divisors](/assets/algebraic-geometry/toric/fan-blowups-contractions-self-intersections.png)

Inserting a ray between two adjacent rays raises $\rank\Pic$ by one, raises $\chi$ by one, creates a $-1$-curve, and drops the self-intersection of each neighbour by one.
Contracting reverses all four.
An examiner asking for a surface with prescribed intersection numbers is asking for a sequence of insertions.

## Beyond surfaces

[[FE-TORWPS]]

Weighted projective space is the standard first example of a variety that is simplicial but not smooth, so it is $\QQ$-factorial with $\Pic$ of finite index in $\Cl$.
In three dimensions the same construction gives $V(xy - zw)$, the cone over the quadric surface, from the four rays $(1,0,0), (0,1,0), (1,0,1), (0,1,1)$ — a cone that is not simplicial, and the standard example of a singularity with two small resolutions and no preferred one.
