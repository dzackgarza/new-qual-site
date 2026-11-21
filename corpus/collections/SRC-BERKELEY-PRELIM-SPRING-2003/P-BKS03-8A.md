---
schema: qual/card@1
id: P-BKS03-8A
kind: problem
title: Integral of $e^{-x^2}\cos(x^2)$ over $(0,\infty)$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps for issue #2: the integrand written as a Gaussian of argument
    $e^{i\pi/8}z$, the wedge contour with the vanishing arc, the two boundary integrals evaluated, and the
    real part taken. No retained solution set covers this exercise, so the argument is the card's own; the
    arc estimate and the final value were recomputed for this pass.
---

::: {.problem}
Evaluate
$$
\int_0^{\infty}e^{-x^2}\cos(x^2)\,dx.
$$
:::

::: {.solution}
No retained solution set covers this exercise; the argument is the card's own, and the final value was checked numerically for this pass. The integral to be evaluated is the real part of $I=\int_{0}^{\infty}e^{-(1+i)x^{2}}\,dx$, since $e^{-(1+i)x^{2}}=e^{-x^{2}}\bigl(\cos x^{2}-i\sin x^{2}\bigr)$.

::: pf

::: {.pf-step #rewrite}
$e^{-(1+i)z^{2}}=e^{-\sqrt2\,(e^{i\pi/8}z)^{2}}$ for every $z\in\CC$.

::: pf-proof
$1+i=\sqrt2\,e^{i\pi/4}$, so $(1+i)z^{2}=\sqrt2\,e^{i\pi/4}z^{2}$; and $e^{i\pi/4}z^{2}=(e^{i\pi/8}z)^{2}$ because $e^{2i\pi/8}=e^{i\pi/4}$. Hence the two exponentials agree.
:::

:::

::: {.pf-step #wedge}
For $R>0$ the integral of $e^{-\sqrt2z^{2}}$ around the closed contour $C_{R}$ consisting of the segment $[0,R]$, the arc $\gamma_{R}(t)=Re^{it}$ for $0\le t\le\pi/8$, and the segment from $e^{i\pi/8}R$ back to $0$, is zero.

::: pf-proof
The integrand $e^{-\sqrt2z^{2}}$ is entire, and $C_{R}$ is a closed piecewise smooth curve, so Cauchy's theorem gives $\int_{C_{R}}e^{-\sqrt2z^{2}}dz=0$.
:::

:::

::: {.pf-step #arc}
$\int_{\gamma_{R}}e^{-\sqrt2z^{2}}dz\to0$ as $R\to\infty$.

::: pf-proof
On the arc $z=Re^{it}$ with $0\le t\le\pi/8$, one has $-\sqrt2z^{2}=-\sqrt2R^{2}e^{2it}$, whose real part is $-\sqrt2R^{2}\cos 2t\le-\sqrt2R^{2}\cos(\pi/4)=-R^{2}$, because $\cos2t\ge\cos(\pi/4)$ on that range. Hence $\abs{e^{-\sqrt2z^{2}}}\le e^{-R^{2}}$ on the arc, and the length of the arc is $(\pi/8)R$; so the modulus of the integral is at most $(\pi/8)Re^{-R^{2}}$, which tends to $0$.
:::

:::

::: {.pf-step #limits}
Letting $R\to\infty$ in the three pieces gives $2^{-1/4}\frac{\sqrt\pi}{2}=e^{i\pi/8}I$.

::: pf-proof
The first piece tends to $\int_{0}^{\infty}e^{-\sqrt2x^{2}}dx$, and the substitution $u=2^{1/4}x$ turns it into $2^{-1/4}\int_{0}^{\infty}e^{-u^{2}}du=2^{-1/4}\frac{\sqrt\pi}{2}$. The third piece is $-\int_{0}^{R}e^{-\sqrt2(e^{i\pi/8}x)^{2}}e^{i\pi/8}dx=-e^{i\pi/8}\int_{0}^{R}e^{-(1+i)x^{2}}dx$ by step [](#rewrite){.pf-ref}, tending to $-e^{i\pi/8}I$. With step [](#wedge){.pf-ref} and step [](#arc){.pf-ref} the total is zero in the limit, so the first and third pieces are equal: $2^{-1/4}\frac{\sqrt\pi}{2}=e^{i\pi/8}I$.
:::

:::

::: {.pf-step}
$\int_{0}^{\infty}e^{-x^{2}}\cos(x^{2})\,dx=2^{-5/4}\sqrt\pi\cos\frac{\pi}{8}$.

::: pf-proof
From step [](#limits){.pf-ref}, $I=2^{-1/4}e^{-i\pi/8}\frac{\sqrt\pi}{2}$, and its real part is $2^{-1/4}\frac{\sqrt\pi}{2}\cos\frac{\pi}{8}=2^{-5/4}\sqrt\pi\cos\frac{\pi}{8}$, since multiplying by $e^{-i\pi/8}$ multiplies the modulus by $1$ and shifts the argument by $-\pi/8$. That real part is the integral asked for, as noted at the outset.
:::

:::

:::
:::
