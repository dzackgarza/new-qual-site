---
title: Toric surfaces and toric morphisms
order: 4
topics:
- Toric Varieties
- Surfaces
- Morphisms
---

# Toric surfaces and toric morphisms

[[PR-TORMOR]]

![The fan of $\PP^2$ with each cone labelled by $\lim_{t \to 0} \lambda^u(t)$](/assets/algebraic-geometry/toric/one-parameter-subgroup-limits-in-fan-of-p2.png)

For $u\in N$, $\lim_{t\to0}\lambda^u(t)$ exists in $X_\Sigma$ exactly when $u$ lies in a cone of $\Sigma$; testing properness on these limits gives the criterion that $X_\Sigma$ is complete exactly when $\abs\Sigma=N_\RR$.

## The classification

[[T-TORSURF]]

[[FE-TORHIRZ]]

[[FE-FULHIRZBUN]]

$\FF_0 = \PP^1 \times \PP^1$ is the quadric surface, $\FF_1 = \Bl_p \PP^2$, and every smooth complete toric surface with at least five rays is obtained from $\PP^2$ or some $\FF_a$ by inserting rays.

[[PR-FULKSQ]]

## Blowups

[[FE-TORBLOW]]

![A fan for $\PP^2$ under two blowups and a contraction, with the self-intersection numbers of the boundary divisors](/assets/algebraic-geometry/toric/fan-blowups-contractions-self-intersections.png)

Inserting a ray between two adjacent rays raises $\rank\Pic$ by one, raises $\chi$ by one, creates a $-1$-curve, and drops the self-intersection of each neighbour by one.
Contracting reverses all four.

## Beyond surfaces

[[FE-TORWPS]]

The fan of a weighted projective space is simplicial, so it is $\QQ$-factorial, with $\Pic$ of finite index in $\Cl$; $\PP(1,1,2)$ is singular, being the projective cone over a conic.
The three-dimensional cone on $(1,0,0)$, $(0,1,0)$, $(1,0,1)$, $(0,1,1)$ is not simplicial, and its affine toric variety is $V(xy-zw)$, the cone over the quadric surface.
Subdividing the cone along either diagonal of the square gives the two small resolutions of $V(xy-zw)$, each with exceptional locus a $\PP^1$.

## Cohomology of smooth toric varieties

[[T-TORCOHOM]]
