---
title: Dimension
order: 7
topics:
- Dimension
- Krull Dimension
- Codimension
---

# Dimension

[[D-SCHDIM]]

Dimension depends only on the underlying topological space, so $\dim X=\dim X^\red$ for every scheme $X$ ([[D-SCHDIM]]).

## Krull dimension

[[D-5LJUX]]

For a finitely generated integral domain $B$ over a field $k$, $\krulldim B=\trdeg_k\Frac B$, and for $\mfp\in\Spec B$,
$$
\height\mfp+\krulldim(B/\mfp)=\krulldim B
$$
[@Har77, Theorem I.1.8A].

## Codimension one

[[PR-VARHT]]

In a unique factorization domain every height-one prime is principal, and a noetherian integral domain is a unique factorization domain exactly when every height-one prime is principal [@Har77, Proposition I.1.12A]; so on a locally factorial scheme every irreducible closed subset of codimension one is cut out by one equation.

## Dimension and cohomology

[[T-COHGROTH]]

The bound is attained: $H^n(\PP^n,\OO(-n-1))\neq0$ ([[T-IJW1K]]).

## Dimension in families

[[T-MORFIBDIM]]

For a morphism $f\colon X\to Y$ of finite type between schemes locally of finite type over a field, the local fibre dimension $x\mapsto\dim_x X_{f(x)}$ is upper semicontinuous on $X$, and $y\mapsto\dim X_y$ is upper semicontinuous on $Y$ when $f$ is proper [@Vak25, Theorem 12.4.3].
Properness is a hypothesis of the second statement: the open immersion $f\colon\AA^1_k\sm\theset{0}\into\AA^1_k$ has empty fibre over $0$ and a zero-dimensional fibre over every other point, so $\theset{y\in\AA^1_k:\dim X_y\ge0}=\AA^1_k\sm\theset{0}$ is not closed.
For flat $f$ the jump is bounded below by $\dim_x X_{f(x)}=\dim_x X-\dim_{f(x)}Y$ ([[T-MORFIBDIM]]), and for $X$ Cohen--Macaulay and $Y$ regular the dimension equality at every point forces $f$ to be flat ([[T-MORMIRACLE]]).

[[algebraic-geometry/varieties/dimension-and-degree|Dimension and degree]] is the projective case, where the Hilbert polynomial refines the dimension by the degree.
