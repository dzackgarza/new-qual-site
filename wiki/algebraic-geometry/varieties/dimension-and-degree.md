---
title: Dimension and degree
order: 3
topics:
- Dimension
- Degree
- Hilbert Polynomial
---

# Dimension and degree

[[D-5LJUX]]

## Dimension

The chain definition is the topological one; on an affine variety it agrees with the Krull dimension of the coordinate ring [@Har77, Proposition I.1.7], and for a finitely generated domain over any field the Krull dimension is the transcendence degree of the fraction field [@Har77, Theorem I.1.8A].
So the dimension is determined by the function field $k(X)$.
Krull's principal ideal theorem makes one equation cut the dimension by at most one, and on affine space it makes the codimension-one irreducible closed subsets exactly the hypersurfaces ([[PR-VARHT]]).

[[PR-VARHT]]

## Degree, before the Hilbert polynomial

[[D-VARDEG]]

The degree counts the points of $X\cap H_1\cap\cdots\cap H_n$ for general hyperplanes, and independence of the choice of hyperplanes is part of what the definition asserts ([[D-VARDEG]]).
For a hypersurface the three notions of degree agree: the degree of the defining equation, the leading coefficient of the Hilbert polynomial, and the intersection count are all $d$ ([[PR-JR7TS]]).
Bézout's theorem is the multiplicativity of this count: for a variety $Y$ of dimension $r\ge1$ and degree $e$ in $\PP^n$ and a hypersurface $H$ of degree $d$ not containing $Y$, the components $Z_j$ of $Y\cap H$ satisfy $\sum_j i(Y,H;Z_j)\deg Z_j=de$ [@Har77, Theorem I.7.7], and for two distinct plane curves of degrees $d$ and $e$ the sum of the intersection multiplicities is $de$ [@Har77, Corollary I.7.8].
The count itself drops for hyperplanes that are not general while the sum of multiplicities stays: a line tangent to a conic meets it in one point of multiplicity two ([[D-VARDEG]]).
A $d$-uple embedding multiplies the degree by $d^n$, and the Segre embedding of $\PP^r\times\PP^s$ has degree $\binom{r+s}{r}$ [@Har77, Exercise I.7.1].

[[D-VARSCROLL]]

## The Hilbert polynomial

[[D-L6ERW]]

[[PR-JR7TS]]

The dimension is the degree of the Hilbert polynomial and the degree of $X$ is $n!$ times its leading coefficient ([[D-L6ERW]], [[D-VARDEG]]); the arithmetic genus is read off its constant term:
$$
p_a(X)=(-1)^n\bigl(P_X(0)-1\bigr),
$$
which is $0$ for $\PP^n$, $\binom{d-1}{n}$ for a hypersurface of degree $d$ in $\PP^n$, and $\frac12(d-1)(d-2)$ for a plane curve of degree $d$ [@Har77, Exercise I.7.2].
The same values come from the Euler characteristic, since $h^0(X,\OO_X(m))=\chi(X,\OO_X(m))$ for $m\gg0$ ([[D-L6ERW]], [[D-COHEULER]]).

## What depends on the embedding

Dimension does not depend on the embedding ([[D-5LJUX]]). The [[D-L6ERW|Hilbert polynomial]] does: its leading coefficient, and so the [[D-VARDEG|degree]], changes with the embedding, while its value at zero does not, so the arithmetic genus is intrinsic — defined as $(-1)^n(\chi(\OO_X)-1)$, it depends only on $X$ [@Har77, Exercise III.5.3].
Dimension, degree and arithmetic genus are thus the degree, the leading coefficient and the constant term of one polynomial, and the embedding enters only through the middle one.

## Families of varieties

[[D-VARVERYGEN]]

[[D-VARCHOW]]
