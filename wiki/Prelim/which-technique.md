---
title: Which technique?
order: 0
problems:
  topics:
  - Integrals
  - u-Substitution
  - Integration by Parts
  - Trigonometric Substitution
---

# Which technique?

The prelim is a computation paper.
Almost every integral is one of six forms, and recognizing the form is the whole exam.

## Integrals, by the shape of the integrand

| The integrand contains | Try |
| --- | --- |
| a function and its derivative | $u\dash$substitution |
| a product of unlike kinds | integration by parts, LIATE for the choice of $u$ |
| $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ | trigonometric substitution, $\sin$, $\tan$, $\sec$ |
| a proper rational function | partial fractions |
| odd powers of $\sin$ or $\cos$ | peel one factor off and substitute |
| even powers only | the half-angle identities |
| $R(\sin, \cos)$ with no better structure | the Weierstrass substitution $t = \tan(x/2)$ |

Two habits that shorten most problems:

- **Check for symmetry first.**
  An odd integrand over a symmetric interval integrates to zero, and an even one halves the work.
- **Check whether the answer is a standard form.**
  $\int \frac{\dx}{a^2+x^2}$, $\int\frac{\dx}{\sqrt{a^2-x^2}}$ and $\int \sec x \dx$ appear constantly and are worth knowing rather than deriving.

## Repeated integration by parts

When parts must be applied more than once, the tabular method is faster and less error-prone, and when the integral reappears on the right-hand side, solve for it algebraically rather than continuing.

## Series

- **Convergence:** ratio test for factorials and powers, root test for $n$th powers, comparison against a $p\dash$series otherwise, alternating series test for alternating ones, and integral test when the terms come from a monotone function.
- **Value:** geometric, telescoping, or a known expansion evaluated at a point.
  Almost every prelim series is one of those three.

## Limits

L'Hôpital, then Taylor expansion when L'Hôpital cycles, then squeeze.
For sequences defined recursively, show monotone and bounded and identify the limit from the fixed-point equation.

## Multivariable

- **Line integrals:** check whether the field is conservative first, since then only the endpoints matter.
- **A closed curve in the plane:** Green's theorem.
- **A closed surface:** the divergence theorem.
- **Otherwise:** parameterize, and choose coordinates matching the symmetry of the region.

The tables and worked cases are on [[Prelim/Useful Tricks|Useful tricks]].
