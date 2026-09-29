---
schema: qual/card@1
id: E-NKDKF
kind: problem
title: Primitives imply vanishing integral
classification:
  areas:
  - complex-analysis
  topics:
  - Contour Integration
  - Cauchy Integral Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that if $f$ has a primitive $F$ on $\Omega$ then $\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.
:::

::: {.solution}
**Goal:** Show that if $f$ has a primitive $F$ on $\Omega$ (i.e. $F' = f$ on $\Omega$), then $\int_\gamma f = 0$ for every closed curve $\gamma \subseteq \Omega$.

::: pf

::: {.pf-step #smooth-curve-ftc}
If $\gamma$ is a smooth curve from $a$ to $b$ parametrized by $z(t)$, $t \in [0,1]$, then $\int_\gamma f = F(b) - F(a)$.

::: pf-proof
By the chain rule, $\ddd{t}F(z(t)) = F'(z(t)) z'(t) = f(z(t)) z'(t)$, so $\int_\gamma f = \int_0^1 f(z(t))z'(t)\,dt = \int_0^1 \ddd{t}F(z(t))\,dt = F(z(1)) - F(z(0)) = F(b) - F(a)$.
:::

:::

::: {.pf-step #closed-curve-zero}
For a closed curve $\gamma$, the endpoints coincide, so $\int_\gamma f = F(a) - F(a) = 0$.

::: pf-proof
Step [](#smooth-curve-ftc){.pf-ref} with $b = a$: a closed curve has $z(1) = z(0)$.
:::

:::

::: {.pf-step #piecewise-extension}
The claim extends to piecewise smooth closed curves by summing over the smooth pieces.

::: pf-proof
Subdivide $\gamma$ into smooth arcs; the integral is the sum of the arc integrals, and the endpoint terms telescope to $0$ around the closed loop.
:::

:::

::: pf-qed
Steps [](#smooth-curve-ftc){.pf-ref}, [](#closed-curve-zero){.pf-ref} and [](#piecewise-extension){.pf-ref} prove the claim for (piecewise) smooth closed curves, which is the standard meaning of $\int_\gamma f$ in this context.
:::

:::
