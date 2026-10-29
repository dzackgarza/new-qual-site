---
schema: qual/card@1
id: P-DO7TE
kind: problem
title: $\sin z/z$ has no poles
classification:
  areas:
  - complex-analysis
  topics:
  - Removable Singularities
  - Laurent Series
  - Singularities
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
Show that $\sin(z)/z$ has no poles.
:::

::: {.solution}

::: pf

::: pf-step
$\sin z/z$ is holomorphic on $\CC\setminus\{0\}$.

::: pf-proof
It is a quotient of entire functions whose denominator vanishes only at $0$.
:::

:::

::: pf-step
The singularity at $0$ is removable, so $\sin z/z$ has no poles.

::: pf-proof
From $\sin z=\sum_{n\ge0}(-1)^nz^{2n+1}/(2n+1)!$, for $z\ne0$,
$$
\frac{\sin z}{z}=\sum_{n=0}^\infty\frac{(-1)^nz^{2n}}{(2n+1)!}=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots,
$$
and the right side is an entire function with value $1$ at $0$.
:::

:::

:::

:::
