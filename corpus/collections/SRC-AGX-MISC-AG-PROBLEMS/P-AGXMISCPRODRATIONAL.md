---
schema: qual/card@1
id: P-AGXMISCPRODRATIONAL
kind: problem
title: $\PP^n\cross \PP^m$ is a rational variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Varieties
  - Birational Maps
  - Projective Space
relations: []
review: draft
---

::: {.problem}
Show that $\PP^n\cross \PP^m$ is rational.
:::

::: {.solution}
Take
\[
[x_0: x_1: \ldots: x_n] \cross [y_0: y_1: \ldots: y_m] \mapsto \left[1: \frac{x_1}{x_0}: \frac{x_2}{x_0}: \ldots: \frac{x_n}{x_0}: \frac{y_1}{y_0}: \frac{y_2}{y_0}: \ldots: \frac{y_m}{y_0}\right]
.\]
This has inverse
\[
[1: z_1: \ldots: z_{n+m}] \mapsto [1: z_1: \ldots: z_n] \cross [1: z_{n+1}: \ldots: z_{n+m}]
.\]
:::
