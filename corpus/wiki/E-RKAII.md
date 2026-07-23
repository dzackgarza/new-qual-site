---
schema: qual/card@1
id: E-RKAII
kind: exercise
title: "Show that if $\\Re(f(z)) \\geq 0$ for all $z\\in \\CC$, then $f$ is consta\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that if $\Re(f(z)) \geq 0$ for all $z\in \CC$, then $f$ is constant.

#complex/exercise/completed

:::

:::{.solution}
Define $g(z) \da e^{-f(z)}$, then
\[
\abs{g(z)} = e^{-\Re(f(z))} \leq e^0 = 1
.\]
Since $g$ is entire and bounded, $g$ is constant and thus so is $f$.
:::

