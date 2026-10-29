---
schema: qual/card@1
id: E-ZGFJA
kind: problem
title: Blaschke bound for a self-map of the disc vanishing at $0$ and $\pm r$
classification:
  areas:
  - complex-analysis
  topics:
  - Blaschke Factors
  - Schwarz Lemma
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source wrote "Suppose f: D -> D" without saying f is holomorphic, which the bound needs; the statement now takes f holomorphic.'
---

::: {.exercise}
Suppose $f:\DD\to \DD$ is holomorphic with $f(0) = 0$ and that there exists an $r\in (0, 1)$ with $f(r) = f(-r) = 0$.
Show that
$$
\abs{f(z)} \leq \abs{\frac{z^2-r^2}{1-r^2 z^2}}.
$$
:::

::: {.solution}
Write $\psi_a(z)\coloneqq\dfrac{z-a}{1-az}$ for real $a\in(-1,1)$, and $B\coloneqq\psi_r\psi_{-r}$, so that $B(z) = \dfrac{z^2-r^2}{1-r^2z^2}$.

::: pf

::: {.pf-step #blaschke}
$B$ is holomorphic on a neighbourhood of $\bar\DD$, vanishes in $\DD$ exactly at $\pm r$, both simple zeros, and $\abs{B(z)}\to1$ uniformly as $\abs z\to1$.

::: pf-proof
Each $\psi_a$ is a Blaschke factor: its only pole $1/a$ lies outside $\bar\DD$, its only zero is the simple zero $a$, and $\abs{\psi_a}=1$ on the unit circle.
Uniform convergence of $\abs B$ to $1$ follows from uniform continuity of $\abs B$ on $\bar\DD$.
:::

:::

::: {.pf-step #quotient}
$g\coloneqq f/B$ extends to a holomorphic function on $\DD$.

::: pf-proof
By step [](#blaschke){.pf-ref}, the only singularities of $g$ in $\DD$ are at $\pm r$, where $B$ has simple zeros and $f$ vanishes, so they are removable.
:::

:::

::: {.pf-step #bound}
$\abs{g}\le1$ on $\DD$.

::: pf-proof
Fix $z_0\in\DD$ and $\varepsilon>0$.
By step [](#blaschke){.pf-ref}, there is $\rho$ with $\abs{z_0}<\rho<1$ and $\abs{B}\ge1-\varepsilon$ on $\abs z=\rho$.
Since $\abs f<1$, $\abs g\le\frac{1}{1-\varepsilon}$ on $\abs z=\rho$, and by the maximum modulus principle $\abs{g(z_0)}\le\frac1{1-\varepsilon}$.
Letting $\varepsilon\to0$ gives $\abs{g(z_0)}\le1$.
:::

:::

::: pf-step
$\abs{f(z)}\le\abs{\dfrac{z^2-r^2}{1-r^2z^2}}$ for all $z\in\DD$.

::: pf-proof
By step [](#bound){.pf-ref}, $\abs{f} = \abs g\abs B\le\abs B$.
:::

:::

:::

:::
