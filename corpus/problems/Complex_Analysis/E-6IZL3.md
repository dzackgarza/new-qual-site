---
schema: qual/card@1
id: E-6IZL3
kind: problem
title: Harmonic functions on $\DD$ with $u(1/2)=2$ and $\abs u\ge2$
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Maximum Modulus Principle
relations: []
review: draft
audit:
- event: statement-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source reads "Find all harmonic functions u: D -> C such that u(1/2) = 2 and |u(z)| >= 2 for all |z| <= 1". The condition on the closed disc does not match the domain D, and complex-valued solutions form no describable family (see the remark), so the statement asks for real-valued u with the condition on D.'
---

::: {.exercise}
Find all real-valued harmonic functions $u$ on $\DD$ such that $u(1/2) = 2$ and $\abs{u(z)}\geq 2$ for all $z\in\DD$.
:::

::: {.solution}
::: pf

::: {.pf-step #sign}
$u\ge2$ on $\DD$.

::: pf-proof
The sets $\theset{u\ge2}$ and $\theset{u\le-2}$ are disjoint, closed in $\DD$, and cover $\DD$.
Since $\DD$ is connected, one of them is all of $\DD$, and $u(1/2)=2$ selects the first.
:::

:::

::: pf-step
The only such function is $\boxed{u\equiv2}$.

::: pf-proof
By step [](#sign){.pf-ref}, $u$ attains its minimum value $2$ at the interior point $1/2$, so $u\equiv2$ by the minimum principle for harmonic functions.
The constant $2$ satisfies both conditions.
:::

:::

:::

:::

::: {.remark}
For complex-valued harmonic $u$ the two conditions cut out no family simpler than the conditions themselves.
For every real harmonic $h$ on $\DD$ with $h(1/2)=0$, $u=2+ih$ satisfies both, since $\abs{u}^2=4+h^2$.
The real part need not be constant either: for $0<\varepsilon\le1$ and $K^2\ge4\varepsilon$, the harmonic function $u=2+\varepsilon\qty{(x-\tfrac12)^2-y^2}+iKy$ has $u(1/2)=2$ and $\Re u\ge2-\varepsilon y^2\ge1$ on $\overline\DD$, so $\abs{u}^2\ge(2-\varepsilon y^2)^2+K^2y^2\ge4+(K^2-4\varepsilon)y^2\ge4$.
:::
