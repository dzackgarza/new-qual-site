---
schema: qual/card@1
id: E-WNNSK
kind: exercise
title: Working with conjugates
classification:
  areas:
  - complex-analysis
  topics:
  - Geometry
relations: []
review: draft
solved: true
---

:::{.exercise title="Working with conjugates"}
Find $\Re\qty{z+2\over z-1}$.

:::

:::{.solution}
\[
{z+2\over z-1}\cdot{\bar{z-1} \over \bar{z-1}}
&= {(z+2)\bar{z-1} \over \abs{z-1}^2} \\
&= {((z-1) + 3)\bar{z-1} \over \abs{z-1}^2} \\
&= {\abs{z-1}^2 + 3\bar{z} -3 \over \abs{z-1}^2} \\
&= {(x-1)^2 + y^2 + 3(x-iy) - 3 \over (x-1)^2 + y^2} \\
&= {(x-1)^2 + 3x - 3 + y^2\over (x-1)^2 + y^2} + i{-3y\over (x-1)^2 + y^2} \\
&= {(x-1)(x+2) + y^2\over (x-1)^2 + y^2} + i{-3y\over (x-1)^2 + y^2} 
.\]

:::
