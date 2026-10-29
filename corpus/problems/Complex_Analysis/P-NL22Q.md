---
schema: qual/card@1
id: P-NL22Q
kind: problem
title: The ring of analytic functions on a domain is an integral domain
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Suppose $D$ is a domain and $f, g$ are analytic on $D$.

Prove that if $fg = 0$ on $D$, then either $f \equiv 0$ or $g\equiv 0$ on $D$.
:::

::: {.solution}
Suppose $f\not\equiv0$; we show $g\equiv0$.

::: pf

::: {.pf-step #open-set}
There is a nonempty open set $U\subseteq D$ on which $f$ has no zero.

::: pf-proof
Pick $z_1\in D$ with $f(z_1)\neq0$. By continuity, $f$ has no zero on some disk $U$ about $z_1$.
:::

:::

::: {.pf-step #g-on-u}
$g\equiv0$ on $U$.

::: pf-proof
For $z\in U$, $f(z)g(z)=0$ and $f(z)\neq0$.
:::

:::

::: pf-step
$g\equiv0$ on $D$.

::: pf-proof
By step [](#g-on-u){.pf-ref}, $g$ vanishes on the nonempty open set $U$ of step [](#open-set){.pf-ref}. Since $D$ is connected, the identity theorem gives $g\equiv0$ on $D$.
:::

:::

:::
:::
