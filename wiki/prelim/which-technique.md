---
title: Which technique?
order: 1
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

::: {.example title="A symmetric interval halves or kills the integral"}
Substituting $x\mapsto -x$ shows that an odd integrand has $\int_{-a}^a f = 0$ and an even one has $\int_{-a}^a f = 2\int_0^a f$; for instance $\int_{-1}^1 x^3 e^{x^2}\dx = 0$, the integrand being odd.

:::

Three antiderivatives worth recognizing:
$$
\int \frac{\dx}{a^2+x^2} = \frac1a\arctan\frac xa + C, \qquad
\int\frac{\dx}{\sqrt{a^2-x^2}} = \arcsin\frac xa + C, \qquad
\int \sec x \dx = \ln\abs{\sec x+\tan x} + C,
$$
the second for $\abs x<a$, and the third by multiplying the integrand by $(\sec x+\tan x)/(\sec x+\tan x)$.

## Repeated integration by parts

For $\int P(x)g(x)\dx$ with $P$ a polynomial, the tabular method applies integration by parts $\deg P$ times, and its table has $\deg P + 1$ nonzero rows; see [[prelim/useful-tricks|Useful tricks]].
If the original integral reappears after integrating by parts, as in $\int e^x\sin x\dx$, the resulting equation can be solved for the integral.

## Series

For convergence, the ratio test applies to terms built from factorials and powers, the root test to terms that are $n$th powers, comparison with a $p$-series to terms comparable to $n^{-p}$, the alternating series test to alternating series whose terms decrease to $0$, and the integral test to $\sum f(n)$ with $f$ positive and decreasing.

For the value, a geometric series, a telescoping series, or a known power series evaluated at a point gives the sum; a power series converges absolutely on the interior of its interval of convergence, and the sum is differentiable there term by term.

## Limits

For an indeterminate form of type $0/0$ or $\infty/\infty$ the rule of l'Hôpital gives
$$
\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}
$$
whenever the second limit exists, $f$ and $g$ being differentiable near $a$ with $g'$ nonzero there; Taylor expansion replaces it when repeated differentiation does not simplify the quotient, and the squeeze theorem applies when the function is bounded between two functions of known limit.

A recursively defined sequence that is monotone and bounded converges, and if $a_{n+1}=g(a_n)$ with $g$ continuous and $a_n\to L$, then $L = g(L)$.

## Multivariable integrals

For a conservative field $F = \nabla\phi$ on an open set containing the curve $C$, the line integral is $\int_C F\cdot d\mathbf{r} = \phi(\text{end})-\phi(\text{start})$, by the chain rule along a parametrization.

For a closed curve $\partial\Omega$ bounding a plane region $\Omega$, [[T-4M73O|Green's theorem]] turns the line integral into the double integral of $\partial g/\partial x - \partial f/\partial y$.

For a closed surface $\partial V$ bounding a solid $V$ with outward normal $n$, the divergence theorem turns the surface integral into the triple integral of the divergence:
$$
\iint_{\partial V} F\cdot n\,dS = \iiint_V \nabla\cdot F\,dV.
$$

Otherwise, parametrize the curve or the surface, in coordinates adapted to the symmetry of the region.
