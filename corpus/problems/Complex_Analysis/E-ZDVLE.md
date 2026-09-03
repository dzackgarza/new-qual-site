---
schema: qual/card@1
id: E-ZDVLE
kind: problem
title: Entire functions with nonnegative real part are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Liouville's Theorem
  - Entire Functions
  - Harmonic Functions
relations: []
review: draft
---

:::{.exercise}
Show that if $\Re(f(z)) \geq 0$ for all $z\in \CC$, then $f$ is constant.

:::

:::{.solution}
Define $g(z) \da e^{-f(z)}$, then
\[
\abs{g(z)} = e^{-\Re(f(z))} \leq e^0 = 1
.\]
Since $g$ is entire and bounded, $g$ is constant and thus so is $f$.
:::

