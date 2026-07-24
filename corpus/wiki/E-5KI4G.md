---
schema: qual/card@1
id: E-5KI4G
kind: exercise
title: "Determine where the following real-valued function is or is not unifor\u2026"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Determine where the following real-valued function is or is not uniformly convergent:
\[
f_n(x) \da {\sin(nx)\over 1+nx}
.\]

:::

:::{.solution}
This converges uniformly on $[a, \infty)$ for $a$ any constant:
\[
\abs{\sin(nx) \over 1+nx} \leq {1\over 1 + na} < \eps = \eps(n, a)
.\]

This does not converge uniformly on $(0, \infty)$: 
\[
x_n \da {1\over n} \implies \abs{f_n(x_n)} = \abs{\sin(1) \over 2} > \eps
.\]
:::

