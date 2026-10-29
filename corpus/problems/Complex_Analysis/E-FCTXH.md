---
schema: qual/card@1
id: E-FCTXH
kind: problem
title: $f(z)=-\frac12\bigl(z+\frac1z\bigr)$ maps the upper half-disk conformally onto
  the upper half-plane
classification:
  areas:
  - complex-analysis
  topics:
  - Conformal Maps
  - Geometry
relations: []
review: draft
---

::: {.problem}
Prove that $\displaystyle{f(z)=-\frac{1}{2}\left(z+\frac{1}{z}\right)}$ is a conformal map from the half disc
$$
\{z=x+iy:\ \abs{z}<1,\ y>0\}
$$
to $\HH \coloneqq \{z=x+iy:\ y>0\}$.
:::

::: {.solution}
Let $D^+\coloneqq\{z:\abs z<1,\ \Im z>0\}$.
For $0<R<1$ put $H_R\coloneqq-\frac12\qty(R+R^{-1})$ and $V_R\coloneqq\frac12\qty(R^{-1}-R)$, so that $H_R^2-V_R^2=1$, $\abs{H_R}>1$ and $V_R>0$.

::: pf

::: {.pf-step #local}
$f$ is holomorphic on $D^+$ with $f'\neq0$ there.

::: pf-proof
$f$ is holomorphic away from $0$, and $f'(z)=-\frac12\qty(1-z^{-2})$ vanishes only at $z=\pm1\notin D^+$.
:::

:::

::: {.pf-step #arcs}
For $0<R<1$, $f$ maps the arc $\{Re^{it}:0<t<\pi\}$ injectively onto the upper half of the ellipse $E_R$ with semi-axes $\abs{H_R}$ and $V_R$ and foci $\pm1$.

::: pf-proof
$f(Re^{it})=-\frac12\qty(Re^{it}+R^{-1}e^{-it})=H_R\cos t+iV_R\sin t$.
As $t$ runs through $(0,\pi)$, the real part $H_R\cos t$ is strictly monotone and the imaginary part is positive, so the image is the open upper half of $E_R$, traced once.
Its foci are $\pm\sqrt{H_R^2-V_R^2}=\pm1$.
:::

:::

::: {.pf-step #ellipses}
Each $w\in\HH$ lies on $E_R$ for exactly one $R\in(0,1)$.

::: pf-proof
A point $w\notin[-1,1]$ lies on the unique ellipse with foci $\pm1$ whose major semi-axis is $\frac12\qty(\abs{w-1}+\abs{w+1})>1$.
As $R$ decreases from $1$ to $0$, $\abs{H_R}=\frac12\qty(R+R^{-1})$ increases strictly from $1$ to $\infty$, so each such semi-axis is $\abs{H_R}$ for exactly one $R$.
:::

:::

::: pf-step
$f$ is a conformal map of $D^+$ onto $\HH$.

::: pf-proof
The arcs of step [](#arcs){.pf-ref} for $0<R<1$ partition $D^+$, so by steps [](#arcs){.pf-ref} and [](#ellipses){.pf-ref} $f$ maps $D^+$ bijectively onto $\HH$.
With step [](#local){.pf-ref}, $f$ is a biholomorphism.
:::

:::

:::

:::
