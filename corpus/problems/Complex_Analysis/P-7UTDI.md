---
schema: qual/card@1
id: P-7UTDI
kind: problem
title: Constancy of holomorphic functions of constant modulus, real part, argument,
  or conjugate
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Let $f(z)$ be analytic in a domain, and prove that $f$ is constant if it satisfies any of the following conditions:

(a) $\abs{f(z)}$ is constant.

(b) $\Re(f(z))$ is constant.

(c) $\arg(f(z))$ is constant.

(d) $\overline{f(z)}$ is analytic.
:::

::: {.solution}
Write $f=u+iv$ on the connected domain $\Omega$.

::: pf

::: pf-step
(a) If $\abs f$ is constant, then $f$ is constant.

::: pf-proof
If $\abs f\equiv0$ then $f\equiv0$.
Otherwise $f(\Omega)$ lies in a circle, which has empty interior.
A nonconstant holomorphic function on a domain is an open map, so $f$ is constant.
:::

:::

::: {.pf-step #real-part}
(b) If $\Re f$ is constant, then $f$ is constant.

::: pf-proof
$u_x=u_y=0$, so the Cauchy--Riemann equations give $v_y=u_x=0$ and $v_x=-u_y=0$.
Thus $v$ is constant on the connected set $\Omega$, and so is $f$.
:::

:::

::: pf-step
(c) If $\arg f\equiv\theta_0$, then $f$ is constant.

::: pf-proof
Then $e^{-i\theta_0}f$ is holomorphic and real-valued, so its imaginary part is constant.
Applying step [](#real-part){.pf-ref} to $i e^{-i\theta_0}f$, whose real part is $-\Im(e^{-i\theta_0}f)=0$, shows that $f$ is constant.
:::

:::

::: pf-step
(d) If $\overline f$ is analytic, then $f$ is constant.

::: pf-proof
The Cauchy--Riemann equations for $u+iv$ and for $u-iv$ give $u_x=v_y=-v_y$ and $u_y=-v_x=v_x$.
Thus $u_x=u_y=v_x=v_y=0$, so $f$ is constant on the connected set $\Omega$.
:::

:::

:::

:::
