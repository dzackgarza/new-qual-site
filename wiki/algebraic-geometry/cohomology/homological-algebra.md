---
title: Homological algebra
order: 6
topics:
- Homological Algebra
- Abelian Categories
- Derived Functors
---

# Homological algebra

Let $\Gamma(X,-)$ be the global-sections functor on $\mods{\OO_X}$ for a ringed space $X$.
Sheaf cohomology is its right derived functor, so computing $H^i(X,\mcf)$ means resolving $\mcf$, applying $\Gamma(X,-)$, and taking cohomology ([[D-DEFDERIV]]).

## Abelian categories

[[D-DEFABCAT]]

[[D-A7LCT]]

Both $\mods{A}$ and $\mods{\OO_X}$ are abelian ([[D-DEFABCAT]]), and in $\mods{\OO_X}$ the cokernel is the [[D-A7LCT|cokernel sheaf]], the sheafification of $U\mapsto\coker\bigl(f(U)\bigr)$: the presheaf need not be a sheaf, and sheafifying is what gives the universal property [@Har77, Proposition-Definition II.1.2].
In $\mods{A}$ nothing needs sheafifying and the cokernel is the quotient $N/\im f$.

## Additive functors and exactness

[[D-DEFADDFN]]

[[D-DEFEXACT]]

An additive functor carries a complex to a complex and a homotopy to a homotopy, which is the hypothesis under which $R^iF$ is defined ([[D-DEFCPLX]]).
$\Gamma(X,-)$ is left exact and not exact: on $X=\CC\sm\theset{0}$ the exponential is an epimorphism of sheaves whose global sections are not all logarithms, and $H^1(X,\ZZ)$ measures the failure ([[FE-DNTT6]]).

## Complexes and homotopy

[[D-DEFCPLX]]

## Resolutions

[[D-DEFINJOB]]

[[D-DEFPROJO]]

Every ringed space has $\mods{\OO_X}$ with enough injectives, so the right derived functors of a left exact functor on $\mods{\OO_X}$ exist [@Har77, Proposition III.2.2].
For $X=\PP^1_k$ over an infinite field there is no projective $\mcp\in\mods{\OO_X}$ admitting a surjection onto $\OO_X$, so $\mods{\OO_X}$ does not have enough projectives and $\Hom$ has no right derived functors in its first variable [@Har77, Caution III.6.5.2 and Exercise III.6.2]; sheaf cohomology is therefore a right derived functor and $\Tor$ a left one.

## Derived functors

[[D-DEFDERIV]]

## Universality

[[D-DEFDELTA]]

A $\delta$-functor that is effaceable in positive degrees is universal, so two universal $\delta$-functors agreeing in degree zero agree in every degree ([[D-DEFDELTA]]).
The two definitions of $\Ext$ agree, and the long exact sequence of a short exact sequence of sheaves is determined by its degree-zero part ([[PR-COHLES]]).

## Acyclic resolutions

[[D-DEFACYC]]

## Ext and Tor

[[D-DEFEXT]]

[[D-DEFTOR]]

$\Ext^1_A(M,N)$ is the group of extensions of $M$ by $N$, and $\Tor_1^A(M,N)$ measures the failure of $-\tensor_A N$ to be exact; over $\ZZ$ they are $\Ext^1_\ZZ(\ZZ/n,N)\cong N/nN$ and $\Tor_1^\ZZ(\ZZ/m,B)\cong\theset{b\in B:mb=0}$ ([[D-DEFEXT]], [[D-DEFTOR]]).
