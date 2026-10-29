---
schema: qual/card@1
id: E-J3QMJ
kind: problem
title: Constancy on a closed subdisk of $\DD$ implies constancy on $\DD$
classification:
  areas:
  - complex-analysis
  topics:
  - Identity Theorem
  - Maximum Modulus Principle
relations: []
review: draft
---

::: {.exercise}
Show that if $f\in\Hol(\DD)$ is constant on a closed disk $r\overline\DD$ for some $0<r<1$, then $f$ is constant on $\DD$.
:::

::: {.solution}
Let $c$ be the value of $f$ on $r\overline\DD$.

::: pf

::: pf-step
$f\equiv c$ on $\DD$.

::: pf-proof
The holomorphic function $f-c$ vanishes on the nonempty open set $r\DD$, and $\DD$ is connected, so the identity theorem gives $f-c\equiv0$ on $\DD$.
:::

:::

:::

:::
