---
title: Differentials
order: 2
topics:
- Differentials
- Smoothness
- Canonical Divisor
---

# Differentials

Differentials encode both infinitesimal structure and smoothness.

[[D-4GCH6]]

Quasicoherence follows because the affine construction commutes with localization.
For a finite-type scheme over a field, local freeness of $\Omega_{X/k}$ of the expected rank detects smoothness and matches the Jacobian criterion.

## The two sequences

The relative sequence, for $X \to Y \to S$:
\[
f^*\Omega_{Y/S} \to \Omega_{X/S} \to \Omega_{X/Y} \to 0 .
\]
The conormal sequence, for a closed immersion $Z \subseteq X$ with ideal $\mci$:
\[
\mci/\mci^2 \to \Omega_{X/S}\ro{}{Z} \to \Omega_{Z/S} \to 0 .
\]

Neither is exact on the left in general, and that is where the content is.
The first becomes short exact on the left for a smooth morphism, and its failure for a nonconstant map of curves is what Riemann--Hurwitz measures: the cokernel of $f^*\Omega_Y \to \Omega_X$ is the ramification divisor.
The second becomes short exact on the left when $Z$ is smooth, and taking determinants then gives adjunction,
\[
\omega_Z = \left( \omega_X \tensor \det(\mci/\mci^2)\dual \right)\ro{}{Z} ,
\]
which is the computation behind every genus formula in [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

[[D-MODCONORM]]

## The canonical sheaf

For $X$ smooth of dimension $n$, $\omega_X = \det \Omega_{X/k} = \bigwedge^n \Omega_{X/k}$.
On $\PP^n$ it is $\OO(-n-1)$, which is the single computation the rest of the subject leans on: it gives $H^0(\PP^1, \Omega^1) = H^0(\PP^1, \OO(-2)) = 0$, it makes projective space Fano, and through adjunction it produces the genus of a plane curve.

## Projective space

The canonical sheaf of $\PP^n$ is not computed by hand; it is read off a determinant.

[[T-MODEULER]]

The Euler sequence and its top exterior power give $\omega_{\PP^n}\cong\OO(-n-1)$.

## The de Rham complex

[[FE-DERHAMNONLIN]]
