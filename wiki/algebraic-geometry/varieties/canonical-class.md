---
title: Varieties by canonical class
order: 7
topics:
- Fano Varieties
- Calabi-Yau Varieties
- Adjunction Formula
---

# Varieties by canonical class

For a smooth variety $X$ the canonical class $K_X$ is the class of $\omega_X=\det\Omega_{X/k}$ in $\Pic(X)$ ([[D-MODCONORM]]), and the sign of $K_X$ against the ample cone sorts the smooth complete varieties into three families ([[D-VARFANO]]).

[[D-VARFANO]]

## Hypersurfaces

[[FE-VARADJ]]

For a nonsingular divisor $D$ in a nonsingular variety $X$, adjunction computes the canonical class of $D$ from that of $X$:
$$
\omega_D\cong\omega_X\tensor\OO_X(D)\tensor\OO_D
$$
[@Har77, Proposition II.8.20].
For a hypersurface $D=V(f)\subseteq\PP^n$ of degree $d$ this gives $K_D=\OO_D(d-n-1)$, so $D$ is Fano, Calabi--Yau, or of general type according as $d<n+1$, $d=n+1$, or $d>n+1$ ([[FE-VARADJ]], [[D-VARFANO]]).
The line is sharp: a smooth plane curve of degree $d$ has genus $\binom{d-1}{2}$, which is $0$ for $d=1,2$ and at least $1$ for $d\ge3$ ([[algebraic-geometry/curves-and-surfaces/genus|genus]]).

## Projective space

[[T-MODEULER]]

On $\PP^n$ the determinant of the Euler sequence is $\OO_{\PP^n}(-n-1)$, so $K_{\PP^n}=\OO(-n-1)$ and $\PP^n$ is Fano with $-K_{\PP^n}=\OO(n+1)$ ample ([[D-VARFANO]]).

## Curves

On a smooth projective curve the canonical class has degree $2g-2$, so a curve is Fano exactly when $g=0$, Calabi--Yau in the weak sense exactly when $g=1$, and of general type exactly when $g\ge2$ ([[D-VARFANO]], [[T-LKT0U]]).
Riemann--Roch turns this degree into the dimensions of the spaces $H^0(C,\OO_C(mK_C))$, the plurigenera, which are birational invariants of the curve ([[T-BIRINV]]).

## Completeness and the classification

[[D-VARCOMP]]

The three conditions are conditions on $K_X$ relative to the ample cone, so they presuppose a complete $X$: ampleness and bigness are properties of classes on a complete variety, and the trichotomy is stated for smooth projective $X$ ([[D-VARFANO]], [[D-VARCOMP]]).
The minimal model programme is the general form of the question — which birational class contains a member whose canonical class is minimal — and the surface case is where it is a complete classification ([[algebraic-geometry/curves-and-surfaces/blowups-and-the-classification-of-surfaces|blowups and the classification of surfaces]]).
