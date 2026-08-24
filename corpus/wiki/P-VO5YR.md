---
schema: qual/card@1
id: P-VO5YR
kind: problem
title: Invert $\sin(z)$ using geometric series
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Power Series
  - Trigonometry
relations: []
review: draft
---

:::{.exercise title="Invert $\sin(z)$ using geometric series"}
Invert $\sin(z)$ using a geometric series, heeding the warning above.
:::

:::{.solution}
Just a computation:
\[
{1\over \sin(z)} 
&= {1\over z-{z^3\over 3!} + {z^5\over 5!} - \bigo(z^7) } \\
&={1\over z\qty{ 1 - {z^2\over 3!} + {z^4 \over 5!} - \bigo(z^6)} } \\
&= z\inv \qty{1\over 1 - p(z)} 
\qquad p(z) \da {z^2\over 3!} - {z^4\over 5!} + \bigo(z^6) \\
&= z\inv \sum_{k\geq 0} p(z)^k \\
&= z\inv\qty{ 1 + p(z) + p(z)^2 + \bigo(z^2)^3 } \\
&= z\inv\qty{ 1 
\ + \qty{{z^2\over 3!} - {z^4\over 5!} + \bigo(z^6)} 
\ + \qty{{z^2\over 3!} - {z^4\over 5!} + \bigo(z^6)}^2
\ + \bigo(z^6)} \\
&= {1\over z}\qty{ 1 + {1\over 3!}z^2 + \qty{\qty{1\over 3!}^2 - {1\over 5!} }z^4 + \bigo(z^6) }\\
&= {1\over z} + {1\over 6}z + {7\over 360}z^3 + \bigo(z^5)
.\]

:::

