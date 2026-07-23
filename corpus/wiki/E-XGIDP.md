---
schema: qual/card@1
id: E-XGIDP
kind: exercise
title: "SS 1.13: Constant real/imaginary/magnitude implies constant"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="SS 1.13: Constant real/imaginary/magnitude implies constant"}
If $f$ is holomorphic on $\Omega$ and any of the following hold, then $f$ is constant:

1. $\Re(f)$ is constant.
2. $\Im(f)$ is constant.
3. $\abs{f}$ is constant.

#complex/exercise/completed

:::

:::{.solution}
**Part 3**:

- Write $\abs{f} = c \in \RR$.
- If $c=0$, done, so suppose $c>0$.
- Use $f\bar{f} = \abs{f}^2 = c^2$ to write $\bar{f}=c^2/f$.
- Since $\abs{f(z)} = 0 \iff f(z) = 0$, we have $f\neq 0$ on $\Omega$, so $\bar{f}$ is analytic.
- Similarly $f$ is analytic, and $f,\bar{f}$ analytic implies $f'=0$ implies $f$ is constant. 

:::
