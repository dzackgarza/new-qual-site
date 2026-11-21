---
schema: qual/card@1
id: E-SS6.EX-10
kind: problem
title: Mellin transforms of $\cos t$ and $\sin t$
classification:
  areas:
  - complex-analysis
  topics:
  - Mellin Transform
  - Gamma Function
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
    Lamport structure over the prose that was already there. The contour rotation is now a
    step with the two arc estimates written out (the large arc by R^(sigma-1), the small one
    by eps^sigma, using 0 < Re z < 1), the conversion of the two exponential integrals into
    the cosine and sine integrals names the convergence that makes linearity legal (the
    modulus t^(sigma-1) is integrable at 0 and Dirichlet applies at infinity), and the strip
    extension is split into the holomorphy of the integral, the cancellation of the pole of
    Gamma at 0, and the identity theorem on a connected domain. The two numerical values are
    then evaluations of the continued function. Not checked: the book's own text of the
    exercise, since no copy of Stein and Shakarchi is retained in this checkout; the
    statement is as transcribed on the card. No retained solution set covers the exercise
    (the collection's provenance is a Google Books record), so the argument is the card's
    own. No statement repair.
---

::: {.exercise}
An integral of the form
$$
F(z) = \int_0^{\infty} f(t)\, t^{z-1}\, dt
$$
is called a Mellin transform, and we shall write $\mathcal{M}(f)(z) = F(z)$. For example, the gamma function is the Mellin transform of the function $e^{-t}$.

(a) Prove that
$$
\mathcal{M}(\cos)(z) = \int_0^{\infty} \cos(t)\, t^{z-1}\, dt = \Gamma(z) \cos\left( \pi\frac{z}{2} \right) \quad \text{for } 0 < \Re(z) < 1,
$$
and
$$
\mathcal{M}(\sin)(z) = \int_0^{\infty} \sin(t)\, t^{z-1}\, dt = \Gamma(z) \sin\left( \pi\frac{z}{2} \right) \quad \text{for } 0 < \Re(z) < 1.
$$

(b) Show that the second of the above identities is valid in the larger strip $-1 < \Re(z) < 1$, and that as a consequence, one has
$$
\int_0^{\infty} \frac{\sin x}{x}\, dx = \frac{\pi}{2} \quad \text{and} \quad \int_0^{\infty} \frac{\sin x}{x^{3/2}}\, dx = \sqrt{2\pi}.
$$
This generalizes the calculation in Exercise 2 of Chapter 2.

[Hint: For the first part, consider the integral of the function $f(w) = e^{-w} w^{z-1}$ around the contour illustrated in Figure 1. Use analytic continuation to prove the second part.]

Figure 1. The contour in Exercise 10
:::

::: {.solution}
No retained solution set covers this exercise: the collection's provenance is a Google Books record, so the argument is the card's own. Throughout, $w^z$ is taken on the principal branch, so that $(iu)^z=u^ze^{i\pi z/2}$ for $u>0$, and $\Gamma(z)=\int_0^\infty e^{-t}t^{z-1}dt$ for $\operatorname{Re}z>0$.

::: pf

::: {.pf-step #rotate}
For $0<\operatorname{Re}z<1$,
$$
\int_0^{\infty}e^{iu}u^{z-1}\,du=e^{i\pi z/2}\Gamma(z).
$$

::: pf-proof
Let $f(w)=e^{-w}w^{z-1}$, holomorphic on the sector $\{w:-\pi/2\le\arg w\le0,\ \varepsilon\le\abs{w}\le R\}$, whose boundary consists of the segment $[\varepsilon,R]$ of the real axis, the arc $\abs{w}=R$, the segment of the ray $\arg w=-\pi/2$ from $-iR$ to $-i\varepsilon$, and the arc $\abs{w}=\varepsilon$. By Cauchy's theorem the four boundary integrals sum to $0$. On the outer arc $\abs{e^{-w}}\le1$ because $\operatorname{Re}w\ge0$ there, and $\abs{w^{z-1}}\le R^{\sigma-1}e^{\abs{\tau}\pi/2}$ with $z=\sigma+i\tau$, so that integral is $O(R^{\sigma})\to0$ since $\sigma<1$. On the inner arc the same estimate gives $O(\varepsilon^{\sigma})\to0$ since $\sigma>0$. Hence the real-axis piece and the ray piece cancel in the limit, that is $\Gamma(z)$ plus the ray integral equals $0$. Parametrize the ray by $w=-iu$ with $u$ running from $R$ down to $\varepsilon$ along the boundary: $dw=-i\,du$ and $w^{z-1}=u^{z-1}e^{-i\pi(z-1)/2}$, since $-iu$ has argument $-\pi/2$ and the principal branch is in force. So the ray contribution is
$$
\int_R^\varepsilon e^{iu}u^{z-1}e^{-i\pi(z-1)/2}(-i)\,du=i\,e^{-i\pi(z-1)/2}\int_\varepsilon^R e^{iu}u^{z-1}\,du,
$$
and $i\,e^{-i\pi(z-1)/2}=i\,e^{-i\pi z/2}e^{i\pi/2}=i\cdot i\cdot e^{-i\pi z/2}=-e^{-i\pi z/2}$. Letting $\varepsilon\to0$ and $R\to\infty$ in the Cauchy identity gives $\Gamma(z)-e^{-i\pi z/2}\int_0^\infty e^{iu}u^{z-1}du=0$, and dividing by $e^{-i\pi z/2}\ne0$ gives the claim, since $e^{i\pi z/2}$ is the reciprocal of $e^{-i\pi z/2}$.
:::

:::

::: {.pf-step #conjugate}
For $0<\operatorname{Re}z<1$,
$$
\int_0^{\infty}e^{-iu}u^{z-1}\,du=e^{-i\pi z/2}\Gamma(z).
$$

::: pf-proof
Apply step [](#rotate){.pf-ref} to the conjugate exponent, or repeat the rotation with the sector above the real axis ($\arg w\in[0,\pi/2]$), where the same two arc estimates hold for the same reason; the parametrization $w=iu$ produces $(iu)^{z-1}i\,du=e^{i\pi(z-1)/2}iu^{z-1}du=e^{i\pi z/2}u^{z-1}du$, so $\Gamma(z)=e^{i\pi z/2}\int_0^\infty e^{-iu}u^{z-1}du$ and the claim follows by division.
:::

:::

::: {.pf-step #convergence}
For $0<\sigma=\operatorname{Re}z<1$, both improper integrals $\int_0^\infty e^{\pm iu}u^{z-1}du$ converge, and so does $\int_0^\infty\cos u\,u^{z-1}du$ and $\int_0^\infty\sin u\,u^{z-1}du$.

::: pf-proof
At $0$ the modulus is $u^{\sigma-1}$, integrable exactly when $\sigma>0$. At infinity $u^{z-1}=u^{\sigma-1}e^{i\tau\log u}$ has modulus $u^{\sigma-1}$, which decreases to $0$ and is eventually monotone because $\sigma<1$, while $e^{\pm iu}$ and $\cos u$, $\sin u$ have bounded primitives; Dirichlet's test gives convergence of each of the four improper integrals. Since a linear combination of two convergent improper integrals converges to the corresponding combination, the cosine and sine integrals converge as well.
:::

:::

::: {.pf-step #cos}
(a) $\mathcal M(\cos)(z)=\Gamma(z)\cos\dfrac{\pi z}{2}$ for $0<\operatorname{Re}z<1$.

::: pf-proof
By $\cos u=(e^{iu}+e^{-iu})/2$ and step [](#convergence){.pf-ref},
$$
\int_0^\infty\cos u\,u^{z-1}du=\tfrac12\Bigl(e^{i\pi z/2}\Gamma(z)+e^{-i\pi z/2}\Gamma(z)\Bigr)=\Gamma(z)\cos\frac{\pi z}{2},
$$
by steps [](#rotate){.pf-ref} and [](#conjugate){.pf-ref} and $\cos\theta=(e^{i\theta}+e^{-i\theta})/2$.
:::

:::

::: {.pf-step #sin}
(a) $\mathcal M(\sin)(z)=\Gamma(z)\sin\dfrac{\pi z}{2}$ for $0<\operatorname{Re}z<1$.

::: pf-proof
By $\sin u=(e^{iu}-e^{-iu})/(2i)$ and step [](#convergence){.pf-ref},
$$
\int_0^\infty\sin u\,u^{z-1}du=\frac{1}{2i}\Bigl(e^{i\pi z/2}\Gamma(z)-e^{-i\pi z/2}\Gamma(z)\Bigr)=\Gamma(z)\sin\frac{\pi z}{2},
$$
using $\sin\theta=(e^{i\theta}-e^{-i\theta})/(2i)$.
:::

:::

::: {.pf-step #holomorphy}
(b) $S(z)=\int_0^\infty\sin u\,u^{z-1}du$ is holomorphic on the strip $-1<\operatorname{Re}z<1$.

::: pf-proof
At $0$ use $\abs{\sin u}\le u$: the integrand is $O(u^{\sigma})$ with $\sigma>-1$, so the integral converges and is holomorphic in $z$ on compact subsets of that half-plane by dominated convergence, the integrand being holomorphic in $z$ and bounded by an integrable function of $u$ once $\sigma$ ranges over a compact set. At infinity integrate by parts: for $R>0$,
$$
\int_R^\infty\sin u\,u^{z-1}du=\bigl[-\cos u\,u^{z-1}\bigr]_R^\infty+(z-1)\int_R^\infty\cos u\,u^{z-2}du,
$$
which converges as $R\to\infty$ for $\sigma<1$ and is locally uniform in $z$, since the boundary term is $O(R^{\sigma-1})$ and the remaining integral converges absolutely for $\sigma<2$. Splitting the integral at $1$ gives holomorphy on the strip.
:::

:::

::: {.pf-step #extend}
(b) $S(z)=\Gamma(z)\sin\dfrac{\pi z}{2}$ holds on $-1<\operatorname{Re}z<1$.

::: pf-proof
The function $\Gamma$ is meromorphic with its only pole in the closed strip $\abs{\operatorname{Re}z}\le1$ at $z=0$, of order one, and $\sin(\pi z/2)$ has a simple zero at $z=0$; hence $\Gamma(z)\sin(\pi z/2)$ extends holomorphically across $0$ and is holomorphic on the strip. It agrees with $S$ on the nonempty open set $0<\operatorname{Re}z<1$ by step [](#sin){.pf-ref}, and the strip is connected, so the identity theorem gives equality throughout the strip.
:::

:::

::: {.pf-step #values}
(b) $\displaystyle\int_0^\infty\frac{\sin x}{x}dx=\frac{\pi}{2}$ and $\displaystyle\int_0^\infty\frac{\sin x}{x^{3/2}}dx=\sqrt{2\pi}$.

::: pf-proof
The first integral is $S(0)$, and by step [](#extend){.pf-ref} it equals $\lim_{z\to0}\Gamma(z)\sin(\pi z/2)$. Since $\Gamma$ has residue $1$ at $0$, $\Gamma(z)=\frac1z+O(1)$ there, while $\sin(\pi z/2)=\frac{\pi z}{2}+O(z^3)$, so the product tends to $\frac{\pi}{2}$ and $S$ is continuous at $0$. The second is $S(-1/2)=\Gamma(-1/2)\sin(-\pi/4)$; with $\Gamma(-1/2)=-2\sqrt\pi$ and $\sin(-\pi/4)=-\frac{\sqrt2}{2}$ this is $(-2\sqrt\pi)\bigl(-\frac{\sqrt2}{2}\bigr)=\sqrt{2\pi}$.
:::

:::

:::

:::
