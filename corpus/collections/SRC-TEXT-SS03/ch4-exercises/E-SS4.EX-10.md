---
schema: qual/card@1
id: E-SS4.EX-10
kind: problem
title: Gaussian decay in a strip passes to the Fourier transform
classification:
  areas:
  - complex-analysis
  topics:
  - Fourier Transform
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card carried two solution blocks: the answer, and a separate block holding only the provenance
    note that no retained solution set covers the exercise. Both rendered as solutions. The note was
    moved to the head of the single solution block; its wording and the answer were not changed.

---

::: {.exercise}
This exercise generalizes some of the properties of $e^{-\pi x^2}$ related to the fact that it is its own Fourier transform.

Suppose $f(z)$ is an entire function that satisfies
$$
\abs{f(x + iy)} \leq c e^{-ax^2 + by^2}
$$
for some $a, b, c > 0$. Let
$$
\hat{f}(\zeta) = \int_{-\infty}^{\infty} f(x) e^{-2\pi i x\zeta}\, dx.
$$
Then, $\hat{f}$ is an entire function of $\zeta$ that satisfies
$$
\abs{\hat{f}(\xi + i\eta)} \leq c' e^{-a'\xi^2 + b'\eta^2}
$$
for some $a', b', c' > 0$.

[Hint: To prove $\hat{f}(\xi) = O(e^{-a'\xi^2})$, assume $\xi > 0$ and change the contour of integration to $x - iy$ for some $y > 0$ fixed, and $-\infty < x < \infty$. Then
$$
\hat{f}(\xi) = O(e^{-2\pi y\xi} e^{by^2}).
$$
Finally, choose $y = d\xi$ where $d$ is a small constant.]
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. The hypothesis is $\abs{f(x+iy)}\le ce^{-ax^2+by^2}$ with $a,b,c>0$, and the claim is that
$$
\abs{\widehat f(\xi+i\eta)}\le c'e^{-a'\xi^2+b'\eta^2}
$$
for some $a',b',c'>0$. Throughout $f$ is applied at points of the form $z=x-iy$, where $\abs{f(x-iy)}\le ce^{-ax^2+by^2}$ by the hypothesis applied to $\abs{\operatorname{Im}z}=y$.

::: pf

::: {.pf-step #entire}
$\widehat f(\zeta)=\int_{\RR}f(x)e^{-2\pi ix\zeta}dx$ is entire.

::: pf-proof
For real $x$ the hypothesis gives $\abs{f(x)}\le ce^{-ax^2}$, so $f$ is integrable on $\RR$. For $\zeta=\xi+i\eta$ one has $\abs{f(x)e^{-2\pi ix\zeta}}\le ce^{-ax^2+2\pi\abs{\eta}\abs{x}}$, which is integrable in $x$ and depends on $\eta$ only through its modulus. Hence on compact subsets of the $\zeta$-plane the integrand is dominated by an integrable function independent of $\zeta$, and differentiation under the integral sign to all orders is justified; so $\widehat f$ is entire and its derivatives are given by the differentiated integrals.
:::

:::

::: {.pf-step #shift}
For real $\xi$ and real $y$,
$$
\widehat f(\xi)=\int_{\RR}f(x-iy)e^{-2\pi i(x-iy)\xi}dx .
\tag{1}
$$

::: pf-proof
Integrate the entire function $z\mapsto f(z)e^{-2\pi iz\xi}$ around the rectangle with vertices $\pm R$ and $\pm R-iy$; the integral is $0$ by Cauchy's theorem. The horizontal sides are the segment $[-R,R]$ and the segment $[-R-iy,R-iy]$ traversed backwards, giving the difference of the two integrals appearing in (1). On the vertical sides $z=\pm R+is$ with $-y\le s\le0$, the bound $\abs{f(z)}\le ce^{-aR^2+bs^2}$ holds and $\abs{e^{-2\pi iz\xi}}\le e^{2\pi\abs{s}\abs{\xi}}$ is bounded independently of $R$, so those two integrals are $O(Re^{-aR^2})\to0$; the side lengths being $\abs{y}$ and the bounds depending only on $y,\xi$. Letting $R\to\infty$ gives (1).
:::

:::

::: {.pf-step #real}
There are $a'>0$ and $C$ with $\abs{\widehat f(\xi)}\le Ce^{-a'\xi^2}$ for all real $\xi$.

::: pf-proof
By (1) with $y=d\xi$, where $d>0$ is to be chosen, and the bound on $f$,
$$
\abs{\widehat f(\xi)}\le\int_{\RR}ce^{-ax^2+bd^2\xi^2}\abs{e^{-2\pi i(x-iy)\xi}}dx=ce^{bd^2\xi^2-2\pi d\xi^2}\int_{\RR}e^{-ax^2}dx,
$$
since $\abs{e^{-2\pi i(x-iy)\xi}}=e^{-2\pi y\xi}$ for real $\xi$ and $y=d\xi$ gives $-2\pi y\xi=-2\pi d\xi^2$. Choose $0<d<2\pi/b$, possible because $b>0$, and set $a'=2\pi d-bd^2>0$; then the exponent is $-a'\xi^2$ and the claim follows with $C=c\sqrt{\pi/a}$. The same computation applies to $\xi<0$ because $y=d\xi$ is then negative and $-2\pi y\xi=-2\pi d\xi^2<0$ still holds.
:::

:::

::: {.pf-step #eta}
$\abs{\widehat f(\xi+i\eta)}\le C_0e^{\pi^2\eta^2/a}$ for all $\zeta=\xi+i\eta$, with $C_0>0$ a constant.

::: pf-proof
Directly from the defining integral, $\abs{\widehat f(\zeta)}\le c\int_{\RR}e^{-ax^2+2\pi\eta x}dx$, since $\abs{e^{-2\pi ix\zeta}}=e^{2\pi\eta x}$. Completing the square, $-ax^2+2\pi\eta x=-a\bigl(x-\frac{\pi\eta}{a}\bigr)^2+\frac{\pi^2\eta^2}{a}$, so the integral equals $e^{\pi^2\eta^2/a}\sqrt{\pi/a}$ and the display holds with $C_0=c\sqrt{\pi/a}$.
:::

:::

::: {.pf-step #both}
$\abs{\widehat f(\xi+i\eta)}\le c'e^{-a'\xi^2+b'\eta^2}$ with $a'>0$ and $b'=\pi^2/a>0$.

::: pf-proof
Apply the shift (1) with $y=d\xi$ for complex $\zeta=\xi+i\eta$. Then
$$
\abs{e^{-2\pi i(x-iy)(\xi+i\eta)}}=e^{2\pi\eta x-2\pi y\xi},
$$
so the integrand is bounded by $ce^{-ax^2+bd^2\xi^2+2\pi\eta x-2\pi d\xi^2}$, and completing the square in $x$ gives
$$
\abs{\widehat f(\xi+i\eta)}\le C_0\exp\Bigl((-2\pi d+bd^2)\xi^2+\frac{\pi^2}{a}\eta^2\Bigr).
$$
With the same $d$ as in step [](#real){.pf-ref} the coefficient $-2\pi d+bd^2=-a'$ is negative, so the display holds with $b'=\pi^2/a$ and $c'=C_0$.
:::

:::

::: {.pf-step}
$\widehat f$ is entire and satisfies a Gaussian bound in both variables, which is the assertion of the exercise.

::: pf-proof
Step [](#entire){.pf-ref} gives that $\widehat f$ is entire, and step [](#both){.pf-ref} gives the bound $\abs{\widehat f(\xi+i\eta)}\le c'e^{-a'\xi^2+b'\eta^2}$ with $a',b',c'>0$, which is the estimate the exercise asks for. Note that the two constants come from different mechanisms: $a'$ from the contour shift, $b'=\pi^2/a$ from the width of the Gaussian bound on $f$.
:::

:::

:::

For real $x$, the hypothesis gives $\abs{f(x)}\le c e^{-ax^2}$, so $f\restrict_{\RR}\in L^1(\RR)$. For $\zeta=\xi+i\eta$,
$$
\abs{f(x)e^{-2\pi i x\zeta}}\le c e^{-ax^2+2\pi \abs{\eta}\abs{x}},
$$
and the right side is integrable. Uniform domination on compact subsets of the $\zeta$-plane therefore permits differentiation under the integral sign to all orders; hence $\widehat f$ is entire.

We first obtain Gaussian decay on the real axis. Fix real $\xi$. For any real $y$, Cauchy's theorem on the rectangle with vertices $\pm R$ and $\pm R-iy$, followed by $R\to\infty$, gives
$$
\widehat f(\xi)=\int_{-\infty}^{\infty}f(x-iy)e^{-2\pi i(x-iy)\xi}\,dx.
\tag{1}
$$
Indeed, on the vertical sides the factor $f(z)$ is bounded by
$c e^{-aR^2+by^2}$, while $\abs{e^{-2\pi i z\xi}}$ is bounded there by a constant depending only on $y,\xi$, so those side integrals tend to $0$.

For $\xi>0$, choose $y=d\xi$ with $d>0$. From (1),
$$
\abs{\widehat f(\xi)}
\le c e^{-2\pi d\xi^2+bd^2\xi^2}
\int_{-\infty}^{\infty}e^{-ax^2}\,dx.
$$
Choose $0<d<2\pi/b$. Then
$$
a':=2\pi d-bd^2>0,
$$
and therefore $\abs{\widehat f(\xi)}\le C e^{-a'\xi^2}$. For $\xi<0$, shift upward by writing $y=d\xi$ in the same formula; the identical estimate results. Thus
$$
\abs{\widehat f(\xi)}\le C e^{-a'\xi^2}\qquad(\xi\in\RR).
\tag{2}
$$

Finally let $\zeta=\xi+i\eta$. Directly from the defining integral,
$$
\abs{\widehat f(\xi+i\eta)}
\le c\int_{-\infty}^{\infty}e^{-ax^2+2\pi\eta x}\,dx
=C_0 e^{\pi^2\eta^2/a}.
\tag{3}
$$
To retain decay in $\xi$ simultaneously, repeat the contour shift above with $y=d\xi$. Then
$$
\abs{e^{-2\pi i(x-iy)(\xi+i\eta)}}
=e^{2\pi\eta x-2\pi y\xi},
$$
so completing the square in $x$ gives
$$
\abs{\widehat f(\xi+i\eta)}
\le C_0
\exp\!\left((-2\pi d+bd^2)\xi^2+\frac{\pi^2}{a}\eta^2\right).
$$
With the same choice of $d$ this is
$$
\abs{\widehat f(\xi+i\eta)}\le c' e^{-a'\xi^2+b'\eta^2},
\qquad b'=\frac{\pi^2}{a}>0.
$$
This is the required estimate.
:::

