---
title: Varieties by canonical class
order: 7
topics:
- Fano Varieties
- Calabi-Yau Varieties
- Adjunction Formula
---

# Varieties by canonical class

For a smooth variety $X$ over a field $k$ the canonical sheaf is the top exterior power of the cotangent sheaf, $\omega_X=\det\Omega_{X/k}$, and the sign of its class $K_X$ against the ample cone sorts the smooth complete varieties into three families ([[D-MODCONORM]], [[D-VARFANO]]).
The trichotomy is a statement about a line bundle on a complete variety, so the classes are Fano when $-K_X$ is ample, Calabi--Yau when $K_X$ is torsion, and of general type when $K_X$ is big ([[D-VARFANO]]).
It is not exhaustive outside dimension one, and its three conditions behave differently under birational equivalence: being of general type is a birational property, while being Fano is not.

## The canonical class as an invertible sheaf

[[D-MODCONORM]]

On a smooth variety of dimension $n$ the sheaf of differentials $\Omega_{X/k}$ is locally free of rank $n$, so its determinant is an invertible sheaf $\omega_X=\det\Omega_{X/k}$ and $K_X$ is defined up to linear equivalence [@Har77, Chapter II, §8] ([[D-MODCONORM]]).
Determinants of exact sequences make this computable: for a short exact sequence $0\to\mcf'\to\mcf\to\mcf''\to0$ of locally free sheaves, $\det\mcf\cong\det\mcf'\tensor\det\mcf''$ [@Har77, Exercise II.5.16], so the canonical class of a variety built from a filtration of bundles is the alternating product of theirs ([[D-MODCONORM]]).
That is the computation behind both of the next two sections: the Euler sequence computes $K_{\PP^n}$, and the conormal sequence computes $K_D$ for a divisor $D$.

## Hypersurfaces and adjunction

[[FE-VARADJ]]

Adjunction is the statement $\omega_D\cong(\omega_X\tensor\OO_X(D))\restrict_D$ for a nonsingular divisor $D$ in a nonsingular variety $X$ [@Har77, Proposition II.8.20] ([[FE-VARADJ]]).
For a smooth hypersurface $D\subseteq\PP^n$ of degree $d$ this reads $K_D\sim(d-n-1)H\restrict_D$, so the sign of $d-n-1$ decides the family: $D$ is Fano for $d<n+1$, Calabi--Yau for $d=n+1$, and of general type for $d>n+1$ ([[FE-VARADJ]]).

The three cases are populated and separated by degree alone:
a quadric surface in $\PP^3$ is del Pezzo and is isomorphic to $\PP^1\times\PP^1$; a quartic surface in $\PP^3$ is a K3 surface, with $\omega_D\cong\OO_D$; a quintic threefold in $\PP^4$ has trivial canonical bundle.
For $n=2$ the same computation is the genus formula for a smooth plane curve, $g=\binom{d-1}{2}$, which is $0$ for $d\le2$ and positive for every $d\ge3$ ([[algebraic-geometry/curves-and-surfaces/genus|genus]]).
When $d=n+1$ the adjunction isomorphism $\omega_D\cong\OO_D$ is only half of the strict Calabi--Yau convention: the vanishing of the intermediate cohomology $H^j(D,\OO_D)$ for $1\le j\le n-2$ follows in addition, from the cohomology of the sequence $0\to\OO_{\PP^n}(-n-1)\to\OO_{\PP^n}\to\OO_D\to0$ ([[FE-VARADJ]]).

## Projective space

[[T-MODEULER]]

The Euler sequence $0\to\Omega_{\PP^n}\to\OO_{\PP^n}(-1)^{n+1}\to\OO_{\PP^n}\to0$ has determinant $\OO_{\PP^n}(-n-1)$, so $K_{\PP^n}=-\,(n+1)H$ and $-K_{\PP^n}=\OO(n+1)$ is ample; $\PP^n$ is Fano ([[T-MODEULER]], [[D-VARFANO]]).
The sequence is the sheaf-level shadow of the quotient $\PP^n=(\AA^{n+1}\sm0)/\GG_m$, and its dual $0\to\OO\to\OO(1)^{n+1}\to T_{\PP^n}\to0$ identifies the Euler vector field as the trivial subbundle ([[T-MODEULER]]).

## Curves

On a smooth projective curve the canonical class has degree $2g-2$ [@Har77, Example IV.1.3.3], and on a curve a divisor is ample exactly when its degree is positive.
So a curve is Fano exactly when $g=0$, Calabi--Yau in the weak sense exactly when $g=1$, and of general type exactly when $g\ge2$: the trichotomy is exhaustive in dimension one and cut out by one integer.
Riemann--Roch turns the degree into the dimensions of the spaces $H^0(C,\OO_C(mK_C))$, the plurigenera, and those are birational invariants of the curve ([[T-BIRINV]]).

## The three conditions

[[D-VARFANO]]

The definition is a definition on a smooth complete variety with a chosen $K_X$, and each clause carries a hypothesis worth stating.
$-K_X$ ample forces projectivity: a positive multiple of an ample line bundle on a scheme of finite type over a noetherian ring is very ample [@Har77, Theorem II.7.6], so a Fano variety is a projective variety and the definition never applies to a merely quasi-projective one ([[D-VARFANO]]).
Calabi--Yau has two conventions in circulation, the weak one requiring $K_X\sim_\QQ0$ and the strict one requiring $\omega_X\cong\OO_X$ together with $H^j(X,\OO_X)=0$ for $1\le j\le\dim X-1$; the abelian varieties of dimension at least $2$ satisfy the first and not the second ([[D-VARFANO]]).
General type requires $K_X$ big, which is a condition on the growth of the plurigenera rather than on positivity against every curve, and on a smooth projective variety it is preserved by birational maps ([[T-BIRINV]]).

The del Pezzo surfaces are the two-dimensional Fanos: over an algebraically closed field they are $\PP^1\times\PP^1$ and $\PP^2$ blown up at $r\le8$ points in general position, with $K^2=9-r$; the smooth cubic surface is the case $r=6$ and carries $27$ lines ([[D-VARFANO]]).

## Completeness and invariance

[[D-VARCOMP]]

The ampleness and bigness in the definitions are properties of divisor classes on a complete variety, and the trichotomy is stated for smooth projective $X$ for that reason ([[D-VARCOMP]]).
Completeness itself is not a birational condition but a properness condition on the structure morphism, and for an integral complete variety over an algebraically closed field $\Gamma(X,\OO_X)=k$, so the plurigenera are numbers rather than modules ([[D-VARCOMP]]).

[[T-BIRINV]]

Being of general type is birational: the plurigenera $P_m=h^0(X,mK_X)$, and with them the Kodaira dimension, are invariant under birational pullback between smooth projective varieties, so a variety is of general type exactly when every birational model is ([[T-BIRINV]]).
Being Fano is not birational, and the failure is visible on surfaces: blowing up a point $p$ of a surface $S$ with exceptional curve $E$ gives $K_{\widetilde S}=\pi^*K_S+E$, so $-\widetilde K$ restricts to a class with $(-\widetilde K)\cdot E=1$; blowing up a point lying on a $(-1)$-curve produces a $(-2)$-curve, on which $K$ has degree $0$ by adjunction, so $-\widetilde K$ is not ample there although $S$ was Fano ([[T-BIRINV]], [[algebraic-geometry/varieties/blowups|blowups]]).

The minimal model programme asks, for each birational class, whether it contains a member with $K$ as negative as possible, and the surface case is where the question is settled by a complete classification ([[algebraic-geometry/curves-and-surfaces/blowups-and-the-classification-of-surfaces|blowups and the classification of surfaces]]).
