---
title: Polytopes and divisors
order: 3
topics:
- Toric Varieties
- Polytopes
- Divisors
---

# Polytopes and divisors

A torus-invariant divisor $D=\sum_\rho a_\rho D_\rho$ on $X_\Sigma$ has polytope $P_D=\{m\in M_\RR:\langle m,u_\rho\rangle\ge-a_\rho\text{ for every ray }\rho\}$, and the characters $\chi^m$ for $m\in P_D\cap M$ form a basis of $H^0(X_\Sigma,\OO(D))$.

[[D-TORPOLY]]

[[D-TORMOMENT]]

[[D-FULSIMPLE]]

## Divisors from the rays

[[T-TORDIV]]

![The two compatible exact sequences computing $\Cl$ and $\Pic$ of a toric variety](/assets/algebraic-geometry/toric/divisor-class-picard-exact-sequences.png)

In the two sequences, $\Pic$ and $\Cl$ are the quotients of $\CDiv_T$, the torus-invariant Cartier divisors, and of $\Div_T$, all torus-invariant Weil divisors, by the principal divisors $\operatorname{div}(\chi^m)$.
On a smooth fan $\Pic=\Cl$.
On a simplicial fan $\Pic$ has finite index in $\Cl$: the cone over the rational normal curve of degree $d$ has $\Cl\cong\ZZ/d$ and $\Pic=0$.
On a non-simplicial fan the index can be infinite: the cone over a square, whose toric variety is $V(xy-zw)\subset\AA^4$, has $\Cl\cong\ZZ$ and $\Pic=0$.

## The polytope of a divisor

[[D-TORQD]]

![The anticanonical polytope of $\PP^2$ and its polar dual, lattice points marked](/assets/algebraic-geometry/toric/anticanonical-polytope-and-dual-for-p2.png)

[[FE-TORP2]]

## Positivity

[[PR-TORPOS]]

For $D = \sum a_\rho D_\rho$ on a complete fan, compute $P_D$ from the inequalities $\inner{m}{u_\rho} \geq -a_\rho$ and compare its vertices with the maximal cones.
If the vertices of $P_D$ correspond bijectively to the maximal cones of $\Sigma$, then $D$ is ample, and $h^0(\OO(D))$ is the number of lattice points in $P_D$.
If two maximal cones give the same vertex, the support function is linear across the wall between them and $D$ is not ample; it is base point free when the support function is still convex.

[[D-FULNORMPOLY]]

[[FE-FULAVA]]

Very ampleness is not visible from the fan alone; the [[FE-FULAVA|example of an ample divisor that is not very ample]] gives a strictly convex support function and an ample divisor whose associated map is two-to-one rather than an embedding.

## Fano and Calabi-Yau

[[D-TORREFL]]

![The five reflexive polygons of the toric del Pezzo surfaces](/assets/algebraic-geometry/toric/reflexive-polygons-of-toric-del-pezzo-surfaces.png)

Reflexivity is also where toric geometry meets mirror symmetry: a reflexive polytope $P$ gives a Calabi-Yau anticanonical hypersurface in $X_P$, and $P^\circ$ gives its mirror.
This mirror construction motivates the classification and tabulation of the $16$ reflexive polygons and the $4319$ reflexive polytopes in dimension three.
