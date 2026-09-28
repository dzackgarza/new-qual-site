---
schema: qual/card@1
id: E-SS4.EX-10
kind: problem
title: "This exercise generalizes some of the properties of  related to the fact that it"
classification:
  areas:
  - complex-analysis
  topics: ['Fourier Transform', 'Poisson Summation']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.exercise}
10. This exercise generalizes some of the properties of $e ^ { - \pi x ^ { 2 } }$ related to the fact that it is its own Fourier transform.

Suppose $f ( z )$ is an entire function that satisfies

$$
| f (x + i y) | \leq c e ^ {- a x ^ {2} + b y ^ {2}}
$$

for some $a , b , c > 0$ . Let

$$
\hat {f} (\zeta) = \int_ {- \infty} ^ {\infty} f (x) e ^ {- 2 \pi i x \zeta} d x.
$$

Then, $\hat { f }$ is an entire function of ζ that satisfies

$$
| \hat {f} (\xi + i \eta) | \leq c ^ {\prime} e ^ {- a ^ {\prime} \xi^ {2} + b ^ {\prime} \eta^ {2}}
$$

for some $a ^ { \prime } , b ^ { \prime } , c ^ { \prime } > 0$

[Hint: To prove $\hat { f } ( \xi ) = O ( e ^ { - a ^ { \prime } \xi ^ { 2 } } )$ , assume $\xi > 0$ and change the contour of integration to $x - i y$ for some $y > 0$ fixed, and $- \infty < x < \infty$ . Then

$$
\hat {f} (\xi) = O (e ^ {- 2 \pi y \xi} e ^ {b y ^ {2}}).
$$

Finally, choose $y = d \xi$ where d is a small constant.]
:::

::: {.solution}
For real $x$, the hypothesis gives $|f(x)|\le c e^{-ax^2}$, so $f|_{\mathbb R}\in L^1(\mathbb R)$. For $\zeta=\xi+i\eta$,
\[
|f(x)e^{-2\pi i x\zeta}|\le c e^{-ax^2+2\pi |\eta||x|},
\]
and the right side is integrable. Uniform domination on compact subsets of the $\zeta$-plane therefore permits differentiation under the integral sign to all orders; hence $\widehat f$ is entire.

We first obtain Gaussian decay on the real axis. Fix real $\xi$. For any real $y$, Cauchy's theorem on the rectangle with vertices $\pm R$ and $\pm R-iy$, followed by $R\to\infty$, gives
\[
\widehat f(\xi)=\int_{-\infty}^{\infty}f(x-iy)e^{-2\pi i(x-iy)\xi}\,dx.
\tag{1}
\]
Indeed, on the vertical sides the factor $f(z)$ is bounded by
$c e^{-aR^2+by^2}$, while $|e^{-2\pi i z\xi}|$ is bounded there by a constant depending only on $y,\xi$, so those side integrals tend to $0$.

For $\xi>0$, choose $y=d\xi$ with $d>0$. From (1),
\[
|\widehat f(\xi)|
\le c e^{-2\pi d\xi^2+bd^2\xi^2}
\int_{-\infty}^{\infty}e^{-ax^2}\,dx.
\]
Choose $0<d<2\pi/b$. Then
\[
a':=2\pi d-bd^2>0,
\]
and therefore $|\widehat f(\xi)|\le C e^{-a'\xi^2}$. For $\xi<0$, shift upward by writing $y=d\xi$ in the same formula; the identical estimate results. Thus
\[
|\widehat f(\xi)|\le C e^{-a'\xi^2}\qquad(\xi\in\mathbb R).
\tag{2}
\]

Finally let $\zeta=\xi+i\eta$. Directly from the defining integral,
\[
|\widehat f(\xi+i\eta)|
\le c\int_{-\infty}^{\infty}e^{-ax^2+2\pi\eta x}\,dx
=C_0 e^{\pi^2\eta^2/a}.
\tag{3}
\]
To retain decay in $\xi$ simultaneously, repeat the contour shift above with $y=d\xi$. Then
\[
|e^{-2\pi i(x-iy)(\xi+i\eta)}|
=e^{2\pi\eta x-2\pi y\xi},
\]
so completing the square in $x$ gives
\[
|\widehat f(\xi+i\eta)|
\le C_0
\exp\!\left((-2\pi d+bd^2)\xi^2+\frac{\pi^2}{a}\eta^2\right).
\]
With the same choice of $d$ this is
\[
|\widehat f(\xi+i\eta)|\le c' e^{-a'\xi^2+b'\eta^2},
\qquad b'=\frac{\pi^2}{a}>0.
\]
This is the required estimate.
:::
