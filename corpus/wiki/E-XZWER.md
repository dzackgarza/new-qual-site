---
schema: qual/card@1
id: E-XZWER
kind: exercise
title: "Show that $\\sin(z) = z$ has infinitely many solutions in $\\CC$."
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="?"}
Show that $\sin(z) = z$ has infinitely many solutions in $\CC$.

:::

:::{.solution}
Let $f(z) = \sin(z)-z$ and apply Big Picard: $f$ takes on every value in $\CC$, except possibly for some single $z_0$, infinitely many times.
So there is at most one $z_0$ such that there are *finitely* many solutions to $\sin(z) - z = z_0$.
If $z_0\neq 0$, we're done, so suppose such an exception $z_0$ does exist whose fiber has finitely many points.
Since $z_0+2\pi \neq z_0$, there must then be infinitely many solutions to $f(z) = z_0 + 2\pi$.
But then
\[
f(z+2\pi) = \sin(z+2\pi) - z - 2\pi = \sin(z) - z - 2\pi = (z_0 + 2\pi)-2\pi = z_0
,\]
so we can produce infinitely many points in the fiber over $w_0$, contradicting finiteness. 
So no exception $z_0$ exists, and in particular, $z_0=0$ is not an exception so $f(z) = 0$ has infinitely many solutions.
:::

