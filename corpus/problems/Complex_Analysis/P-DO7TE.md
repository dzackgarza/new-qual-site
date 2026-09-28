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
  - Singularities
  - Trigonometry
relations: []
review: draft
---

::: {.problem}
- Show that $\sin(z)/z$ has no poles.
:::

::: {.solution}
For $z\ne0$, the quotient $\sin z/z$ is holomorphic. At $z=0$, use the Taylor
series
\[
\sin z=z-\frac{z^3}{3!}+\frac{z^5}{5!}-\cdots.
\]
Then
\[
\frac{\sin z}{z}
=1-\frac{z^2}{3!}+\frac{z^4}{5!}-\cdots,
\]
which converges near $0$ and extends the quotient holomorphically there with
value $1$. Hence the apparent singularity at $0$ is removable, and
$\sin z/z$ has no poles anywhere.
:::
