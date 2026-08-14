---
schema: qual/card@1
id: E-FXYTL
kind: exercise
title: "Show that if $fg \\equiv 0$ on a domain $\\Omega$ then either $f\\equiv 0$ or $g\\equiv 0$."
classification:
  areas:
  - complex-analysis
  topics:
  - identity-theorem
  - zeros
relations: []
review: draft
---

::: {.exercise title="?"}
Show that if $fg \equiv 0$ on a domain $\Omega$ then either $f\equiv 0$ or $g\equiv 0$.
:::

::: {.solution}
If $f\not\equiv 0$, there is a point $z_0$ where $f(z_0)\neq 0$, and thus a neighborhood $U\ni z_0$ where $f$ is nonvanishing.
This forces $g\equiv 0$ on $U$, however $U$ is a set with a limit point, so $g\equiv 0$ on $\Omega$ by the identity principle.
:::
