---
title: Tangent, normal, and canonical sheaves
order: 6
topics:
- Tangent Sheaf
- Canonical Sheaf
- Conormal Sheaf
- Adjunction Formula
---

# Tangent, normal, and canonical sheaves

On a nonsingular variety the sheaf of differentials is locally free, and every sheaf on this page is built from it: the tangent sheaf is its dual, the canonical sheaf is its determinant, the conormal sheaf of a subvariety is the ideal modulo its square, and the normal sheaf is the dual of that.
The payoff is the adjunction formula, which computes the canonical sheaf of a subvariety from that of the ambient variety and the class of the subvariety — the single calculation behind the genus of a plane curve, the canonical class of a hypersurface, and the classification of surfaces.

## Tangent and cotangent

[[D-4GCH6]]

The sheaf of relative differentials $\Omega_{X/k}$ is quasicoherent for every morphism of schemes, and it is locally free of rank $n$ exactly when $X$ is smooth of relative dimension $n$ over $k$ ([[D-MORSM]]).
On a nonsingular variety over a field the tangent sheaf is its dual, the fibre at a point is the Zariski tangent space there ([[D-0SYCY]]), and the sheaf of vector fields is a sheaf of Lie algebras rather than of $\OO_X$-algebras.
The differential is a derivation over the base and not over $\OO_X$, so it does not commute with multiplication by functions; the same failure makes the de Rham differential non-linear over $\OO_X$ ([[FE-DERHAMNONLIN]]).

## The canonical sheaf

[[D-MODCONORM]]

For a smooth variety $X$ of dimension $n$ the canonical invertible sheaf is $\omega_X\coloneqq\det\Omega_{X/k}=\bigwedge^n\Omega_{X/k}$, and its class in $\Pic X$ is the canonical class $K_X$.
On projective space the determinants compute themselves: the Euler sequence $0\to\Omega_{\PP^n}\to\OO_{\PP^n}(-1)^{\oplus(n+1)}\to\OO_{\PP^n}\to0$ has determinant $\OO_{\PP^n}(-n-1)$, so $K_{\PP^n}=\OO(-n-1)$ ([[T-MODEULER]]).
Every later computation of a canonical class is a determinant of a short exact sequence of locally free sheaves, applied to the conormal sequence below or to a resolution.

## Normal and conormal sheaves

For a closed immersion $i\colon Z\hookrightarrow X$ with ideal sheaf $\mci$, the conormal sheaf $\mci/\mci^2$ is the part of $\inverseof{i}\Omega_X$ that is normal to $Z$, and the normal sheaf $\mcn_{Z/X}$ is its dual.
The conormal sequence
$$
\inverseof{i}\Omega_{X/k}\longrightarrow\Omega_{Z/k}\longrightarrow0
$$
is exact on the right, and its kernel is $\mci/\mci^2$ when $Z$ and $X$ are smooth.
When $Z$ is a local complete intersection the conormal sheaf is locally free, which is exactly what makes the determinant of the sequence exist and the adjunction formula an identity of invertible sheaves rather than merely of classes.

## Local complete intersections

[[D-SCHCMGOR]]

The three conditions in that card are strictly ordered, Cohen--Macaulay then Gorenstein then local complete intersection, and each is what remains of smoothness after the tangent bundle is discarded.
For the canonical sheaf the middle one is the useful one: a Cohen--Macaulay scheme that is Gorenstein has a dualizing sheaf that is invertible, so $\omega_X$ exists as a line bundle on a singular variety, and the adjunction formula continues to hold for divisors in a Gorenstein scheme.
A hypersurface in a smooth variety is a local complete intersection of codimension one, hence Gorenstein, hence has an invertible canonical sheaf even when it is singular.

## Adjunction

[[T-SRFADJ]]

For a smooth curve $C$ on a smooth projective surface $X$, adjunction reads
$$
2g(C)-2=C\cdot(C+K_X),
$$
so the genus of a curve is determined by the intersection form on the surface and the canonical class.
For a divisor $D$ in a smooth variety of dimension $n$ the same computation gives $K_D=\restrictionof{(K_X+D)}{D}$, obtained by taking determinants in $0\to\OO_X(-D)\to\OO_X\to\OO_D\to0$.
That is the formula that computes the canonical class of a smooth hypersurface of degree $d$ in $\PP^n$ as $\OO(d-n-1)$, and it is the first thing to write down when a surface is given by an equation ([[FE-VARADJ]]).

## Where the three sheaves are used

Differentials and the canonical sheaf are the input to Serre duality, so they decide what the cohomology of a smooth projective variety is dual to ([[T-COHSD]]); the normal sheaf is the input to deformation theory, where $\Ext^1$ of the tangent sheaf classifies first-order deformations ([[T-DEFEXT]]); and a crepant resolution is defined by the equality $K_Y=f^*K_X$, which is a statement about canonical sheaves ([[D-VARCREPANT]]).
