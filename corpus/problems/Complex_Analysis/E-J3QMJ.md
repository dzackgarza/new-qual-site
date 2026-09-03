---
schema: qual/card@1
id: E-J3QMJ
kind: problem
title: Constancy on a closed subdisk of $\mathbb{D}$ implies constancy on $\mathbb{D}$
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
Show that if $f\in\Hol(\DD)$ is constant on a closed disk $r\bar\DD$ for some $0<r<1$, then $f$ is constant on $\DD$.
:::

::: {.solution}
Let $c$ be the constant value of $f$ on $r\bar\DD$.
Then the holomorphic function $f-c$ vanishes on the nonempty open set $r\DD$.
Since $\DD$ is connected, the identity theorem gives $f-c\equiv0$ on $\DD$.
Hence $f\equiv c$ on $\DD$.
:::
