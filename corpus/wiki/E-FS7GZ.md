---
schema: qual/card@1
id: E-FS7GZ
kind: exercise
title: "Radius of convergence"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Radius of convergence"}
Find the radius of convergences for the power series expansion of $\sqrt{z}$ about $z_0 = 4 +3i$.
Repeat with $z_1=-4+3i$.

:::

:::{.solution}
Choose the principal branch of $\log$, so take a branch cut at $\RR_{\leq 0}$, to define $z^{1\over 2} = e^{{1\over 2}\log(z)}$.
The radius of convergence is the distance to the nearest singularity or branch cut, so note that $f(z) = z^{1\over 2}$ is singular at $z=0$, so we compute $\abs{z_0 - 0} = \abs{4+3i} = 5$.
The distance to the branch is also 5, so $R=5$.

For $z_1$, the distance to zero is $\abs{4+3i - 0} = 5$ but the distance to the branch is 4, so $R=4$.

> Note the subtle distinction: the series converges to $f$ in a disc $\abs{z-z_0}<1$, but the series itself converges in larger discs.

:::

