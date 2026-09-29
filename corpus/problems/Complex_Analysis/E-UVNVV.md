---
schema: qual/card@1
id: E-UVNVV
kind: problem
title: Injectivity relates to derivatives
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
---

::: {.exercise}
Show that if $z_0$ is a zero of $f'$ of order $n$, then $f$ is $(n+1)$-to-one in a neighborhood of $z_0$.
:::

::: {.solution}
**Goal:** Show that if $z_0$ is a zero of $f'$ of order $n$, then $f$ is $(n+1)$-to-one in a neighborhood of $z_0$ (for $z$ near $z_0$, the equation $f(z) = w$ has exactly $n+1$ solutions in a punctured neighborhood of $z_0$, for $w$ near $f(z_0)$, $w \neq f(z_0)$).

::: pf

::: {.pf-step #expand-fprime}
Setup: expand $f$ about $z_0$.

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

::: pf-step
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
Step [](#zeta-biholomorphism){.pf-ref} shows the change of variables $z \leftrightarrow \zeta$ is one-to-one, and step [](#power-map-multiplicity){.pf-ref} shows $f$ in these coordinates is $(n+1)$-to-one; composing, $f$ is $(n+1)$-to-one near $z_0$.
:::

:::
