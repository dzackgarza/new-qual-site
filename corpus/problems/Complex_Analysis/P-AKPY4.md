---
schema: qual/card@1
id: P-AKPY4
kind: problem
title: If $fg=0$ on a domain then $f\equiv 0$ or $g\equiv 0$
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Zeros
relations: []
review: draft
---

::: {.problem}
Suppose $D$ is a domain and $f, g$ are analytic on $D$.

Prove that if $fg = 0$ on $D$, then either $f \equiv 0$ or $g\equiv 0$ on $D$.
:::

::: {.solution}
Suppose $fg=0$ on $D$ and $f\not\equiv 0$; we show $g\equiv0$.

::: pf

::: {.pf-step #local}
$g$ vanishes on a nonempty open set $U\subseteq D$.

::: pf-proof
Pick $z_0\in D$ with $f(z_0)\neq0$.
Since $f$ is continuous, $f$ has no zeros on some open neighbourhood $U\subseteq D$ of $z_0$.
For $z\in U$, $f(z)g(z)=0$ and $f(z)\neq0$, so $g(z)=0$, because $\CC$ is a field.
:::

:::

::: pf-step
$g\equiv0$ on $D$.

::: pf-proof
The open set $U$ of step [](#local){.pf-ref} has limit points in $D$, and $D$ is connected, so the identity theorem applies.
:::

:::

:::

:::
