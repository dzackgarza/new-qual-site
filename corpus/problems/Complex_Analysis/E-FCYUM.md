---
schema: qual/card@1
id: E-FCYUM
kind: problem
title: $\Res_{z=0}\frac{1}{z^2\sin z}$
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Laurent Series
  - Poles
  - Trigonometry
relations: []
review: draft
---

::: {.exercise}
Compute
\[
\Res_{z=0} {1\over z^2 \sin(z)}
.\]

:::

::: {.solution}
First expand $(\sin(z))\inv$:
\[
{1\over \sin(z)}
&= \qty{z - {1\over 3!}z^3 + {1\over 5!}z^5 -\cdots }\inv \\
&= z\inv \qty{1 - {1\over 3!}z^2 + {1\over 5!}z^4 - \cdots }\inv \\
&= z\inv \qty{1 + 
\qty{{1\over 3!}z^2 - {1\over 5!} z^4 + \cdots} +
\qty{{1\over 3!}z^2 - \cdots}^2 + \cdots
} \\
&= z\inv\qty{1 + {1\over 3!}z^2 + O(z^4) }
,\]
using that $(1-x)\inv = 1 + x + x^2 + \cdots$ with $x={1\over 3!}z^2 - {1\over 5!} z^4 + \cdots$.

Thus
\[
z^{-2}\qty{\sin(z)}\inv 
&= z^{-2} \cdot
z\inv\qty{1 + {1\over 3!}z^2 + O(z^4) } \\
&= z^{-3} + {1\over 3!}z\inv + O(z)
,\]
and the residue is the coefficient of $z\inv$:
\[
\Res_{z=0} {1\over z^2 \sin(z)}=\boxed{1\over 6}
.\]
:::

