---
schema: qual/card@1
id: E-M7K4C
kind: exercise
title: Cauchy formula and principal parts
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Integral Formula
  - Residues
  - Principal Parts
  - Contour Integration
relations: []
review: draft
---

:::{.exercise}
Compute
\[
\int_\gamma {z^2+1 \over z(z^2 + 4)}\dz
\]
for 

- A circle of radius $1$,
- A circle of radius $2+\eps$,

:::

:::{.solution}
For the smaller circle, use Cauchy's formula
\[
\int_{\abs{z} = 1} f(z) \dz 
&= \int_{\abs{z} = 1} { {z^2 + 1 \over z^2 + 4} \over z} \dz \\
&=  2\pi i \qty{z^2 + 1 \over z^2 + 4} \evalfrom_{z=0} \\
&= {i\pi \over 2}
.\].

For the larger circle, break into principal parts.
Write
\[
{z^2 + 1 \over z(z^2+4)} = {a\over z} + {b\over z+2i} + {c\over z-2i}
,\]
and use PFD/cover-up method/finding residues:

- $a = \qty{z^2+1\over z^2+4}\evalfrom_{z=0} = {1\over 4}$
- $b= \qty{z^2 + 1 \over z(z-2i)}\evalfrom_{z=-2i} = {-4+1\over -2i(-4i)} = {3\over 8}$
- $c = \qty{z^2 + 1 \over z(z+2i)}\evalfrom_{z=2i} = {-4+1 \over 2i(4i)} = {3\over 8}$

Thus
\[
\int_\gamma f(z) \dz 
&= \int_\gamma \qty{ {1/4\over z} + {3/8\over z+2i} + {3/8 \over z-2i} } \dz \\
&= 2\pi i\qty{ {1\over 4} + {3\over 8} + {3\over 8}}
.\]

:::

