---
schema: qual/card@1
id: P-CAS24D
kind: problem
title: 'Positive harmonic function as $e^u\sin v$ on a simply connected region'
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $\phi$ be a positive harmonic function on a simply connected region $G$.
Prove that there are two harmonic functions $u,v$ on $G$ such that $\phi = e^u \sin v$.
:::

::: {.solution}

::: pf

::: pf-step

Since $G$ is simply connected and $\phi > 0$ is harmonic, $\phi$ has a harmonic conjugate $\psi$, so $F = \phi + i\psi$ is analytic on $G$.

::: pf-proof

a positive harmonic function on a simply connected region has a harmonic conjugate (its harmonic conjugate is obtained by integrating the closed form $-\phi_y\, dx + \phi_x\, dy$).

:::

:::

::: pf-step

$F$ is nowhere zero on $G$.

::: pf-proof

$\operatorname{Re} F = \phi > 0$, so $F \neq 0$.

:::

:::

::: pf-step

Since $G$ is simply connected and $F$ is nowhere zero, $F$ has an analytic logarithm: $F = e^H$ for some analytic $H$ on $G$.

::: pf-proof

a nowhere-vanishing analytic function on a simply connected region has an analytic logarithm.

:::

:::

::: pf-step

Write $H = u + iv$ with $u, v$ harmonic (the real and imaginary parts of an analytic function are harmonic).

::: pf-proof

real and imaginary parts of an analytic function are harmonic.

:::

:::

::: pf-step

Then $\phi = \operatorname{Re} F = \operatorname{Re}(e^{u + iv}) = e^u \cos v$.

::: pf-proof

$e^{u+iv} = e^u(\cos v + i\sin v)$, so its real part is $e^u \cos v$.

:::

:::

::: {.pf-step #s6}

Replace $v$ by $v + \pi/2$ (equivalently, absorb a constant into $H$) to get $\phi = e^u \sin v$.

::: pf-proof

$\cos v = \sin(v + \pi/2)$, and $v + \pi/2$ is still harmonic.

:::

:::

::: pf-qed

Step [](#s6){.pf-ref}.

:::

:::

:::
