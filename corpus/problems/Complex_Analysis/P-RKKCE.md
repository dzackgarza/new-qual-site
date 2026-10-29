---
schema: qual/card@1
id: P-RKKCE
kind: problem
title: $\int_{-\infty}^{\infty}\frac{e^{-2\pi ix\xi}}{\cosh\pi x}\,dx$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Hyperbolic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Compute the Fourier transform integral:
$$I(\xi) = \int_{-\infty}^{\infty} \frac{e^{-2\pi i x \xi}}{\cosh(\pi x)} \, dx$$
where $\xi \in \RR$ and $\cosh z = \frac{e^z + e^{-z}}{2}$.
:::

::: {.solution}
Let
$$
F(z)=\frac{e^{-2\pi i\xi z}}{\cosh(\pi z)},
$$
and let $\Gamma_R$ be the positively oriented boundary of the rectangle with vertices $-R,R,R+i,-R+i$.

::: pf

::: {.pf-step #residue}

$\int_{\Gamma_R}F(z)\,dz=2e^{\pi\xi}$.

::: pf-proof

The zeros of $\cosh(\pi z)$ are $z=i(k+\frac12)$, $k\in\ZZ$, so the only pole inside $\Gamma_R$ is the simple pole $z=i/2$, where
$$
\Res_{z=i/2}F=\frac{e^{\pi\xi}}{\pi\sinh(i\pi/2)}=\frac{e^{\pi\xi}}{i\pi}.
$$
The residue theorem gives $2\pi i\cdot e^{\pi\xi}/(i\pi)=2e^{\pi\xi}$.

:::

:::

::: {.pf-step #top}

$\displaystyle\int_{R+i}^{-R+i}F(z)\,dz=e^{2\pi\xi}\int_{-R}^{R}\frac{e^{-2\pi i\xi x}}{\cosh(\pi x)}\,dx$.

::: pf-proof

We have $\cosh(\pi(x+i))=-\cosh(\pi x)$ and $e^{-2\pi i\xi(x+i)}=e^{2\pi\xi}e^{-2\pi i\xi x}$; the minus sign cancels against the reversed orientation.

:::

:::

::: {.pf-step #sides}

The integrals over the vertical sides tend to $0$ as $R\to\infty$.

::: pf-proof

For $z=\pm R+iy$ with $0\le y\le1$,
$$
\abs{e^{-2\pi i\xi z}}\le e^{2\pi\abs\xi},
\qquad
\abs{\cosh(\pi z)}\ge\sinh(\pi R),
$$
and each side has length $1$.

:::

:::

::: pf-step

$I(\xi)=\boxed{\dfrac1{\cosh(\pi\xi)}}$.

::: pf-proof

Letting $R\to\infty$ in steps [](#residue){.pf-ref}, [](#top){.pf-ref} and [](#sides){.pf-ref} gives $(1+e^{2\pi\xi})I(\xi)=2e^{\pi\xi}$, so
$$
I(\xi)=\frac{2e^{\pi\xi}}{1+e^{2\pi\xi}}=\frac1{\cosh(\pi\xi)}.
$$

:::

:::

:::

:::
