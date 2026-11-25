---
title: Cohomology of projective schemes
order: 4
topics:
- Coherent Sheaves
- Vanishing Theorems
- Euler Characteristic
---

# Cohomology of projective schemes

[[T-COHFIN]]

The finiteness is where projective schemes part from affine ones: on an affine scheme the higher cohomology of a quasicoherent sheaf vanishes outright ([[T-COHAFF]]), while on a projective scheme over a noetherian ring the cohomology is finitely generated in every degree and vanishes above the dimension ([[T-COHFIN]]).

[[T-COHSVAN]]

Serre vanishing says that a coherent sheaf on a projective scheme has no higher cohomology after a twist, and the bound depends on the sheaf rather than on the scheme alone ([[T-COHSVAN]]).

## Euler characteristic and Hilbert polynomial

[[D-COHEULER]]

The Euler characteristic is the alternating sum of the $h^i$, finite by finiteness and vanishing ([[D-COHEULER]]); as a function of the twist by a very ample invertible sheaf it is a polynomial, the Hilbert polynomial of the sheaf with respect to that twist, and its value at zero is the intrinsic Euler characteristic ([[D-COHEULER]]).

[[T-COHFLATCHI]]

For $f\colon X\to T$ projective with $T$ noetherian and $\mcf$ coherent on $X$ and flat over $T$, each $h^i(X_t,\mcf_t)$ is upper semicontinuous in $t$ and $\chi(X_t,\mcf_t)$ is locally constant, by the [[T-COHBC|semicontinuity theorem]].
For a finitely generated graded $k$-algebra $S$ generated in degree one and a finite graded $S$-module $M$, the sheaf $\mcf=\widetilde M$ on $\Proj S$ has $\chi(\mcf(n))$ equal to the Hilbert polynomial of $M$ at every integer $n$ ([[D-COHEULER]], [@Har77, Exercise III.5.2]).
Flatness is what makes the Hilbert polynomial constant in a family, and for a closed subscheme of $\PP^n_T$ the converse holds: the polynomial of the fibre is the same for every $t$ exactly when the family is flat ([[T-COHFLATCHI]]).
In such a family the fibre dimension, degree and arithmetic genus are constant, being read off the common polynomial, while irreducibility, reducedness and smoothness need not be ([[T-COHFLATCHI]]).
