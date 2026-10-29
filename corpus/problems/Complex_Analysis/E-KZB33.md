---
schema: qual/card@1
id: E-KZB33
kind: problem
title: Injective holomorphic maps have nonvanishing derivative
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Zeros
  - Conformal Maps
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source does not say what f is; the statement takes f holomorphic on an open set Omega.
---

::: {.exercise}
Let $f$ be holomorphic on an open set $\Omega\subseteq\CC$. Show that if $f$ is injective, then $f'$ is nowhere vanishing and thus $f$ is conformal.

:::

::: {.solution}
We prove the contrapositive: suppose $f'(z_0)=0$ for some $z_0\in\Omega$; we show $f$ is not injective. If $f$ is constant near $z_0$ it is not injective, so assume it is not.

::: pf

::: {.pf-step #factor}
There are $n\ge2$ and a holomorphic $H$ near $z_0$ with $H(z_0)=0$, $H'(z_0)\neq0$ and $f(z)-f(z_0)=H(z)^n$.

::: pf-proof
The zero of $f-f(z_0)$ at $z_0$ has some finite order $n$, and $n\ge2$ because $f'(z_0)=0$. Write $f(z)-f(z_0)=(z-z_0)^ng(z)$ with $g(z_0)\neq0$. On a disk around $z_0$ where $g$ does not vanish, $g$ has a holomorphic $n$-th root $h$. Then $H(z)\coloneqq(z-z_0)h(z)$ has $H'(z_0)=h(z_0)\neq0$.
:::

:::

::: pf-step
$f$ is not injective near $z_0$.

::: pf-proof
By step [](#factor){.pf-ref} and the inverse function theorem, $H$ maps a neighborhood $U$ of $z_0$ biholomorphically onto a disk $\DD_r(0)$. For $0<\rho<r$, the $n\ge2$ distinct points $\rho e^{2\pi ij/n}$ have preimages in $U$ on which $f-f(z_0)=H^n$ takes the same value $\rho^n$.
:::

:::

:::

:::
