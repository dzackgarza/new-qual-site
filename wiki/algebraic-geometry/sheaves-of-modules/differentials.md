---
title: Differentials
order: 2
topics:
- Differentials
- Smoothness
- Canonical Divisor
---

# Differentials

[[D-4GCH6]]

Quasicoherence follows because the affine construction commutes with localization.
For $X$ of finite type over a field $k$ and equidimensional of dimension $n$, $X$ is smooth over $k$ exactly when $\Omega_{X/k}$ is locally free of rank $n$; on an affine chart this is the Jacobian criterion.

## The two sequences

The relative sequence, for $X \to Y \to S$:
\[
f^*\Omega_{Y/S} \to \Omega_{X/S} \to \Omega_{X/Y} \to 0 .
\]
The conormal sequence, for a closed immersion $Z \subseteq X$ with ideal $\mci$:
\[
\mci/\mci^2 \to \Omega_{X/S}\ro{}{Z} \to \Omega_{Z/S} \to 0 .
\]

Neither sequence is left exact in general.
For the Frobenius $F\colon\AA^1_k\to\AA^1_k$ in characteristic $p$, the map $F^*\Omega_{\AA^1}\to\Omega_{\AA^1}$ is zero.
For $Z=V(x^2)\subset\AA^1_k$ with $\operatorname{char}k\neq3$, the class of $x^3$ in $\mci/\mci^2=(x^2)/(x^4)$ is nonzero and maps to $3x^2\,dx=0$ in $\Omega_{\AA^1}|_Z$.

The relative sequence is exact on the left when $X\to Y$ is smooth.
For a finite separable morphism $f\colon X\to Y$ of smooth curves, $0\to f^*\Omega_Y\to\Omega_X\to\Omega_{X/Y}\to0$ is exact, $\Omega_{X/Y}$ is a torsion sheaf whose lengths give the ramification divisor $R$, and $\Omega_X\cong f^*\Omega_Y(R)$.
The conormal sequence is exact on the left when $X$ and $Z$ are smooth over a field, and taking determinants then gives adjunction,
\[
\omega_Z = \left( \omega_X \tensor \det(\mci/\mci^2)\dual \right)\ro{}{Z} .
\]
For a smooth curve $C$ on a smooth surface $X$, $\det(\mci/\mci^2)^\vee=\OO_X(C)|_C$, so $\omega_C=(\omega_X\otimes\OO_X(C))|_C$; see [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

[[D-MODCONORM]]

## The canonical sheaf

For $X$ smooth of dimension $n$, $\omega_X = \det \Omega_{X/k} = \bigwedge^n \Omega_{X/k}$.
On $\PP^n$ it is $\OO(-n-1)$.
Hence $H^0(\PP^1,\Omega^1)=H^0(\PP^1,\OO(-2))=0$; $\omega_{\PP^n}^\vee=\OO(n+1)$ is ample, so $\PP^n$ is Fano; and adjunction gives $\omega_C\cong\OO_C(d-3)$ for a smooth plane curve $C$ of degree $d$, so $2g-2=d(d-3)$.

## Projective space

[[T-MODEULER]]

The Euler sequence and its top exterior power give $\omega_{\PP^n}\cong\OO(-n-1)$.

## The de Rham complex

[[FE-DERHAMNONLIN]]
