---
schema: qual/card@1
id: E-SQ4GJ
kind: exercise
title: "Expansion for a reciprocal"
classification:
  areas:
  - complex-analysis
  topics:
  - laurent-series
  - power-series
  - poles
relations: []
review: draft
solved: true
---
:::{.exercise title="Expansion for a reciprocal"}
Find a power series expansion of 
\[
f(z) = {1\over e^z-1}
.\]

:::

:::{.solution}
One way: polynomial long division.
\[
{1\over e^z-1} 
&= {1\over z + {1\over 2}z^2 + {1\over 6}z^2 + \cdots } \\
&= {1\over z}\qty{1 - {1\over 2}z + \qty{-{1\over 6} + {1\over 4} }z^2 + \cdots } \\
&= z\inv - {1\over 2} + {1\over 12}z + \bigo(z^3)
.\]
Alternatively, use geometric series.
Note that something like ${1\over 1-e^z} = \sum_{k\geq 0} e^{kz}$ won't converge, and won't even be calculable since each $e^{kz}$ contributes a constant term!
\[
{1\over e^z-1} 
&= {1\over z + {1\over 2}z^2 + {1\over 6}z^3 + \cdots } \\
&= {1\over z(1 + {1\over 2}z + {1\over 6}z^2 + \cdots) } \\
&= z\inv {1\over 1 + q(z) } \qquad q(z) \da {1\over 2}z + {1\over 6}z^2 + \cdots \\
&= z\inv \sum_{k\geq 0}(-q(z))^k \\
&= z\inv \qty{1 - q(z) + q(z)^2 - \cdots } \\
&= z\inv\qty{1 - \qty{{1\over 2}z + {1\over 6}z^2 + \cdots } + \qty{{1\over 2}z + {1\over 6}z^2 + \cdots }^2 - \cdots } \\
&= z\inv\qty{ 1 - {1\over 2} z + \qty{-{1\over 6} + \qty{1\over 2}^2 } z^2 + \bigo(z^3) } \\
&= z\inv - {1\over 2} + {1\over 12}z + \bigo(z^2)
.\]
:::

