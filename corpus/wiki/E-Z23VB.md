---
schema: qual/card@1
id: E-Z23VB
kind: exercise
title: Conformal maps to arbitrary points
classification:
  areas:
  - complex-analysis
  topics:
  - Fractional Linear Transformations
  - Conformal Maps
relations: []
review: draft
solved: true
---

:::{.exercise title="Conformal maps to arbitrary points"}
Find a Mobius transformation sending 

- $1\to 3$
- $i\to 0$
- $2\to -1$

:::

:::{.solution}
Use cross ratios: set $T(z) \da (z;,1,i,2)$ and $S(w) = (w;,3,0,-1)$ and solve $T(z) = S(w) \implies w = (S\inv T)(z)$:
\[
{z-i \over z-2}{1-2\over 1-i} 
&= {w-0\over w+1}{3+1 \over 3-0} \\
\implies -\frac{\left(i + 1\right) \, {\left(z - i\right)}}{2 \, {\left(z - 2\right)}}
&=
\frac{4 \, w}{3 \, {\left(w + 1\right)}} \\
\implies w
&=
-\frac{3 \, {\left(\left(i + 1\right) \, z - i + 1\right)}}{\left(3 i + 11\right) \, z - 3 i - 13}
\\
&= - {3z - 3i \over {3i+11\over i+1}z + {-3i-13 \over 3i+11}} \\
&= - {3z - 3i \over (7-4i) z + {-8+5i} } \\
&= \frac{-3 z+3 i}{(7-4 i) z+(-8+5 i)}
.\]

:::

