---
title: Riemann--Roch for curves
order: 10
topics:
- Riemann-Roch
- Serre Duality
- Special Divisors
---

# Riemann--Roch for curves

Riemann–Roch is the one theorem that computes a space of functions on a curve from discrete data: the dimension of the space of sections of a divisor is its degree, corrected by the genus and by one unknown, the index of speciality.
Serre duality identifies that unknown with the space of sections of the complementary divisor, which is what turns Riemann–Roch from an inequality into an equation, and the two together give the Euler characteristic outright.
This page states both, derives $\deg K_C=2g-2$ from them, and reads off the consequences in the ranges of degree where the answer is immediate and where it is not.

## The statement

[[T-MWDVL]]

The two theorems are used as a pair and it is worth seeing why: Riemann–Roch alone relates three quantities, so it computes nothing until one of the two section spaces is known, and Serre duality says the second one is the first one of a different divisor.
Equivalently, Riemann–Roch is the statement $\chi(\OO_C(D))=\deg D+1-g$, and Serre duality is the statement $h^1(\OO_C(D))=h^0(\OO_C(K-D))$ which converts the Euler characteristic into a dimension ([[T-COHSD]]).

## The degree of the canonical divisor

Taking $D=K_C$ in Riemann–Roch gives
$$
\ell(K_C)-\ell(0)=\deg K_C+1-g ,
$$
and $\ell(0)=1$ while $\ell(K_C)=h^1(\OO_C)=g$ by Serre duality, so $\deg K_C=2g-2$ [@Har77, Proposition IV.1.3].
That number is the reason $2g-2$ appears everywhere in the theory of curves: it is the degree of the canonical class, it is the threshold beyond which a divisor is nonspecial, and it is the exponent in the adjunction formula $2g-2=C\cdot(C+K)$ for a curve on a surface ([[T-SRFADJ]]).

## Special and nonspecial divisors

[[D-CRVSPEC]]

Above degree $2g-2$ the correction term vanishes and the dimension is exactly $\deg D+1-g$; the divisors that are not of this form are the interesting ones, and they are the ones a linear system is asked about.
Two consequences are used constantly: a divisor of degree at least $g$ has a nonzero section, since $\ell(D)\ge\deg D+1-g\ge1$; and a divisor of negative degree has none, since an effective divisor has nonnegative degree.
The genus $0$ case is the sharpest: every divisor has $\ell(D)=\deg D+1$ once $\deg D\ge0$, matching the sections of $\OO_{\PP^1}(d)$, and a smooth projective curve of genus $0$ is isomorphic to $\PP^1$.

## Small degree and Clifford's theorem

[[T-CRVCLIFF]]

In the special range $\ell(D)$ is bounded by half the degree plus one, and the bound is attained only by the trivial divisors, the canonical divisor, and — when the curve is hyperelliptic — by a $g^1_2$.
That is the first statement of the Brill–Noether theory of the chapter: the gonality of a curve is the smallest $d$ for which a $g^1_d$ exists, and Clifford says a special divisor with a small dimension forces the curve to have a map of low degree to $\PP^1$ ([[D-CRVGON]]).

[[PR-VGA2L]]

[[D-CRVHYP]]

## The canonical embedding

[[T-D8TUX]]

For $g\ge2$ the canonical map is the map attached to $\linearsystem{K_C}$, and Riemann–Roch computes its source: $\ell(K_C)=g$, so the canonical map goes to $\PP^{g-1}$.
It is an embedding exactly when the curve is not hyperelliptic (and $g\ge3$), and for a hyperelliptic curve it factors through the degree-two map to $\PP^1$ — the case the canonically embedded curve cannot distinguish from its image, which is why the hyperelliptic involution is invisible in the canonical model.
So the genus and the hyperelliptic involution are both readable from one linear system, and the divisors nobody asked about — the special ones — are exactly the ones the geometry is made of ([[algebraic-geometry/curves-and-surfaces/special-divisors-and-the-canonical-map|special divisors and the canonical map]]).

## Riemann--Roch as a vanishing theorem

The equality $\chi(\OO_C(D))=\deg D+1-g$ holds for every divisor, but it is the vanishing of $h^1$ above degree $2g-2$ that makes it readable as a dimension.
That is Serre vanishing in dimension one, and it is the same phenomenon as $H^i(\PP^n,\OO(d))=0$ for $i>0$ and $d$ large ([[T-IJW1K]]): on a curve there is only one interesting cohomology group, and Riemann–Roch is the statement that it can be traded for a degree.
