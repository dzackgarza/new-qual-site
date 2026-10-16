---
schema: qual/card@1
id: E-VCLTY
kind: problem
title: Laurent expansions about different points
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Poles
  - Principal Parts
relations: []
review: draft
---

::: {.exercise}
Find the Laurent expansion about $z=0$ and $z=1$ respectively of the following function:
\[
f(z) \definedas {z+1 \over z(z-1)}
.\]

:::

::: {.hint}
Expand $f$ in powers of $(z - z_0)$ about each point.
:::

::: {.solution}
For $z=0$:
\[
{z+1 \over z(z-1)}
&= {1\over z} {z+1 \over z-1} \\
&= -{z+1\over z} {1\over 1-z} \\
&= -\qty{1 + {1\over z}}\sum_{k\geq 0} z^k
.\]

For $z=1$:
\[
{z+1 \over z(z-1)}
&= {1\over z-1}\qty{1 + {1\over z} } \\
&= {1\over z-1}\qty{1 + {1\over 1 - (1-z)} } \\
&= {1\over z-1} \qty{1 + \sum_{k\geq 0} (1-z)^k } \\
&= {1\over z-1} \qty{1 + \sum_{k\geq 0} (-1)^k (z-1)^k }
.\]

:::

