---
title: Which technique?
order: 0
topics:
- Integrals
- u-Substitution
- Integration by Parts
- Trigonometric Substitution
---

# Which technique?

## Integrals, by the form of the integrand

| The integrand contains | Method |
| --- | --- |
| a function and its derivative | $u$-substitution |
| a product of functions of different types | integration by parts, with $u$ chosen in the order logarithmic, inverse trigonometric, algebraic, trigonometric, exponential |
| $\sqrt{a^2-x^2}$, $\sqrt{a^2+x^2}$, $\sqrt{x^2-a^2}$ | trigonometric substitution $x=a\sin\theta$, $x=a\tan\theta$, $x=a\sec\theta$ respectively |
| a proper rational function | partial fractions |
| an odd power of $\sin$ or $\cos$ | factor out one $\sin$ or $\cos$, rewrite the rest with $\sin^2+\cos^2=1$, and substitute |
| even powers of $\sin$ and $\cos$ only | the half-angle identities |
| a rational function $R(\sin x, \cos x)$ | the Weierstrass substitution $t = \tan(x/2)$ |

**Symmetry.** If $f$ is odd, then $\int_{-a}^a f = 0$; if $f$ is even, then $\int_{-a}^a f = 2\int_0^a f$.

**Standard forms.**
$$
\int \frac{\dx}{a^2+x^2} = \frac1a\arctan\frac xa + C, \qquad \int\frac{\dx}{\sqrt{a^2-x^2}} = \arcsin\frac xa + C, \qquad \int \sec x \dx = \ln\abs{\sec x+\tan x} + C.
$$

## Repeated integration by parts

For $\int P(x)g(x)\dx$ with $P$ a polynomial, the tabular method applies integration by parts $\deg P + 1$ times; see [[prelim/useful-tricks|Useful tricks]].
If the original integral reappears after integrating by parts, as in $\int e^x\sin x\dx$, the resulting equation can be solved for the integral.

## Series

- **Convergence.** The ratio test applies to terms built from factorials and powers, the root test to terms that are $n$th powers, comparison with a $p$-series to terms comparable to $n^{-p}$, the alternating series test to alternating series with terms decreasing to $0$, and the integral test to $\sum f(n)$ with $f$ positive and decreasing.

- **Value.** Geometric series, telescoping series, and known power series evaluated at a point.

## Limits

For indeterminate forms: L'Hôpital's rule; Taylor expansion, when repeated applications of L'Hôpital's rule do not simplify the quotient; the squeeze theorem.
A recursively defined sequence that is monotone and bounded converges, and if $a_{n+1}=g(a_n)$ with $g$ continuous, its limit $L$ satisfies $L = g(L)$.

## Multivariable integrals

- **Line integrals.** If the field is conservative, $F = \nabla\phi$, then $\int_C F\cdot d\mathbf{r} = \phi(\text{end})-\phi(\text{start})$.

- **Closed curves in the plane.** Green's theorem.

- **Closed surfaces.** The divergence theorem.

- **Other integrals.** Parametrize the curve or surface, in coordinates adapted to the symmetry of the region.
