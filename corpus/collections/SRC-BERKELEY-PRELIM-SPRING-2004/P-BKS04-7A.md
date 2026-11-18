---
schema: qual/card@1
id: P-BKS04-7A
kind: problem
title: The Dirichlet integral $\int_0^\infty\sin x/x\,dx$
classification:
  areas: [prelim]
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Evaluate $\int_0^\infty\frac{\sin x}{x}\,dx$.
:::

::: {.solution}

The argument is the card's own: integrate $e^{iz}/z$ over the boundary of a large half-disc indented at the origin, bound the three auxiliary pieces, and let the radius and the indentation go to their limits.

::: pf

::: {.pf-step #contour}

For $R>1$ let $\gamma$ be the closed contour running along the real axis from $1/R$ to $R$, up the segment to $R+Ri$, along the top to $-R+Ri$, down to $-R$, along the axis to $-1/R$, and back around the upper semicircle of radius $1/R$ to $1/R$; then $\displaystyle\int_{\gamma}\frac{e^{iz}}{z}\,dz=0$.

::: pf-proof

$e^{iz}/z$ is holomorphic on the region enclosed by $\gamma$: its only singularity is $z=0$, which the indentation at radius $1/R$ excludes, and the closed contour lies in the closed upper half-plane, where $e^{iz}$ is entire and $1/z$ is holomorphic off $0$. By Cauchy's theorem the integral over the closed contour vanishes.

:::

:::

::: {.pf-step #vertical}

$\displaystyle\int_{\gamma_{2}}\frac{e^{iz}}{z}\,dz\to0$ and $\displaystyle\int_{\gamma_{4}}\frac{e^{iz}}{z}\,dz\to0$ as $R\to\infty$.

::: pf-proof

On the segment $\gamma_{2}$ we have $z=R+it$, $0\le t\le R$, so $\abs{e^{iz}}=e^{-t}$ and $\abs{z}\ge R$; hence
$$
\abs{\int_{\gamma_{2}}\frac{e^{iz}}{z}dz}\le\int_{0}^{R}\frac{e^{-t}}{R}dt=\frac{1-e^{-R}}{R}\to0.
$$
The segment $\gamma_{4}$ is the reflection $z=-R+it$, where $\abs{e^{iz}}=e^{-t}$ and $\abs{z}\ge R$, giving the same bound.

:::

:::

::: {.pf-step #top}

$\displaystyle\int_{\gamma_{3}}\frac{e^{iz}}{z}\,dz\to0$ as $R\to\infty$.

::: pf-proof

On the top segment $z=t+iR$, $-R\le t\le R$, we have $\abs{e^{iz}}=e^{-R}$ and $\abs{z}\ge R$, so
$$
\abs{\int_{\gamma_{3}}\frac{e^{iz}}{z}dz}\le\int_{-R}^{R}\frac{e^{-R}}{R}dt=2e^{-R}\to0.
$$

:::

:::

::: {.pf-step #indent}

$\displaystyle\lim_{R\to\infty}\int_{\gamma_{6}}\frac{e^{iz}}{z}\,dz=-i\pi$.

::: pf-proof

$e^{iz}/z=1/z+\psi(z)$ with $\psi$ entire, so $\int_{\gamma_{6}}\psi\to0$ as the semicircle shrinks, while $\int_{\gamma_{6}}dz/z=-i\pi$: parametrising $z=\frac1Re^{i\theta}$ with $\theta$ from $\pi$ to $0$ gives $\int_{\pi}^{0}i\,d\theta=-i\pi$.

:::

:::

::: {.pf-step #real}

$\displaystyle\int_{0}^{\infty}\frac{\sin x}{x}\,dx=\frac{\pi}{2}$.

::: pf-proof

Summing the pieces of $\gamma$ in step [](#contour){.pf-ref}: the two real-axis segments contribute $\int_{1/R}^{R}\frac{e^{ix}}{x}dx+\int_{-R}^{-1/R}\frac{e^{ix}}{x}dx\to2i\int_{0}^{\infty}\frac{\sin x}{x}dx$ as $R\to\infty$, since $\frac{e^{ix}-e^{-ix}}{x}=\frac{2i\sin x}{x}$. Steps [](#vertical){.pf-ref}, [](#top){.pf-ref} and [](#indent){.pf-ref} give, in the limit,
$$
2i\int_{0}^{\infty}\frac{\sin x}{x}dx-i\pi=0,
$$
hence
$$
\boxed{\int_{0}^{\infty}\frac{\sin x}{x}\,dx=\frac{\pi}{2}.}
$$

:::

:::

:::

:::
