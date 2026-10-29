---
schema: qual/card@1
id: P-VTCZF
kind: problem
title: A holomorphic function with vanishing derivative on a connected domain is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Connectedness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
Show that if $f$ is holomorphic on a connected region $\Omega$ and $f'\equiv 0$ on $\Omega$, then $f$ is constant on $\Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #polygonal}

Any two points of $\Omega$ can be joined by a polygonal path in $\Omega$.

::: pf-proof

Fix $z_0 \in \Omega$ and let $U$ be the set of points of $\Omega$ joined to $z_0$ by a polygonal path in $\Omega$. Every point of $\Omega$ has a disc neighborhood in $\Omega$, and any two points of a disc are joined by a segment in it. So $U$ and $\Omega \setminus U$ are both open. Since $z_0 \in U$ and $\Omega$ is connected, $U = \Omega$.

:::

:::

::: {.pf-step #segment}

If the segment from $z_0$ to $z_1$ lies in $\Omega$, then $f(z_1) = f(z_0)$.

::: pf-proof

Parametrize the segment by $z(t) = z_0 + t(z_1 - z_0)$, $t \in [0,1]$. By the chain rule, $\frac{d}{dt} f(z(t)) = f'(z(t))(z_1 - z_0) = 0$, so the real and imaginary parts of $t \mapsto f(z(t))$ are constant on $[0, 1]$.

:::

:::

::: pf-step

$f$ is constant on $\Omega$.

::: pf-proof

Fix $z_0 \in \Omega$. For $z \in \Omega$, join $z_0$ to $z$ by a polygonal path in $\Omega$ (step [](#polygonal){.pf-ref}). By step [](#segment){.pf-ref}, $f$ takes the same value at the two ends of each segment of the path, so $f(z) = f(z_0)$.

:::

:::

:::

:::
