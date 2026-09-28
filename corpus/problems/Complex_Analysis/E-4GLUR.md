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
The function $\sin(z)/z$ is holomorphic on $\CC\setminus\theset{0}$, and $\sin(z)$ has a simple zero at $0$.
The Laurent expansion about zero is
\[
\inverseof{z} \sin(z) = \inverseof{z}\qty{ z - {z^3 \over 3!} + {z^5\over 5!} - \cdots} = 1 - {z^2\over 3!} + {z^4 \over 5!} - \cdots
,\]
which has no terms $z^{-k}$ with $k\geq 1$.
So $z=0$ is a removable singularity, and $\sin(z)/z$ has no poles.
:::
