---
schema: qual/card@1
id: E-AOQLK
kind: exercise
title: Residues using partial fractions/principal parts
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Principal Parts
  - Poles
relations: []
review: draft
solved: true
---

:::{.exercise title="Residues using partial fractions/principal parts"}
Find all residues of the following function by writing it as a sum of principal parts at its poles:
\[
f(z) = {z^3 \over z^2 + 1}
.\]

:::

:::{.solution}
Use polynomial long division to write
\[
z^3 = z(z^2+1) - z \implies {z^3 \over z^2 + 1} = z - {z\over z^2 + 1}
.\]
Factor the latter part:
\[
{z\over z^2 + 1} = {a\over z+i} + {b\over z-i} \implies a(z-i) + b(z+i) = z
,\]
evaluate at $z=i$ to get $b=1/2$, and at $z=-i$ to get $a=1/2$.
Thus
\[
f(z) = z - {1/2 \over z+i} - {1/2 \over z-i} = P_\infty + P_{-i} + P_{i}
,\]
yielding poles at $\pm i$ with residues
\[
\Res_{z=\infty} f(z) &= -1 \\
\Res_{z = i} f(z) &= -1/2 \\
\Res_{z = -i} f(z) &= -1/2 \\
.\]

:::

