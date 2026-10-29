---
schema: qual/card@1
id: E-4GLUR
kind: problem
title: $\sin(z)/z$ has a removable singularity at $0$
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Laurent Series
  - Trigonometry
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Show that $\sin(z)/z$ has no poles.

:::

::: {.solution}

::: pf

::: {.pf-step #laurent}
The Laurent expansion of $\sin(z)/z$ about $0$ is $1 - \frac{z^2}{3!} + \frac{z^4}{5!} - \cdots$.

::: pf-proof
Divide the Taylor series $\sin z = z - \frac{z^3}{3!} + \frac{z^5}{5!} - \cdots$, valid on $\CC$, by $z$.
:::

:::

::: pf-step
$\sin(z)/z$ has no poles.

::: pf-proof
The function is holomorphic on $\CC\setminus\theset{0}$, so $0$ is its only possible pole.
By step [](#laurent){.pf-ref} its Laurent expansion at $0$ has no terms $z^{-k}$ with $k\ge1$, so $0$ is a removable singularity.
:::

:::

:::

:::
