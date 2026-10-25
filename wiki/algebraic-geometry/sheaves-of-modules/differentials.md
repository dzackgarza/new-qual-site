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
$$
f^*\Omega_{Y/S} \to \Omega_{X/S} \to \Omega_{X/Y} \to 0 .
$$
The conormal sequence, for a closed immersion $Z \subseteq X$ with ideal $\mci$:
$$
\mci/\mci^2 \to \Omega_{X/S}\restrictionof{}{Z} \to \Omega_{Z/S} \to 0 .
$$

Neither sequence is left exact in general; injectivity of the leftmost map requires additional hypotheses.
The first becomes short exact on the left for a smooth morphism, and its failure for a nonconstant map of curves is what Riemann--Hurwitz measures: the cokernel of $f^*\Omega_Y \to \Omega_X$ is the ramification divisor.
The second becomes short exact on the left when $Z$ is smooth, and taking determinants then gives adjunction,
$$
\omega_Z = \left( \omega_X \tensor \dualof{\det(\mci/\mci^2)} \right)\restrictionof{}{Z} ,
$$
which is the computation behind every genus formula in [[algebraic-geometry/curves-and-surfaces/index|curves and surfaces]].

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
