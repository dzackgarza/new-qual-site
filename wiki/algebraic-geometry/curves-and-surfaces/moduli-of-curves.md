---
title: Moduli of curves
order: 6
topics:
- Moduli
- Automorphisms
- Curves
---

# Moduli of curves

Genus $0$ is one curve and genus $1$ is a line's worth of them.
From genus $2$ on, "classify the curves" stops being a list and becomes a question about a space, and the first thing to settle is what kind of space is being asked for.

[[D-CRVMOD]]

Coarse asks only that a family of curves produce a map; fine asks that a map *be* a family.
The gap between the two is entirely accounted for by automorphisms, and the twisted family is the example to be able to write down on demand.

Genus $1$ is the case where the space is small enough to see: on [[algebraic-geometry/curves-and-surfaces/elliptic-curves|Elliptic curves]] the $j$-invariant is the coordinate, $\AA^1$ is the coarse space, and the failure to be fine is already visible there.

## The dimension count

[[T-CRVMG]]

The answer is $3g-3$, and there are three ways to get at it: the deformation count $h^1(C, T_C) = h^0(\omega_C^{\otimes 2}) = 3g-3$, the hyperelliptic branch points in genus $2$, and the plane quartics in genus $3$.
An examiner asking for the dimension usually wants one of the last two run out loud, so keep straight which group divides in each: $\PGL_2$ on the branch points, $\PGL_3$ on the plane.

## Why automorphisms keep appearing

[[PR-CRVAUT]]

This is the card both halves of the page lean on.
Finiteness of $\Aut C$ is what makes the orbits in the quartic count $8$-dimensional, so the dimension comes out; nontriviality of $\Aut C$ on the hyperelliptic locus is what keeps any genus from having a fine moduli space.

## Smoothness and properness of the moduli stacks

[[T-MGSMOOTH]]
