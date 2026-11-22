---
title: Contours and primitives
order: 5
topics:
- Contour Integration
- Primitives
- Winding Number
---

# Contours and primitives

A contour integral is computed by parameterizing the curve, and it is decided without any computation when the integrand has a primitive: the value is read off the endpoints by [[D-6RZQN|the primitive]], and a closed curve gives zero.

## Contours

[[D-6DAXB]]

[[D-YKB3V]]

The estimate every arc argument uses bounds the integral by the largest value of $\abs f$ on the curve times its length:

[[T-SFXI7]]

For a curve that bounds a positively oriented region, Green's theorem converts the integral into an area integral of $\delbar f$ ([[T-4M73O]]), which is one route to Cauchy's theorem ([[T-2OVCI]]).

## Primitives

[[D-6RZQN]]

[[T-PRIM]]

[[T-NRSFZ|The logarithm and roots of a nonvanishing function]] are constructed from such a primitive.

[[D-PJ7JM]]

The winding number measures this failure: on $\CC\sm\theset{a}$ the function $\inverseof{(z-a)}$ has no primitive, and its integral over a closed curve is $2\pi i$ times the [[D-PJ7JM|winding number]] of the curve about $a$ ([[D-6RZQN]]).

## Problems

[[E-RLHXB]] [[E-VGNUI]] [[E-3B2YA]] [[E-5GT6F]]
