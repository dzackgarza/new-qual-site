---
schema: qual/card@1
id: E-JUT2P
kind: problem
title: A singularity is removable for $f$ if and only if it is removable for $f'$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Cauchy Estimates
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Suppose $f$ is meromorphic. Show that if $z_0$ is a removable singularity of $f$, then it is also a removable singularity of $f'$.
Conversely, if $z_0$ is removable for $f'$, then it is also removable for $f$.

:::

::: {.solution}
Let $f$ be holomorphic on a punctured disk $D^*\coloneqq\DD_\varepsilon^*(z_0)$, and write $D\coloneqq\DD_\varepsilon(z_0)$.

::: pf

::: pf-step
If $z_0$ is removable for $f$, then it is removable for $f'$.

::: pf-proof
Let $F$ be the holomorphic extension of $f$ to $D$. Then $F'$ is holomorphic on $D$ and equals $f'$ on $D^*$.
:::

:::

::: pf-step
If $z_0$ is removable for $f'$, then it is removable for $f$.

::: pf-proof
Let $g$ be the holomorphic extension of $f'$ to $D$. A holomorphic function on a disk has a primitive, so $F(z)\coloneqq\int_{z_0}^zg(\xi)\,d\xi$ is holomorphic on $D$ with $F'=g$. Then $(F-f)'=0$ on the connected set $D^*$, so $f=F-c$ there for a constant $c$, and $F-c$ is a holomorphic extension of $f$ to $D$.
:::

:::

:::

:::
