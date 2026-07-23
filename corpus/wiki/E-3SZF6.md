---
schema: qual/card@1
id: E-3SZF6
kind: exercise
title: "Show that if $f, g$ are entire with $\\abs{f(z)}\\leq \\abs{g(z)}$, then\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that if $f, g$ are entire with $\abs{f(z)}\leq \abs{g(z)}$, then $f(z) = cg(z)$ for some constant $c$.

#complex/exercise/completed

:::

:::{.solution}
Write $h \da f/g$, so $h$ is meromorphic with $\abs h \leq 1$.
Moreover, $h$ can only have singularities where $g (z_k) = 0$, but is bounded by 1 in punctured neighborhoods about any such $z_k$.
So any such singularities are removable, and $h$ extends over the singularities by Riemann's removable singularity theorem to give an entire function.
Now $h$ is bounded and entire, thus constant, so $c = h = f/g \implies f=cg$.
:::

