---
schema: qual/card@1
id: E-4H3JY
kind: exercise
title: "Disc to upper half-plane"
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
---
:::{.exercise title="Disc to upper half-plane"}
Find a conformal map from $\DD$ to $\HH$.
:::

:::{.solution}
Note that the standard Cayley map $f(z)\da {z-i\over z+i}$ sends $\HH\to \DD$.
Why this is true: $\abs{f(z)} < 1$, since $\abs{z-i} < \abs{z+i}$ for $z\in \HH$.
Finding an explicit inverse:
\[
w &= {z-i\over z+i} \\
\implies w(z+i) - (z-i) &= 0 \\
\implies z &= -i {w+1\over w-1}
,\]
which is the desired map.
Why the image is in $\HH$: it suffices to show that $\Im(f(z)) > 0$ for all $z\in \DD$.
Write $z = x+iy$ and note that $\Im(iz) = \Re(z)$, then
\[
\Im(f(z)) 
&= \Re\qty{1-z\over 1+z} \\
&= \Re\qty{1-x-iy \over 1+x+iy} \\
&= \Re\qty{1-x^2-y^2 - i2y \over 1+x^2 + y^2} \\
&= {1-(x^2+y^2) \over 1+(x^2+y^2) } \\
&> 0
,\]
since $x^2+y^2<1$ for $x+iy \in \DD$.

:::

