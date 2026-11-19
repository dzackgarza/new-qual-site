---
title: Contours and primitives
order: 5
topics:
- Contour Integration
- Primitives
- Winding Number
---

# Contours and primitives

A contour integral is computed by parameterizing the curve, and it is decided without any computation when the integrand has a primitive: the value depends only on the endpoints, and vanishes over a closed curve.

## Contours

[[D-6DAXB]]

[[D-YKB3V]]

The integral of $f$ along a curve is bounded by the largest value of $\abs f$ on the curve times its length, which is the estimate every arc argument uses.

[[T-SFXI7]]

A curve that is the boundary of a region oriented positively has an integral that Green's theorem converts into an area integral of $\delbar f$, which is Cauchy's theorem when $f$ is holomorphic ([[T-4M73O]], [[T-2OVCI]]).

## Primitives

[[D-6RZQN]]

On a [[D-GFM35|simply connected]] region every holomorphic function has a primitive, since its integrals over closed curves vanish ([[T-2OVCI]]); the primitive is then the integral from a fixed base point, and [[T-NRSFZ]] constructs the logarithm and its powers that way.

The winding number is the number that measures this failure.
On $\CC\sm\theset{a}$ the function $\inverseof{(z-a)}$ has no primitive, since
$$
\int_\gamma{\dz\over z-a} = 2\pi i\,\Index_\gamma(a)
$$
for a closed curve $\gamma$ avoiding $a$, and the right-hand side is not always zero.

[[D-PJ7JM]]

## Problems

[[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]] [[E-5GT6F]]
