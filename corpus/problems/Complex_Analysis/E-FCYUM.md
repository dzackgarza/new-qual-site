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
First expand $\inverseof{(\sin(z))}$:
\[
{1\over \sin(z)}
&= \inverseof{\qty{z - {1\over 3!}z^3 + {1\over 5!}z^5 -\cdots }} \\
&= \inverseof{z} \inverseof{\qty{1 - {1\over 3!}z^2 + {1\over 5!}z^4 - \cdots }} \\
&= \inverseof{z} \qty{1 +
\qty{{1\over 3!}z^2 - {1\over 5!} z^4 + \cdots} +
\qty{{1\over 3!}z^2 - \cdots}^2 + \cdots
} \\
&= \inverseof{z}\qty{1 + {1\over 3!}z^2 + O(z^4) }
,\]
using that $\inverseof{(1-x)} = 1 + x + x^2 + \cdots$ with $x={1\over 3!}z^2 - {1\over 5!} z^4 + \cdots$.

Thus
\[
z^{-2}\inverseof{\qty{\sin(z)}}
&= z^{-2} \cdot
\inverseof{z}\qty{1 + {1\over 3!}z^2 + O(z^4) } \\
&= z^{-3} + {1\over 3!}\inverseof{z} + O(z)
,\]
and the residue is the coefficient of $\inverseof{z}$:
\[
\Res_{z=0} {1\over z^2 \sin(z)}=\boxed{1\over 6}
.\]
:::
