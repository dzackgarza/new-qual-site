---
schema: qual/card@1
id: P-3JE4U
kind: problem
title: $\int_0^\infty\frac{x^{a-1}}{1+x^n}\,dx=\frac{\pi}{n\sin(\pi a/n)}$ and $\int_0^\infty\frac{\log
  x}{(1+x^2)^2}\,dx=-\frac{\pi}{4}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Integrals
  - Complex Logarithm
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Compute the following integrals.

(i) $\displaystyle \int_0^\infty \frac{x^{a-1}}{1 + x^n} \, dx$, $0< a < n$

(ii) $\displaystyle \int_0^\infty \frac{\log x}{(1 + x^2)^2}\, dx$
:::

::: {.solution}

For (i), let $I\coloneqq\int_0^\infty \frac{x^{a-1}}{1+x^n}\,dx$ and $f(z)\coloneqq z^{a-1}/(1+z^n)$, with $z^{a-1}\coloneqq\abs{z}^{a-1}e^{i(a-1)\arg z}$ for $0\leq\arg z\leq 2\pi/n$.
For $0<\varepsilon<1<R$, let $\Gamma$ be the boundary of the sector $\theset{\varepsilon\leq\abs{z}\leq R,\ 0\leq\arg z\leq2\pi/n}$, oriented counterclockwise.

::: pf

::: {.pf-step #sector}
$I\qty(1-e^{2\pi i a/n})=2\pi i\Res_{z=e^{i\pi/n}}f$.

::: pf-proof
The only zero of $1+z^n$ inside $\Gamma$ is $z_0=e^{i\pi/n}$.
On the ray $z=xe^{2\pi i/n}$, $f(z)\,dz=e^{2\pi i(a-1)/n}e^{2\pi i/n}\frac{x^{a-1}}{1+x^n}\,dx$, and this ray is traversed inward, so it contributes $-e^{2\pi ia/n}\int_\varepsilon^R\frac{x^{a-1}}{1+x^n}\,dx$.
The arc of radius $\varepsilon$ contributes $O(\varepsilon^{a})\to0$ because $a>0$, and the arc of radius $R$ contributes $O(R^{a-n})\to0$ because $a<n$.
The residue theorem then gives the identity in the limit.
:::

:::

::: {.pf-step #residue}
$\Res_{z=z_0}f=-\frac1ne^{i\pi a/n}$.

::: pf-proof
The pole is simple, so the residue is $\frac{z_0^{a-1}}{nz_0^{n-1}}=\frac1nz_0^{a-n}=\frac1ne^{i\pi a/n}e^{-i\pi}$.
:::

:::

::: pf-step
(i) $I=\boxed{\dfrac{\pi}{n\sin(\pi a/n)}}$.

::: pf-proof
By steps [](#sector){.pf-ref} and [](#residue){.pf-ref},
$$
I=\frac{-2\pi i}{n}\cdot\frac{e^{i\pi a/n}}{1-e^{2\pi ia/n}}=\frac{2\pi i}{n}\cdot\frac{1}{e^{i\pi a/n}-e^{-i\pi a/n}}=\frac{2\pi i}{n}\cdot\frac1{2i\sin(\pi a/n)}.
$$
:::

:::

::: {.pf-step #inversion}
With $J\coloneqq\int_0^\infty \frac{\log x}{(1+x^2)^2}\,dx$, $2J=\int_0^\infty\log x\,\frac{1-x^2}{(1+x^2)^2}\,dx$.

::: pf-proof
The integral $J$ converges absolutely, since the integrand is $O(\abs{\log x})$ near $0$ and $O(x^{-4}\log x)$ at $\infty$.
The substitution $x=1/t$ gives $J=-\int_0^\infty\frac{t^2\log t}{(1+t^2)^2}\,dt$; add this to $J$.
:::

:::

::: pf-step
(ii) $J=\boxed{-\dfrac\pi4}$.

::: pf-proof
Since $\frac{d}{dx}\frac{x}{1+x^2}=\frac{1-x^2}{(1+x^2)^2}$, integration by parts in step [](#inversion){.pf-ref} gives
$$
2J=\qty[\frac{x\log x}{1+x^2}]_0^\infty-\int_0^\infty\frac{dx}{1+x^2}=0-\frac\pi2,
$$
because $x\log x\to0$ as $x\to0$ and $\frac{x\log x}{1+x^2}\to0$ as $x\to\infty$.
:::

:::

:::

:::
