---
title: Riemann--Roch for curves
order: 10
topics:
- Riemann-Roch
- Serre Duality
- Special Divisors
---

# Riemann--Roch for curves

Riemann--Roch computes the dimension $\ell(D)$ of the space of sections of a divisor from its degree, the genus, and the index of speciality, and Serre duality identifies the index of speciality with $\ell(K_C-D)$ ([[T-MWDVL]], [[T-COHSD]]).
Together the two give the Euler characteristic $\chi(\OO_C(D))=\deg D+1-g$, and $\deg K_C=2g-2$ follows by taking $D=K_C$.

## The statement

[[T-MWDVL]]

Riemann--Roch relates three quantities, so it determines $\ell(D)$ only once one of the two section spaces is known; Serre duality supplies the second as the first of the complementary divisor, $h^1(\OO_C(D))=h^0(\OO_C(K-D))$ ([[T-COHSD]]).

## The degree of the canonical divisor

Taking $D=K_C$ in Riemann–Roch gives
$$
\ell(K_C)-\ell(0)=\deg K_C+1-g ,
$$
and $\ell(0)=1$ while $\ell(K_C)=h^1(\OO_C)=g$ by Serre duality, so $\deg K_C=2g-2$ [@Har77, Theorem IV.1.3].
That number is the degree of the canonical class, the threshold beyond which a divisor is nonspecial, and the exponent in the adjunction formula $2g-2=C\cdot(C+K)$ for a curve on a surface ([[T-SRFADJ]]).

## Special and nonspecial divisors

[[D-CRVSPEC]]

Above degree $2g-2$ the correction term vanishes and $\ell(D)=\deg D+1-g$ ([[T-MWDVL]]).
A divisor of degree at least $g$ therefore has a nonzero section, and a divisor of negative degree has none, an effective divisor having nonnegative degree.
In genus $0$ every divisor of degree at least $0$ has $\ell(D)=\deg D+1$, matching the sections of $\OO_{\PP^1}(d)$, and over an algebraically closed field a smooth projective curve of genus $0$ is isomorphic to $\PP^1$ ([[PR-VGA2L]]).

## Small degree and Clifford's theorem

[[T-CRVCLIFF]]

In the special range Clifford's theorem bounds $\ell(D)\le\deg D/2+1$, with equality only for $D=0$, for $D=K$, and, on a hyperelliptic curve, for $D$ a multiple of the unique $g^1_2$ ([[T-CRVCLIFF]]).
The gonality is the smallest $d$ for which a $g^1_d$ exists, so a special divisor of small dimension forces a map of low degree to $\PP^1$ ([[D-CRVGON]]).

[[PR-VGA2L]]

[[D-CRVHYP]]

## The canonical embedding

[[T-D8TUX]]

For $g\ge2$ the canonical map is the map attached to $\linearsystem{K_C}$, and Riemann–Roch computes its source: $\ell(K_C)=g$, so the canonical map goes to $\PP^{g-1}$.
It is an embedding exactly when the curve is not hyperelliptic (and $g\ge3$), and for a hyperelliptic curve it factors through the degree-two map to $\PP^1$ ([[T-D8TUX]], [[D-CRVHYP]]).
The canonical model therefore determines the genus and whether $C$ is hyperelliptic; the special divisors are treated on [[algebraic-geometry/curves-and-surfaces/special-divisors-and-the-canonical-map|special divisors and the canonical map]].

## Riemann--Roch as a vanishing theorem

The equality $\chi(\OO_C(D))=\deg D+1-g$ holds for every divisor, and above degree $2g-2$ the vanishing of $h^1$ makes it a dimension ([[T-MWDVL]]).
That vanishing is also the one-dimensional case of Serre vanishing for a sufficiently positive twist of a coherent sheaf [@Har77, Theorem III.5.2] ([[T-CARTSERRE]]).
