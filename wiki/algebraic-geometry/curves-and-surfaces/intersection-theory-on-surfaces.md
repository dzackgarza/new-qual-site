---
title: Intersection theory on surfaces
order: 8
topics:
- Intersection Theory
- Adjunction
- Hodge Index Theorem
---

# Intersection theory on surfaces

On a curve, a divisor has a degree and that number answers most questions.
On a surface the corresponding invariant is a bilinear form, and every question about genus, ampleness or positivity becomes an intersection number.

[[D-SRFINT]]

Self-intersection is the part that has no curve analogue, because a curve inside a surface cannot be moved off itself.
The number is the degree of the normal bundle, and it is allowed to be negative — which is exactly what happens on an exceptional curve.

[[T-SRFADJ]]

Adjunction is the formula the surfaces material is built on, since it converts genus into intersection.
Running it on $\PP^2$ with $K = -3H$ gives the degree-genus formula $g = \tfrac{1}{2}(d-1)(d-2)$, and running it on $\PP^1 \times \PP^1$ with $K = (-2,-2)$ gives $g = (a-1)(b-1)$.
Being able to produce either in one line is the point.

[[T-SRFRR]]

The surface version of Riemann--Roch is rarely used to compute $\chi$.
It is used to force a section: bound $h^2$ by Serre duality, and a divisor with $D^2$ large enough must move.

## The shape of the Néron--Severi lattice

[[D-SRFNS]]

Intersection numbers cannot distinguish divisors in $\Pic^0$, so the pairing really lives on $\NS(X)$, where it is a nondegenerate form on a finitely generated group.

[[T-SRFHODGE]]

One positive direction and the rest negative: the ample cone gives the plus sign, and its orthogonal complement is negative definite.
That signature is what makes $\NS(X)$ a hyperbolic lattice and what supplies the reverse Cauchy--Schwarz inequality $(D\cdot E)^2 \geq D^2 E^2$.

[[T-SRFNAKAI]]

Ampleness on a surface is purely numerical, so it depends only on the class in $\NS(X)$, and both conditions are needed — $\pi^*H$ on a blowup has positive square but meets the exceptional curve in zero.
