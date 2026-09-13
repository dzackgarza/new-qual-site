---
title: Polytopes and divisors
order: 3
topics:
- Toric Varieties
- Polytopes
- Divisors
---

# Polytopes and divisors

The fan controls the variety; the polytope controls a divisor on it.
Passing between the two is the second half of the dictionary, and it converts every question about linear systems into a question about counting lattice points.

[[D-TORPOLY]]

[[D-TORMOMENT]]

[[D-FULSIMPLE]]

## Divisors from the rays

[[T-TORDIV]]

![The two compatible exact sequences computing $\Cl$ and $\Pic$ of a toric variety](/assets/algebraic-geometry/toric/divisor-class-picard-exact-sequences.png)

The two sequences sit one above the other, and the whole difference between $\Pic$ and $\Cl$ is the difference between $\CDiv_T$ and $\Div_T$ — that is, between the divisors with a global Cartier datum and all of them.
On a smooth fan the two agree.
On a simplicial fan they agree up to finite index.
Beyond that, the cone over the rational normal curve shows how badly they can differ.

## The polytope of a divisor

[[D-TORQD]]

![The anticanonical polytope of $\PP^2$ and its polar dual, lattice points marked](/assets/algebraic-geometry/toric/anticanonical-polytope-and-dual-for-p2.png)

[[FE-TORP2]]

## Positivity

[[PR-TORPOS]]

A useful order of operations when asked whether a divisor is ample.
Write $D = \sum a_\rho D_\rho$, compute $P_D$ from the inequalities $\inp{m}{u_\rho} \geq -a_\rho$, and check whether its vertices are in bijection with the maximal cones.
If they are, $D$ is ample and $h^0$ is the number of lattice points in $P_D$; if two maximal cones share a vertex, the support function failed to crease and $D$ is at best base point free.

[[D-FULNORMPOLY]]

[[FE-FULAVA]]

Very ampleness is the one clause on that list that is not visible on the fan alone, and the example shows what it costs to ignore it: a strictly convex support function, an ample divisor, and a map that is two-to-one instead of an embedding.

## Fano and Calabi-Yau

[[D-TORREFL]]

![The five reflexive polygons of the toric del Pezzo surfaces](/assets/algebraic-geometry/toric/reflexive-polygons-of-toric-del-pezzo-surfaces.png)

Reflexivity is also where toric geometry meets mirror symmetry: a reflexive polytope $P$ gives a Calabi-Yau anticanonical hypersurface in $X_P$, and $P^\circ$ gives its mirror.
That is beyond what a qualifying exam will ask, but it explains why the $16$ reflexive polygons and the $4319$ reflexive polytopes in dimension three are tabulated at all.
