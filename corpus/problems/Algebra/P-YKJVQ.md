---
schema: qual/card@1
id: P-YKJVQ
kind: problem
title: $\langle 2,x\rangle$ is not principal in $\ZZ[x]$
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Principal Ideal Domains
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Show that $\generators{ 2, x }\normal \ZZ[x]$ is not a principal ideal.
:::

::: {.solution}
Let $I=(2,x)\subseteq\ZZ[x]$.

::: pf

::: {.pf-step #constant}
If $I=(f)$, then $f=\pm1$ or $f=\pm2$.

::: pf-proof
$2\in(f)$ gives $2=fg$; in the domain $\ZZ[x]$ degrees add, so $\deg f=0$ and $f$ is an integer dividing $2$.
:::

:::

::: {.pf-step #proper}
$I\ne\ZZ[x]$.

::: pf-proof
The kernel of the homomorphism $\ZZ[x]\to\FF_2$ given by reduction modulo $2$ and evaluation at $0$ contains $2$ and $x$ but not $1$.
:::

:::

::: pf-step
$\boxed{I\text{ is not principal.}}$

::: pf-proof
By step [](#constant){.pf-ref}, $(f)$ would be $\ZZ[x]$, which step [](#proper){.pf-ref} excludes, or $(2)$, which does not contain $x$.
:::

:::

:::

:::
