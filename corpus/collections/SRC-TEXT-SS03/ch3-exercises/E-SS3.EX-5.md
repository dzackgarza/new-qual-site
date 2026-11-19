---
schema: qual/card@1
id: E-SS3.EX-5
kind: problem
title: The Fourier transform of $(1+x^2)^{-2}$
classification:
  areas:
    - complex-analysis
  topics: [Fourier Transforms, Residue Theorem, Contour Integration]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Structured into Lamport steps from the card's own prose, with the residue recomputed from
      scratch: the derivative of e^{-2 pi i z xi}/(z-i)^2 at z = -i is [(-2 pi i xi)(z-i) - 2]
      e^{-2 pi i z xi}/(z-i)^3 there, with z-i = -2i, (z-i)^3 = 8i and e^{-2 pi i z xi} =
      e^{-2 pi xi}, giving (i/4)(1 + 2 pi xi) e^{-2 pi xi}, and -2 pi i times it is
      (pi/2)(1 + 2 pi xi) e^{-2 pi xi}; the card's arithmetic is correct. Added, absent from the
      prose: the modulus estimate pi R (R^2-1)^{-2} on the closing semicircle, which is what makes
      the contour integral tend to I(xi), and the substitution x -> -x that gives I(-xi) = I(xi)
      in place of a second residue computation at z = i. The case xi = 0 is evaluated directly
      (x = tan theta, integral pi/2), which agrees with the displayed formula. The statement is
      unchanged. No retained solution set covers the exercises of Stein-Shakarchi, so the card's
      solution states the argument is its own.
---

::: {.exercise}
Use contour integration to show that
$$
\int_{-\infty}^{\infty} \frac{e^{-2\pi i x\xi}}{(1+x^{2})^{2}}\,dx = \frac{\pi}{2}\bigl(1+2\pi\abs{\xi}\bigr)e^{-2\pi\abs{\xi}}
$$
for all real $\xi$.
:::

::: {.solution}
The statement is Exercise 5 of [@SS03, ch. 3 (p. 103)], printed as $\int_{-\infty}^{\infty}\frac{e^{-2\pi ix\xi}}{(1+x^2)^2}\,dx=\frac{\pi}{2}(1+2\pi\abs{\xi})e^{-2\pi\abs{\xi}}$ for real $\xi$.

Write $I(\xi)$ for the integral. For $\xi>0$ the exponential decays in the lower half-plane, so the contour is closed there and the enclosed singularity is the double pole at $z=-i$; for $\xi<0$ the substitution $x\mapsto-x$ gives $I(\xi)=I(-\xi)$ at once. The estimate on the closing arc, the residue, and the cases $\xi>0$ and $\xi=0$ are separated below. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi. The two tools used are the residue theorem (Theorem 4.1 of Chapter 3) and the standard extension of the residue theorem to a rational function times an exponential on a semicircle, which is the estimate in step [](#arc){.pf-ref}.

::: pf

::: {.pf-step #setup}
For $\xi>0$ and $z=x+iy$ in the closed lower half-plane, $\abs{e^{-2\pi iz\xi}}=e^{2\pi y\xi}\le1$, and on the semicircle $\abs z=R$ with $\Im z\le0$ the rest of the integrand is bounded by $(R^2-1)^{-2}$ for $R>1$.

::: pf-proof
$e^{-2\pi iz\xi}=e^{-2\pi ix\xi}e^{2\pi y\xi}$ because $-2\pi i(x+iy)\xi=-2\pi ix\xi+2\pi y\xi$; the first factor has modulus $1$ and the second is at most $1$ when $y\le0$ and $\xi>0$. Also $\abs{1+z^2}\ge \abs z^2-1=R^2-1$ on $\abs z=R$, so the squared denominator is at least $(R^2-1)^2$, and this is positive for $R>1$.
:::

:::


::: {.pf-step #arc}
The integral of $\dfrac{e^{-2\pi iz\xi}}{(1+z^2)^2}$ over the semicircle $\abs z=R$, $\Im z\le0$, tends to $0$ as $R\to\infty$. Hence for $\xi>0$
$$
I(\xi)=\lim_{R\to\infty}\oint_{\Gamma_R}\frac{e^{-2\pi iz\xi}}{(1+z^2)^2}\dz,
$$
where $\Gamma_R$ is the boundary of the half-disc $\abs z<R$, $\Im z<0$, traversed clockwise.

::: pf-proof
By step [](#setup){.pf-ref} the modulus of the integrand on that semicircle is at most $(R^2-1)^{-2}$, and the semicircle has length $\pi R$, so the modulus of the integral is at most $\pi R(R^2-1)^{-2}\to0$. The closed contour $\Gamma_R$ is the semicircle followed by the interval from $R$ to $-R$ along the real axis, and the integral over that interval tends to $\int_{-\infty}^{\infty}$ of the given integrand, which is absolutely convergent because $\abs{1+x^2}^{-2}\le\abs x^{-4}$ for large $\abs x$; so the contour integral over $\Gamma_R$ tends to $I(\xi)$.
:::

:::


::: {.pf-step #residue}
The integrand has a double pole at $z=-i$ and
$$
\operatorname{Res}_{z=-i}\frac{e^{-2\pi iz\xi}}{(1+z^2)^2}=\frac{i}{4}(1+2\pi\xi)e^{-2\pi\xi}\qquad(\xi>0).
$$

::: pf-proof
$1+z^2=(z-i)^2(z+i)^2$, so the residue at $z=-i$ is $\dfrac{d}{dz}\Bigl[\dfrac{e^{-2\pi iz\xi}}{(z-i)^2}\Bigr]$ at $z=-i$. The quotient rule gives
$$
\frac{d}{dz}\frac{e^{-2\pi iz\xi}}{(z-i)^2}=\frac{\bigl[(-2\pi i\xi)(z-i)-2\bigr]e^{-2\pi iz\xi}}{(z-i)^3}.
$$
At $z=-i$ one has $z-i=-2i$, $(z-i)^3=8i$, $e^{-2\pi iz\xi}=e^{-2\pi\xi}$, and $(-2\pi i\xi)(-2i)-2=-4\pi\xi-2$; hence the residue is $(-4\pi\xi-2)e^{-2\pi\xi}/(8i)$, and $1/(8i)=-i/8$, so it equals $(4\pi\xi+2)e^{-2\pi\xi}i/8=\frac{i}{4}(1+2\pi\xi)e^{-2\pi\xi}$.
:::

:::


::: {.pf-step #positive}
For $\xi>0$, $\displaystyle I(\xi)=\frac{\pi}{2}(1+2\pi\xi)e^{-2\pi\xi}$.

::: pf-proof
The contour $\Gamma_R$ of step [](#arc){.pf-ref} is traversed clockwise, so the residue theorem gives the contour integral as $-2\pi i$ times the sum of the residues at the poles inside it; for $R>1$ the only such pole is $z=-i$, since $z=i$ lies in the upper half-plane. Hence, by steps [](#arc){.pf-ref} and [](#residue){.pf-ref},
$$
I(\xi)=-2\pi i\cdot\frac{i}{4}(1+2\pi\xi)e^{-2\pi\xi}=\frac{\pi}{2}(1+2\pi\xi)e^{-2\pi\xi},
$$
using $-2\pi i\cdot i/4=2\pi/4=\pi/2$.
:::

:::


::: {.pf-step #negative}
For $\xi<0$, $\displaystyle I(\xi)=\frac{\pi}{2}(1-2\pi\xi)e^{2\pi\xi}=\frac{\pi}{2}(1+2\pi\abs\xi)e^{-2\pi\abs\xi}$.

::: pf-proof
In the integral defining $I(-\xi)$, substitute $x=-u$, $\dx=-\,du$, and flip the limits:
$$
I(-\xi)=\int_{-\infty}^{\infty}\frac{e^{2\pi iu\xi}}{(1+u^2)^2}\,du=\int_{-\infty}^{\infty}\frac{e^{-2\pi iu\xi}}{(1+u^2)^2}\,du=I(\xi),
$$
the middle integral being the complex conjugate of $I(\xi)$ because $(1+u^2)^{-2}$ is real. So $I$ is even, and for $\xi<0$ step [](#positive){.pf-ref} applied to $\abs\xi$ gives the first display; the second is its rewriting with $\abs\xi=-\xi$, using $1-2\pi\xi=1+2\pi\abs\xi$ and $2\pi\xi=-2\pi\abs\xi$.
:::

:::


::: {.pf-step #zero}
For $\xi=0$, $\displaystyle I(0)=\int_{-\infty}^{\infty}\frac{\dx}{(1+x^2)^2}=\frac{\pi}{2}$, which is the displayed formula at $\xi=0$.

::: pf-proof
Substituting $x=\tan\theta$, $\dx=\sec^2\theta\dtheta$ and $1+x^2=\sec^2\theta$ on $(-\pi/2,\pi/2)$,
$$
\int_{-\infty}^{\infty}\frac{\dx}{(1+x^2)^2}=\int_{-\pi/2}^{\pi/2}\cos^2\theta\dtheta=\frac{\pi}{2},
$$
since the mean value of $\cos^2$ over a period is $\frac12$. The right-hand side of the displayed formula at $\xi=0$ is $\frac{\pi}{2}(1+0)\cdot1=\frac{\pi}{2}$.
:::

:::


::: {.pf-step #conclusion}
For every real $\xi$, $\displaystyle I(\xi)=\frac{\pi}{2}\bigl(1+2\pi\abs\xi\bigr)e^{-2\pi\abs\xi}$.

::: pf-proof
The three cases $\xi>0$, $\xi<0$ and $\xi=0$ are exhaustive and are settled by steps [](#positive){.pf-ref}, [](#negative){.pf-ref} and [](#zero){.pf-ref}; the three values agree with the single expression $\frac{\pi}{2}(1+2\pi\abs\xi)e^{-2\pi\abs\xi}$, which is what the statement asserts.
:::

:::

:::
:::
