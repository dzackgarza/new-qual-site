---
schema: qual/card@1
id: E-UVNVV
kind: problem
title: "A zero of $f'$ of order $n$ makes $f$ locally $(n+1)$-to-one"
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Open Mapping Theorem
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source omits that f is holomorphic; the statement adds it.
---

::: {.exercise}
Let $f$ be holomorphic near $z_0$. Show that if $z_0$ is a zero of $f'$ of order $n$, then $f$ is $(n+1)$-to-one in a neighborhood of $z_0$.
:::

::: {.solution}
::: pf

::: {.pf-step #expand-fprime}
$f(z) - f(z_0) = (z - z_0)^{n+1} \phi(z)$ with $\phi$ holomorphic near $z_0$ and $\phi(z_0) \neq 0$.

::: pf-proof
Since $z_0$ is a zero of $f'$ of order $n$, we have $f'(z) = (z - z_0)^n h(z)$ with $h$ analytic near $z_0$, $h(z_0) \neq 0$.
Integrating, $f(z) - f(z_0) = (z - z_0)^{n+1} \phi(z)$ where $\phi$ is analytic near $z_0$ and $\phi(z_0) = h(z_0)/(n+1) \neq 0$.
:::

:::

::: {.pf-step #phi-root}
$\phi$ is nonzero on a neighborhood of $z_0$, so $\phi$ has an $(n+1)$-st root $\psi$ with $\psi^{n+1} = \phi$, $\psi$ analytic, $\psi(z_0) \neq 0$.

::: pf-proof
$\phi(z_0) \neq 0$ by step [](#expand-fprime){.pf-ref}; by continuity $\phi \neq 0$ in a disk around $z_0$, where a holomorphic branch of the $(n+1)$-st root exists (the disk is simply connected and $\phi$ avoids $0$).
:::

:::

::: {.pf-step #zeta-biholomorphism}
Define $\zeta(z) = (z - z_0)\psi(z)$; then $\zeta$ is a biholomorphism from a neighborhood of $z_0$ onto a neighborhood of $0$, with $\zeta(z_0) = 0$ and $\zeta'(z_0) = \psi(z_0) \neq 0$.

::: pf-proof
$\zeta'(z_0) = \psi(z_0) \neq 0$, so the inverse function theorem gives the local biholomorphism.
:::

:::

::: {.pf-step #zeta-coordinate}
In the $\zeta$ coordinate, $f(z) = f(z_0) + \zeta(z)^{n+1}$.

::: pf-proof
Steps [](#expand-fprime){.pf-ref} and [](#phi-root){.pf-ref}: $f(z) - f(z_0) = (z - z_0)^{n+1}\phi(z) = ((z - z_0)\psi(z))^{n+1} = \zeta(z)^{n+1}$.
:::

:::

::: {.pf-step #power-map-multiplicity}
The map $w \mapsto f(z_0) + w^{n+1}$ is $(n+1)$-to-one on a punctured neighborhood of $0$.

::: pf-proof
For $w' \neq 0$ near $0$, the equation $w^{n+1} = w'$ has exactly $n+1$ distinct solutions (the $n+1$ roots of $w'$), all lying in a small disk around $0$.
:::

:::

::: pf-qed
By step [](#zeta-biholomorphism){.pf-ref}, $\zeta$ maps a neighborhood $U$ of $z_0$ bijectively onto a disk $\abs{\zeta}<r$. For $0<\abs{w-f(z_0)}<r^{n+1}$, steps [](#zeta-coordinate){.pf-ref} and [](#power-map-multiplicity){.pf-ref} show that $f(z)=w$ has exactly $n+1$ solutions $z\in U$, all different from $z_0$; and $f(z)=f(z_0)$ only at $z=z_0$ in $U$.
:::

:::

:::

::: {.remark title="Alternative proof by Rouché's theorem"}
$f-f(z_0)$ has a zero of order exactly $n+1$ at $z_0$.
Choose $\rho>0$ so that $f\neq f(z_0)$ and $f'\neq0$ on $0<\abs{z-z_0}\le\rho$, and let $\delta=\min_{\abs{z-z_0}=\rho}\abs{f(z)-f(z_0)}$.
For $\abs{w-f(z_0)}<\delta$, Rouché's theorem gives $f-w$ exactly $n+1$ zeros with multiplicity in $\abs{z-z_0}<\rho$; for $w\neq f(z_0)$ each is a simple zero because $f'\neq0$ there, so they are $n+1$ distinct points.
:::
