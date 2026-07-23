---
schema: qual/card@1
id: E-MTRVA
kind: exercise
title: "SS 3.2.15"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="SS 3.2.15"}
Suppose $f$ is continuous and nonzero on $\bar\DD$ and holomorphic on $\DD$.
Show that if $\abs{f(z)} = \abs{z}$ for all $\abs{z} = 1$ then $f$ is constant.

#complex/exercise/completed

:::

:::{.solution}
If $f$ has no zeros in $\DD$, apply the MMP to $1/f$ to get $\abs{f} = 1$ on all of $\DD$.
By Cauchy-Riemann (or the open mapping theorem), if $\abs{f}$ is constant, $f$ is constant.
:::

