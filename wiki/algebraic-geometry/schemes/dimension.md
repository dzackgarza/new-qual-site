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

Let $f\colon X\to Y$ be a morphism of finite type between schemes locally of finite type over a field.
The dimension of the largest irreducible component of the fibre $X_{f(x)}$ through a point $x$ is upper semicontinuous on $X$: for every integer $r$ the locus of points lying on a fibre component of dimension at least $r$ is closed, so the fibre dimension jumps up only on closed subsets of $X$ [@Vak25, Theorem 12.4.3(a)].
The local dimension $\dim_x X_{f(x)}=\krulldim\OO_{X_{f(x)},x}$ is a different function and is not upper semicontinuous:

::: {.example title="The local dimension of a fibre is not upper semicontinuous"}
For the structure morphism $f\colon\AA^1_k\to\Spec k$ the single fibre is $\AA^1_k$, on which every point lies on the one component, of dimension $1$, while $\dim_x X_{f(x)}$ is $1$ at each closed point and $0$ at the generic point $\eta$.
The locus $\theset{x:\dim_x X_{f(x)}\ge1}$ is the set of closed points, which is not closed, so the local dimension is not upper semicontinuous at $\eta$ ([[T-MORFIBDIM]]).
:::

For $f$ closed, in particular for $f$ proper, the function $y\mapsto\dim X_y$ is upper semicontinuous on $Y$ [@Vak25, Theorem 12.4.3(b)].
Properness is a hypothesis of that statement: the open immersion $f\colon\AA^1_k\sm\theset{0}\into\AA^1_k$ has empty fibre over $0$ and a zero-dimensional fibre over every other point, so $\theset{y\in\AA^1_k:\dim X_y\ge0}=\AA^1_k\sm\theset{0}$ is not closed.
For flat $f$ the local dimension of the fibre is $\dim_x X-\dim_{f(x)}Y$ at each point ([[T-MORFIBDIM]]), and conversely, for $X$ Cohen--Macaulay and $Y$ regular, the pointwise equality $\dim\OO_{X,x}=\dim\OO_{Y,f(x)}+\dim\OO_{X_{f(x)},x}$, with the local ring of each fibre equidimensional, forces $f$ to be flat: the purity of the fibre ring is the hypothesis of the local theorem, and the numerical equality alone is what flatness guarantees ([[T-MORMIRACLE]]).

[[algebraic-geometry/varieties/dimension-and-degree|Dimension and degree]] is the projective case, where the Hilbert polynomial refines the dimension by the degree.
