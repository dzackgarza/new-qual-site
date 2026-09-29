---
schema: qual/card@1
id: P-ZORLW
kind: problem
title: Holomorphic functions vanishing on the boundary are constant or have an interior
  zero
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
- Show that if $\abs{f} = 0$ on $\bd \Omega$ then either $f$ is constant or $f$ has a zero in $\Omega$.
:::

::: {.solution}
**Goal:** If $f$ is holomorphic on a bounded region $\Omega$, continuous on $\bar\Omega$, and $\abs f = 0$ (i.e. $f = 0$) on $\bd\Omega$, show that either $f$ is constant or $f$ has a zero in $\Omega$.

::: pf

::: {.pf-step #s1}

If $f$ has no zeros in $\Omega$, then $\abs{f}$ attains its maximum on $\bd\Omega$.

::: pf-proof

$\abs{f}$ is continuous on the compact set $\bar\Omega$, so it attains its maximum somewhere in $\bar\Omega$; by the maximum modulus principle (or its version for $1/f$, valid because $f$ has no zeros), the maximum is attained on the boundary $\bd\Omega$.

:::

:::

::: {.pf-step #s2}

If $f$ has no zeros in $\Omega$, then $f \equiv 0$ on $\bar\Omega$.

::: pf-proof

By step [](#s1){.pf-ref} and the hypothesis $\abs f = 0$ on $\bd\Omega$, $\max_{\bar\Omega}\abs f = 0$, so $f \equiv 0$ on $\bar\Omega$.

:::

:::

::: {.pf-step #s3}

If $f$ is not constant, then $f$ has a zero in $\Omega$.

::: pf-proof

Contrapositive of step [](#s2){.pf-ref}: if $f$ has no zero in $\Omega$, then by step [](#s2){.pf-ref} $f \equiv 0$ on $\bar\Omega$, so $f$ is constant (the zero function).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} shows that a nonconstant $f$ must vanish somewhere in $\Omega$, which together with the trivial constant case proves the claim.

:::

:::

:::
