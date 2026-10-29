---
schema: qual/card@1
id: P-EH22O
kind: problem
title: Area of $f(\{\abs{z}<r\})$ is $\pi\sum_{n=1}^\infty n\abs{c_n}^2 r^{2n}$ for univalent
  $f(z)=\sum_{n=0}^\infty c_n z^n$
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
  - Conformal Maps
  - Integrals
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Let $f(z) = \sum_{n=0}^\infty c_n z^n$ be analytic and one-to-one in $\abs{z} < 1$.
For $0<r<1$, let $D_r$ be the disk $\abs{z}<r$.
Show that the area of $f(D_r)$ is finite and is given by $$S = \pi \sum_{n=1}^\infty n \abs{c_n}^2 r^{2n}.$$ (Note that in general the area of $f(D_1)$ is infinite.)
:::

::: {.solution}

::: pf

::: {.pf-step #area-integral}
$\operatorname{Area}(f(D_r))=\iint_{D_r}\abs{f'(z)}^2\,dA(z)$, and this is finite.

::: pf-proof
An injective holomorphic map has nonvanishing derivative, so $f$ is a $C^1$ diffeomorphism of $D_r$ onto its image, with real Jacobian determinant $\abs{f'}^2$ by the Cauchy--Riemann equations.
The change-of-variables formula gives the identity, and $\abs{f'}^2$ is bounded on the compact set $\overline{D_r}\subset\DD$.
:::

:::

::: {.pf-step #orthogonality}
For integers $n,m\ge0$, $\iint_{D_r}z^n\bar z^m\,dA=0$ if $n\ne m$, and $\iint_{D_r}\abs{z}^{2n}\,dA=\frac{\pi r^{2n+2}}{n+1}$.

::: pf-proof
In polar coordinates, $\iint_{D_r}z^n\bar z^m\,dA=\int_0^r\rho^{n+m+1}\,d\rho\int_0^{2\pi}e^{i(n-m)\theta}\,d\theta$.
:::

:::

::: pf-step
$\iint_{D_r}\abs{f'}^2\,dA=\pi\sum_{n=1}^\infty n\abs{c_n}^2r^{2n}$.

::: pf-proof
$f'(z)=\sum_{n\ge1}nc_nz^{n-1}$ converges absolutely and uniformly on $\overline{D_r}$, so the double series for $\abs{f'}^2=\sum_{n,m\ge1}nm\,c_n\bar c_m z^{n-1}\bar z^{m-1}$ may be integrated term by term.
By step [](#orthogonality){.pf-ref}, only $n=m$ survives, and the integral is $\sum_{n\ge1}n^2\abs{c_n}^2\frac{\pi r^{2n}}{n}$; step [](#area-integral){.pf-ref} gives the result.
:::

:::

:::

:::
