---
title: Homological algebra
order: 6
topics:
- Homological Algebra
- Abelian Categories
- Derived Functors
---

# Homological algebra

Sheaf cohomology is the right derived functor of $\Gamma(X,\wait)$, so every computation in the rest of this chapter is one construction applied to one functor: resolve, apply, take cohomology.
This page writes that construction out once, in the generality the chapter uses and no further, so that the vanishing theorems that follow can be read as statements about a functor rather than as separate arguments.

## Abelian categories

[[D-DEFABCAT]]

The two categories the chapter computes in are $\mods{A}$ for a ring $A$ and $\mods{\OO_X}$ for a ringed space $X$; both are abelian, and in both a cokernel is not the naive one.
The cokernel of a map of sheaves is the sheafification of the presheaf cokernel, and the image is the sheafification of the presheaf image ([[D-A7LCT]]).
The additive category of topological abelian groups is the standard warning that kernels and cokernels alone are not enough: it has both, and it fails the last axiom, since the identity map from $\RR$ with the discrete topology to $\RR$ with the Euclidean topology is a monomorphism and an epimorphism and not an isomorphism.

## Additive functors and exactness

[[D-DEFADDFN]]

[[D-DEFEXACT]]

Additivity is not decoration: it is what makes a functor carry a complex to a complex and a homotopy to a homotopy, so it is the hypothesis under which $R^iF$ is well defined.
Exactness is what fails, and the failure is the subject.
$\Gamma(X,\wait)$ is left exact; on $X=\CC\sm\theset{0}$ the exponential $\OO_X\to\OO_X^\times$ is an epimorphism of sheaves whose global sections are not all logarithms, so the induced map on $H^0$ is not onto and $H^1(X,\ZZ)$ measures the gap ([[FE-DNTT6]]).

## Complexes and homotopy

[[D-DEFCPLX]]

Two resolutions of the same object are compared by a lift of the identity, which exists by injectivity, and any two such lifts are homotopic.
So the object $h^i(F(I^\bullet))$ depends on the functor and the object, not on the resolution chosen to compute it — which is the only reason $R^iF(A)$ is a definition rather than a convention.

## Resolutions

[[D-DEFINJOB]]

[[D-DEFPROJO]]

The asymmetry between the two resolutions is the asymmetry of the chapter.
Every ringed space has $\mods{\OO_X}$ with enough injectives [@Har77, Proposition III.2.2], so right derived functors of left exact functors always exist there; there are spaces over which $\mods{\OO_X}$ has too few projectives to compute anything [@Har77, Exercise III.6.2], which is why sheaf cohomology is a right derived functor and $\Tor$ is a left one.

## Derived functors

[[D-DEFDERIV]]

For a left exact $F$, $R^0F\cong F$ and $R^iF=0$ for $i>0$ exactly when $F$ is exact, so the higher derived functors are a measurement of the failure of exactness and nothing else.

## Universality

[[D-DEFDELTA]]

Grothendieck's theorem is what lets two computations of the same groups agree without a comparison map being written down each time: a $\delta$-functor that is effaceable in positive degrees is universal, and two universal $\delta$-functors agreeing in degree zero agree everywhere.
Two computations of the same groups then agree without a comparison map being written down each time: this is why the two definitions of $\Ext$ coincide, and why the long exact sequence attached to a short exact sequence of sheaves ([[PR-COHLES]]) is forced by its degree-zero part.

## Acyclic resolutions

[[D-DEFACYC]]

A resolution by $F$-acyclic objects computes $R^\bullet F$, and the useful acyclic objects are rarely injective: flasque sheaves are $\Gamma$-acyclic, free modules are acyclic for $\wait\tensor_A N$, and quasicoherent sheaves on an affine scheme are $\Gamma$-acyclic.
The last of these is the engine of the next two pages: it turns an affine open cover into a complex that computes $H^i(X,\mcf)$ for a quasicoherent $\mcf$ on a noetherian separated scheme [@Har77, Theorem III.4.5].

## Ext and Tor

[[D-DEFEXT]]

[[D-DEFTOR]]

$\Ext^1_A(M,N)$ is the group of extensions of $M$ by $N$, and $\Tor_1^A(M,N)$ is the obstruction to tensoring being exact; both are computed by resolving either argument, and the coincidence of the two answers is again universality.
Over $\ZZ$ they have closed forms, $\Ext^1_\ZZ(\ZZ/n,N)=N/nN$ and $\Tor_1^\ZZ(\ZZ/m,B)=\theset{b\in B\st mb=0}$, which is why they can be used to test a statement about modules without a resolution being written out.

## Where this is used

The long exact sequence of a short exact sequence of sheaves, and the identification of $H^1(X,\OO_X^\times)$ with the Picard group, both come from this page applied to $\Gamma(X,\wait)$ ([[PR-ET5PQ]]).
[[algebraic-geometry/cohomology/derived-functors-and-vanishing|Derived functors and vanishing]] applies it to a ringed space; [[algebraic-geometry/sheaves-of-modules/differentials|differentials]] uses it to compute on projective space.
