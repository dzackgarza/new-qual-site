---
schema: qual/card@1
id: E-FXYTL
kind: problem
title: 'Holomorphic functions on a domain: $fg\equiv 0$ implies $f\equiv 0$ or $g\equiv
  0$'
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source reads "Show that if fg = 0 on a domain Omega then either f = 0 or g = 0" and does not say that f and g are holomorphic; the statement adds that hypothesis, without which the claim fails.
---

::: {.exercise}
Let $f$ and $g$ be holomorphic on a domain $\Omega$.
Show that if $fg \equiv 0$ on $\Omega$ then either $f\equiv 0$ or $g\equiv 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #nonvanishing}
If $f\not\equiv 0$, then there is a nonempty open set $U\subseteq\Omega$ on which $f$ has no zeros.

::: pf-proof
Choose $z_0\in\Omega$ with $f(z_0)\neq 0$.
Since $f$ is continuous, $f$ has no zeros on some open disk $U$ about $z_0$.
:::

:::

::: pf-step
If $f\not\equiv 0$, then $g\equiv 0$ on $\Omega$.

::: pf-proof
On the set $U$ of step [](#nonvanishing){.pf-ref}, $fg=0$ and $f\neq0$, so $g=0$ on $U$.
The open set $U$ has a limit point in $\Omega$ and $\Omega$ is connected, so the identity theorem gives $g\equiv0$ on $\Omega$.
:::

:::

:::

:::
