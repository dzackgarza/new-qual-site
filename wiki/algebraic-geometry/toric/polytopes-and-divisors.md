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

For $D=\sum a_\rho D_\rho$ Cartier on a complete $X_\Sigma$, $P_D$ is cut out by the inequalities $\inner{m}{u_\rho}\geq-a_\rho$.
If the Cartier data $m_\sigma$ are distinct vertices of $P_D$, one for each maximal cone, then $D$ is ample; if every $m_\sigma$ lies in $P_D$ but two maximal cones have the same $m_\sigma$, then $D$ is base-point free and not ample.

[[D-FULNORMPOLY]]

[[FE-FULAVA]]

Very ampleness depends on the lattice points of $P_D$ as well as on $\Sigma$: for the lattice simplex $P$ with vertices $(0,0,0)$, $(0,1,1)$, $(1,0,1)$, $(1,1,0)$, the divisor $D_P$ is ample, and its four lattice points give a finite morphism $X_P\to\PP^3$ of degree $2$.

## Fano and Calabi-Yau

[[D-TORREFL]]

![The five reflexive polygons of the toric del Pezzo surfaces](/assets/algebraic-geometry/toric/reflexive-polygons-of-toric-del-pezzo-surfaces.png)

Reflexivity is also where toric geometry meets mirror symmetry: a reflexive polytope $P$ gives a Calabi-Yau anticanonical hypersurface in $X_P$, and $P^\circ$ gives its mirror.
There are $16$ reflexive polygons and $4319$ reflexive polytopes in dimension three, up to lattice isomorphism.
