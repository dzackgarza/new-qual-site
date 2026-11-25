---
title: Toric del Pezzo surfaces
order: 8
topics:
- Toric Varieties
- Fano Varieties
- Polytopes
- Blowups
---

# Toric del Pezzo surfaces

Recall that a [[D-VARFANO|del Pezzo surface]] is a Fano variety of dimension two.
Among the sixteen reflexive polygons of the plane exactly five are smooth, and those five are the toric del Pezzo surfaces — the plane, the quadric surface, and the plane blown up at one, two, and three torus-fixed points.
The failure of a fourth blowup is a single intersection number.

## Reflexive polytopes

[[D-TORREFL]]

The class $-K$ is Cartier and ample exactly when $P_{-K}$ is a [[D-TORREFL|reflexive]] lattice polytope whose normal fan is $\Sigma$ ([[PR-FULCRIT]]).
In dimension two there are sixteen reflexive polygons up to equivalence, hence sixteen Gorenstein Fano toric surfaces; smoothness of the surface is smoothness of the polygon ([[D-TORREFL]]).

The five smooth ones are
$$
\PP^2,\qquad \PP^1\times\PP^1,\qquad \Bl_1\PP^2,\qquad \Bl_2\PP^2,\qquad \Bl_3\PP^2,
$$
and the last three are obtained from the first by blowing up torus-fixed points one at a time.
What makes the list short is the smoothness condition: a smooth reflexive polygon is rigid, being the triangle, the square, or one of the three polygons obtained from the triangle by cutting off vertices in the only way that keeps every new edge at distance one from the origin.

## The five surfaces as fans

[[FE-TORP2]]

[[FE-TORHIRZ]]

The plane is the fan with three rays $e_1,e_2,-e_1-e_2$; the quadric $\PP^1\times\PP^1$ is the fan with four rays $\pm e_1,\pm e_2$, which is the square's normal fan; and the three blowups are the fans with four, five and six rays obtained by star subdivisions, the first of which is the fan of $\FF_1$.
The invariant that counts this is the number of rays, through the self-intersection of the canonical class: for a smooth complete toric surface with $d$ rays, $K^2=12-d$ ([[PR-FULKSQ]]).
So the degrees of the five are $9, 8, 8, 7, 6$: the plane has $K^2=9$, and each blowup at a point lowers it by one.

## The blowup relations

[[FE-TORBLOW]]

Blowing up a torus-fixed point is a star subdivision of the fan at the corresponding maximal cone, so the blowup of a toric surface at a fixed point is again toric and its fan has one more ray.
Each of $\Bl_1\PP^2$, $\Bl_2\PP^2$, $\Bl_3\PP^2$ is a blowup of the previous one at a torus-fixed point, so their fans are the plane's fan subdivided once, twice and three times ([[FE-TORBLOW]]); the quadric surface is not a blowup of the plane and enters the list as the normal fan of the square.
The exceptional curves of these blowups are the divisors of the new rays, each with self-intersection $-1$, and contracting them returns the previous surface ([[PR-VAREM1]], [[T-SRFCAST]]).

[[D-VARFANO]]

## The criterion in fan terms

[[PR-FULCRIT]]

For a smooth complete toric surface, the Fano condition is exactly that the anticanonical polytope
$$
P_{-K}=\theset{m\in M_\RR \st \inner{m}{u_\rho}\ge-1 \text{ for every ray } \rho}
$$
is a reflexive lattice polytope whose normal fan is $\Sigma$, so the classification of toric del Pezzo surfaces is a classification of lattice polygons and nothing else.
Smoothness, completeness and projectivity are then conditions on the polygon, and each is decided by a determinant or a cone count ([[PR-FULCRIT]]).

## The obstruction to a fourth blowup

The obstruction to a fourth blowup is one number.
Blowing up a torus-fixed point of $\Bl_3\PP^2$ creates two $(-2)$-curves $C$, and adjunction gives $-K\cdot C=2+C^2=2-2=0$, so $-K$ is nef and big but not ample, and the surface is not del Pezzo [@Har77, Theorem V.1.10].
In the fan the fourth blowup adds a ray $\rho$ with $-K\cdot D_\rho=1$, so the inequality $\inner{m}{u_\rho}\ge-1$ cuts a genuine facet of $P_{-K}$; the two $(-2)$-curves are the divisors with $-K\cdot D=0$, and their inequalities are the redundant ones, so the normal fan of $P_{-K}$ is the coarsening of $\Sigma$ obtained by deleting their two rays, a proper coarsening, and $\Sigma$ is not the normal fan of a reflexive lattice polytope ([[PR-FULCRIT]]).

Among the ten deformation classes of del Pezzo surfaces — $\PP^1\times\PP^1$ and $\Bl_k\PP^2$ for $0\le k\le8$ — exactly these five carry a torus action, and the other five, $\Bl_k\PP^2$ for $4\le k\le8$, carry no torus action and are not toric ([[D-VARFANO]], [[D-TORREFL]]).
