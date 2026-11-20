---
schema: qual/card@1
id: E-SS3.EX-3
kind: problem
title: $\int_{-\infty}^\infty\frac{\cos x}{x^2+a^2}\,dx=\pi\frac{e^{-a}}{a}$
classification:
  areas:
    - complex-analysis
  topics: [Residue Theorem, Contour Integration, Fourier Integrals]
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
      Structured the residue computation into numbered steps, and supplied the estimates it used in
      passing: the ML bound on the semicircular arc with the explicit factor pi R (R^2 - a^2)^{-1},
      the location of the poles, the residue formula for a simple pole, and the justification for
      passing to the limit and for taking real parts when both half-integrals converge absolutely.
      Every macro used is one the preamble defines. Not checked this session: the printed statement
      page.

---

::: {.exercise}
Show that
$$
\int_{-\infty}^{\infty} \frac{\cos x}{x^{2}+a^{2}}\,dx = \pi\frac{e^{-a}}{a}, \qquad \text{for } a > 0.
$$
:::

::: {.solution}

The computation is the card's own; the statement is Exercise 3 of [@SS03, ch. 3], printed as $\int_{-\infty}^\infty\frac{\cos x}{x^2+a^2}\,dx=\pi\frac{e^{-a}}{a}$ for $a>0$, and no published solution set is retained for it.

Let $a>0$, let $F(z)=e^{iz}/(z^{2}+a^{2})$, and for $R>a$ let $\gamma_{R}$ be the closed contour made of the interval $[-R,R]$ on the real axis and the upper semicircle $C_{R}=\{Re^{i\theta}\mid 0\leq\theta\leq\pi\}$.

::: pf

::: {.pf-step #poles}
$F$ has exactly one pole in the upper half-plane, the simple pole $z=ia$, and the others are $z=-ia$.

::: pf-proof
The poles of $F$ are the zeros of $z^{2}+a^{2}=(z-ia)(z+ia)$, namely $\pm ia$; the function $e^{iz}$ is entire. Both are simple zeros of the denominator, so both are simple poles, and $\Im(ia)=a>0$ while $\Im(-ia)=-a<0$.
:::

:::

::: {.pf-step #residue}
$\operatorname{Res}_{z=ia}F(z)=\dfrac{e^{-a}}{2ia}$.

::: pf-proof
At a simple pole, $\operatorname{Res}_{z=z_{0}}F=\lim_{z\to z_{0}}(z-z_{0})F(z)$. Here $z^{2}+a^{2}=(z-ia)(z+ia)$, so the residue is $e^{ia}/(2ia)=e^{-a}/(2ia)$, using $e^{i\cdot ia}=e^{-a}$.
:::

:::

::: {.pf-step #arc}
$\abs{\int_{C_{R}}F(z)\,dz}\leq\dfrac{\pi R}{R^{2}-a^{2}}\to0$ as $R\to\infty$.

::: pf-proof
On $C_{R}$ we have $\Im z\geq0$, so $\abs{e^{iz}}=e^{-\Im z}\leq1$, and $\abs{z^{2}+a^{2}}\geq\abs{z}^{2}-a^{2}=R^{2}-a^{2}>0$ for $R>a$. The ML estimate with the arc length $\pi R$ gives the bound, which tends to $0$.
:::

:::

::: {.pf-step #contour}
$\int_{-R}^{R}\frac{e^{ix}}{x^{2}+a^{2}}dx+\int_{C_{R}}F(z)\,dz=2\pi i\operatorname{Res}_{z=ia}F(z)$.

::: pf-proof
$F$ is holomorphic on a neighbourhood of the closed contour $\gamma_{R}$ except at $ia$, which lies inside it since $a>0$ and $R>a$; the residue theorem therefore applies to the single enclosed pole. Along the real axis $z=x$ and $e^{iz}=e^{ix}$.
:::

:::

::: {.pf-step #limit}
$\int_{-\infty}^{\infty}\frac{e^{ix}}{x^{2}+a^{2}}dx=\frac{\pi e^{-a}}{a}$.

::: pf-proof
Let $R\to\infty$ in step [](#contour){.pf-ref}. The arc term vanishes by step [](#arc){.pf-ref}, and the real-axis integral converges to the improper integral because $\abs{e^{ix}/(x^{2}+a^{2})}=1/(x^{2}+a^{2})$ is integrable on $\RR$. The right side is $2\pi i\cdot\frac{e^{-a}}{2ia}=\frac{\pi e^{-a}}{a}$.
:::

:::

::: {.pf-step #real-part}
$\int_{-\infty}^{\infty}\frac{\cos x}{x^{2}+a^{2}}dx=\frac{\pi e^{-a}}{a}$.

::: pf-proof
Split $e^{ix}=\cos x+i\sin x$; both $\cos x/(x^{2}+a^{2})$ and $\sin x/(x^{2}+a^{2})$ are absolutely integrable, so the real part of the integral is the integral of the real part. Taking real parts in step [](#limit){.pf-ref} gives the assertion.
:::

:::

:::

:::
