---
schema: qual/card@1
id: E-2DO4D
kind: exercise
title: "Estimating and conformal maps"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Estimating and conformal maps"}
Suppose $f$ is holomorphic and $\abs{f(z)}\leq 1$ for $\Re(z) > 0$ with $f(1) = 0$.
Find an upper bound for $f(2)$.

#complex/exercise/completed

:::

:::{.solution}
Use the conformal map $g: z\mapsto -1{z+1\over z-1}$ to map $\Re(z)>0$ to $\DD$.
Composing $F: \DD \mapsvia{g} -i\HH \mapsvia{f} \DD$ yields a map $F = f\circ g:\DD\to \DD$.
Since $F(0) = f(g(0)) = f(1) = 0$, Schwarz applies and $\abs{F(z)} \leq \abs{z}$.
Using the standard trick,
\[
\abs{f(2)} = \abs{(f\circ \circ g\inv )(2)} = \abs{F(g\inv(2))} = \abs{F\qty{z-1\over z+1}\evalfrom_{z=2}} = \abs{F\qty{1\over 3}} \leq \abs{1\over 3}
.\]
:::
